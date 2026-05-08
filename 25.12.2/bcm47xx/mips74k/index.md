---
layout: default
title: "OpenWrt 25.12.2 bcm47xx/mips74k"
---

# AmneziaWG feed

- OpenWrt version: `25.12.2`
- Target: `bcm47xx`
- Subtarget: `mips74k`
- Package architecture: `mipsel_74kc`

## Upstream OpenWrt target

[https://downloads.openwrt.org/releases/25.12.2/targets/bcm47xx/mips74k/](https://downloads.openwrt.org/releases/25.12.2/targets/bcm47xx/mips74k/)

## Configure Feed

```sh
mkdir -p /etc/apk/keys
wget -O /etc/apk/keys/awg-openwrt-feed.pem "https://slava-shchipunov.github.io/awg-openwrt/keys/awg-openwrt-feed.pem"
echo "https://slava-shchipunov.github.io/awg-openwrt/25.12.2/bcm47xx/mips74k/packages.adb" >> /etc/apk/repositories.d/customfeeds.list
```

## Install Packages

```sh
apk update
apk add amneziawg-tools kmod-amneziawg luci-proto-amneziawg
```

## Feed files

- [amneziawg-tools-1.0.20260223-r1.apk](https://slava-shchipunov.github.io/awg-openwrt/25.12.2/bcm47xx/mips74k/amneziawg-tools-1.0.20260223-r1.apk)
- [feed.json](https://slava-shchipunov.github.io/awg-openwrt/25.12.2/bcm47xx/mips74k/feed.json)
- [index.json](https://slava-shchipunov.github.io/awg-openwrt/25.12.2/bcm47xx/mips74k/index.json)
- [kmod-amneziawg-6.12.74.1.0.20260329-r1.apk](https://slava-shchipunov.github.io/awg-openwrt/25.12.2/bcm47xx/mips74k/kmod-amneziawg-6.12.74.1.0.20260329-r1.apk)
- [luci-i18n-amneziawg-ru-0.260508.67423.apk](https://slava-shchipunov.github.io/awg-openwrt/25.12.2/bcm47xx/mips74k/luci-i18n-amneziawg-ru-0.260508.67423.apk)
- [luci-proto-amneziawg-2.0.4-r1.apk](https://slava-shchipunov.github.io/awg-openwrt/25.12.2/bcm47xx/mips74k/luci-proto-amneziawg-2.0.4-r1.apk)
- [packages.adb](https://slava-shchipunov.github.io/awg-openwrt/25.12.2/bcm47xx/mips74k/packages.adb)
