include $(TOPDIR)/rules.mk

PKG_VERSION:=2.2.0

LUCI_TITLE:=Support for AmneziaWG VPN
LUCI_DEPENDS:=+amneziawg-tools +ucode +luci-lib-uqr +resolveip
LUCI_PKGARCH:=all

PKG_LICENSE:=Apache-2.0
PKG_MAINTAINER:=Amnezia Admin <admin@amnezia.org>

include $(TOPDIR)/feeds/luci/luci.mk

# call BuildPackage - OpenWrt buildroot signature
