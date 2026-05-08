---
layout: default
title: "OpenWrt 25.12.3 mvebu/cortexa72"
---

# AmneziaWG feed

- OpenWrt version: `25.12.3`
- Target: `mvebu`
- Subtarget: `cortexa72`
- Package architecture: `aarch64_cortex-a72`

Device compatibility is determined by the OpenWrt version plus target/subtarget and the kmod kernel ABI. Package architecture is shown here as metadata from the APK repository, not as a separate user-facing choice.

## OpenWrt target

[https://downloads.openwrt.org/releases/25.12.3/targets/mvebu/cortexa72/](https://downloads.openwrt.org/releases/25.12.3/targets/mvebu/cortexa72/)

## Repository

```sh
echo "https://slava-shchipunov.github.io/awg-openwrt/25.12.3/mvebu/cortexa72/packages.adb" >> /etc/apk/repositories.d/customfeeds.list
apk update
apk add amneziawg-tools kmod-amneziawg luci-proto-amneziawg
```

## Feed files

- [amneziawg-tools-1.0.20260223-r1.apk](https://slava-shchipunov.github.io/awg-openwrt/25.12.3/mvebu/cortexa72/amneziawg-tools-1.0.20260223-r1.apk)
- [feed.json](https://slava-shchipunov.github.io/awg-openwrt/25.12.3/mvebu/cortexa72/feed.json)
- [index.json](https://slava-shchipunov.github.io/awg-openwrt/25.12.3/mvebu/cortexa72/index.json)
- [kmod-amneziawg-6.12.85.1.0.20260329-r1.apk](https://slava-shchipunov.github.io/awg-openwrt/25.12.3/mvebu/cortexa72/kmod-amneziawg-6.12.85.1.0.20260329-r1.apk)
- [luci-i18n-amneziawg-ru-0.apk](https://slava-shchipunov.github.io/awg-openwrt/25.12.3/mvebu/cortexa72/luci-i18n-amneziawg-ru-0.apk)
- [luci-proto-amneziawg-2.0.4-r1.apk](https://slava-shchipunov.github.io/awg-openwrt/25.12.3/mvebu/cortexa72/luci-proto-amneziawg-2.0.4-r1.apk)
- [packages.adb](https://slava-shchipunov.github.io/awg-openwrt/25.12.3/mvebu/cortexa72/packages.adb)
