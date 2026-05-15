---
layout: default
title: "OpenWrt 25.12.4 imx/cortexa9"
---

# AmneziaWG feed

Index of [(root)](https://slava-shchipunov.github.io/awg-openwrt/) / [25.12.4](https://slava-shchipunov.github.io/awg-openwrt/25.12.4/) / [imx](https://slava-shchipunov.github.io/awg-openwrt/25.12.4/imx/)

- OpenWrt version: `25.12.4`
- Target: `imx`
- Subtarget: `cortexa9`
- Package architecture: `arm_cortex-a9_neon`

## Upstream OpenWrt target

[https://downloads.openwrt.org/releases/25.12.4/targets/imx/cortexa9/](https://downloads.openwrt.org/releases/25.12.4/targets/imx/cortexa9/)

## Configure Feed

```sh
mkdir -p /etc/apk/keys
wget -O /etc/apk/keys/awg-openwrt-feed.pem "https://slava-shchipunov.github.io/awg-openwrt/keys/awg-openwrt-feed.pem"
echo "https://slava-shchipunov.github.io/awg-openwrt/25.12.4/imx/cortexa9/packages.adb" >> /etc/apk/repositories.d/customfeeds.list
```

## Install Packages

```sh
apk update
apk add amneziawg-tools kmod-amneziawg luci-proto-amneziawg
```

<script src="https://slava-shchipunov.github.io/awg-openwrt/assets/copy-code.js?v=2"></script>

## Feed files

- [amneziawg-tools-1.0.20260223-r1.apk](https://slava-shchipunov.github.io/awg-openwrt/25.12.4/imx/cortexa9/amneziawg-tools-1.0.20260223-r1.apk)
- [feed.json](https://slava-shchipunov.github.io/awg-openwrt/25.12.4/imx/cortexa9/feed.json)
- [index.json](https://slava-shchipunov.github.io/awg-openwrt/25.12.4/imx/cortexa9/index.json)
- [kmod-amneziawg-6.12.87.1.0.20260329-r1.apk](https://slava-shchipunov.github.io/awg-openwrt/25.12.4/imx/cortexa9/kmod-amneziawg-6.12.87.1.0.20260329-r1.apk)
- [luci-i18n-amneziawg-ru-0.260515.71768.apk](https://slava-shchipunov.github.io/awg-openwrt/25.12.4/imx/cortexa9/luci-i18n-amneziawg-ru-0.260515.71768.apk)
- [luci-proto-amneziawg-2.0.4-r1.apk](https://slava-shchipunov.github.io/awg-openwrt/25.12.4/imx/cortexa9/luci-proto-amneziawg-2.0.4-r1.apk)
- [packages.adb](https://slava-shchipunov.github.io/awg-openwrt/25.12.4/imx/cortexa9/packages.adb)
