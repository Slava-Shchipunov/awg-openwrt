---
layout: default
title: "OpenWrt 25.12.0 malta/le"
---

# AmneziaWG feed

- OpenWrt version: `25.12.0`
- Target: `malta`
- Subtarget: `le`
- Package architecture: `mipsel_24kc`

Device compatibility is determined by the OpenWrt version plus target/subtarget and the kmod kernel ABI. Package architecture is shown here as metadata from the APK repository, not as a separate user-facing choice.

## OpenWrt target

[https://downloads.openwrt.org/releases/25.12.0/targets/malta/le/](https://downloads.openwrt.org/releases/25.12.0/targets/malta/le/)

## Repository

```sh
mkdir -p /etc/apk/keys
wget -O /etc/apk/keys/awg-openwrt-feed.pub "https://slava-shchipunov.github.io/awg-openwrt/keys/awg-openwrt-feed.pub"
echo "https://slava-shchipunov.github.io/awg-openwrt/25.12.0/malta/le/packages.adb" >> /etc/apk/repositories.d/customfeeds.list
apk update
apk add amneziawg-tools kmod-amneziawg luci-proto-amneziawg
```

## Feed files

- [amneziawg-tools-1.0.20260223-r1.apk](https://slava-shchipunov.github.io/awg-openwrt/25.12.0/malta/le/amneziawg-tools-1.0.20260223-r1.apk)
- [feed.json](https://slava-shchipunov.github.io/awg-openwrt/25.12.0/malta/le/feed.json)
- [index.json](https://slava-shchipunov.github.io/awg-openwrt/25.12.0/malta/le/index.json)
- [kmod-amneziawg-6.12.71.1.0.20260329-r1.apk](https://slava-shchipunov.github.io/awg-openwrt/25.12.0/malta/le/kmod-amneziawg-6.12.71.1.0.20260329-r1.apk)
- [luci-i18n-amneziawg-ru-0.apk](https://slava-shchipunov.github.io/awg-openwrt/25.12.0/malta/le/luci-i18n-amneziawg-ru-0.apk)
- [luci-proto-amneziawg-2.0.4-r1.apk](https://slava-shchipunov.github.io/awg-openwrt/25.12.0/malta/le/luci-proto-amneziawg-2.0.4-r1.apk)
- [packages.adb](https://slava-shchipunov.github.io/awg-openwrt/25.12.0/malta/le/packages.adb)
