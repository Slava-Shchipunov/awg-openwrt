---
layout: default
title: "OpenWrt 25.12.3 bcm27xx/bcm2711"
---

# AmneziaWG feed

Index of [(root)](https://slava-shchipunov.github.io/awg-openwrt/) / [25.12.3](https://slava-shchipunov.github.io/awg-openwrt/25.12.3/) / [bcm27xx](https://slava-shchipunov.github.io/awg-openwrt/25.12.3/bcm27xx/) / [bcm2711](https://slava-shchipunov.github.io/awg-openwrt/25.12.3/bcm27xx/bcm2711/)

- OpenWrt version: `25.12.3`
- Target: `bcm27xx`
- Subtarget: `bcm2711`
- Package architecture: `aarch64_cortex-a72`

## Upstream OpenWrt target

[https://downloads.openwrt.org/releases/25.12.3/targets/bcm27xx/bcm2711/](https://downloads.openwrt.org/releases/25.12.3/targets/bcm27xx/bcm2711/)

## Configure Feed

```sh
mkdir -p /etc/apk/keys
wget -O /etc/apk/keys/awg-openwrt-feed.pem "https://slava-shchipunov.github.io/awg-openwrt/keys/awg-openwrt-feed.pem"
echo "https://slava-shchipunov.github.io/awg-openwrt/25.12.3/bcm27xx/bcm2711/packages.adb" >> /etc/apk/repositories.d/customfeeds.list
```

## Install Packages

```sh
apk update
apk add amneziawg-tools kmod-amneziawg luci-proto-amneziawg
```

<script src="https://slava-shchipunov.github.io/awg-openwrt/assets/copy-code.js?v=2"></script>

## Feed files

- [amneziawg-tools-1.0.20260223-r1.apk](https://slava-shchipunov.github.io/awg-openwrt/25.12.3/bcm27xx/bcm2711/amneziawg-tools-1.0.20260223-r1.apk)
- [feed.json](https://slava-shchipunov.github.io/awg-openwrt/25.12.3/bcm27xx/bcm2711/feed.json)
- [index.json](https://slava-shchipunov.github.io/awg-openwrt/25.12.3/bcm27xx/bcm2711/index.json)
- [kmod-amneziawg-6.12.85.1.0.20260329-r1.apk](https://slava-shchipunov.github.io/awg-openwrt/25.12.3/bcm27xx/bcm2711/kmod-amneziawg-6.12.85.1.0.20260329-r1.apk)
- [luci-i18n-amneziawg-ru-0.260509.07205.apk](https://slava-shchipunov.github.io/awg-openwrt/25.12.3/bcm27xx/bcm2711/luci-i18n-amneziawg-ru-0.260509.07205.apk)
- [luci-proto-amneziawg-2.0.4-r1.apk](https://slava-shchipunov.github.io/awg-openwrt/25.12.3/bcm27xx/bcm2711/luci-proto-amneziawg-2.0.4-r1.apk)
- [packages.adb](https://slava-shchipunov.github.io/awg-openwrt/25.12.3/bcm27xx/bcm2711/packages.adb)
