---
layout: default
title: "OpenWrt 25.12.0 imx/cortexa53"
---

# AmneziaWG feed

Index of [(root)](https://slava-shchipunov.github.io/awg-openwrt/) / [25.12.0](https://slava-shchipunov.github.io/awg-openwrt/25.12.0/) / [imx](https://slava-shchipunov.github.io/awg-openwrt/25.12.0/imx/) / [cortexa53](https://slava-shchipunov.github.io/awg-openwrt/25.12.0/imx/cortexa53/)

- OpenWrt version: `25.12.0`
- Target: `imx`
- Subtarget: `cortexa53`
- Package architecture: `aarch64_cortex-a53`

## Upstream OpenWrt target

[https://downloads.openwrt.org/releases/25.12.0/targets/imx/cortexa53/](https://downloads.openwrt.org/releases/25.12.0/targets/imx/cortexa53/)

## Configure Feed

```sh
mkdir -p /etc/apk/keys
wget -O /etc/apk/keys/awg-openwrt-feed.pem "https://slava-shchipunov.github.io/awg-openwrt/keys/awg-openwrt-feed.pem"
echo "https://slava-shchipunov.github.io/awg-openwrt/25.12.0/imx/cortexa53/packages.adb" >> /etc/apk/repositories.d/customfeeds.list
```

## Install Packages

```sh
apk update
apk add amneziawg-tools kmod-amneziawg luci-proto-amneziawg
```

<script src="https://slava-shchipunov.github.io/awg-openwrt/assets/copy-code.js"></script>

## Feed files

- [amneziawg-tools-1.0.20260223-r1.apk](https://slava-shchipunov.github.io/awg-openwrt/25.12.0/imx/cortexa53/amneziawg-tools-1.0.20260223-r1.apk)
- [feed.json](https://slava-shchipunov.github.io/awg-openwrt/25.12.0/imx/cortexa53/feed.json)
- [index.json](https://slava-shchipunov.github.io/awg-openwrt/25.12.0/imx/cortexa53/index.json)
- [kmod-amneziawg-6.12.71.1.0.20260329-r1.apk](https://slava-shchipunov.github.io/awg-openwrt/25.12.0/imx/cortexa53/kmod-amneziawg-6.12.71.1.0.20260329-r1.apk)
- [luci-i18n-amneziawg-ru-0.260508.62503.apk](https://slava-shchipunov.github.io/awg-openwrt/25.12.0/imx/cortexa53/luci-i18n-amneziawg-ru-0.260508.62503.apk)
- [luci-i18n-amneziawg-ru-0.apk](https://slava-shchipunov.github.io/awg-openwrt/25.12.0/imx/cortexa53/luci-i18n-amneziawg-ru-0.apk)
- [luci-proto-amneziawg-2.0.4-r1.apk](https://slava-shchipunov.github.io/awg-openwrt/25.12.0/imx/cortexa53/luci-proto-amneziawg-2.0.4-r1.apk)
- [packages.adb](https://slava-shchipunov.github.io/awg-openwrt/25.12.0/imx/cortexa53/packages.adb)
