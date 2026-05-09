---
layout: default
title: "OpenWrt 25.12.0 ipq806x/chromium"
---

# AmneziaWG feed

Index of [(root)](https://slava-shchipunov.github.io/awg-openwrt/) / [25.12.0](https://slava-shchipunov.github.io/awg-openwrt/25.12.0/) / [ipq806x](https://slava-shchipunov.github.io/awg-openwrt/25.12.0/ipq806x/) / [chromium](https://slava-shchipunov.github.io/awg-openwrt/25.12.0/ipq806x/chromium/)

- OpenWrt version: `25.12.0`
- Target: `ipq806x`
- Subtarget: `chromium`
- Package architecture: `arm_cortex-a15_neon-vfpv4`

## Upstream OpenWrt target

[https://downloads.openwrt.org/releases/25.12.0/targets/ipq806x/chromium/](https://downloads.openwrt.org/releases/25.12.0/targets/ipq806x/chromium/)

## Configure Feed

```sh
mkdir -p /etc/apk/keys
wget -O /etc/apk/keys/awg-openwrt-feed.pem "https://slava-shchipunov.github.io/awg-openwrt/keys/awg-openwrt-feed.pem"
echo "https://slava-shchipunov.github.io/awg-openwrt/25.12.0/ipq806x/chromium/packages.adb" >> /etc/apk/repositories.d/customfeeds.list
```

## Install Packages

```sh
apk update
apk add amneziawg-tools kmod-amneziawg luci-proto-amneziawg
```

<script src="https://slava-shchipunov.github.io/awg-openwrt/assets/copy-code.js"></script>

## Feed files

- [amneziawg-tools-1.0.20260223-r1.apk](https://slava-shchipunov.github.io/awg-openwrt/25.12.0/ipq806x/chromium/amneziawg-tools-1.0.20260223-r1.apk)
- [feed.json](https://slava-shchipunov.github.io/awg-openwrt/25.12.0/ipq806x/chromium/feed.json)
- [index.json](https://slava-shchipunov.github.io/awg-openwrt/25.12.0/ipq806x/chromium/index.json)
- [kmod-amneziawg-6.12.71.1.0.20260329-r1.apk](https://slava-shchipunov.github.io/awg-openwrt/25.12.0/ipq806x/chromium/kmod-amneziawg-6.12.71.1.0.20260329-r1.apk)
- [luci-i18n-amneziawg-ru-0.260508.63231.apk](https://slava-shchipunov.github.io/awg-openwrt/25.12.0/ipq806x/chromium/luci-i18n-amneziawg-ru-0.260508.63231.apk)
- [luci-i18n-amneziawg-ru-0.apk](https://slava-shchipunov.github.io/awg-openwrt/25.12.0/ipq806x/chromium/luci-i18n-amneziawg-ru-0.apk)
- [luci-proto-amneziawg-2.0.4-r1.apk](https://slava-shchipunov.github.io/awg-openwrt/25.12.0/ipq806x/chromium/luci-proto-amneziawg-2.0.4-r1.apk)
- [packages.adb](https://slava-shchipunov.github.io/awg-openwrt/25.12.0/ipq806x/chromium/packages.adb)
