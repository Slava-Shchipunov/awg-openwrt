include $(TOPDIR)/rules.mk

LUCI_TITLE:=Support for AmneziaWG VPN
LUCI_DESCRIPTION:=Provides support and Web UI for AmneziaWG VPN
PKG_VERSION:=3.1.0
LUCI_DEPENDS:=+amneziawg-tools +ucode +luci-lib-uqr +resolveip
LUCI_PKGARCH:=all
PKGARCH:=all

PKG_LICENSE:=Apache-2.0

include $(TOPDIR)/feeds/luci/luci.mk

# call BuildPackage - OpenWrt buildroot signature
