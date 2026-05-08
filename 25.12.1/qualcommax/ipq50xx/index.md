---
layout: default
title: "OpenWrt 25.12.1 qualcommax/ipq50xx"
---

# AmneziaWG feed

- OpenWrt version: `25.12.1`
- Target: `qualcommax`
- Subtarget: `ipq50xx`
- Package architecture: `aarch64_cortex-a53`

## Upstream OpenWrt target

[https://downloads.openwrt.org/releases/25.12.1/targets/qualcommax/ipq50xx/](https://downloads.openwrt.org/releases/25.12.1/targets/qualcommax/ipq50xx/)

## Configure Feed

```sh
mkdir -p /etc/apk/keys
wget -O /etc/apk/keys/awg-openwrt-feed.pem "https://slava-shchipunov.github.io/awg-openwrt/keys/awg-openwrt-feed.pem"
echo "https://slava-shchipunov.github.io/awg-openwrt/25.12.1/qualcommax/ipq50xx/packages.adb" >> /etc/apk/repositories.d/customfeeds.list
```

## Install Packages

```sh
apk update
apk add amneziawg-tools kmod-amneziawg luci-proto-amneziawg
```

## Feed files

- [amneziawg-tools-1.0.20260223-r1.apk](https://slava-shchipunov.github.io/awg-openwrt/25.12.1/qualcommax/ipq50xx/amneziawg-tools-1.0.20260223-r1.apk)
- [feed.json](https://slava-shchipunov.github.io/awg-openwrt/25.12.1/qualcommax/ipq50xx/feed.json)
- [index.json](https://slava-shchipunov.github.io/awg-openwrt/25.12.1/qualcommax/ipq50xx/index.json)
- [kmod-amneziawg-6.12.74.1.0.20260329-r1.apk](https://slava-shchipunov.github.io/awg-openwrt/25.12.1/qualcommax/ipq50xx/kmod-amneziawg-6.12.74.1.0.20260329-r1.apk)
- [luci-i18n-amneziawg-ru-0.apk](https://slava-shchipunov.github.io/awg-openwrt/25.12.1/qualcommax/ipq50xx/luci-i18n-amneziawg-ru-0.apk)
- [luci-proto-amneziawg-2.0.4-r1.apk](https://slava-shchipunov.github.io/awg-openwrt/25.12.1/qualcommax/ipq50xx/luci-proto-amneziawg-2.0.4-r1.apk)
- [packages.adb](https://slava-shchipunov.github.io/awg-openwrt/25.12.1/qualcommax/ipq50xx/packages.adb)
