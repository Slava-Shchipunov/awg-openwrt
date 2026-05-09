---
layout: default
title: "OpenWrt 25.12.3 realtek/rtl930x"
---

# AmneziaWG feed

Index of [(root)](https://slava-shchipunov.github.io/awg-openwrt/) / [25.12.3](https://slava-shchipunov.github.io/awg-openwrt/25.12.3/) / [realtek](https://slava-shchipunov.github.io/awg-openwrt/25.12.3/realtek/) / [rtl930x](https://slava-shchipunov.github.io/awg-openwrt/25.12.3/realtek/rtl930x/)

- OpenWrt version: `25.12.3`
- Target: `realtek`
- Subtarget: `rtl930x`
- Package architecture: `mips_24kc`

## Upstream OpenWrt target

[https://downloads.openwrt.org/releases/25.12.3/targets/realtek/rtl930x/](https://downloads.openwrt.org/releases/25.12.3/targets/realtek/rtl930x/)

## Configure Feed

```sh
mkdir -p /etc/apk/keys
wget -O /etc/apk/keys/awg-openwrt-feed.pem "https://slava-shchipunov.github.io/awg-openwrt/keys/awg-openwrt-feed.pem"
echo "https://slava-shchipunov.github.io/awg-openwrt/25.12.3/realtek/rtl930x/packages.adb" >> /etc/apk/repositories.d/customfeeds.list
```

## Install Packages

```sh
apk update
apk add amneziawg-tools kmod-amneziawg luci-proto-amneziawg
```

## Feed files

- [amneziawg-tools-1.0.20260223-r1.apk](https://slava-shchipunov.github.io/awg-openwrt/25.12.3/realtek/rtl930x/amneziawg-tools-1.0.20260223-r1.apk)
- [feed.json](https://slava-shchipunov.github.io/awg-openwrt/25.12.3/realtek/rtl930x/feed.json)
- [index.json](https://slava-shchipunov.github.io/awg-openwrt/25.12.3/realtek/rtl930x/index.json)
- [kmod-amneziawg-6.12.85.1.0.20260329-r1.apk](https://slava-shchipunov.github.io/awg-openwrt/25.12.3/realtek/rtl930x/kmod-amneziawg-6.12.85.1.0.20260329-r1.apk)
- [luci-i18n-amneziawg-ru-0.260509.08742.apk](https://slava-shchipunov.github.io/awg-openwrt/25.12.3/realtek/rtl930x/luci-i18n-amneziawg-ru-0.260509.08742.apk)
- [luci-proto-amneziawg-2.0.4-r1.apk](https://slava-shchipunov.github.io/awg-openwrt/25.12.3/realtek/rtl930x/luci-proto-amneziawg-2.0.4-r1.apk)
- [packages.adb](https://slava-shchipunov.github.io/awg-openwrt/25.12.3/realtek/rtl930x/packages.adb)
