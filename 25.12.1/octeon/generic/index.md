---
layout: default
title: "OpenWrt 25.12.1 octeon/generic"
---

# AmneziaWG feed

- OpenWrt version: `25.12.1`
- Target: `octeon`
- Subtarget: `generic`
- Package architecture: `mips64_octeonplus`

Device compatibility is determined by the OpenWrt version plus target/subtarget and the kmod kernel ABI. Package architecture is shown here as metadata from the APK repository, not as a separate user-facing choice.

## OpenWrt target

[https://downloads.openwrt.org/releases/25.12.1/targets/octeon/generic/](https://downloads.openwrt.org/releases/25.12.1/targets/octeon/generic/)

## Repository

```sh
mkdir -p /etc/apk/keys
wget -O /etc/apk/keys/awg-openwrt-feed.pub "https://slava-shchipunov.github.io/awg-openwrt/keys/awg-openwrt-feed.pub"
echo "https://slava-shchipunov.github.io/awg-openwrt/25.12.1/octeon/generic/packages.adb" >> /etc/apk/repositories.d/customfeeds.list
apk update
apk add amneziawg-tools kmod-amneziawg luci-proto-amneziawg
```

## Feed files

- [amneziawg-tools-1.0.20260223-r1.apk](https://slava-shchipunov.github.io/awg-openwrt/25.12.1/octeon/generic/amneziawg-tools-1.0.20260223-r1.apk)
- [feed.json](https://slava-shchipunov.github.io/awg-openwrt/25.12.1/octeon/generic/feed.json)
- [index.json](https://slava-shchipunov.github.io/awg-openwrt/25.12.1/octeon/generic/index.json)
- [kmod-amneziawg-6.12.74.1.0.20260329-r1.apk](https://slava-shchipunov.github.io/awg-openwrt/25.12.1/octeon/generic/kmod-amneziawg-6.12.74.1.0.20260329-r1.apk)
- [luci-i18n-amneziawg-ru-0.apk](https://slava-shchipunov.github.io/awg-openwrt/25.12.1/octeon/generic/luci-i18n-amneziawg-ru-0.apk)
- [luci-proto-amneziawg-2.0.4-r1.apk](https://slava-shchipunov.github.io/awg-openwrt/25.12.1/octeon/generic/luci-proto-amneziawg-2.0.4-r1.apk)
- [packages.adb](https://slava-shchipunov.github.io/awg-openwrt/25.12.1/octeon/generic/packages.adb)
