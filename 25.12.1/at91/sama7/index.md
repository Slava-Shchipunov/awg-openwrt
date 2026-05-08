---
layout: default
title: "OpenWrt 25.12.1 at91/sama7"
---

# AmneziaWG feed

Index of [(root)](https://slava-shchipunov.github.io/awg-openwrt/) / [25.12.1](https://slava-shchipunov.github.io/awg-openwrt/25.12.1/) / [at91](https://slava-shchipunov.github.io/awg-openwrt/25.12.1/at91/) / [sama7](https://slava-shchipunov.github.io/awg-openwrt/25.12.1/at91/sama7/)

- OpenWrt version: `25.12.1`
- Target: `at91`
- Subtarget: `sama7`
- Package architecture: `arm_cortex-a7_vfpv4`

## Upstream OpenWrt target

[https://downloads.openwrt.org/releases/25.12.1/targets/at91/sama7/](https://downloads.openwrt.org/releases/25.12.1/targets/at91/sama7/)

## Configure Feed

```sh
mkdir -p /etc/apk/keys
wget -O /etc/apk/keys/awg-openwrt-feed.pem "https://slava-shchipunov.github.io/awg-openwrt/keys/awg-openwrt-feed.pem"
echo "https://slava-shchipunov.github.io/awg-openwrt/25.12.1/at91/sama7/packages.adb" >> /etc/apk/repositories.d/customfeeds.list
```

## Install Packages

```sh
apk update
apk add amneziawg-tools kmod-amneziawg luci-proto-amneziawg
```

## Feed files

- [amneziawg-tools-1.0.20260223-r1.apk](https://slava-shchipunov.github.io/awg-openwrt/25.12.1/at91/sama7/amneziawg-tools-1.0.20260223-r1.apk)
- [feed.json](https://slava-shchipunov.github.io/awg-openwrt/25.12.1/at91/sama7/feed.json)
- [index.json](https://slava-shchipunov.github.io/awg-openwrt/25.12.1/at91/sama7/index.json)
- [kmod-amneziawg-6.12.74.1.0.20260329-r1.apk](https://slava-shchipunov.github.io/awg-openwrt/25.12.1/at91/sama7/kmod-amneziawg-6.12.74.1.0.20260329-r1.apk)
- [luci-i18n-amneziawg-ru-0.260508.66966.apk](https://slava-shchipunov.github.io/awg-openwrt/25.12.1/at91/sama7/luci-i18n-amneziawg-ru-0.260508.66966.apk)
- [luci-i18n-amneziawg-ru-0.apk](https://slava-shchipunov.github.io/awg-openwrt/25.12.1/at91/sama7/luci-i18n-amneziawg-ru-0.apk)
- [luci-proto-amneziawg-2.0.4-r1.apk](https://slava-shchipunov.github.io/awg-openwrt/25.12.1/at91/sama7/luci-proto-amneziawg-2.0.4-r1.apk)
- [packages.adb](https://slava-shchipunov.github.io/awg-openwrt/25.12.1/at91/sama7/packages.adb)
