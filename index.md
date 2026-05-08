---
layout: default
title: AmneziaWG OpenWrt Feed
---

# AmneziaWG OpenWrt Feed

This GitHub Pages site publishes an APK package feed for OpenWrt 25.x and newer.

OpenWrt 24.x and older are not supported by this feed. Use GitHub Releases artifacts for legacy `.ipk` packages.

## Signing key

Install the feed public key before adding the repository:

```sh
mkdir -p /etc/apk/keys
wget -O /etc/apk/keys/awg-openwrt-feed.pem "https://slava-shchipunov.github.io/awg-openwrt/keys/awg-openwrt-feed.pem"
```

Public key file: [https://slava-shchipunov.github.io/awg-openwrt/keys/awg-openwrt-feed.pem](https://slava-shchipunov.github.io/awg-openwrt/keys/awg-openwrt-feed.pem)

## Available OpenWrt versions

- [25.12.0](https://slava-shchipunov.github.io/awg-openwrt/25.12.0/)
- [25.12.1](https://slava-shchipunov.github.io/awg-openwrt/25.12.1/)
- [25.12.2](https://slava-shchipunov.github.io/awg-openwrt/25.12.2/)
- [25.12.3](https://slava-shchipunov.github.io/awg-openwrt/25.12.3/)
