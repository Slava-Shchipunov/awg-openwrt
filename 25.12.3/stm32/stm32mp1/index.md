---
layout: default
title: "OpenWrt 25.12.3 stm32/stm32mp1"
---

# AmneziaWG feed

Index of [(root)](https://slava-shchipunov.github.io/awg-openwrt/) / [25.12.3](https://slava-shchipunov.github.io/awg-openwrt/25.12.3/) / [stm32](https://slava-shchipunov.github.io/awg-openwrt/25.12.3/stm32/) / [stm32mp1](https://slava-shchipunov.github.io/awg-openwrt/25.12.3/stm32/stm32mp1/)

- OpenWrt version: `25.12.3`
- Target: `stm32`
- Subtarget: `stm32mp1`
- Package architecture: `arm_cortex-a7_neon-vfpv4`

## Upstream OpenWrt target

[https://downloads.openwrt.org/releases/25.12.3/targets/stm32/stm32mp1/](https://downloads.openwrt.org/releases/25.12.3/targets/stm32/stm32mp1/)

## Configure Feed

```sh
mkdir -p /etc/apk/keys
wget -O /etc/apk/keys/awg-openwrt-feed.pem "https://slava-shchipunov.github.io/awg-openwrt/keys/awg-openwrt-feed.pem"
echo "https://slava-shchipunov.github.io/awg-openwrt/25.12.3/stm32/stm32mp1/packages.adb" >> /etc/apk/repositories.d/customfeeds.list
```

## Install Packages

```sh
apk update
apk add amneziawg-tools kmod-amneziawg luci-proto-amneziawg
```

<script src="https://slava-shchipunov.github.io/awg-openwrt/assets/copy-code.js?v=2"></script>

## Feed files

- [amneziawg-tools-1.0.20260223-r1.apk](https://slava-shchipunov.github.io/awg-openwrt/25.12.3/stm32/stm32mp1/amneziawg-tools-1.0.20260223-r1.apk)
- [feed.json](https://slava-shchipunov.github.io/awg-openwrt/25.12.3/stm32/stm32mp1/feed.json)
- [index.json](https://slava-shchipunov.github.io/awg-openwrt/25.12.3/stm32/stm32mp1/index.json)
- [kmod-amneziawg-6.12.85.1.0.20260329-r1.apk](https://slava-shchipunov.github.io/awg-openwrt/25.12.3/stm32/stm32mp1/kmod-amneziawg-6.12.85.1.0.20260329-r1.apk)
- [luci-i18n-amneziawg-ru-0.260509.08656.apk](https://slava-shchipunov.github.io/awg-openwrt/25.12.3/stm32/stm32mp1/luci-i18n-amneziawg-ru-0.260509.08656.apk)
- [luci-proto-amneziawg-2.0.4-r1.apk](https://slava-shchipunov.github.io/awg-openwrt/25.12.3/stm32/stm32mp1/luci-proto-amneziawg-2.0.4-r1.apk)
- [packages.adb](https://slava-shchipunov.github.io/awg-openwrt/25.12.3/stm32/stm32mp1/packages.adb)
