---
layout: default
title: "OpenWrt 25.12.0 lantiq/xrx200_legacy"
---

# AmneziaWG feed

Index of [(root)](https://slava-shchipunov.github.io/awg-openwrt/) / [25.12.0](https://slava-shchipunov.github.io/awg-openwrt/25.12.0/) / [lantiq](https://slava-shchipunov.github.io/awg-openwrt/25.12.0/lantiq/) / [xrx200_legacy](https://slava-shchipunov.github.io/awg-openwrt/25.12.0/lantiq/xrx200_legacy/)

- OpenWrt version: `25.12.0`
- Target: `lantiq`
- Subtarget: `xrx200_legacy`
- Package architecture: `mips_24kc`

## Upstream OpenWrt target

[https://downloads.openwrt.org/releases/25.12.0/targets/lantiq/xrx200_legacy/](https://downloads.openwrt.org/releases/25.12.0/targets/lantiq/xrx200_legacy/)

## Configure Feed

```sh
mkdir -p /etc/apk/keys
wget -O /etc/apk/keys/awg-openwrt-feed.pem "https://slava-shchipunov.github.io/awg-openwrt/keys/awg-openwrt-feed.pem"
echo "https://slava-shchipunov.github.io/awg-openwrt/25.12.0/lantiq/xrx200_legacy/packages.adb" >> /etc/apk/repositories.d/customfeeds.list
```

## Install Packages

```sh
apk update
apk add amneziawg-tools kmod-amneziawg luci-proto-amneziawg
```

<script src="https://slava-shchipunov.github.io/awg-openwrt/assets/copy-code.js"></script>

## Feed files

- [amneziawg-tools-1.0.20260223-r1.apk](https://slava-shchipunov.github.io/awg-openwrt/25.12.0/lantiq/xrx200_legacy/amneziawg-tools-1.0.20260223-r1.apk)
- [feed.json](https://slava-shchipunov.github.io/awg-openwrt/25.12.0/lantiq/xrx200_legacy/feed.json)
- [index.json](https://slava-shchipunov.github.io/awg-openwrt/25.12.0/lantiq/xrx200_legacy/index.json)
- [kmod-amneziawg-6.12.71.1.0.20260329-r1.apk](https://slava-shchipunov.github.io/awg-openwrt/25.12.0/lantiq/xrx200_legacy/kmod-amneziawg-6.12.71.1.0.20260329-r1.apk)
- [luci-i18n-amneziawg-ru-0.260508.63808.apk](https://slava-shchipunov.github.io/awg-openwrt/25.12.0/lantiq/xrx200_legacy/luci-i18n-amneziawg-ru-0.260508.63808.apk)
- [luci-i18n-amneziawg-ru-0.apk](https://slava-shchipunov.github.io/awg-openwrt/25.12.0/lantiq/xrx200_legacy/luci-i18n-amneziawg-ru-0.apk)
- [luci-proto-amneziawg-2.0.4-r1.apk](https://slava-shchipunov.github.io/awg-openwrt/25.12.0/lantiq/xrx200_legacy/luci-proto-amneziawg-2.0.4-r1.apk)
- [packages.adb](https://slava-shchipunov.github.io/awg-openwrt/25.12.0/lantiq/xrx200_legacy/packages.adb)
