---
layout: default
title: "OpenWrt 25.12.3 sunxi/arm926ejs"
---

# AmneziaWG feed

Index of [(root)](https://slava-shchipunov.github.io/awg-openwrt/) / [25.12.3](https://slava-shchipunov.github.io/awg-openwrt/25.12.3/) / [sunxi](https://slava-shchipunov.github.io/awg-openwrt/25.12.3/sunxi/)

- OpenWrt version: `25.12.3`
- Target: `sunxi`
- Subtarget: `arm926ejs`
- Package architecture: `arm_arm926ej-s`

## Upstream OpenWrt target

[https://downloads.openwrt.org/releases/25.12.3/targets/sunxi/arm926ejs/](https://downloads.openwrt.org/releases/25.12.3/targets/sunxi/arm926ejs/)

## Configure Feed

```sh
mkdir -p /etc/apk/keys
wget -O /etc/apk/keys/awg-openwrt-feed.pem "https://slava-shchipunov.github.io/awg-openwrt/keys/awg-openwrt-feed.pem"
echo "https://slava-shchipunov.github.io/awg-openwrt/25.12.3/sunxi/arm926ejs/packages.adb" >> /etc/apk/repositories.d/customfeeds.list
```

## Install Packages

```sh
apk update
apk add amneziawg-tools kmod-amneziawg luci-proto-amneziawg
```

<script src="https://slava-shchipunov.github.io/awg-openwrt/assets/copy-code.js?v=2"></script>

## Feed files

- [amneziawg-tools-1.0.20260223-r1.apk](https://slava-shchipunov.github.io/awg-openwrt/25.12.3/sunxi/arm926ejs/amneziawg-tools-1.0.20260223-r1.apk)
- [feed.json](https://slava-shchipunov.github.io/awg-openwrt/25.12.3/sunxi/arm926ejs/feed.json)
- [index.json](https://slava-shchipunov.github.io/awg-openwrt/25.12.3/sunxi/arm926ejs/index.json)
- [kmod-amneziawg-6.12.85.1.0.20260329-r1.apk](https://slava-shchipunov.github.io/awg-openwrt/25.12.3/sunxi/arm926ejs/kmod-amneziawg-6.12.85.1.0.20260329-r1.apk)
- [luci-i18n-amneziawg-ru-0.260509.08569.apk](https://slava-shchipunov.github.io/awg-openwrt/25.12.3/sunxi/arm926ejs/luci-i18n-amneziawg-ru-0.260509.08569.apk)
- [luci-proto-amneziawg-2.0.4-r1.apk](https://slava-shchipunov.github.io/awg-openwrt/25.12.3/sunxi/arm926ejs/luci-proto-amneziawg-2.0.4-r1.apk)
- [packages.adb](https://slava-shchipunov.github.io/awg-openwrt/25.12.3/sunxi/arm926ejs/packages.adb)
