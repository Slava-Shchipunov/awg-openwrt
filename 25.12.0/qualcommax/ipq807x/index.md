---
layout: default
title: "OpenWrt 25.12.0 qualcommax/ipq807x"
---

# AmneziaWG feed

Index of [(root)](https://slava-shchipunov.github.io/awg-openwrt/) / [25.12.0](https://slava-shchipunov.github.io/awg-openwrt/25.12.0/) / [qualcommax](https://slava-shchipunov.github.io/awg-openwrt/25.12.0/qualcommax/) / [ipq807x](https://slava-shchipunov.github.io/awg-openwrt/25.12.0/qualcommax/ipq807x/)

- OpenWrt version: `25.12.0`
- Target: `qualcommax`
- Subtarget: `ipq807x`
- Package architecture: `aarch64_cortex-a53`

## Upstream OpenWrt target

[https://downloads.openwrt.org/releases/25.12.0/targets/qualcommax/ipq807x/](https://downloads.openwrt.org/releases/25.12.0/targets/qualcommax/ipq807x/)

## Configure Feed

```sh
mkdir -p /etc/apk/keys
wget -O /etc/apk/keys/awg-openwrt-feed.pem "https://slava-shchipunov.github.io/awg-openwrt/keys/awg-openwrt-feed.pem"
echo "https://slava-shchipunov.github.io/awg-openwrt/25.12.0/qualcommax/ipq807x/packages.adb" >> /etc/apk/repositories.d/customfeeds.list
```

## Install Packages

```sh
apk update
apk add amneziawg-tools kmod-amneziawg luci-proto-amneziawg
```

## Feed files

- [amneziawg-tools-1.0.20260223-r1.apk](https://slava-shchipunov.github.io/awg-openwrt/25.12.0/qualcommax/ipq807x/amneziawg-tools-1.0.20260223-r1.apk)
- [feed.json](https://slava-shchipunov.github.io/awg-openwrt/25.12.0/qualcommax/ipq807x/feed.json)
- [index.json](https://slava-shchipunov.github.io/awg-openwrt/25.12.0/qualcommax/ipq807x/index.json)
- [kmod-amneziawg-6.12.71.1.0.20260329-r1.apk](https://slava-shchipunov.github.io/awg-openwrt/25.12.0/qualcommax/ipq807x/kmod-amneziawg-6.12.71.1.0.20260329-r1.apk)
- [luci-i18n-amneziawg-ru-0.260508.63611.apk](https://slava-shchipunov.github.io/awg-openwrt/25.12.0/qualcommax/ipq807x/luci-i18n-amneziawg-ru-0.260508.63611.apk)
- [luci-i18n-amneziawg-ru-0.apk](https://slava-shchipunov.github.io/awg-openwrt/25.12.0/qualcommax/ipq807x/luci-i18n-amneziawg-ru-0.apk)
- [luci-proto-amneziawg-2.0.4-r1.apk](https://slava-shchipunov.github.io/awg-openwrt/25.12.0/qualcommax/ipq807x/luci-proto-amneziawg-2.0.4-r1.apk)
- [packages.adb](https://slava-shchipunov.github.io/awg-openwrt/25.12.0/qualcommax/ipq807x/packages.adb)
