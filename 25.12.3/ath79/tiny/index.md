---
layout: default
title: "OpenWrt 25.12.3 ath79/tiny"
---

# AmneziaWG feed

Index of [(root)](https://slava-shchipunov.github.io/awg-openwrt/) / [25.12.3](https://slava-shchipunov.github.io/awg-openwrt/25.12.3/) / [ath79](https://slava-shchipunov.github.io/awg-openwrt/25.12.3/ath79/) / [tiny](https://slava-shchipunov.github.io/awg-openwrt/25.12.3/ath79/tiny/)

- OpenWrt version: `25.12.3`
- Target: `ath79`
- Subtarget: `tiny`
- Package architecture: `mips_24kc`

## Upstream OpenWrt target

[https://downloads.openwrt.org/releases/25.12.3/targets/ath79/tiny/](https://downloads.openwrt.org/releases/25.12.3/targets/ath79/tiny/)

## Configure Feed

```sh
mkdir -p /etc/apk/keys
wget -O /etc/apk/keys/awg-openwrt-feed.pem "https://slava-shchipunov.github.io/awg-openwrt/keys/awg-openwrt-feed.pem"
echo "https://slava-shchipunov.github.io/awg-openwrt/25.12.3/ath79/tiny/packages.adb" >> /etc/apk/repositories.d/customfeeds.list
```

## Install Packages

```sh
apk update
apk add amneziawg-tools kmod-amneziawg luci-proto-amneziawg
```

## Feed files

- [amneziawg-tools-1.0.20260223-r1.apk](https://slava-shchipunov.github.io/awg-openwrt/25.12.3/ath79/tiny/amneziawg-tools-1.0.20260223-r1.apk)
- [feed.json](https://slava-shchipunov.github.io/awg-openwrt/25.12.3/ath79/tiny/feed.json)
- [index.json](https://slava-shchipunov.github.io/awg-openwrt/25.12.3/ath79/tiny/index.json)
- [kmod-amneziawg-6.12.85.1.0.20260329-r1.apk](https://slava-shchipunov.github.io/awg-openwrt/25.12.3/ath79/tiny/kmod-amneziawg-6.12.85.1.0.20260329-r1.apk)
- [luci-i18n-amneziawg-ru-0.260509.07198.apk](https://slava-shchipunov.github.io/awg-openwrt/25.12.3/ath79/tiny/luci-i18n-amneziawg-ru-0.260509.07198.apk)
- [luci-proto-amneziawg-2.0.4-r1.apk](https://slava-shchipunov.github.io/awg-openwrt/25.12.3/ath79/tiny/luci-proto-amneziawg-2.0.4-r1.apk)
- [packages.adb](https://slava-shchipunov.github.io/awg-openwrt/25.12.3/ath79/tiny/packages.adb)
