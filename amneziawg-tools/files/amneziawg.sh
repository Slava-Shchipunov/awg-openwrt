#!/bin/sh
# Copyright 2016-2017 Dan Luedtke <mail@danrl.com>
# Licensed to the public under the Apache License 2.0.

# shellcheck disable=SC1091,SC3003,SC3043

AWG=/usr/bin/awg
if [ ! -x $AWG ]; then
	logger -t "amneziawg" "error: missing amneziawg-tools (${AWG})"
	exit 0
fi

[ -n "$INCLUDE_ONLY" ] || {
	. /lib/functions.sh
	. ../netifd-proto.sh
	init_proto "$@"
}

# AmneziaWG obfuscation parameters, in `<uci option>:<configuration file key>'
# notation. The values are copied verbatim into the [Interface] section of the
# generated configuration file, so keeping this single list in sync with
# luci-proto-amneziawg is all that is needed to support a new parameter.
AWG_PARAMS="
awg_jc:Jc
awg_jmin:Jmin
awg_jmax:Jmax
awg_s1:S1
awg_s2:S2
awg_s3:S3
awg_s4:S4
awg_h1:H1
awg_h2:H2
awg_h3:H3
awg_h4:H4
awg_i1:I1
awg_i2:I2
awg_i3:I3
awg_i4:I4
awg_i5:I5
awg_header_protection_key:HeaderProtectionKey
awg_content_padding_addition:ContentPaddingAddition
awg_rekey_after_time:RekeyAfterTime
awg_rekey_timeout:RekeyTimeout
awg_reject_after_time:RejectAfterTime
awg_keepalive_timeout:KeepaliveTimeout
awg_max_handshake_attempts:MaxHandshakeAttempts
"

proto_amneziawg_init_config() {
	proto_config_add_string "private_key"
	proto_config_add_int "listen_port"
	proto_config_add_int "mtu"
	proto_config_add_string "fwmark"
	proto_config_add_int "awg_jc"
	proto_config_add_int "awg_jmin"
	proto_config_add_int "awg_jmax"
	proto_config_add_int "awg_s1"
	proto_config_add_int "awg_s2"
	proto_config_add_int "awg_s3"
	proto_config_add_int "awg_s4"
	proto_config_add_string "awg_h1"
	proto_config_add_string "awg_h2"
	proto_config_add_string "awg_h3"
	proto_config_add_string "awg_h4"
	proto_config_add_string "awg_i1"
	proto_config_add_string "awg_i2"
	proto_config_add_string "awg_i3"
	proto_config_add_string "awg_i4"
	proto_config_add_string "awg_i5"
	# AmneziaWG 3.0 parameters
	proto_config_add_string "awg_header_protection_key"
	proto_config_add_string "awg_content_padding_addition"
	proto_config_add_string "awg_rekey_after_time"
	proto_config_add_string "awg_rekey_timeout"
	proto_config_add_string "awg_reject_after_time"
	proto_config_add_string "awg_keepalive_timeout"
	proto_config_add_string "awg_max_handshake_attempts"
# shellcheck disable=SC2034
	available=1
# shellcheck disable=SC2034
	no_proto_task=1
}

proto_amneziawg_is_kernel_mode() {
	if [ ! -e /sys/module/amneziawg ]; then
		modprobe amneziawg > /dev/null 2>&1 || true

		if [ -e /sys/module/amneziawg ]; then
			return 0
		else
			if ! command -v "${AWG_QUICK_USERSPACE_IMPLEMENTATION:-amneziawg-go}" >/dev/null; then
				ret=$?
				echo "Please install either kernel module (kmod-amneziawg package) or user-space implementation in /usr/bin/amneziawg-go."
				exit $ret
			else
				return 1
			fi
		fi
	else
		return 0
	fi
}

proto_amneziawg_setup_peer() {
	local peer_config="$1"

	local disabled
	local public_key
	local preshared_key
	local allowed_ips
	local route_allowed_ips
	local endpoint_host
	local endpoint_port
	local persistent_keepalive

	config_get_bool disabled "${peer_config}" "disabled" 0
	config_get public_key "${peer_config}" "public_key"
	config_get preshared_key "${peer_config}" "preshared_key"
	config_get allowed_ips "${peer_config}" "allowed_ips"
	config_get_bool route_allowed_ips "${peer_config}" "route_allowed_ips" 0
	config_get endpoint_host "${peer_config}" "endpoint_host"
	config_get endpoint_port "${peer_config}" "endpoint_port"
	config_get persistent_keepalive "${peer_config}" "persistent_keepalive"

	if [ "${disabled}" -eq 1 ]; then
		# skip disabled peers
		return 0
	fi

	if [ -z "$public_key" ]; then
		echo "Skipping peer config $peer_config because public key is not defined."
		return 0
	fi

	echo "[Peer]" >> "${awg_cfg}"
	echo "PublicKey=${public_key}" >> "${awg_cfg}"
	if [ "${preshared_key}" ]; then
		echo "PresharedKey=${preshared_key}" >> "${awg_cfg}"
	fi
	for allowed_ip in ${allowed_ips}; do
		echo "AllowedIPs=${allowed_ip}" >> "${awg_cfg}"
	done
	if [ "${endpoint_host}" ]; then
		case "${endpoint_host}" in
			*:*)
				endpoint="[${endpoint_host}]"
				;;
			*)
				endpoint="${endpoint_host}"
				;;
		esac
		if [ "${endpoint_port}" ]; then
			endpoint="${endpoint}:${endpoint_port}"
		else
			endpoint="${endpoint}:51820"
		fi
		echo "Endpoint=${endpoint}" >> "${awg_cfg}"
	fi
	# Since AmneziaWG 3.0 this may also be a `min-max' range, e.g. `25-30'
	if [ "${persistent_keepalive}" ]; then
		echo "PersistentKeepalive=${persistent_keepalive}" >> "${awg_cfg}"
	fi

	if [ ${route_allowed_ips} -ne 0 ]; then
		for allowed_ip in ${allowed_ips}; do
			case "${allowed_ip}" in
				*:*/*)
					proto_add_ipv6_route "${allowed_ip%%/*}" "${allowed_ip##*/}"
					;;
				*.*/*)
					proto_add_ipv4_route "${allowed_ip%%/*}" "${allowed_ip##*/}"
					;;
				*:*)
					proto_add_ipv6_route "${allowed_ip%%/*}" "128"
					;;
				*.*)
					proto_add_ipv4_route "${allowed_ip%%/*}" "32"
					;;
			esac
		done
	fi
}

proto_amneziawg_write_params() {
	local config="$1"

	local param
	local option
	local value

	for param in ${AWG_PARAMS}; do
		option="${param%%:*}"
		config_get value "${config}" "${option}"

		[ -n "${value}" ] && echo "${param##*:}=${value}" >> "${awg_cfg}"
	done

	return 0
}

ensure_key_is_generated() {
	local private_key
	private_key="$(uci -q get network."$1".private_key)"

	if [ "$private_key" = "generate" ]; then
		local ucitmp
		oldmask="$(umask)"
		umask 077
		ucitmp="$(mktemp -d)"
		private_key="$("${AWG}" genkey)"
		uci -q -t "$ucitmp" set network."$1".private_key="$private_key" && \
			uci -q -t "$ucitmp" commit network
		rm -rf "$ucitmp"
		umask "$oldmask"
	fi
}

proto_amneziawg_setup() {
	local config="$1"
	local awg_dir="/tmp/amneziawg"
	local awg_cfg="${awg_dir}/${config}"

	local private_key
	local listen_port
	local addresses
	local mtu
	local fwmark
	local ip6prefix
	local nohostroute
	local tunlink

	ensure_key_is_generated "${config}"

	config_load network
	config_get private_key "${config}" "private_key"
	config_get listen_port "${config}" "listen_port"
	config_get addresses "${config}" "addresses"
	config_get mtu "${config}" "mtu"
	config_get fwmark "${config}" "fwmark"
	config_get ip6prefix "${config}" "ip6prefix"
	config_get nohostroute "${config}" "nohostroute"
	config_get tunlink "${config}" "tunlink"

	if proto_amneziawg_is_kernel_mode; then
		logger -t "amneziawg" "info: using kernel-space kmod-amneziawg for ${AWG}"
		ip link del dev "${config}" 2>/dev/null
		ip link add dev "${config}" type amneziawg
	else
		logger -t "amneziawg" "info: using user-space amneziawg-go for ${AWG}"
		rm -f "/var/run/amneziawg/${config}.sock"
		amneziawg-go "${config}"
	fi

	if [ "${mtu}" ]; then
		ip link set mtu "${mtu}" dev "${config}"
	fi

	proto_init_update "${config}" 1

	umask 077
	mkdir -p "${awg_dir}"
	echo "[Interface]" > "${awg_cfg}"
	echo "PrivateKey=${private_key}" >> "${awg_cfg}"
	if [ "${listen_port}" ]; then
		echo "ListenPort=${listen_port}" >> "${awg_cfg}"
	fi
	if [ "${fwmark}" ]; then
		echo "FwMark=${fwmark}" >> "${awg_cfg}"
	fi
	proto_amneziawg_write_params "${config}"
	config_foreach proto_amneziawg_setup_peer "amneziawg_${config}"

	# Apply configuration file
	${AWG} setconf "${config}" "${awg_cfg}"
	AWG_RETURN=$?

	rm -f "${awg_cfg}"

	if [ ${AWG_RETURN} -ne 0 ]; then
		sleep 5
		proto_setup_failed "${config}"
		exit 1
	fi

	for address in ${addresses}; do
		case "${address}" in
			*:*/*)
				proto_add_ipv6_address "${address%%/*}" "${address##*/}"
				;;
			*.*/*)
				proto_add_ipv4_address "${address%%/*}" "${address##*/}"
				;;
			*:*)
				proto_add_ipv6_address "${address%%/*}" "128"
				;;
			*.*)
				proto_add_ipv4_address "${address%%/*}" "32"
				;;
		esac
	done

	for prefix in ${ip6prefix}; do
		proto_add_ipv6_prefix "$prefix"
	done

	# endpoint dependency
	if [ "${nohostroute}" != "1" ]; then
		# shellcheck disable=SC2034
		${AWG} show "${config}" endpoints | \
		sed -E 's/\[?([0-9.:a-f]+)\]?:([0-9]+)/\1 \2/' | \
		while IFS=$'\t ' read -r key address port; do
			[ -n "${port}" ] || continue
			proto_add_host_dependency "${config}" "${address}" "${tunlink}"
		done
	fi

	proto_send_update "${config}"
}

proto_amneziawg_teardown() {
	local config="$1"
	if proto_amneziawg_is_kernel_mode; then
		ip link del dev "${config}" >/dev/null 2>&1
	else
		rm -f "/var/run/amneziawg/${config}.sock"
	fi
}

[ -n "$INCLUDE_ONLY" ] || {
	add_protocol amneziawg
}
