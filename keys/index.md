---
layout: default
title: Feed Signing Keys
---

# Feed signing keys

Install this public key on OpenWrt before adding the AWG feed:

```sh
mkdir -p /etc/apk/keys
wget -O /etc/apk/keys/awg-openwrt-feed.pub "https://slava-shchipunov.github.io/awg-openwrt/keys/awg-openwrt-feed.pub"
```

## Files

- [awg-openwrt-feed.pub](https://slava-shchipunov.github.io/awg-openwrt/keys/awg-openwrt-feed.pub)
