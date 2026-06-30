# Custom package feed (GitHub Pages)

Этот репозиторий публикует полноценный OpenWrt package feed для OpenWrt 25.x и новее, где используется `apk` и APK v3 metadata.

OpenWrt 24.x и более старые версии в GitHub Pages feed не поддерживаются. Для них используйте `.ipk` пакеты из GitHub Releases.

Feed публикуется workflow `.github/workflows/build-feed.yml` в ветку `gh-pages` в формате:

`/<openwrt-version>/<target>/<subtarget>/`

Пример:

`/25.12.3/mediatek/filogic/`

Корневой сайт feed:

`https://slava-shchipunov.github.io/awg-openwrt/`

Навигация на сайте построена по уровням:

`/<openwrt-version>/`

`/<openwrt-version>/<target>/`

`/<openwrt-version>/<target>/<subtarget>/`

В feed публикуются:

- `.apk` packages
- `packages.adb`
- SDK-generated APK repository metadata
- public signing key для проверки metadata

## OpenWrt 25.x

Сначала установите public signing key:

```sh
mkdir -p /etc/apk/keys
wget -O /etc/apk/keys/awg-openwrt-feed.pem https://slava-shchipunov.github.io/awg-openwrt/keys/awg-openwrt-feed.pem
```

Затем добавьте feed (замените `VERSION`, `TARGET`, `SUBTARGET`):

```sh
echo "https://slava-shchipunov.github.io/awg-openwrt/VERSION/TARGET/SUBTARGET/packages.adb" >> /etc/apk/repositories.d/customfeeds.list
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

`https://slava-shchipunov.github.io/awg-openwrt/keys/awg-openwrt-feed.pem`

Для доверенной установки добавьте public key в `/etc/apk/keys/`:

```sh
mkdir -p /etc/apk/keys
wget -O /etc/apk/keys/awg-openwrt-feed.pem https://slava-shchipunov.github.io/awg-openwrt/keys/awg-openwrt-feed.pem
apk update
```

Workflow подписывает все matrix jobs одним стабильным keypair из GitHub Secrets:

- `AWG_FEED_APK_PRIVATE_KEY`
- `AWG_FEED_APK_PUBLIC_KEY`

Сгенерировать keypair можно командой:

```sh
openssl ecparam -name prime256v1 -genkey -noout -out awg-openwrt-feed.pem
openssl ec -in awg-openwrt-feed.pem -pubout > awg-openwrt-feed.pub.pem
```

В secrets нужно сохранить содержимое файлов `awg-openwrt-feed.pem` и `awg-openwrt-feed.pub.pem`. Private key не публикуется; public key публикуется на GitHub Pages как `keys/awg-openwrt-feed.pem`.
