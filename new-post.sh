#!/usr/bin/env bash
# Create a new post: posts/<folder-name>/index.qmd with today's date.
#
# Usage:
#   ./new-post.sh <folder-name> ["Post title"]
#
# Examples:
#   ./new-post.sh why-habits-beat-goals "Why habits beat goals"
#   ./new-post.sh why-habits-beat-goals          # title left empty
#
# The folder name is lowercased, punctuation is removed and spaces become
# dashes, so "Why Habits Beat Goals?" also gives posts/why-habits-beat-goals/.
set -euo pipefail

if [ $# -lt 1 ] || [ -z "$1" ]; then
  echo "Usage: ./new-post.sh <folder-name> [\"Post title\"]" >&2
  exit 1
fi

cd "$(dirname "$0")"

# Lowercase, drop apostrophes ("don't" → "dont"), turn every other run of
# punctuation or spaces into one dash, and trim dashes from the ends.
folder=$(printf '%s' "$1" | tr '[:upper:]' '[:lower:]' | sed -e "s/['’‘]//g" \
  | LC_ALL=C sed -e 's/[^a-z0-9]\{1,\}/-/g' -e 's/^-//' -e 's/-$//')
if [ -z "$folder" ]; then
  echo "Error: the folder name has no letters or numbers." >&2
  exit 1
fi
title=${2:-}
title=${title//\\/\\\\}   # escape backslashes and double quotes for YAML
title=${title//\"/\\\"}
today=$(date +%Y-%m-%d)   # e.g. 2026-06-03

dir="posts/$folder"
if [ -e "$dir" ]; then
  echo "Error: $dir already exists." >&2
  exit 1
fi

mkdir -p "$dir"
cat > "$dir/index.qmd" <<EOF
---
title: "$title"
date: '$today'
---

EOF

echo "Created $dir/index.qmd"
