#
# Copyright (C) 2016 Dan Luedtke <mail@danrl.com>
#
# This is free software, licensed under the Apache License, Version 2.0 .
#

include $(TOPDIR)/rules.mk

LUCI_TITLE:=Support for AmneziaWG VPN
LUCI_DEPENDS:=+amneziawg-tools +ucode +qrencode
LUCI_PKGARCH:=all

PKG_PROVIDES:=luci-app-amneziawg

include $(TOPDIR)/feeds/luci/luci.mk

# call BuildPackage - OpenWrt buildroot signature
