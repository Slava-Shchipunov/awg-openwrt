---
layout: default
title: "OpenWrt 25.12.2 layerscape/armv8_64b"
---

# AmneziaWG feed

- OpenWrt version: `25.12.2`
- Target: `layerscape`
- Subtarget: `armv8_64b`
- Package architecture: `aarch64_generic`

Device compatibility is determined by the OpenWrt version plus target/subtarget and the kmod kernel ABI. Package architecture is shown here as metadata from the APK repository, not as a separate user-facing choice.

## OpenWrt target

[https://downloads.openwrt.org/releases/25.12.2/targets/layerscape/armv8_64b/](https://downloads.openwrt.org/releases/25.12.2/targets/layerscape/armv8_64b/)

## Repository

```sh
echo "https://slava-shchipunov.github.io/awg-openwrt/25.12.2/layerscape/armv8_64b/packages.adb" >> /etc/apk/repositories.d/customfeeds.list
apk update
apk add amneziawg-tools kmod-amneziawg luci-proto-amneziawg
```

## Feed files

- [amneziawg-tools-1.0.20260223-r1.apk](https://slava-shchipunov.github.io/awg-openwrt/25.12.2/layerscape/armv8_64b/amneziawg-tools-1.0.20260223-r1.apk)
- [feed.json](https://slava-shchipunov.github.io/awg-openwrt/25.12.2/layerscape/armv8_64b/feed.json)
- [index.json](https://slava-shchipunov.github.io/awg-openwrt/25.12.2/layerscape/armv8_64b/index.json)
- [kmod-amneziawg-6.12.74.1.0.20260329-r1.apk](https://slava-shchipunov.github.io/awg-openwrt/25.12.2/layerscape/armv8_64b/kmod-amneziawg-6.12.74.1.0.20260329-r1.apk)
- [luci-i18n-amneziawg-ru-0.apk](https://slava-shchipunov.github.io/awg-openwrt/25.12.2/layerscape/armv8_64b/luci-i18n-amneziawg-ru-0.apk)
- [luci-proto-amneziawg-2.0.4-r1.apk](https://slava-shchipunov.github.io/awg-openwrt/25.12.2/layerscape/armv8_64b/luci-proto-amneziawg-2.0.4-r1.apk)
- [packages.adb](https://slava-shchipunov.github.io/awg-openwrt/25.12.2/layerscape/armv8_64b/packages.adb)
