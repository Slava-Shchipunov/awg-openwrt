---
layout: default
title: "OpenWrt 25.12.1 bcm27xx/bcm2711"
---

# AmneziaWG feed

- OpenWrt version: `25.12.1`
- Target: `bcm27xx`
- Subtarget: `bcm2711`
- Package architecture: `aarch64_cortex-a72`

Device compatibility is determined by the OpenWrt version plus target/subtarget and the kmod kernel ABI. Package architecture is shown here as metadata from the APK repository, not as a separate user-facing choice.

## OpenWrt target

[https://downloads.openwrt.org/releases/25.12.1/targets/bcm27xx/bcm2711/](https://downloads.openwrt.org/releases/25.12.1/targets/bcm27xx/bcm2711/)

## Repository

```sh
mkdir -p /etc/apk/keys
wget -O /etc/apk/keys/awg-openwrt-feed.pub "https://slava-shchipunov.github.io/awg-openwrt/keys/awg-openwrt-feed.pub"
echo "https://slava-shchipunov.github.io/awg-openwrt/25.12.1/bcm27xx/bcm2711/packages.adb" >> /etc/apk/repositories.d/customfeeds.list
apk update
apk add amneziawg-tools kmod-amneziawg luci-proto-amneziawg
```

## Feed files

- [amneziawg-tools-1.0.20260223-r1.apk](https://slava-shchipunov.github.io/awg-openwrt/25.12.1/bcm27xx/bcm2711/amneziawg-tools-1.0.20260223-r1.apk)
- [feed.json](https://slava-shchipunov.github.io/awg-openwrt/25.12.1/bcm27xx/bcm2711/feed.json)
- [index.json](https://slava-shchipunov.github.io/awg-openwrt/25.12.1/bcm27xx/bcm2711/index.json)
- [kmod-amneziawg-6.12.74.1.0.20260329-r1.apk](https://slava-shchipunov.github.io/awg-openwrt/25.12.1/bcm27xx/bcm2711/kmod-amneziawg-6.12.74.1.0.20260329-r1.apk)
- [luci-i18n-amneziawg-ru-0.apk](https://slava-shchipunov.github.io/awg-openwrt/25.12.1/bcm27xx/bcm2711/luci-i18n-amneziawg-ru-0.apk)
- [luci-proto-amneziawg-2.0.4-r1.apk](https://slava-shchipunov.github.io/awg-openwrt/25.12.1/bcm27xx/bcm2711/luci-proto-amneziawg-2.0.4-r1.apk)
- [packages.adb](https://slava-shchipunov.github.io/awg-openwrt/25.12.1/bcm27xx/bcm2711/packages.adb)
