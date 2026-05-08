---
layout: default
title: "OpenWrt 25.12.0 at91/sam9x"
---

# AmneziaWG feed

- OpenWrt version: `25.12.0`
- Target: `at91`
- Subtarget: `sam9x`
- Package architecture: `arm_arm926ej-s`

## Upstream OpenWrt target

[https://downloads.openwrt.org/releases/25.12.0/targets/at91/sam9x/](https://downloads.openwrt.org/releases/25.12.0/targets/at91/sam9x/)

## Configure Feed

```sh
mkdir -p /etc/apk/keys
wget -O /etc/apk/keys/awg-openwrt-feed.pem "https://slava-shchipunov.github.io/awg-openwrt/keys/awg-openwrt-feed.pem"
echo "https://slava-shchipunov.github.io/awg-openwrt/25.12.0/at91/sam9x/packages.adb" >> /etc/apk/repositories.d/customfeeds.list
```

## Install Packages

```sh
apk update
apk add amneziawg-tools kmod-amneziawg luci-proto-amneziawg
```

## Feed files

- [amneziawg-tools-1.0.20260223-r1.apk](https://slava-shchipunov.github.io/awg-openwrt/25.12.0/at91/sam9x/amneziawg-tools-1.0.20260223-r1.apk)
- [feed.json](https://slava-shchipunov.github.io/awg-openwrt/25.12.0/at91/sam9x/feed.json)
- [index.json](https://slava-shchipunov.github.io/awg-openwrt/25.12.0/at91/sam9x/index.json)
- [kmod-amneziawg-6.12.71.1.0.20260329-r1.apk](https://slava-shchipunov.github.io/awg-openwrt/25.12.0/at91/sam9x/kmod-amneziawg-6.12.71.1.0.20260329-r1.apk)
- [luci-i18n-amneziawg-ru-0.260508.62495.apk](https://slava-shchipunov.github.io/awg-openwrt/25.12.0/at91/sam9x/luci-i18n-amneziawg-ru-0.260508.62495.apk)
- [luci-i18n-amneziawg-ru-0.apk](https://slava-shchipunov.github.io/awg-openwrt/25.12.0/at91/sam9x/luci-i18n-amneziawg-ru-0.apk)
- [luci-proto-amneziawg-2.0.4-r1.apk](https://slava-shchipunov.github.io/awg-openwrt/25.12.0/at91/sam9x/luci-proto-amneziawg-2.0.4-r1.apk)
- [packages.adb](https://slava-shchipunov.github.io/awg-openwrt/25.12.0/at91/sam9x/packages.adb)
