---
layout: default
title: "OpenWrt 25.12.1 x86/legacy"
---

# AmneziaWG feed

Index of [(root)](https://slava-shchipunov.github.io/awg-openwrt/) / [25.12.1](https://slava-shchipunov.github.io/awg-openwrt/25.12.1/) / [x86](https://slava-shchipunov.github.io/awg-openwrt/25.12.1/x86/) / [legacy](https://slava-shchipunov.github.io/awg-openwrt/25.12.1/x86/legacy/)

- OpenWrt version: `25.12.1`
- Target: `x86`
- Subtarget: `legacy`
- Package architecture: `i386_pentium-mmx`

## Upstream OpenWrt target

[https://downloads.openwrt.org/releases/25.12.1/targets/x86/legacy/](https://downloads.openwrt.org/releases/25.12.1/targets/x86/legacy/)

## Configure Feed

```sh
mkdir -p /etc/apk/keys
wget -O /etc/apk/keys/awg-openwrt-feed.pem "https://slava-shchipunov.github.io/awg-openwrt/keys/awg-openwrt-feed.pem"
echo "https://slava-shchipunov.github.io/awg-openwrt/25.12.1/x86/legacy/packages.adb" >> /etc/apk/repositories.d/customfeeds.list
```

## Install Packages

```sh
apk update
apk add amneziawg-tools kmod-amneziawg luci-proto-amneziawg
```

## Feed files

- [amneziawg-tools-1.0.20260223-r1.apk](https://slava-shchipunov.github.io/awg-openwrt/25.12.1/x86/legacy/amneziawg-tools-1.0.20260223-r1.apk)
- [feed.json](https://slava-shchipunov.github.io/awg-openwrt/25.12.1/x86/legacy/feed.json)
- [index.json](https://slava-shchipunov.github.io/awg-openwrt/25.12.1/x86/legacy/index.json)
- [kmod-amneziawg-6.12.74.1.0.20260329-r1.apk](https://slava-shchipunov.github.io/awg-openwrt/25.12.1/x86/legacy/kmod-amneziawg-6.12.74.1.0.20260329-r1.apk)
- [luci-i18n-amneziawg-ru-0.260508.66987.apk](https://slava-shchipunov.github.io/awg-openwrt/25.12.1/x86/legacy/luci-i18n-amneziawg-ru-0.260508.66987.apk)
- [luci-i18n-amneziawg-ru-0.apk](https://slava-shchipunov.github.io/awg-openwrt/25.12.1/x86/legacy/luci-i18n-amneziawg-ru-0.apk)
- [luci-proto-amneziawg-2.0.4-r1.apk](https://slava-shchipunov.github.io/awg-openwrt/25.12.1/x86/legacy/luci-proto-amneziawg-2.0.4-r1.apk)
- [packages.adb](https://slava-shchipunov.github.io/awg-openwrt/25.12.1/x86/legacy/packages.adb)
