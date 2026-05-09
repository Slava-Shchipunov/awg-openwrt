---
layout: default
title: "OpenWrt 25.12.1 apm821xx/nand"
---

# AmneziaWG feed

Index of [(root)](https://slava-shchipunov.github.io/awg-openwrt/) / [25.12.1](https://slava-shchipunov.github.io/awg-openwrt/25.12.1/) / [apm821xx](https://slava-shchipunov.github.io/awg-openwrt/25.12.1/apm821xx/) / [nand](https://slava-shchipunov.github.io/awg-openwrt/25.12.1/apm821xx/nand/)

- OpenWrt version: `25.12.1`
- Target: `apm821xx`
- Subtarget: `nand`
- Package architecture: `powerpc_464fp`

## Upstream OpenWrt target

[https://downloads.openwrt.org/releases/25.12.1/targets/apm821xx/nand/](https://downloads.openwrt.org/releases/25.12.1/targets/apm821xx/nand/)

## Configure Feed

```sh
mkdir -p /etc/apk/keys
wget -O /etc/apk/keys/awg-openwrt-feed.pem "https://slava-shchipunov.github.io/awg-openwrt/keys/awg-openwrt-feed.pem"
echo "https://slava-shchipunov.github.io/awg-openwrt/25.12.1/apm821xx/nand/packages.adb" >> /etc/apk/repositories.d/customfeeds.list
```

## Install Packages

```sh
apk update
apk add amneziawg-tools kmod-amneziawg luci-proto-amneziawg
```

<script src="https://slava-shchipunov.github.io/awg-openwrt/assets/copy-code.js?v=2"></script>

## Feed files

- [amneziawg-tools-1.0.20260223-r1.apk](https://slava-shchipunov.github.io/awg-openwrt/25.12.1/apm821xx/nand/amneziawg-tools-1.0.20260223-r1.apk)
- [feed.json](https://slava-shchipunov.github.io/awg-openwrt/25.12.1/apm821xx/nand/feed.json)
- [index.json](https://slava-shchipunov.github.io/awg-openwrt/25.12.1/apm821xx/nand/index.json)
- [kmod-amneziawg-6.12.74.1.0.20260329-r1.apk](https://slava-shchipunov.github.io/awg-openwrt/25.12.1/apm821xx/nand/kmod-amneziawg-6.12.74.1.0.20260329-r1.apk)
- [luci-i18n-amneziawg-ru-0.260508.67004.apk](https://slava-shchipunov.github.io/awg-openwrt/25.12.1/apm821xx/nand/luci-i18n-amneziawg-ru-0.260508.67004.apk)
- [luci-i18n-amneziawg-ru-0.apk](https://slava-shchipunov.github.io/awg-openwrt/25.12.1/apm821xx/nand/luci-i18n-amneziawg-ru-0.apk)
- [luci-proto-amneziawg-2.0.4-r1.apk](https://slava-shchipunov.github.io/awg-openwrt/25.12.1/apm821xx/nand/luci-proto-amneziawg-2.0.4-r1.apk)
- [packages.adb](https://slava-shchipunov.github.io/awg-openwrt/25.12.1/apm821xx/nand/packages.adb)
