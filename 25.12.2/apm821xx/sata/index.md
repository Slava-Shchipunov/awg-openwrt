---
layout: default
title: "OpenWrt 25.12.2 apm821xx/sata"
---

# AmneziaWG feed

- OpenWrt version: `25.12.2`
- Target: `apm821xx`
- Subtarget: `sata`
- Package architecture: `powerpc_464fp`

## Upstream OpenWrt target

[https://downloads.openwrt.org/releases/25.12.2/targets/apm821xx/sata/](https://downloads.openwrt.org/releases/25.12.2/targets/apm821xx/sata/)

## Configure Feed

```sh
mkdir -p /etc/apk/keys
wget -O /etc/apk/keys/awg-openwrt-feed.pem "https://slava-shchipunov.github.io/awg-openwrt/keys/awg-openwrt-feed.pem"
echo "https://slava-shchipunov.github.io/awg-openwrt/25.12.2/apm821xx/sata/packages.adb" >> /etc/apk/repositories.d/customfeeds.list
```

## Install Packages

```sh
apk update
apk add amneziawg-tools kmod-amneziawg luci-proto-amneziawg
```

## Feed files

- [amneziawg-tools-1.0.20260223-r1.apk](https://slava-shchipunov.github.io/awg-openwrt/25.12.2/apm821xx/sata/amneziawg-tools-1.0.20260223-r1.apk)
- [feed.json](https://slava-shchipunov.github.io/awg-openwrt/25.12.2/apm821xx/sata/feed.json)
- [index.json](https://slava-shchipunov.github.io/awg-openwrt/25.12.2/apm821xx/sata/index.json)
- [kmod-amneziawg-6.12.74.1.0.20260329-r1.apk](https://slava-shchipunov.github.io/awg-openwrt/25.12.2/apm821xx/sata/kmod-amneziawg-6.12.74.1.0.20260329-r1.apk)
- [luci-i18n-amneziawg-ru-0.260508.67428.apk](https://slava-shchipunov.github.io/awg-openwrt/25.12.2/apm821xx/sata/luci-i18n-amneziawg-ru-0.260508.67428.apk)
- [luci-proto-amneziawg-2.0.4-r1.apk](https://slava-shchipunov.github.io/awg-openwrt/25.12.2/apm821xx/sata/luci-proto-amneziawg-2.0.4-r1.apk)
- [packages.adb](https://slava-shchipunov.github.io/awg-openwrt/25.12.2/apm821xx/sata/packages.adb)
