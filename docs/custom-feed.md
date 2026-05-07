# Custom package feed (GitHub Pages)

Этот репозиторий поддерживает отдельный bootstrap workflow `.github/workflows/build-feed.yml`, который публикует полноценный feed в ветку `gh-pages` в формате:

`/<openwrt-version>/<target>/<subtarget>/<pkgarch>/`

Пример:

`/25.12.3/mediatek/filogic/aarch64_cortex-a53/`

В feed публикуются не только `.apk/.ipk`, но и SDK-generated metadata (`Packages`, `Packages.gz`, `Packages.sig` для opkg; `packages.adb`, `packages.adb.sig` для apk) и подписи/публичные ключи из сборки.

## OpenWRT 24.x (opkg)

Добавьте feed (замените `VERSION`, `TARGET`, `SUBTARGET`, `PKGARCH`):

```sh
echo "src/gz awg_custom https://slava-shchipunov.github.io/awg-openwrt/VERSION/TARGET/SUBTARGET/PKGARCH" >> /etc/opkg/customfeeds.conf
opkg update
opkg install amneziawg-tools kmod-amneziawg luci-proto-amneziawg
```

Если на устройстве включена проверка подписи, установите публичный ключ feed в usign keyring:

```sh
wget -O /tmp/awg-feed.pub https://slava-shchipunov.github.io/awg-openwrt/keys/<KEY_FILE>.pub
cp /tmp/awg-feed.pub /etc/opkg/keys/
opkg update
```

Ключи публикуются в стабильном пути:

`https://slava-shchipunov.github.io/awg-openwrt/keys/`

## OpenWRT 25.x (apk)

Добавьте feed (замените `VERSION`, `TARGET`, `SUBTARGET`, `PKGARCH`):

```sh
echo "https://slava-shchipunov.github.io/awg-openwrt/VERSION/TARGET/SUBTARGET/PKGARCH/packages.adb" >> /etc/apk/repositories.d/customfeeds.list
apk update
apk add amneziawg-tools kmod-amneziawg luci-proto-amneziawg
```

Минимальная проверка feed:

```sh
apk update
apk add amneziawg-tools
```

Для доверенной установки добавьте public key в `/etc/apk/keys/`:

```sh
wget -O /etc/apk/keys/awg-feed.pub https://slava-shchipunov.github.io/awg-openwrt/keys/<KEY_FILE>.pub
apk update
```

Ключи публикуются в стабильном пути:

`https://slava-shchipunov.github.io/awg-openwrt/keys/`

## ASU / owut

Для ASU/owut используйте URL feed в этом же формате:

`https://slava-shchipunov.github.io/awg-openwrt/VERSION/TARGET/SUBTARGET/PKGARCH/`

и для APK-потока индекс:

`https://slava-shchipunov.github.io/awg-openwrt/VERSION/TARGET/SUBTARGET/PKGARCH/packages.adb`
