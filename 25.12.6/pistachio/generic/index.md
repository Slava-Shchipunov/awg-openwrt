---
layout: default
title: "OpenWrt 25.12.6 pistachio/generic"
---

# AmneziaWG feed

Index of [(root)](https://slava-shchipunov.github.io/awg-openwrt/) / [25.12.6](https://slava-shchipunov.github.io/awg-openwrt/25.12.6/) / [pistachio](https://slava-shchipunov.github.io/awg-openwrt/25.12.6/pistachio/)

- OpenWrt version: `25.12.6`
- Target: `pistachio`
- Subtarget: `generic`
- Package architecture: `mipsel_24kc_24kf`

## Upstream OpenWrt target

[https://downloads.openwrt.org/releases/25.12.6/targets/pistachio/generic/](https://downloads.openwrt.org/releases/25.12.6/targets/pistachio/generic/)

## Configure Feed

```sh
mkdir -p /etc/apk/keys
wget -O /etc/apk/keys/awg-openwrt-feed.pem "https://slava-shchipunov.github.io/awg-openwrt/keys/awg-openwrt-feed.pem"
echo "https://slava-shchipunov.github.io/awg-openwrt/25.12.6/pistachio/generic/packages.adb" >> /etc/apk/repositories.d/customfeeds.list
```

## Install Packages

```sh
apk update
apk add amneziawg-tools kmod-amneziawg luci-proto-amneziawg
```

<script src="https://slava-shchipunov.github.io/awg-openwrt/assets/copy-code.js?v=2"></script>

## Feed files

- [amneziawg-tools-3.1.20260812-r1.apk](https://slava-shchipunov.github.io/awg-openwrt/25.12.6/pistachio/generic/amneziawg-tools-3.1.20260812-r1.apk)
- [feed.json](https://slava-shchipunov.github.io/awg-openwrt/25.12.6/pistachio/generic/feed.json)
- [index.json](https://slava-shchipunov.github.io/awg-openwrt/25.12.6/pistachio/generic/index.json)
- [kmod-amneziawg-6.12.112.3.1.20260906-r1.apk](https://slava-shchipunov.github.io/awg-openwrt/25.12.6/pistachio/generic/kmod-amneziawg-6.12.112.3.1.20260906-r1.apk)
- [luci-i18n-amneziawg-ru-0.261019.20240.apk](https://slava-shchipunov.github.io/awg-openwrt/25.12.6/pistachio/generic/luci-i18n-amneziawg-ru-0.261019.20240.apk)
- [luci-proto-amneziawg-3.1.0-r1.apk](https://slava-shchipunov.github.io/awg-openwrt/25.12.6/pistachio/generic/luci-proto-amneziawg-3.1.0-r1.apk)
- [packages.adb](https://slava-shchipunov.github.io/awg-openwrt/25.12.6/pistachio/generic/packages.adb)
