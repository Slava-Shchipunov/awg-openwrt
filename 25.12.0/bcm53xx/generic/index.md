---
layout: default
title: "OpenWrt 25.12.0 bcm53xx/generic"
---

# AmneziaWG feed

Index of [(root)](https://slava-shchipunov.github.io/awg-openwrt/) / [25.12.0](https://slava-shchipunov.github.io/awg-openwrt/25.12.0/) / [bcm53xx](https://slava-shchipunov.github.io/awg-openwrt/25.12.0/bcm53xx/) / [generic](https://slava-shchipunov.github.io/awg-openwrt/25.12.0/bcm53xx/generic/)

- OpenWrt version: `25.12.0`
- Target: `bcm53xx`
- Subtarget: `generic`
- Package architecture: `arm_cortex-a9`

## Upstream OpenWrt target

[https://downloads.openwrt.org/releases/25.12.0/targets/bcm53xx/generic/](https://downloads.openwrt.org/releases/25.12.0/targets/bcm53xx/generic/)

## Configure Feed

```sh
mkdir -p /etc/apk/keys
wget -O /etc/apk/keys/awg-openwrt-feed.pem "https://slava-shchipunov.github.io/awg-openwrt/keys/awg-openwrt-feed.pem"
echo "https://slava-shchipunov.github.io/awg-openwrt/25.12.0/bcm53xx/generic/packages.adb" >> /etc/apk/repositories.d/customfeeds.list
```

## Install Packages

```sh
apk update
apk add amneziawg-tools kmod-amneziawg luci-proto-amneziawg
```

<script src="https://slava-shchipunov.github.io/awg-openwrt/assets/copy-code.js?v=2"></script>

## Feed files

- [amneziawg-tools-1.0.20260223-r1.apk](https://slava-shchipunov.github.io/awg-openwrt/25.12.0/bcm53xx/generic/amneziawg-tools-1.0.20260223-r1.apk)
- [feed.json](https://slava-shchipunov.github.io/awg-openwrt/25.12.0/bcm53xx/generic/feed.json)
- [index.json](https://slava-shchipunov.github.io/awg-openwrt/25.12.0/bcm53xx/generic/index.json)
- [kmod-amneziawg-6.12.71.1.0.20260329-r1.apk](https://slava-shchipunov.github.io/awg-openwrt/25.12.0/bcm53xx/generic/kmod-amneziawg-6.12.71.1.0.20260329-r1.apk)
- [luci-i18n-amneziawg-ru-0.260508.63045.apk](https://slava-shchipunov.github.io/awg-openwrt/25.12.0/bcm53xx/generic/luci-i18n-amneziawg-ru-0.260508.63045.apk)
- [luci-i18n-amneziawg-ru-0.apk](https://slava-shchipunov.github.io/awg-openwrt/25.12.0/bcm53xx/generic/luci-i18n-amneziawg-ru-0.apk)
- [luci-proto-amneziawg-2.0.4-r1.apk](https://slava-shchipunov.github.io/awg-openwrt/25.12.0/bcm53xx/generic/luci-proto-amneziawg-2.0.4-r1.apk)
- [packages.adb](https://slava-shchipunov.github.io/awg-openwrt/25.12.0/bcm53xx/generic/packages.adb)
