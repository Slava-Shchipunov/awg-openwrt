---
layout: default
title: "OpenWrt 25.12.3 bcm47xx/legacy"
---

# AmneziaWG feed

- OpenWrt version: `25.12.3`
- Target: `bcm47xx`
- Subtarget: `legacy`
- Package architecture: `mipsel_mips32`

## Upstream OpenWrt target

[https://downloads.openwrt.org/releases/25.12.3/targets/bcm47xx/legacy/](https://downloads.openwrt.org/releases/25.12.3/targets/bcm47xx/legacy/)

## Configure Feed

```sh
mkdir -p /etc/apk/keys
wget -O /etc/apk/keys/awg-openwrt-feed.pem "https://slava-shchipunov.github.io/awg-openwrt/keys/awg-openwrt-feed.pem"
echo "https://slava-shchipunov.github.io/awg-openwrt/25.12.3/bcm47xx/legacy/packages.adb" >> /etc/apk/repositories.d/customfeeds.list
```

## Install Packages

```sh
apk update
apk add amneziawg-tools kmod-amneziawg luci-proto-amneziawg
```

## Feed files

- [amneziawg-tools-1.0.20260223-r1.apk](https://slava-shchipunov.github.io/awg-openwrt/25.12.3/bcm47xx/legacy/amneziawg-tools-1.0.20260223-r1.apk)
- [feed.json](https://slava-shchipunov.github.io/awg-openwrt/25.12.3/bcm47xx/legacy/feed.json)
- [index.json](https://slava-shchipunov.github.io/awg-openwrt/25.12.3/bcm47xx/legacy/index.json)
- [kmod-amneziawg-6.12.85.1.0.20260329-r1.apk](https://slava-shchipunov.github.io/awg-openwrt/25.12.3/bcm47xx/legacy/kmod-amneziawg-6.12.85.1.0.20260329-r1.apk)
- [luci-i18n-amneziawg-ru-0.apk](https://slava-shchipunov.github.io/awg-openwrt/25.12.3/bcm47xx/legacy/luci-i18n-amneziawg-ru-0.apk)
- [luci-proto-amneziawg-2.0.4-r1.apk](https://slava-shchipunov.github.io/awg-openwrt/25.12.3/bcm47xx/legacy/luci-proto-amneziawg-2.0.4-r1.apk)
- [packages.adb](https://slava-shchipunov.github.io/awg-openwrt/25.12.3/bcm47xx/legacy/packages.adb)
