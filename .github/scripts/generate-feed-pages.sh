#!/usr/bin/env bash
set -euo pipefail

SITE_DIR="${1:?site directory is required}"
BASE_URL="${2:?base URL is required}"
SCRIPT_DIR=$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)
REPO_ROOT=$(cd "$SCRIPT_DIR/../.." && pwd)

mkdir -p "$SITE_DIR"
rm -f "$SITE_DIR/.nojekyll"
find "$SITE_DIR" -name "index.md" -delete
rm -f "$SITE_DIR/keys/awg-openwrt-feed.pub"

# The current public layout is /<version>/<target>/<subtarget>/.
while IFS= read -r -d '' dir; do
  [ -s "$dir/packages.adb" ] || continue
  parent=$(dirname "$dir")
  if [ ! -s "$parent/packages.adb" ]; then
    cp -a "$dir"/. "$parent"/
    if [ ! -s "$parent/feed.json" ]; then
      pkgarch=$(basename "$dir")
      cat > "$parent/feed.json" <<EOF
{
  "pkgarch": "$pkgarch",
  "feed": "awg"
}
EOF
    fi
  fi
  rm -rf "$dir"
done < <(find "$SITE_DIR" -mindepth 4 -maxdepth 4 -type d -print0)

cat > "$SITE_DIR/_config.yml" <<'EOF'
title: AmneziaWG OpenWrt Feed
description: APK package feed for AmneziaWG on OpenWrt 25.12.x and newer
theme: jekyll-theme-midnight
EOF

mkdir -p "$SITE_DIR/assets"
cp -a "$REPO_ROOT/assets/copy-code.js" "$SITE_DIR/assets/copy-code.js"

cat > "$SITE_DIR/index.md" <<EOF
---
layout: default
title: AmneziaWG OpenWrt Feed
---

# AmneziaWG OpenWrt Feed
This GitHub Pages site publishes an APK package feed for OpenWrt 25.12.x and newer.

OpenWrt 24.10.x and older are not supported by this feed. Use GitHub Releases artifacts for legacy \`.ipk\` packages.

## Available OpenWrt versions

EOF

mapfile -t FEED_DIRS < <(find "$SITE_DIR" -mindepth 3 -maxdepth 3 -type d | sort)
for feed_dir in "${FEED_DIRS[@]}"; do
  if [ ! -s "$feed_dir/packages.adb" ]; then
    continue
  fi

  rel_path="${feed_dir#"$SITE_DIR"/}"
  IFS=/ read -r version target subtarget <<EOF
$rel_path
EOF
  pkgarch="unknown"
  if [ -s "$feed_dir/feed.json" ]; then
    pkgarch=$(sed -n 's/.*"pkgarch": "\([^"]*\)".*/\1/p' "$feed_dir/feed.json" | head -n1)
  fi
  feed_url="$BASE_URL/$rel_path"
  adb_url="$feed_url/packages.adb"
  version_dir="$SITE_DIR/$version"
  target_dir="$version_dir/$target"
  subtarget_dir="$target_dir/$subtarget"
  version_url="$BASE_URL/$version"
  target_url="$version_url/$target"
  subtarget_url="$target_url/$subtarget"
  openwrt_target_url="https://downloads.openwrt.org/releases/$version/targets/$target/$subtarget/"

  if ! grep -q "($version_url/)" "$SITE_DIR/index.md"; then
    printf -- '- [%s](%s/)\n' "$version" "$version_url" >> "$SITE_DIR/index.md"
  fi

  if [ ! -f "$version_dir/index.md" ]; then
    cat > "$version_dir/index.md" <<EOF
---
layout: default
title: "OpenWrt $version"
---

# OpenWrt $version

Index of [(root)]($BASE_URL/)

Choose a target.

## Targets

EOF
  fi
  if ! grep -q "($target_url/)" "$version_dir/index.md"; then
    printf -- '- [%s](%s/)\n' "$target" "$target_url" >> "$version_dir/index.md"
  fi

  if [ ! -f "$target_dir/index.md" ]; then
    cat > "$target_dir/index.md" <<EOF
---
layout: default
title: "OpenWrt $version $target"
---

# OpenWrt $version / $target

Index of [(root)]($BASE_URL/) / [$version]($version_url/)

Choose a subtarget.

## Subtargets

EOF
  fi
  if ! grep -q "($subtarget_url/)" "$target_dir/index.md"; then
    printf -- '- [%s](%s/)\n' "$subtarget" "$subtarget_url" >> "$target_dir/index.md"
  fi

  cat > "$subtarget_dir/index.md" <<EOF
---
layout: default
title: "OpenWrt $version $target/$subtarget"
---

# AmneziaWG feed

Index of [(root)]($BASE_URL/) / [$version]($version_url/) / [$target]($target_url/)

- OpenWrt version: \`$version\`
- Target: \`$target\`
- Subtarget: \`$subtarget\`
- Package architecture: \`$pkgarch\`

## Upstream OpenWrt target

[$openwrt_target_url]($openwrt_target_url)

## Configure Feed

\`\`\`sh
mkdir -p /etc/apk/keys
wget -O /etc/apk/keys/awg-openwrt-feed.pem "$BASE_URL/keys/awg-openwrt-feed.pem"
echo "$adb_url" >> /etc/apk/repositories.d/customfeeds.list
\`\`\`

## Install Packages

\`\`\`sh
apk update
apk add amneziawg-tools kmod-amneziawg luci-proto-amneziawg
\`\`\`

<script src="$BASE_URL/assets/copy-code.js?v=2"></script>

## Feed files

EOF

  find "$feed_dir" -maxdepth 1 -type f \
    ! -name "index.md" \
    -printf "%f\n" | sort | while read -r file_name; do
      printf -- '- [%s](%s/%s)\n' "$file_name" "$feed_url" "$file_name" >> "$feed_dir/index.md"
    done
done
