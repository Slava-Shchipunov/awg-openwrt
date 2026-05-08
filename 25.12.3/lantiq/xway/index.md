---
layout: default
title: "OpenWrt 25.12.3 lantiq/xway"
---

# AmneziaWG feed

- OpenWrt version: `25.12.3`
- Target: `lantiq`
- Subtarget: `xway`
- Package architecture: `mips_24kc`

Device compatibility is determined by the OpenWrt version plus target/subtarget and the kmod kernel ABI. Package architecture is shown here as metadata from the APK repository, not as a separate user-facing choice.

## OpenWrt target

[https://downloads.openwrt.org/releases/25.12.3/targets/lantiq/xway/](https://downloads.openwrt.org/releases/25.12.3/targets/lantiq/xway/)

## Repository

```sh
echo "https://slava-shchipunov.github.io/awg-openwrt/25.12.3/lantiq/xway/packages.adb" >> /etc/apk/repositories.d/customfeeds.list
apk update
apk add amneziawg-tools kmod-amneziawg luci-proto-amneziawg
```

## Feed files

- [amneziawg-tools-1.0.20260223-r1.apk](https://slava-shchipunov.github.io/awg-openwrt/25.12.3/lantiq/xway/amneziawg-tools-1.0.20260223-r1.apk)
- [feed.json](https://slava-shchipunov.github.io/awg-openwrt/25.12.3/lantiq/xway/feed.json)
- [index.json](https://slava-shchipunov.github.io/awg-openwrt/25.12.3/lantiq/xway/index.json)
- [kmod-amneziawg-6.12.85.1.0.20260329-r1.apk](https://slava-shchipunov.github.io/awg-openwrt/25.12.3/lantiq/xway/kmod-amneziawg-6.12.85.1.0.20260329-r1.apk)
- [luci-i18n-amneziawg-ru-0.apk](https://slava-shchipunov.github.io/awg-openwrt/25.12.3/lantiq/xway/luci-i18n-amneziawg-ru-0.apk)
- [luci-proto-amneziawg-2.0.4-r1.apk](https://slava-shchipunov.github.io/awg-openwrt/25.12.3/lantiq/xway/luci-proto-amneziawg-2.0.4-r1.apk)
- [packages.adb](https://slava-shchipunov.github.io/awg-openwrt/25.12.3/lantiq/xway/packages.adb)
