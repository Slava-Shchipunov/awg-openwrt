---
layout: default
title: "OpenWrt 25.12.1 mpc85xx/p1020"
---

# AmneziaWG feed

Index of [(root)](https://slava-shchipunov.github.io/awg-openwrt/) / [25.12.1](https://slava-shchipunov.github.io/awg-openwrt/25.12.1/) / [mpc85xx](https://slava-shchipunov.github.io/awg-openwrt/25.12.1/mpc85xx/) / [p1020](https://slava-shchipunov.github.io/awg-openwrt/25.12.1/mpc85xx/p1020/)

- OpenWrt version: `25.12.1`
- Target: `mpc85xx`
- Subtarget: `p1020`
- Package architecture: `powerpc_8548`

## Upstream OpenWrt target

[https://downloads.openwrt.org/releases/25.12.1/targets/mpc85xx/p1020/](https://downloads.openwrt.org/releases/25.12.1/targets/mpc85xx/p1020/)

## Configure Feed

```sh
mkdir -p /etc/apk/keys
wget -O /etc/apk/keys/awg-openwrt-feed.pem "https://slava-shchipunov.github.io/awg-openwrt/keys/awg-openwrt-feed.pem"
echo "https://slava-shchipunov.github.io/awg-openwrt/25.12.1/mpc85xx/p1020/packages.adb" >> /etc/apk/repositories.d/customfeeds.list
```

## Install Packages

```sh
apk update
apk add amneziawg-tools kmod-amneziawg luci-proto-amneziawg
```

<script src="https://slava-shchipunov.github.io/awg-openwrt/assets/copy-code.js?v=2"></script>

## Feed files

- [amneziawg-tools-1.0.20260223-r1.apk](https://slava-shchipunov.github.io/awg-openwrt/25.12.1/mpc85xx/p1020/amneziawg-tools-1.0.20260223-r1.apk)
- [feed.json](https://slava-shchipunov.github.io/awg-openwrt/25.12.1/mpc85xx/p1020/feed.json)
- [index.json](https://slava-shchipunov.github.io/awg-openwrt/25.12.1/mpc85xx/p1020/index.json)
- [kmod-amneziawg-6.12.74.1.0.20260329-r1.apk](https://slava-shchipunov.github.io/awg-openwrt/25.12.1/mpc85xx/p1020/kmod-amneziawg-6.12.74.1.0.20260329-r1.apk)
- [luci-i18n-amneziawg-ru-0.260508.66213.apk](https://slava-shchipunov.github.io/awg-openwrt/25.12.1/mpc85xx/p1020/luci-i18n-amneziawg-ru-0.260508.66213.apk)
- [luci-i18n-amneziawg-ru-0.apk](https://slava-shchipunov.github.io/awg-openwrt/25.12.1/mpc85xx/p1020/luci-i18n-amneziawg-ru-0.apk)
- [luci-proto-amneziawg-2.0.4-r1.apk](https://slava-shchipunov.github.io/awg-openwrt/25.12.1/mpc85xx/p1020/luci-proto-amneziawg-2.0.4-r1.apk)
- [packages.adb](https://slava-shchipunov.github.io/awg-openwrt/25.12.1/mpc85xx/p1020/packages.adb)
