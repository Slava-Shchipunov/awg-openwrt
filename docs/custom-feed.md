# Custom package feed (GitHub Pages)

Этот репозиторий публикует полноценный OpenWrt package feed для OpenWrt 25.x и новее, где используется `apk` и APK v3 metadata.

OpenWrt 24.x и более старые версии в GitHub Pages feed не поддерживаются. Для них используйте `.ipk` пакеты из GitHub Releases.

Feed публикуется workflow `.github/workflows/build-feed.yml` в ветку `gh-pages` в формате:

`/<openwrt-version>/<target>/<subtarget>/<pkgarch>/`

Пример:

`/25.12.3/mediatek/filogic/aarch64_cortex-a53/`

В feed публикуются:

- `.apk` packages
- `packages.adb`
- SDK-generated APK repository metadata
- публичные ключи из сборки

## OpenWrt 25.x (apk)

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

## Public signing keys

Ключи публикуются в стабильном пути:

`https://slava-shchipunov.github.io/awg-openwrt/keys/`

Для доверенной установки добавьте public key в `/etc/apk/keys/`:

```sh
wget -O /etc/apk/keys/awg-feed.pub https://slava-shchipunov.github.io/awg-openwrt/keys/<KEY_FILE>.pub
apk update
```

`<KEY_FILE>.pub` нужно заменить на фактическое имя опубликованного `.pub` файла из директории `/keys/`.

## ASU / owut

Для ASU/owut используйте URL feed в формате:

`https://slava-shchipunov.github.io/awg-openwrt/VERSION/TARGET/SUBTARGET/PKGARCH/`

APK index:

`https://slava-shchipunov.github.io/awg-openwrt/VERSION/TARGET/SUBTARGET/PKGARCH/packages.adb`
