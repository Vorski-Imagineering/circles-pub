#!/usr/bin/env bash
# Stage the synced docs tree into site_src/ ready for `mkdocs build`.
# Used by .github/workflows/docs.yml and for local previews.
set -euo pipefail

cd "$(dirname "$0")/.."

rm -rf site_src
mkdir -p site_src

# Whole-tree copy: a new page dropped into docs/pub/** upstream publishes
# automatically. Only the sidebar needs a nav: entry in mkdocs.yml.
cp -R docs-pub/. site_src/

# The docs index becomes the site home page.
mv site_src/README.md site_src/index.md

python3 scripts/prepare_synced_docs.py site_src

echo "site_src/ assembled"
