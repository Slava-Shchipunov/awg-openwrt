---
layout: default
title: "OpenWrt 25.12.0 x86/generic"
---

# AmneziaWG feed

- OpenWrt version: `25.12.0`
- Target: `x86`
- Subtarget: `generic`
- Package architecture: `i386_pentium4`

Device compatibility is determined by the OpenWrt version plus target/subtarget and the kmod kernel ABI. Package architecture is shown here as metadata from the APK repository, not as a separate user-facing choice.

## OpenWrt target

[https://downloads.openwrt.org/releases/25.12.0/targets/x86/generic/](https://downloads.openwrt.org/releases/25.12.0/targets/x86/generic/)

## Repository

```sh
mkdir -p /etc/apk/keys
wget -O /etc/apk/keys/awg-openwrt-feed.pem "https://slava-shchipunov.github.io/awg-openwrt/keys/awg-openwrt-feed.pem"
echo "https://slava-shchipunov.github.io/awg-openwrt/25.12.0/x86/generic/packages.adb" >> /etc/apk/repositories.d/customfeeds.list
apk update
apk add amneziawg-tools kmod-amneziawg luci-proto-amneziawg
```

## Feed files

- [amneziawg-tools-1.0.20260223-r1.apk](https://slava-shchipunov.github.io/awg-openwrt/25.12.0/x86/generic/amneziawg-tools-1.0.20260223-r1.apk)
- [feed.json](https://slava-shchipunov.github.io/awg-openwrt/25.12.0/x86/generic/feed.json)
- [index.json](https://slava-shchipunov.github.io/awg-openwrt/25.12.0/x86/generic/index.json)
- [kmod-amneziawg-6.12.71.1.0.20260329-r1.apk](https://slava-shchipunov.github.io/awg-openwrt/25.12.0/x86/generic/kmod-amneziawg-6.12.71.1.0.20260329-r1.apk)
- [luci-i18n-amneziawg-ru-0.apk](https://slava-shchipunov.github.io/awg-openwrt/25.12.0/x86/generic/luci-i18n-amneziawg-ru-0.apk)
- [luci-proto-amneziawg-2.0.4-r1.apk](https://slava-shchipunov.github.io/awg-openwrt/25.12.0/x86/generic/luci-proto-amneziawg-2.0.4-r1.apk)
- [packages.adb](https://slava-shchipunov.github.io/awg-openwrt/25.12.0/x86/generic/packages.adb)
