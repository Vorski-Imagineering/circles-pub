# circles-pub

Public documentation for **Circles** — published to
**[docs.circles.care](https://docs.circles.care/)**.

## Don't edit the docs here

Everything under [`docs-pub/`](docs-pub/) is synced automatically from the
`docs/pub` tree of the [Circles source repo](https://github.com/Vorski-Imagineering/circles)
every time `main` there changes. **Edits made here are overwritten on the next
sync.** To change the docs, edit `docs/pub/**` in the Circles repo and merge to
`main`.

## What this repo does own

- `mkdocs.yml` — site config and navigation
- `.github/workflows/docs.yml` — build and deploy to GitHub Pages
- `scripts/assemble.sh` — stages the synced tree into `site_src/`
- `scripts/prepare_synced_docs.py` — fixes up synced Markdown for the MkDocs
  renderer

## How a change reaches the site

1. A doc under `docs/pub/**` is merged to `main` in the Circles repo.
2. That repo's `publish-docs` workflow pushes the tree into `docs-pub/` here.
3. The push to `main` here triggers **Deploy Docs**, which builds the MkDocs
   site and publishes it to GitHub Pages at `docs.circles.care`.

Adding a new page needs no workflow change — drop it in `docs/pub/**` upstream
and add a `nav:` entry in [`mkdocs.yml`](mkdocs.yml) here if it should appear in
the sidebar.

## Building locally

```bash
pip install mkdocs-material
./scripts/assemble.sh
mkdocs serve
```
