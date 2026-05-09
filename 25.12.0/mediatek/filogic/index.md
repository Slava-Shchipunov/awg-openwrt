---
layout: default
title: "OpenWrt 25.12.0 mediatek/filogic"
---

# AmneziaWG feed

Index of [(root)](https://slava-shchipunov.github.io/awg-openwrt/) / [25.12.0](https://slava-shchipunov.github.io/awg-openwrt/25.12.0/) / [mediatek](https://slava-shchipunov.github.io/awg-openwrt/25.12.0/mediatek/) / [filogic](https://slava-shchipunov.github.io/awg-openwrt/25.12.0/mediatek/filogic/)

- OpenWrt version: `25.12.0`
- Target: `mediatek`
- Subtarget: `filogic`
- Package architecture: `aarch64_cortex-a53`

## Upstream OpenWrt target

[https://downloads.openwrt.org/releases/25.12.0/targets/mediatek/filogic/](https://downloads.openwrt.org/releases/25.12.0/targets/mediatek/filogic/)

## Configure Feed

```sh
mkdir -p /etc/apk/keys
wget -O /etc/apk/keys/awg-openwrt-feed.pem "https://slava-shchipunov.github.io/awg-openwrt/keys/awg-openwrt-feed.pem"
echo "https://slava-shchipunov.github.io/awg-openwrt/25.12.0/mediatek/filogic/packages.adb" >> /etc/apk/repositories.d/customfeeds.list
```

## Install Packages

```sh
apk update
apk add amneziawg-tools kmod-amneziawg luci-proto-amneziawg
```

<script src="https://slava-shchipunov.github.io/awg-openwrt/assets/copy-code.js?v=2"></script>

## Feed files

- [amneziawg-tools-1.0.20260223-r1.apk](https://slava-shchipunov.github.io/awg-openwrt/25.12.0/mediatek/filogic/amneziawg-tools-1.0.20260223-r1.apk)
- [feed.json](https://slava-shchipunov.github.io/awg-openwrt/25.12.0/mediatek/filogic/feed.json)
- [index.json](https://slava-shchipunov.github.io/awg-openwrt/25.12.0/mediatek/filogic/index.json)
- [kmod-amneziawg-6.12.71.1.0.20260329-r1.apk](https://slava-shchipunov.github.io/awg-openwrt/25.12.0/mediatek/filogic/kmod-amneziawg-6.12.71.1.0.20260329-r1.apk)
- [luci-i18n-amneziawg-ru-0.260508.63071.apk](https://slava-shchipunov.github.io/awg-openwrt/25.12.0/mediatek/filogic/luci-i18n-amneziawg-ru-0.260508.63071.apk)
- [luci-i18n-amneziawg-ru-0.apk](https://slava-shchipunov.github.io/awg-openwrt/25.12.0/mediatek/filogic/luci-i18n-amneziawg-ru-0.apk)
- [luci-proto-amneziawg-2.0.4-r1.apk](https://slava-shchipunov.github.io/awg-openwrt/25.12.0/mediatek/filogic/luci-proto-amneziawg-2.0.4-r1.apk)
- [packages.adb](https://slava-shchipunov.github.io/awg-openwrt/25.12.0/mediatek/filogic/packages.adb)
