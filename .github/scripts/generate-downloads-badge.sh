#!/usr/bin/env bash
set -euo pipefail

OUTPUT_FILE="${1:?output file is required}"
REPOSITORY="${2:?repository is required}"

: "${GH_TOKEN:?GH_TOKEN is required}"

page_download_counts=$(
  gh api --paginate \
    -H "Accept: application/vnd.github+json" \
    -H "X-GitHub-Api-Version: 2022-11-28" \
    "/repos/${REPOSITORY}/releases?per_page=10" \
    --jq '[.[] | select(.draft == false) | .assets[].download_count] | add // 0'
)

total_downloads=0
while IFS= read -r page_downloads; do
  [ -n "$page_downloads" ] || continue
  case "$page_downloads" in
    *[!0-9]*)
      echo "Invalid download count returned by GitHub API: $page_downloads" >&2
      exit 1
      ;;
  esac
  total_downloads=$((total_downloads + page_downloads))
done <<< "$page_download_counts"

mkdir -p "$(dirname "$OUTPUT_FILE")"
temporary_file="${OUTPUT_FILE}.tmp"
cat > "$temporary_file" <<EOF
{
  "schemaVersion": 1,
  "label": "release downloads",
  "message": "$total_downloads",
  "color": "blue"
}
EOF
mv "$temporary_file" "$OUTPUT_FILE"

echo "Total GitHub release asset downloads: $total_downloads"
