---
layout: default
title: "OpenWrt 25.12.3 mvebu/cortexa72"
---

# AmneziaWG feed

Index of [(root)](https://slava-shchipunov.github.io/awg-openwrt/) / [25.12.3](https://slava-shchipunov.github.io/awg-openwrt/25.12.3/) / [mvebu](https://slava-shchipunov.github.io/awg-openwrt/25.12.3/mvebu/) / [cortexa72](https://slava-shchipunov.github.io/awg-openwrt/25.12.3/mvebu/cortexa72/)

- OpenWrt version: `25.12.3`
- Target: `mvebu`
- Subtarget: `cortexa72`
- Package architecture: `aarch64_cortex-a72`

## Upstream OpenWrt target

[https://downloads.openwrt.org/releases/25.12.3/targets/mvebu/cortexa72/](https://downloads.openwrt.org/releases/25.12.3/targets/mvebu/cortexa72/)

## Configure Feed

```sh
mkdir -p /etc/apk/keys
wget -O /etc/apk/keys/awg-openwrt-feed.pem "https://slava-shchipunov.github.io/awg-openwrt/keys/awg-openwrt-feed.pem"
echo "https://slava-shchipunov.github.io/awg-openwrt/25.12.3/mvebu/cortexa72/packages.adb" >> /etc/apk/repositories.d/customfeeds.list
```

## Install Packages

```sh
apk update
apk add amneziawg-tools kmod-amneziawg luci-proto-amneziawg
```

## Feed files

- [amneziawg-tools-1.0.20260223-r1.apk](https://slava-shchipunov.github.io/awg-openwrt/25.12.3/mvebu/cortexa72/amneziawg-tools-1.0.20260223-r1.apk)
- [feed.json](https://slava-shchipunov.github.io/awg-openwrt/25.12.3/mvebu/cortexa72/feed.json)
- [index.json](https://slava-shchipunov.github.io/awg-openwrt/25.12.3/mvebu/cortexa72/index.json)
- [kmod-amneziawg-6.12.85.1.0.20260329-r1.apk](https://slava-shchipunov.github.io/awg-openwrt/25.12.3/mvebu/cortexa72/kmod-amneziawg-6.12.85.1.0.20260329-r1.apk)
- [luci-i18n-amneziawg-ru-0.260509.08010.apk](https://slava-shchipunov.github.io/awg-openwrt/25.12.3/mvebu/cortexa72/luci-i18n-amneziawg-ru-0.260509.08010.apk)
- [luci-proto-amneziawg-2.0.4-r1.apk](https://slava-shchipunov.github.io/awg-openwrt/25.12.3/mvebu/cortexa72/luci-proto-amneziawg-2.0.4-r1.apk)
- [packages.adb](https://slava-shchipunov.github.io/awg-openwrt/25.12.3/mvebu/cortexa72/packages.adb)
