---
layout: default
title: "OpenWrt 25.12.0 bcm27xx/bcm2709"
---

# AmneziaWG feed

- OpenWrt version: `25.12.0`
- Target: `bcm27xx`
- Subtarget: `bcm2709`
- Package architecture: `arm_cortex-a7_neon-vfpv4`

Device compatibility is determined by the OpenWrt version plus target/subtarget and the kmod kernel ABI. Package architecture is shown here as metadata from the APK repository, not as a separate user-facing choice.

## OpenWrt target

[https://downloads.openwrt.org/releases/25.12.0/targets/bcm27xx/bcm2709/](https://downloads.openwrt.org/releases/25.12.0/targets/bcm27xx/bcm2709/)

## Repository

```sh
mkdir -p /etc/apk/keys
wget -O /etc/apk/keys/awg-openwrt-feed.pub "https://slava-shchipunov.github.io/awg-openwrt/keys/awg-openwrt-feed.pub"
echo "https://slava-shchipunov.github.io/awg-openwrt/25.12.0/bcm27xx/bcm2709/packages.adb" >> /etc/apk/repositories.d/customfeeds.list
apk update
apk add amneziawg-tools kmod-amneziawg luci-proto-amneziawg
```

## Feed files

- [amneziawg-tools-1.0.20260223-r1.apk](https://slava-shchipunov.github.io/awg-openwrt/25.12.0/bcm27xx/bcm2709/amneziawg-tools-1.0.20260223-r1.apk)
- [feed.json](https://slava-shchipunov.github.io/awg-openwrt/25.12.0/bcm27xx/bcm2709/feed.json)
- [index.json](https://slava-shchipunov.github.io/awg-openwrt/25.12.0/bcm27xx/bcm2709/index.json)
- [kmod-amneziawg-6.12.71.1.0.20260329-r1.apk](https://slava-shchipunov.github.io/awg-openwrt/25.12.0/bcm27xx/bcm2709/kmod-amneziawg-6.12.71.1.0.20260329-r1.apk)
- [luci-i18n-amneziawg-ru-0.apk](https://slava-shchipunov.github.io/awg-openwrt/25.12.0/bcm27xx/bcm2709/luci-i18n-amneziawg-ru-0.apk)
- [luci-proto-amneziawg-2.0.4-r1.apk](https://slava-shchipunov.github.io/awg-openwrt/25.12.0/bcm27xx/bcm2709/luci-proto-amneziawg-2.0.4-r1.apk)
- [packages.adb](https://slava-shchipunov.github.io/awg-openwrt/25.12.0/bcm27xx/bcm2709/packages.adb)
