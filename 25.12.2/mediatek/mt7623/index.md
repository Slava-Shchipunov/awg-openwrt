---
layout: default
title: "OpenWrt 25.12.2 mediatek/mt7623"
---

# AmneziaWG feed

Index of [(root)](https://slava-shchipunov.github.io/awg-openwrt/) / [25.12.2](https://slava-shchipunov.github.io/awg-openwrt/25.12.2/) / [mediatek](https://slava-shchipunov.github.io/awg-openwrt/25.12.2/mediatek/) / [mt7623](https://slava-shchipunov.github.io/awg-openwrt/25.12.2/mediatek/mt7623/)

- OpenWrt version: `25.12.2`
- Target: `mediatek`
- Subtarget: `mt7623`
- Package architecture: `arm_cortex-a7_neon-vfpv4`

## Upstream OpenWrt target

[https://downloads.openwrt.org/releases/25.12.2/targets/mediatek/mt7623/](https://downloads.openwrt.org/releases/25.12.2/targets/mediatek/mt7623/)

## Configure Feed

```sh
mkdir -p /etc/apk/keys
wget -O /etc/apk/keys/awg-openwrt-feed.pem "https://slava-shchipunov.github.io/awg-openwrt/keys/awg-openwrt-feed.pem"
echo "https://slava-shchipunov.github.io/awg-openwrt/25.12.2/mediatek/mt7623/packages.adb" >> /etc/apk/repositories.d/customfeeds.list
```

## Install Packages

```sh
apk update
apk add amneziawg-tools kmod-amneziawg luci-proto-amneziawg
```

<script src="https://slava-shchipunov.github.io/awg-openwrt/assets/copy-code.js"></script>

## Feed files

- [amneziawg-tools-1.0.20260223-r1.apk](https://slava-shchipunov.github.io/awg-openwrt/25.12.2/mediatek/mt7623/amneziawg-tools-1.0.20260223-r1.apk)
- [feed.json](https://slava-shchipunov.github.io/awg-openwrt/25.12.2/mediatek/mt7623/feed.json)
- [index.json](https://slava-shchipunov.github.io/awg-openwrt/25.12.2/mediatek/mt7623/index.json)
- [kmod-amneziawg-6.12.74.1.0.20260329-r1.apk](https://slava-shchipunov.github.io/awg-openwrt/25.12.2/mediatek/mt7623/kmod-amneziawg-6.12.74.1.0.20260329-r1.apk)
- [luci-i18n-amneziawg-ru-0.260508.68982.apk](https://slava-shchipunov.github.io/awg-openwrt/25.12.2/mediatek/mt7623/luci-i18n-amneziawg-ru-0.260508.68982.apk)
- [luci-proto-amneziawg-2.0.4-r1.apk](https://slava-shchipunov.github.io/awg-openwrt/25.12.2/mediatek/mt7623/luci-proto-amneziawg-2.0.4-r1.apk)
- [packages.adb](https://slava-shchipunov.github.io/awg-openwrt/25.12.2/mediatek/mt7623/packages.adb)
