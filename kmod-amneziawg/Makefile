include $(TOPDIR)/rules.mk
include $(INCLUDE_DIR)/kernel.mk

PKG_NAME:=kmod-amneziawg
PKG_VERSION:=3.0.20260805
PKG_RELEASE:=1

PKG_SOURCE_PROTO:=git
PKG_SOURCE_URL:=https://github.com/amnezia-vpn/amneziawg-linux-kernel-module.git
PKG_SOURCE_VERSION:=v$(PKG_VERSION)
PKG_BUILD_DIR:=$(BUILD_DIR)/$(PKG_NAME)-$(PKG_VERSION)

PKG_LICENSE:=GPL-2.0
PKG_LICENSE_FILES:=COPYING

MAKE_PATH:=src

include $(INCLUDE_DIR)/package.mk

define KernelPackage/amneziawg
	SECTION:=kernel
	CATEGORY:=Kernel modules
	SUBMENU:=Network Support
	TITLE:=AmneziaWG VPN Kernel Module
	URL:=https://amnezia.org/
	FILES:=$(PKG_BUILD_DIR)/$(MAKE_PATH)/amneziawg.ko
	AUTOLOAD:=$(call AutoProbe,amneziawg)
	DEPENDS:= \
		+kmod-udptunnel4 \
		+IPV6:kmod-udptunnel6 \
		+kmod-crypto-kpp \
		+kmod-crypto-lib-chacha20poly1305 \
		+kmod-crypto-lib-curve25519
endef

define KernelPackage/amneziawg/description
	AmneziaWG VPN kernel module (obfuscated WireGuard fork).
endef

define Build/Prepare
	$(call Build/Prepare/Default)
	mkdir -p $(PKG_BUILD_DIR)/$(MAKE_PATH)/kernel
	$(CP) $(LINUX_DIR)/* $(PKG_BUILD_DIR)/$(MAKE_PATH)/kernel/
endef

define Build/Compile
	+$(KERNEL_MAKE) $(PKG_JOBS) \
		M="$(PKG_BUILD_DIR)/$(MAKE_PATH)" \
		EXTRA_CFLAGS="$(BUILDFLAGS)" \
		WIREGUARD_VERSION="$(PKG_VERSION)" \
		modules
endef

$(eval $(call KernelPackage,amneziawg))
