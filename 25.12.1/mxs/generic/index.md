---
layout: default
title: "OpenWrt 25.12.1 mxs/generic"
---

# AmneziaWG feed

Index of [(root)](https://slava-shchipunov.github.io/awg-openwrt/) / [25.12.1](https://slava-shchipunov.github.io/awg-openwrt/25.12.1/) / [mxs](https://slava-shchipunov.github.io/awg-openwrt/25.12.1/mxs/) / [generic](https://slava-shchipunov.github.io/awg-openwrt/25.12.1/mxs/generic/)

- OpenWrt version: `25.12.1`
- Target: `mxs`
- Subtarget: `generic`
- Package architecture: `arm_arm926ej-s`

## Upstream OpenWrt target

[https://downloads.openwrt.org/releases/25.12.1/targets/mxs/generic/](https://downloads.openwrt.org/releases/25.12.1/targets/mxs/generic/)

## Configure Feed

```sh
mkdir -p /etc/apk/keys
wget -O /etc/apk/keys/awg-openwrt-feed.pem "https://slava-shchipunov.github.io/awg-openwrt/keys/awg-openwrt-feed.pem"
echo "https://slava-shchipunov.github.io/awg-openwrt/25.12.1/mxs/generic/packages.adb" >> /etc/apk/repositories.d/customfeeds.list
```

## Install Packages

```sh
apk update
apk add amneziawg-tools kmod-amneziawg luci-proto-amneziawg
```

<script src="https://slava-shchipunov.github.io/awg-openwrt/assets/copy-code.js"></script>

## Feed files

- [amneziawg-tools-1.0.20260223-r1.apk](https://slava-shchipunov.github.io/awg-openwrt/25.12.1/mxs/generic/amneziawg-tools-1.0.20260223-r1.apk)
- [feed.json](https://slava-shchipunov.github.io/awg-openwrt/25.12.1/mxs/generic/feed.json)
- [index.json](https://slava-shchipunov.github.io/awg-openwrt/25.12.1/mxs/generic/index.json)
- [kmod-amneziawg-6.12.74.1.0.20260329-r1.apk](https://slava-shchipunov.github.io/awg-openwrt/25.12.1/mxs/generic/kmod-amneziawg-6.12.74.1.0.20260329-r1.apk)
- [luci-i18n-amneziawg-ru-0.260508.66288.apk](https://slava-shchipunov.github.io/awg-openwrt/25.12.1/mxs/generic/luci-i18n-amneziawg-ru-0.260508.66288.apk)
- [luci-i18n-amneziawg-ru-0.apk](https://slava-shchipunov.github.io/awg-openwrt/25.12.1/mxs/generic/luci-i18n-amneziawg-ru-0.apk)
- [luci-proto-amneziawg-2.0.4-r1.apk](https://slava-shchipunov.github.io/awg-openwrt/25.12.1/mxs/generic/luci-proto-amneziawg-2.0.4-r1.apk)
- [packages.adb](https://slava-shchipunov.github.io/awg-openwrt/25.12.1/mxs/generic/packages.adb)
