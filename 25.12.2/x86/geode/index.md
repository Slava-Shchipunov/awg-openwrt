---
layout: default
title: "OpenWrt 25.12.2 x86/geode"
---

# AmneziaWG feed

- OpenWrt version: `25.12.2`
- Target: `x86`
- Subtarget: `geode`
- Package architecture: `i386_pentium-mmx`

Device compatibility is determined by the OpenWrt version plus target/subtarget and the kmod kernel ABI. Package architecture is shown here as metadata from the APK repository, not as a separate user-facing choice.

## OpenWrt target

[https://downloads.openwrt.org/releases/25.12.2/targets/x86/geode/](https://downloads.openwrt.org/releases/25.12.2/targets/x86/geode/)

## Repository

```sh
echo "https://slava-shchipunov.github.io/awg-openwrt/25.12.2/x86/geode/packages.adb" >> /etc/apk/repositories.d/customfeeds.list
apk update
apk add amneziawg-tools kmod-amneziawg luci-proto-amneziawg
```

## Feed files

- [amneziawg-tools-1.0.20260223-r1.apk](https://slava-shchipunov.github.io/awg-openwrt/25.12.2/x86/geode/amneziawg-tools-1.0.20260223-r1.apk)
- [feed.json](https://slava-shchipunov.github.io/awg-openwrt/25.12.2/x86/geode/feed.json)
- [index.json](https://slava-shchipunov.github.io/awg-openwrt/25.12.2/x86/geode/index.json)
- [kmod-amneziawg-6.12.74.1.0.20260329-r1.apk](https://slava-shchipunov.github.io/awg-openwrt/25.12.2/x86/geode/kmod-amneziawg-6.12.74.1.0.20260329-r1.apk)
- [luci-i18n-amneziawg-ru-0.apk](https://slava-shchipunov.github.io/awg-openwrt/25.12.2/x86/geode/luci-i18n-amneziawg-ru-0.apk)
- [luci-proto-amneziawg-2.0.4-r1.apk](https://slava-shchipunov.github.io/awg-openwrt/25.12.2/x86/geode/luci-proto-amneziawg-2.0.4-r1.apk)
- [packages.adb](https://slava-shchipunov.github.io/awg-openwrt/25.12.2/x86/geode/packages.adb)
