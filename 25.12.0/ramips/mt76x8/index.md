---
layout: default
title: "OpenWrt 25.12.0 ramips/mt76x8"
---

# AmneziaWG feed

Index of [(root)](https://slava-shchipunov.github.io/awg-openwrt/) / [25.12.0](https://slava-shchipunov.github.io/awg-openwrt/25.12.0/) / [ramips](https://slava-shchipunov.github.io/awg-openwrt/25.12.0/ramips/) / [mt76x8](https://slava-shchipunov.github.io/awg-openwrt/25.12.0/ramips/mt76x8/)

- OpenWrt version: `25.12.0`
- Target: `ramips`
- Subtarget: `mt76x8`
- Package architecture: `mipsel_24kc`

## Upstream OpenWrt target

[https://downloads.openwrt.org/releases/25.12.0/targets/ramips/mt76x8/](https://downloads.openwrt.org/releases/25.12.0/targets/ramips/mt76x8/)

## Configure Feed

```sh
mkdir -p /etc/apk/keys
wget -O /etc/apk/keys/awg-openwrt-feed.pem "https://slava-shchipunov.github.io/awg-openwrt/keys/awg-openwrt-feed.pem"
echo "https://slava-shchipunov.github.io/awg-openwrt/25.12.0/ramips/mt76x8/packages.adb" >> /etc/apk/repositories.d/customfeeds.list
```

## Install Packages

```sh
apk update
apk add amneziawg-tools kmod-amneziawg luci-proto-amneziawg
```

<script src="https://slava-shchipunov.github.io/awg-openwrt/assets/copy-code.js?v=2"></script>

## Feed files

- [amneziawg-tools-1.0.20260223-r1.apk](https://slava-shchipunov.github.io/awg-openwrt/25.12.0/ramips/mt76x8/amneziawg-tools-1.0.20260223-r1.apk)
- [feed.json](https://slava-shchipunov.github.io/awg-openwrt/25.12.0/ramips/mt76x8/feed.json)
- [index.json](https://slava-shchipunov.github.io/awg-openwrt/25.12.0/ramips/mt76x8/index.json)
- [kmod-amneziawg-6.12.71.1.0.20260329-r1.apk](https://slava-shchipunov.github.io/awg-openwrt/25.12.0/ramips/mt76x8/kmod-amneziawg-6.12.71.1.0.20260329-r1.apk)
- [luci-i18n-amneziawg-ru-0.260508.63028.apk](https://slava-shchipunov.github.io/awg-openwrt/25.12.0/ramips/mt76x8/luci-i18n-amneziawg-ru-0.260508.63028.apk)
- [luci-i18n-amneziawg-ru-0.apk](https://slava-shchipunov.github.io/awg-openwrt/25.12.0/ramips/mt76x8/luci-i18n-amneziawg-ru-0.apk)
- [luci-proto-amneziawg-2.0.4-r1.apk](https://slava-shchipunov.github.io/awg-openwrt/25.12.0/ramips/mt76x8/luci-proto-amneziawg-2.0.4-r1.apk)
- [packages.adb](https://slava-shchipunov.github.io/awg-openwrt/25.12.0/ramips/mt76x8/packages.adb)
