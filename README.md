# Автоматическая настройка AmneziaWG для OpenWRT версии 23.05.0 и более новых
Для автоматической настройки рекомендую использовать [скрипт](https://github.com/itdoginfo/domain-routing-openwrt) от пользователя itdog. Этот скрипт позволяет автоматически скачать нужные пакеты из собранных здесь и настроить [точечный обход блокировок по доменам](https://habr.com/ru/articles/767464/).

Если же вам нужно только установить пакеты, я добавил скрипт amneziawg-install - он автоматически скачает пакеты из этого репозитория под ваше устройство (только для стабильной версии OpenWRT), а также предложит сразу настроить интерфейс с протоколом AmneziaWG. Если пользователь согласится, нужно будет ввести параметры конфига, которые запросит скрипт. При этом скрипт создаст интерфейс, настроит для него правила фаерволла, а также **включит перенаправление всего траффика через тунель AmneziaWG** (установит в настройках Peer галочку Route Allowed IPs).
Для запуска скрипта подключитесь к роутеру по SSH, введите команду и следуйте инструкциям на экране:
```
sh <(wget -O - https://raw.githubusercontent.com/Slava-Shchipunov/awg-openwrt/refs/heads/master/amneziawg-install.sh)
```
AWG 2.0 пока не влит в мастер, поэтому можно установить из фиче ветки (при настройке скриптом параметры S3, S4 и все I параметры нужно будет ввести вручную через luci или в /etc/config/network, позже доработаю скрипт):
```
sh <(wget -O - https://raw.githubusercontent.com/Slava-Shchipunov/awg-openwrt/refs/heads/feat/awg-2.0/amneziawg-install.sh)
```

# Сборка пакетов для всех устройств, поддерживающих OpenWRT
В репозиторий добавлен скрипт, который парсит данные о поддерживаемых платформах со страницы OpenWRT и автоматически запускает сборку пакетов AmneziaWG для всех устройств.
На данный момент я собрал пакеты для всех устройств для OpenWRT версий:
1) [23.05.0](https://github.com/Slava-Shchipunov/awg-openwrt/releases/tag/v23.05.0)
2) [23.05.1](https://github.com/Slava-Shchipunov/awg-openwrt/releases/tag/v23.05.1)
3) [23.05.2](https://github.com/Slava-Shchipunov/awg-openwrt/releases/tag/v23.05.2)
4) [23.05.3](https://github.com/Slava-Shchipunov/awg-openwrt/releases/tag/v23.05.3)
5) [23.05.4](https://github.com/Slava-Shchipunov/awg-openwrt/releases/tag/v23.05.4)
6) [23.05.5](https://github.com/Slava-Shchipunov/awg-openwrt/releases/tag/v23.05.5)
7) AWG-2.0 [23.05.6](https://github.com/Slava-Shchipunov/awg-openwrt/releases/tag/v23.05.6)
8) [24.10.0](https://github.com/Slava-Shchipunov/awg-openwrt/releases/tag/v24.10.0)
9) [24.10.1](https://github.com/Slava-Shchipunov/awg-openwrt/releases/tag/v24.10.1)
10) [24.10.2](https://github.com/Slava-Shchipunov/awg-openwrt/releases/tag/v24.10.2)
11) AWG-2.0 [24.10.3](https://github.com/Slava-Shchipunov/awg-openwrt/releases/tag/v24.10.3)

Также запускал сборку для версии [22.03.7](https://github.com/Slava-Shchipunov/awg-openwrt/releases/tag/v22.03.7), но там для двух платформ сборка завершилась ошибкой. Так как это достаточно старая версия OpenWRT, я не стал разбираться, в чем проблема.

В дальнейшем при выходе новых релизов OpenWRT будут автоматически создаваться релизы с пакетами AmneziaWG и запускаться сборка пакетов под все устройства, поддерживаемые новой версией. Github action для проверки появления нового релиза запускается автоматически раз в 3 дня, а также может быть запущен вручную.

## Выбор пакетов для своего устройства
В соответствии с пунктом [Указываем переменные для сборки](https://github.com/itdoginfo/domain-routing-openwrt/wiki/Amnezia-WG-Build#%D1%83%D0%BA%D0%B0%D0%B7%D1%8B%D0%B2%D0%B0%D0%B5%D0%BC-%D0%BF%D0%B5%D1%80%D0%B5%D0%BC%D0%B5%D0%BD%D0%BD%D1%8B%D0%B5-%D0%B4%D0%BB%D1%8F-%D1%81%D0%B1%D0%BE%D1%80%D0%BA%D0%B8)
определить `target` и `subtarget` вашего устройства. Далее перейти на страницу релиза, соответствующего вашей версии OpenWRT, затем поиском по странице (Ctrl+F) найти 3 пакета, название которых оканчивается на `target_subtarget.ipk`, соответствующие вашему устройству.

## Как запустить сборку для всех поддерживаемых устройств
1) Создать форк этого репозитория
2) Переключиться на вкладку Actions и включить Github actions (по умолчанию для форков они выключены)
3) Затем перейти на вкладку Code => Releases (в правой части экрана) => Draft a new release
4) Нажать Choose a tag и создать новый тег формата vX.X.X, где вместо X.X.X нужно подставить требуемую версию OpenWRT, например, v23.05.4
5) Выбрать в качестве target ветку `master`
6) Ввести Release title
7) Нажать внизу зеленую кнопку Publish release

Для публичных репозиториев Github предоставляет неограниченное по времени использование раннеров, у меня запускалось до 20 параллельных джоб. Каждая джоба  выполняется около 2 часов, общее время на сборку около 10 часов.
В случае возникновения ошибок в одной джобе, будут отменены все незавершенные - в этом случае на вкладке Actions можно выбрать неудавшийся запуск и нажать Re-run failed jobs

## Сборка пакетов под определенную платформу
Как запустить сборку пакетов для определенной платформы можно посмотреть в [инструкции на вики](https://github.com/itdoginfo/domain-routing-openwrt/wiki/Amnezia-WG-Build). Сборка под одно устройство займет около 2 часов.

# Automatic configuration of AmneziaWG for OpenWRT version 23.05.0 and newer
For automatic configuration, I recommend using the [script](https://github.com/itdoginfo/domain-routing-openwrt) from the user itdog. This script allows you to automatically download the necessary packages from those collected here and configure [point-by-point bypass of blocking by domains](https://habr.com/ru/articles/767464/) (instructions in Russian).

If you only need to install packages, I added the amneziawg-install script - it will automatically download packages from this repository for your device (only for the stable version of OpenWRT), and also offer to immediately configure the interface with the AmneziaWG protocol. If the user agrees, you will need to enter the config parameters that the script will request. The script will create an interface, configure firewall rules for it, and also **enable redirection of all traffic through the AmneziaWG tunnel** (check the Route Allowed IPs box in the Peer settings).
To run the script, connect to the router via SSH, enter the command and follow the instructions on the screen:
```
sh <(wget -O - https://raw.githubusercontent.com/Slava-Shchipunov/awg-openwrt/refs/heads/master/amneziawg-install.sh)
```

# Building packages for all devices that support OpenWRT
A script has been added to the repository that parses data on supported platforms from the OpenWRT page and automatically starts building AmneziaWG packages for all devices.
At the moment I have collected packages for all devices for OpenWRT versions:
1) [23.05.0](https://github.com/Slava-Shchipunov/awg-openwrt/releases/tag/v23.05.0)
2) [23.05.1](https://github.com/Slava-Shchipunov/awg-openwrt/releases/tag/v23.05.1)
3) [23.05.2](https://github.com/Slava-Shchipunov/awg-openwrt/releases/tag/v23.05.2)
4) [23.05.3](https://github.com/Slava-Shchipunov/awg-openwrt/releases/tag/v23.05.3)
5) [23.05.4](https://github.com/Slava-Shchipunov/awg-openwrt/releases/tag/v23.05.4)
6) [23.05.5](https://github.com/Slava-Shchipunov/awg-openwrt/releases/tag/v23.05.5)
7) AWG-2.0 [23.05.6](https://github.com/Slava-Shchipunov/awg-openwrt/releases/tag/v23.05.6)
8) [24.10.0](https://github.com/Slava-Shchipunov/awg-openwrt/releases/tag/v24.10.0)
9) [24.10.1](https://github.com/Slava-Shchipunov/awg-openwrt/releases/tag/v24.10.1)
10) [24.10.2](https://github.com/Slava-Shchipunov/awg-openwrt/releases/tag/v24.10.2)
11) AWG-2.0 [24.10.3](https://github.com/Slava-Shchipunov/awg-openwrt/releases/tag/v24.10.3)

I also ran the build for version [22.03.7](https://github.com/Slava-Shchipunov/awg-openwrt/releases/tag/v22.03.7), but the build ended with an error for two platforms. Since this is a fairly old version of OpenWRT, I did not bother to figure out what the problem was.

In the future, when new OpenWRT releases are released, releases with AmneziaWG packages will be automatically created and the package build will be launched for all devices supported by the new version. Github action for checking for a new release is launched automatically every 3 days, and can also be launched manually.

## Automatic package build for SNAPSHOT version
A github action is configured in the repository, which runs every 4 hours and checks the [snapshots page](https://downloads.openwrt.org/snapshots/targets/) of the OpenWRT website. At the same time, if a snapshot with a newer kernel version is found for some platform, the package build for this platform is launched, and the new files replace the old ones. In order to save resources and speed up the build process, packages are built only for popular platforms, which are specified in the `SNAPSHOT_SUBTARGETS_TO_BUILD` array in the index.js file.

## Selecting packages for your device
In accordance with the paragraph [Specify variables for builds](https://github.com/itdoginfo/domain-routing-openwrt/wiki/Amnezia-WG-Build#%D1%83%D0%BA%D0%B0%D0%B7%D1%8B%D0%B2%D0%B0%D0%B5%D0%BC-%D0%BF%D0%B5%D1%80%D0%B5%D0%BC%D0%B5%D0%BD%D0%BD%D1%8B%D0%B5-%D0%B4%D0%BB%D1%8F-%D1%81%D0%B1%D0%BE%D1%80%D0%BA%D0%B8) (instructions in Russian) determine `target` and `subtarget` of your device. Then go to the release page corresponding to your OpenWRT version, then search the page (Ctrl+F) to find 3 packages whose names end in `target_subtarget.ipk` corresponding to your device.

## How to run a build for all supported devices
1) Create a fork of this repository
2) Switch to the Actions tab and enable Github actions (they are disabled for forks by default)
3) Then go to the Code tab => Releases (on the right side of the screen) => Draft a new release
4) Click Choose a tag and create a new tag in the vX.X.X format, where you need to substitute the required OpenWRT version for X.X.X, for example, v23.05.4
5) Select the `master` branch as the target
6) Enter Release title
7) Click the green Publish release button at the bottom

For public repositories, Github provides unlimited use of runners, I had up to 20 parallel jobs running. Each job takes about 2 hours, the total build time is about 10 hours.
If errors occur in one job, all unfinished ones will be canceled - in this case, you can select the failed launch on the Actions tab and click Re-run failed jobs

## Building packages for a specific platform
You can see how to start building packages for a specific platform in the [wiki instructions](https://github.com/itdoginfo/domain-routing-openwrt/wiki/Amnezia-WG-Build) (instructions in Russian). Building for one device will take about 2 hours.
