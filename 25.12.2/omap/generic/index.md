---
layout: default
title: "OpenWrt 25.12.2 omap/generic"
---

# AmneziaWG feed

Index of [(root)](https://slava-shchipunov.github.io/awg-openwrt/) / [25.12.2](https://slava-shchipunov.github.io/awg-openwrt/25.12.2/) / [omap](https://slava-shchipunov.github.io/awg-openwrt/25.12.2/omap/) / [generic](https://slava-shchipunov.github.io/awg-openwrt/25.12.2/omap/generic/)

- OpenWrt version: `25.12.2`
- Target: `omap`
- Subtarget: `generic`
- Package architecture: `arm_cortex-a8_vfpv3`

## Upstream OpenWrt target

[https://downloads.openwrt.org/releases/25.12.2/targets/omap/generic/](https://downloads.openwrt.org/releases/25.12.2/targets/omap/generic/)

## Configure Feed

```sh
mkdir -p /etc/apk/keys
wget -O /etc/apk/keys/awg-openwrt-feed.pem "https://slava-shchipunov.github.io/awg-openwrt/keys/awg-openwrt-feed.pem"
echo "https://slava-shchipunov.github.io/awg-openwrt/25.12.2/omap/generic/packages.adb" >> /etc/apk/repositories.d/customfeeds.list
```

## Install Packages

```sh
apk update
apk add amneziawg-tools kmod-amneziawg luci-proto-amneziawg
```

<script src="https://slava-shchipunov.github.io/awg-openwrt/assets/copy-code.js"></script>

## Feed files

- [amneziawg-tools-1.0.20260223-r1.apk](https://slava-shchipunov.github.io/awg-openwrt/25.12.2/omap/generic/amneziawg-tools-1.0.20260223-r1.apk)
- [feed.json](https://slava-shchipunov.github.io/awg-openwrt/25.12.2/omap/generic/feed.json)
- [index.json](https://slava-shchipunov.github.io/awg-openwrt/25.12.2/omap/generic/index.json)
- [kmod-amneziawg-6.12.74.1.0.20260329-r1.apk](https://slava-shchipunov.github.io/awg-openwrt/25.12.2/omap/generic/kmod-amneziawg-6.12.74.1.0.20260329-r1.apk)
- [luci-i18n-amneziawg-ru-0.260508.69331.apk](https://slava-shchipunov.github.io/awg-openwrt/25.12.2/omap/generic/luci-i18n-amneziawg-ru-0.260508.69331.apk)
- [luci-proto-amneziawg-2.0.4-r1.apk](https://slava-shchipunov.github.io/awg-openwrt/25.12.2/omap/generic/luci-proto-amneziawg-2.0.4-r1.apk)
- [packages.adb](https://slava-shchipunov.github.io/awg-openwrt/25.12.2/omap/generic/packages.adb)
