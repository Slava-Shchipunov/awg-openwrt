---
layout: default
title: "OpenWrt 25.12.5 ramips/mt7621"
---

# AmneziaWG feed

Index of [(root)](https://slava-shchipunov.github.io/awg-openwrt/) / [25.12.5](https://slava-shchipunov.github.io/awg-openwrt/25.12.5/) / [ramips](https://slava-shchipunov.github.io/awg-openwrt/25.12.5/ramips/)

- OpenWrt version: `25.12.5`
- Target: `ramips`
- Subtarget: `mt7621`
- Package architecture: `mipsel_24kc`

## Upstream OpenWrt target

[https://downloads.openwrt.org/releases/25.12.5/targets/ramips/mt7621/](https://downloads.openwrt.org/releases/25.12.5/targets/ramips/mt7621/)

## Configure Feed

```sh
mkdir -p /etc/apk/keys
wget -O /etc/apk/keys/awg-openwrt-feed.pem "https://slava-shchipunov.github.io/awg-openwrt/keys/awg-openwrt-feed.pem"
echo "https://slava-shchipunov.github.io/awg-openwrt/25.12.5/ramips/mt7621/packages.adb" >> /etc/apk/repositories.d/customfeeds.list
```

## Install Packages

```sh
apk update
apk add amneziawg-tools kmod-amneziawg luci-proto-amneziawg
```

<script src="https://slava-shchipunov.github.io/awg-openwrt/assets/copy-code.js?v=2"></script>

## Feed files

- [amneziawg-tools-1.0.20260618-r1.apk](https://slava-shchipunov.github.io/awg-openwrt/25.12.5/ramips/mt7621/amneziawg-tools-1.0.20260618-r1.apk)
- [feed.json](https://slava-shchipunov.github.io/awg-openwrt/25.12.5/ramips/mt7621/feed.json)
- [index.json](https://slava-shchipunov.github.io/awg-openwrt/25.12.5/ramips/mt7621/index.json)
- [kmod-amneziawg-6.12.94.1.0.20260611-r1.apk](https://slava-shchipunov.github.io/awg-openwrt/25.12.5/ramips/mt7621/kmod-amneziawg-6.12.94.1.0.20260611-r1.apk)
- [luci-i18n-amneziawg-ru-0.260630.83367.apk](https://slava-shchipunov.github.io/awg-openwrt/25.12.5/ramips/mt7621/luci-i18n-amneziawg-ru-0.260630.83367.apk)
- [luci-proto-amneziawg-2.0.4-r1.apk](https://slava-shchipunov.github.io/awg-openwrt/25.12.5/ramips/mt7621/luci-proto-amneziawg-2.0.4-r1.apk)
- [packages.adb](https://slava-shchipunov.github.io/awg-openwrt/25.12.5/ramips/mt7621/packages.adb)
