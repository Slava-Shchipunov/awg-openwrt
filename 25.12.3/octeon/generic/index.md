---
layout: default
title: "OpenWrt 25.12.3 octeon/generic"
---

# AmneziaWG feed

Index of [(root)](https://slava-shchipunov.github.io/awg-openwrt/) / [25.12.3](https://slava-shchipunov.github.io/awg-openwrt/25.12.3/) / [octeon](https://slava-shchipunov.github.io/awg-openwrt/25.12.3/octeon/) / [generic](https://slava-shchipunov.github.io/awg-openwrt/25.12.3/octeon/generic/)

- OpenWrt version: `25.12.3`
- Target: `octeon`
- Subtarget: `generic`
- Package architecture: `mips64_octeonplus`

## Upstream OpenWrt target

[https://downloads.openwrt.org/releases/25.12.3/targets/octeon/generic/](https://downloads.openwrt.org/releases/25.12.3/targets/octeon/generic/)

## Configure Feed

```sh
mkdir -p /etc/apk/keys
wget -O /etc/apk/keys/awg-openwrt-feed.pem "https://slava-shchipunov.github.io/awg-openwrt/keys/awg-openwrt-feed.pem"
echo "https://slava-shchipunov.github.io/awg-openwrt/25.12.3/octeon/generic/packages.adb" >> /etc/apk/repositories.d/customfeeds.list
```

## Install Packages

```sh
apk update
apk add amneziawg-tools kmod-amneziawg luci-proto-amneziawg
```

<script src="https://slava-shchipunov.github.io/awg-openwrt/assets/copy-code.js?v=2"></script>

## Feed files

- [amneziawg-tools-1.0.20260223-r1.apk](https://slava-shchipunov.github.io/awg-openwrt/25.12.3/octeon/generic/amneziawg-tools-1.0.20260223-r1.apk)
- [feed.json](https://slava-shchipunov.github.io/awg-openwrt/25.12.3/octeon/generic/feed.json)
- [index.json](https://slava-shchipunov.github.io/awg-openwrt/25.12.3/octeon/generic/index.json)
- [kmod-amneziawg-6.12.85.1.0.20260329-r1.apk](https://slava-shchipunov.github.io/awg-openwrt/25.12.3/octeon/generic/kmod-amneziawg-6.12.85.1.0.20260329-r1.apk)
- [luci-i18n-amneziawg-ru-0.260509.08079.apk](https://slava-shchipunov.github.io/awg-openwrt/25.12.3/octeon/generic/luci-i18n-amneziawg-ru-0.260509.08079.apk)
- [luci-proto-amneziawg-2.0.4-r1.apk](https://slava-shchipunov.github.io/awg-openwrt/25.12.3/octeon/generic/luci-proto-amneziawg-2.0.4-r1.apk)
- [packages.adb](https://slava-shchipunov.github.io/awg-openwrt/25.12.3/octeon/generic/packages.adb)
