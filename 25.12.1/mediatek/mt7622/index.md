---
layout: default
title: "OpenWrt 25.12.1 mediatek/mt7622"
---

# AmneziaWG feed

Index of [(root)](https://slava-shchipunov.github.io/awg-openwrt/) / [25.12.1](https://slava-shchipunov.github.io/awg-openwrt/25.12.1/) / [mediatek](https://slava-shchipunov.github.io/awg-openwrt/25.12.1/mediatek/) / [mt7622](https://slava-shchipunov.github.io/awg-openwrt/25.12.1/mediatek/mt7622/)

- OpenWrt version: `25.12.1`
- Target: `mediatek`
- Subtarget: `mt7622`
- Package architecture: `aarch64_cortex-a53`

## Upstream OpenWrt target

[https://downloads.openwrt.org/releases/25.12.1/targets/mediatek/mt7622/](https://downloads.openwrt.org/releases/25.12.1/targets/mediatek/mt7622/)

## Configure Feed

```sh
mkdir -p /etc/apk/keys
wget -O /etc/apk/keys/awg-openwrt-feed.pem "https://slava-shchipunov.github.io/awg-openwrt/keys/awg-openwrt-feed.pem"
echo "https://slava-shchipunov.github.io/awg-openwrt/25.12.1/mediatek/mt7622/packages.adb" >> /etc/apk/repositories.d/customfeeds.list
```

## Install Packages

```sh
apk update
apk add amneziawg-tools kmod-amneziawg luci-proto-amneziawg
```

<script src="https://slava-shchipunov.github.io/awg-openwrt/assets/copy-code.js?v=2"></script>

## Feed files

- [amneziawg-tools-1.0.20260223-r1.apk](https://slava-shchipunov.github.io/awg-openwrt/25.12.1/mediatek/mt7622/amneziawg-tools-1.0.20260223-r1.apk)
- [feed.json](https://slava-shchipunov.github.io/awg-openwrt/25.12.1/mediatek/mt7622/feed.json)
- [index.json](https://slava-shchipunov.github.io/awg-openwrt/25.12.1/mediatek/mt7622/index.json)
- [kmod-amneziawg-6.12.74.1.0.20260329-r1.apk](https://slava-shchipunov.github.io/awg-openwrt/25.12.1/mediatek/mt7622/kmod-amneziawg-6.12.74.1.0.20260329-r1.apk)
- [luci-i18n-amneziawg-ru-0.260508.66242.apk](https://slava-shchipunov.github.io/awg-openwrt/25.12.1/mediatek/mt7622/luci-i18n-amneziawg-ru-0.260508.66242.apk)
- [luci-i18n-amneziawg-ru-0.apk](https://slava-shchipunov.github.io/awg-openwrt/25.12.1/mediatek/mt7622/luci-i18n-amneziawg-ru-0.apk)
- [luci-proto-amneziawg-2.0.4-r1.apk](https://slava-shchipunov.github.io/awg-openwrt/25.12.1/mediatek/mt7622/luci-proto-amneziawg-2.0.4-r1.apk)
- [packages.adb](https://slava-shchipunov.github.io/awg-openwrt/25.12.1/mediatek/mt7622/packages.adb)
