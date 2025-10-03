const axios = require('axios');
const cheerio = require('cheerio');
const core = require('@actions/core');

const version = process.argv[2]; // Получение версии OpenWRT из аргумента командной строки
const filterTargetsStr = process.argv[3] || ''; // Фильтр по targets (опционально, через запятую)
const filterSubtargetsStr = process.argv[4] || ''; // Фильтр по subtargets (опционально, через запятую)

// Преобразуем строки с запятыми в массивы
const filterTargets = filterTargetsStr ? filterTargetsStr.split(',').map(t => t.trim()).filter(t => t) : [];
const filterSubtargets = filterSubtargetsStr ? filterSubtargetsStr.split(',').map(s => s.trim()).filter(s => s) : [];

if (!version) {
  core.setFailed('Version argument is required');
  process.exit(1);
}

const url = `https://downloads.openwrt.org/releases/${version}/targets/`;

async function fetchHTML(url) {
  try {
    const { data } = await axios.get(url);
    return cheerio.load(data);
  } catch (error) {
    console.error(`Error fetching HTML for ${url}: ${error}`);
    throw error;
  }
}

async function getTargets() {
  const $ = await fetchHTML(url);
  const targets = [];
  $('table tr td.n a').each((index, element) => {
    const name = $(element).attr('href');
    if (name && name.endsWith('/')) {
      targets.push(name.slice(0, -1));
    }
  });
  return targets;
}

async function getSubtargets(target) {
  const $ = await fetchHTML(`${url}${target}/`);
  const subtargets = [];
  $('table tr td.n a').each((index, element) => {
    const name = $(element).attr('href');
    if (name && name.endsWith('/')) {
      subtargets.push(name.slice(0, -1));
    }
  });
  return subtargets;
}

async function getDetails(target, subtarget) {
  const packagesUrl = `${url}${target}/${subtarget}/packages/`;
  const $ = await fetchHTML(packagesUrl);
  let vermagic = '';
  let pkgarch = '';

  $('a').each((index, element) => {
    const name = $(element).attr('href');
    if (name && name.startsWith('kernel_')) {
      const vermagicMatch = name.match(/kernel_\d+\.\d+\.\d+(?:-\d+)?[-~]([a-f0-9]+)(?:-r\d+)?_([a-zA-Z0-9_-]+)\.ipk$/);
      if (vermagicMatch) {
        vermagic = vermagicMatch[1];
        pkgarch = vermagicMatch[2];
      }
    }
  });

  return { vermagic, pkgarch };
}

async function main() {
  try {
    const targets = await getTargets();
    const jobConfig = [];

    for (const target of targets) {
      // Пропускаем target, если указан массив фильтров и target не входит в него
      if (filterTargets.length > 0 && !filterTargets.includes(target)) {
        continue;
      }

      const subtargets = await getSubtargets(target);
      for (const subtarget of subtargets) {
        // Пропускаем subtarget, если указан массив фильтров и subtarget не входит в него
        if (filterSubtargets.length > 0 && !filterSubtargets.includes(subtarget)) {
          continue;
        }

        // Добавляем в конфигурацию только если:
        // 1. Оба массива пустые (автоматическая сборка по тегу) - собираем всё
        // 2. Оба массива НЕ пустые (ручной запуск) - target И subtarget должны быть в своих массивах
        const isAutomatic = filterTargets.length === 0 && filterSubtargets.length === 0;
        const isManualMatch = filterTargets.length > 0 && filterSubtargets.length > 0 &&
                              filterTargets.includes(target) && filterSubtargets.includes(subtarget);
        
        if (!isAutomatic && !isManualMatch) {
          continue;
        }

        const { vermagic, pkgarch } = await getDetails(target, subtarget);

        jobConfig.push({
          tag: version,
          target,
          subtarget,
          vermagic,
          pkgarch,
        });
      }
    }

    core.setOutput('job-config', JSON.stringify(jobConfig));
  } catch (error) {
    core.setFailed(error.message);
  }
}

main();
