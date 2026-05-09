---
layout: default
title: "OpenWrt 25.12.3 mediatek/mt7629"
---

# AmneziaWG feed

Index of [(root)](https://slava-shchipunov.github.io/awg-openwrt/) / [25.12.3](https://slava-shchipunov.github.io/awg-openwrt/25.12.3/) / [mediatek](https://slava-shchipunov.github.io/awg-openwrt/25.12.3/mediatek/) / [mt7629](https://slava-shchipunov.github.io/awg-openwrt/25.12.3/mediatek/mt7629/)

- OpenWrt version: `25.12.3`
- Target: `mediatek`
- Subtarget: `mt7629`
- Package architecture: `arm_cortex-a7`

## Upstream OpenWrt target

[https://downloads.openwrt.org/releases/25.12.3/targets/mediatek/mt7629/](https://downloads.openwrt.org/releases/25.12.3/targets/mediatek/mt7629/)

## Configure Feed

```sh
mkdir -p /etc/apk/keys
wget -O /etc/apk/keys/awg-openwrt-feed.pem "https://slava-shchipunov.github.io/awg-openwrt/keys/awg-openwrt-feed.pem"
echo "https://slava-shchipunov.github.io/awg-openwrt/25.12.3/mediatek/mt7629/packages.adb" >> /etc/apk/repositories.d/customfeeds.list
```

## Install Packages

```sh
apk update
apk add amneziawg-tools kmod-amneziawg luci-proto-amneziawg
```

<script src="https://slava-shchipunov.github.io/awg-openwrt/assets/copy-code.js?v=2"></script>

## Feed files

- [amneziawg-tools-1.0.20260223-r1.apk](https://slava-shchipunov.github.io/awg-openwrt/25.12.3/mediatek/mt7629/amneziawg-tools-1.0.20260223-r1.apk)
- [feed.json](https://slava-shchipunov.github.io/awg-openwrt/25.12.3/mediatek/mt7629/feed.json)
- [index.json](https://slava-shchipunov.github.io/awg-openwrt/25.12.3/mediatek/mt7629/index.json)
- [kmod-amneziawg-6.12.85.1.0.20260329-r1.apk](https://slava-shchipunov.github.io/awg-openwrt/25.12.3/mediatek/mt7629/kmod-amneziawg-6.12.85.1.0.20260329-r1.apk)
- [luci-i18n-amneziawg-ru-0.260509.08311.apk](https://slava-shchipunov.github.io/awg-openwrt/25.12.3/mediatek/mt7629/luci-i18n-amneziawg-ru-0.260509.08311.apk)
- [luci-proto-amneziawg-2.0.4-r1.apk](https://slava-shchipunov.github.io/awg-openwrt/25.12.3/mediatek/mt7629/luci-proto-amneziawg-2.0.4-r1.apk)
- [packages.adb](https://slava-shchipunov.github.io/awg-openwrt/25.12.3/mediatek/mt7629/packages.adb)
