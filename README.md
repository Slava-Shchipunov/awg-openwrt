![Downloads](https://img.shields.io/github/downloads/Slava-Shchipunov/awg-openwrt/total.svg)

# Пакеты amneziawg для роутеров с прошивкой OpenWRT

## Автоматическая настройка AmneziaWG для OpenWRT версии 23.05.0 и более новых
1) Если ваш роутер обладает достаточным объмом доступной ROM, рекомендую воспользоваться скриптом, описанным ниже, только для установки нужных пакетов, а для точечной маршрутизации траффика в туннель использовать podkop от пользователя [@itdoginfo](https://github.com/itdoginfo) - тут в [документации](https://podkop.net/docs/tunnels/awg_settings/) описан процесс настройки

2) Если вам нужно только установить пакеты, я добавил скрипт amneziawg-install - он автоматически скачает пакеты из этого репозитория под ваше устройство (только для стабильной версии OpenWRT), а также предложит сразу настроить интерфейс с протоколом AmneziaWG. Если пользователь согласится, нужно будет ввести параметры конфига, которые запросит скрипт. При этом скрипт создаст интерфейс, настроит для него правила фаерволла, а также **включит перенаправление всего траффика через тунель AmneziaWG** (установит в настройках Peer галочку Route Allowed IPs).
Для запуска скрипта подключитесь к роутеру по SSH, введите команду и следуйте инструкциям на экране:
```
sh <(wget -O - https://raw.githubusercontent.com/Slava-Shchipunov/awg-openwrt/refs/heads/master/amneziawg-install.sh)
```
3) Также предусмотрен неинтерактивный режим простой установки пакетов (без вопросов о настройке интерфейса с протоколом AmneziaWG и установке пакета `luci-i18n-amneziawg-ru`):
```
sh <(wget -O - https://raw.githubusercontent.com/Slava-Shchipunov/awg-openwrt/refs/heads/master/amneziawg-install.sh) -en
```  
4) Кроме того для автоматической настройки также можно использовать [скрипт](https://github.com/itdoginfo/domain-routing-openwrt) от пользователя [@itdoginfo](https://github.com/itdoginfo). Этот скрипт позволяет автоматически скачать нужные пакеты из собранных здесь и настроить [точечный обход блокировок по доменам](https://habr.com/ru/articles/767464/). Подойдёт, если у вас слабый роутер с недостаточным объёмом ROM для установки podkop-a и зависимостей

## Сборка пакетов для всех устройств, поддерживающих OpenWRT
В репозиторий добавлен скрипт, который парсит данные о поддерживаемых платформах со страницы OpenWRT и автоматически запускает сборку пакетов AmneziaWG для всех устройств.
На данный момент я собрал пакеты для всех устройств для OpenWRT версий:
1) [23.05.0](https://github.com/Slava-Shchipunov/awg-openwrt/releases/tag/v23.05.0)
2) [23.05.1](https://github.com/Slava-Shchipunov/awg-openwrt/releases/tag/v23.05.1)
3) [23.05.2](https://github.com/Slava-Shchipunov/awg-openwrt/releases/tag/v23.05.2)
4) [23.05.3](https://github.com/Slava-Shchipunov/awg-openwrt/releases/tag/v23.05.3)
5) [23.05.4](https://github.com/Slava-Shchipunov/awg-openwrt/releases/tag/v23.05.4)
6) [23.05.5](https://github.com/Slava-Shchipunov/awg-openwrt/releases/tag/v23.05.5)
7) AWG-2.0 [23.05.6](https://github.com/Slava-Shchipunov/awg-openwrt/releases/tag/v23.05.6)
8) [24.10.0](https://github.com/Slava-Shchipunov/awg-openwrt/releases/tag/v24.10.0) ([AWG-2.0 для 24.10.0](https://github.com/yanjore/awg-openwrt/releases/tag/v24.10.0) из форка, если кому-то понадобится)
9) [24.10.1](https://github.com/Slava-Shchipunov/awg-openwrt/releases/tag/v24.10.1) ([AWG-2.0 для 24.10.1](https://github.com/yanjore/awg-openwrt/releases/tag/v24.10.1) из форка)
10) [24.10.2](https://github.com/Slava-Shchipunov/awg-openwrt/releases/tag/v24.10.2) ([AWG-2.0 для 24.10.2](https://github.com/yanjore/awg-openwrt/releases/tag/v24.10.2) из форка)
11) AWG-2.0 [24.10.3](https://github.com/Slava-Shchipunov/awg-openwrt/releases/tag/v24.10.3)
12) AWG-2.0 [24.10.4](https://github.com/Slava-Shchipunov/awg-openwrt/releases/tag/v24.10.4)
13) AWG-2.0 [24.10.5](https://github.com/Slava-Shchipunov/awg-openwrt/releases/tag/v24.10.5)
14) AWG-2.0 [24.10.6](https://github.com/Slava-Shchipunov/awg-openwrt/releases/tag/v24.10.6)
15) AWG-2.0 [25.12.0](https://github.com/Slava-Shchipunov/awg-openwrt/releases/tag/v25.12.0)
16) AWG-2.0 [25.12.1](https://github.com/Slava-Shchipunov/awg-openwrt/releases/tag/v25.12.1)
17) AWG-2.0 [25.12.2](https://github.com/Slava-Shchipunov/awg-openwrt/releases/tag/v25.12.2)
18) AWG-2.0 [25.12.3](https://github.com/Slava-Shchipunov/awg-openwrt/releases/tag/v25.12.3)

Также запускал сборку для версии [22.03.7](https://github.com/Slava-Shchipunov/awg-openwrt/releases/tag/v22.03.7), но там для двух платформ сборка завершилась ошибкой. Так как это достаточно старая версия OpenWRT, я не стал разбираться, в чем проблема.

## Выбор пакетов для своего устройства
В соответствии с пунктом [Указываем переменные для сборки](https://github.com/itdoginfo/domain-routing-openwrt/wiki/Amnezia-WG-Build#%D1%83%D0%BA%D0%B0%D0%B7%D1%8B%D0%B2%D0%B0%D0%B5%D0%BC-%D0%BF%D0%B5%D1%80%D0%B5%D0%BC%D0%B5%D0%BD%D0%BD%D1%8B%D0%B5-%D0%B4%D0%BB%D1%8F-%D1%81%D0%B1%D0%BE%D1%80%D0%BA%D0%B8)
определить `target` и `subtarget` вашего устройства. Далее перейти на страницу релиза, соответствующего вашей версии OpenWRT, затем поиском по странице (Ctrl+F) найти 3 пакета, название которых оканчивается на `target_subtarget.ipk`, соответствующие вашему устройству. Для версии AWG 2.0 также доступен пакет русификации  luci-i18n-amneziawg-ru

## Как запустить сборку для всех поддерживаемых устройств
1) Создать форк этого репозитория
2) Переключиться на вкладку Actions и включить Github actions (по умолчанию для форков они выключены)
3) Затем перейти на вкладку Code => Releases (в правой части экрана) => Draft a new release
4) Нажать Choose a tag и создать новый тег формата vX.X.X, где вместо X.X.X нужно подставить требуемую версию OpenWRT, например, v23.05.4
5) Выбрать в качестве target ветку `master`
6) Ввести Release title
7) Нажать внизу зеленую кнопку Publish release

Для публичных репозиториев Github предоставляет неограниченное по времени использование раннеров, у меня запускалось до 20 параллельных джоб. Каждая джоба  выполняется около 10-15 минут, общее время на сборку около 60 минут.

## Сборка пакетов под определенную платформу
Как запустить сборку пакетов AWG 1.0 для определенной платформы можно посмотреть в [инструкции на вики](https://github.com/itdoginfo/domain-routing-openwrt/wiki/Amnezia-WG-Build). Сборка под одно устройство займет около 2 часов.

AWG 2.0 можно собрать под определённую платформу следующим образом:
1) Создать форк этого репозитория
2) Переключиться на вкладку Actions и включить Github actions (по умолчанию для форков они выключены)
3) Слева в списке экшенов выбрать экшен Create Release on Tag
4) Справа нажать кнопку Run workflow
5) В открывшемся списке указать версию Openwrt (например, 24.10.3), список target, разделенных запятыми (например, stm32,ramips), список subtarget, разделенных запятыми (например, stm32mp1,mt7621). Сборка будет произведена только для существующих пар target/subtarget
6) Нажать зеленую кнопку Run workflow
Сборка под одно устройство займет около 10-15 минут. При этом должен создаться релиз с указанной версией OpenWRT

## 🙏 Благодарности

Огромное спасибо за помощь в сборке пакетов AWG 2.0:

- [@kozhini](https://github.com/kozhini) и [@this-username-has-been-taken](https://github.com/this-username-has-been-taken) — ~~у которых я позаимствовал код Makefile-ов~~ чьим примером я вдохновлялся🙃
- [@Kot-nikot](https://github.com/Kot-nikot) и [@Onotot](https://github.com/Onotot) — за полезные материалы и подсказки🤝
- [@ygurov](https://github.com/ygurov) - за [имплементацию](https://github.com/amnezia-vpn/amneziawg-linux-kernel-module/pull/88) awg 2.0 для модуля ядра 💪
- А также всем, кто приносил полезные примеры в личку и в [ишью](https://github.com/Slava-Shchipunov/awg-openwrt/issues/39), отписывались в комменты к PR с имплементацией о возникших багах и проблемах ❤️

## Automatic configuration of AmneziaWG for OpenWRT version 23.05.0 and newer
1) If your router has enough available ROM, I recommend using the script described below only to install the necessary packages, and use podkop from user [@itdoginfo](https://github.com/itdoginfo) for selective traffic routing into the tunnel - the setup process is described in the [documentation](https://podkop.net/docs/tunnels/awg_settings/)

2) If you only need to install packages, I added the amneziawg-install script - it will automatically download packages from this repository for your device (only for the stable version of OpenWRT), and also offer to immediately configure the interface with the AmneziaWG protocol. If the user agrees, you will need to enter the config parameters that the script will request. The script will create an interface, configure firewall rules for it, and also **enable redirection of all traffic through the AmneziaWG tunnel** (check the Route Allowed IPs box in the Peer settings).
To run the script, connect to the router via SSH, enter the command and follow the instructions on the screen:
```
sh <(wget -O - https://raw.githubusercontent.com/Slava-Shchipunov/awg-openwrt/refs/heads/master/amneziawg-install.sh)
```
3) There is also a non-interactive mode for simple package installation (without questions about configuring an interface with the AmneziaWG protocol and installing the `luci-i18n-amneziawg-ru` package):
```
sh <(wget -O - https://raw.githubusercontent.com/Slava-Shchipunov/awg-openwrt/refs/heads/master/amneziawg-install.sh) -en
```
4) In addition, for automatic configuration you can also use the [script](https://github.com/itdoginfo/domain-routing-openwrt) from user [@itdoginfo](https://github.com/itdoginfo). This script allows you to automatically download the necessary packages from those collected here and configure [point-by-point bypass of blocking by domains](https://habr.com/ru/articles/767464/) (instructions in Russian). Suitable if you have a weak router with insufficient ROM to install podkop and its dependencies

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
8) [24.10.0](https://github.com/Slava-Shchipunov/awg-openwrt/releases/tag/v24.10.0) ([AWG-2.0 for 24.10.0](https://github.com/yanjore/awg-openwrt/releases/tag/v24.10.0) from fork)
9) [24.10.1](https://github.com/Slava-Shchipunov/awg-openwrt/releases/tag/v24.10.1) ([AWG-2.0 for 24.10.1](https://github.com/yanjore/awg-openwrt/releases/tag/v24.10.1) from fork)
10) [24.10.2](https://github.com/Slava-Shchipunov/awg-openwrt/releases/tag/v24.10.2) ([AWG-2.0 for 24.10.2](https://github.com/yanjore/awg-openwrt/releases/tag/v24.10.2) from fork)
11) AWG-2.0 [24.10.3](https://github.com/Slava-Shchipunov/awg-openwrt/releases/tag/v24.10.3)
12) AWG-2.0 [24.10.4](https://github.com/Slava-Shchipunov/awg-openwrt/releases/tag/v24.10.4)
13) AWG-2.0 [24.10.5](https://github.com/Slava-Shchipunov/awg-openwrt/releases/tag/v24.10.5)
14) AWG-2.0 [24.10.6](https://github.com/Slava-Shchipunov/awg-openwrt/releases/tag/v24.10.6)
15) AWG-2.0 [25.12.0](https://github.com/Slava-Shchipunov/awg-openwrt/releases/tag/v25.12.0)
16) AWG-2.0 [25.12.1](https://github.com/Slava-Shchipunov/awg-openwrt/releases/tag/v25.12.1)
17) AWG-2.0 [25.12.2](https://github.com/Slava-Shchipunov/awg-openwrt/releases/tag/v25.12.2)
18) AWG-2.0 [25.12.3](https://github.com/Slava-Shchipunov/awg-openwrt/releases/tag/v25.12.3)

I also ran the build for version [22.03.7](https://github.com/Slava-Shchipunov/awg-openwrt/releases/tag/v22.03.7), but the build ended with an error for two platforms. Since this is a fairly old version of OpenWRT, I did not bother to figure out what the problem was.

## Selecting packages for your device
In accordance with the paragraph [Specify variables for builds](https://github.com/itdoginfo/domain-routing-openwrt/wiki/Amnezia-WG-Build#%D1%83%D0%BA%D0%B0%D0%B7%D1%8B%D0%B2%D0%B0%D0%B5%D0%BC-%D0%BF%D0%B5%D1%80%D0%B5%D0%BC%D0%B5%D0%BD%D0%BD%D1%8B%D0%B5-%D0%B4%D0%BB%D1%8F-%D1%81%D0%B1%D0%BE%D1%80%D0%BA%D0%B8) (instructions in Russian) determine `target` and `subtarget` of your device. Then go to the release page corresponding to your OpenWRT version, then search the page (Ctrl+F) to find 3 packages whose names end in `target_subtarget.ipk` corresponding to your device. For AWG 2.0 version, Russian localization package luci-i18n-amneziawg-ru is also available

## How to run a build for all supported devices
1) Create a fork of this repository
2) Switch to the Actions tab and enable Github actions (they are disabled for forks by default)
3) Then go to the Code tab => Releases (on the right side of the screen) => Draft a new release
4) Click Choose a tag and create a new tag in the vX.X.X format, where you need to substitute the required OpenWRT version for X.X.X, for example, v23.05.4
5) Select the `master` branch as the target
6) Enter Release title
7) Click the green Publish release button at the bottom

For public repositories, Github provides unlimited use of runners, I had up to 20 parallel jobs running. Each job takes about 10-15 minutes, the total build time is about 60 minutes.

## Building packages for a specific platform
You can see how to start building AWG 1.0 packages for a specific platform in the [wiki instructions](https://github.com/itdoginfo/domain-routing-openwrt/wiki/Amnezia-WG-Build) (instructions in Russian). Building for one device will take about 2 hours.

AWG 2.0 can be built for a specific platform as follows:
1) Create a fork of this repository
2) Switch to the Actions tab and enable Github actions (they are disabled for forks by default)
3) On the left in the list of actions, select the Create Release on Tag action
4) On the right, click the Run workflow button
5) In the opened list, specify the OpenWRT version (for example, 24.10.3), a list of targets separated by commas (for example, stm32,ramips), a list of subtargets separated by commas (for example, stm32mp1,mt7621). The build will be performed only for existing target/subtarget pairs
6) Click the green Run workflow button
Building for one device will take about 10-15 minutes. A release with the specified OpenWRT version should be created
