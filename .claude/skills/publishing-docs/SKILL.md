---
name: publishing-docs
description: >
  Use when working on docs.circles.care or this repo's build — adding, moving or renaming a
  published page, editing the sidebar nav, fixing a failed "Deploy Docs" run, a page that
  404s or is missing from the site, a `mkdocs build --strict` failure, a broken link
  warning, docs edited here that reverted, or a change merged upstream that never appeared
  on the site. Also covers rebuilding the same setup for another repo pair.
---

# Publishing docs to docs.circles.care

Two repos. `circles` owns the words, `circles-pub` (this repo) owns the site. Docs are
written in `circles/docs/pub/**`, pushed here into `docs-pub/` by CI, and built into a
MkDocs Material site served from GitHub Pages at `docs.circles.care`.

## The rule that catches everyone

**`docs-pub/` here is a build input, not a source. Every file in it is overwritten on the
next upstream sync.** To change a doc, edit `circles/docs/pub/**` and merge to `main`.
Editing `docs-pub/` here publishes once, then silently reverts.

What this repo *does* own: `mkdocs.yml`, `.github/workflows/docs.yml`, `scripts/`.

## The chain

```
circles/docs/pub/**  --(merge to main)-->  publish-docs.yml
      |                                          | cpina/github-action-push-to-another-repository
      |                                          v
      |                              circles-pub/docs-pub/  --(push to main)--> docs.yml
      |                                                                            |
      |                                       assemble.sh -> site_src/ -> mkdocs build --strict
      |                                                                            v
      +--------------------------------------------------> GitHub Pages -> docs.circles.care
```

`assemble.sh` copies `docs-pub/` into `site_src/`, renames `README.md` to `index.md` (the
docs index becomes the site home page), and runs `prepare_synced_docs.py` over it.
`site_src/` and `site/` are gitignored build artifacts — never commit them.

## Common tasks

| Task | Do this |
|---|---|
| Change a page's text | Edit it in `circles/docs/pub/**`, merge to `main`. Never here. |
| Add a page | Add upstream, then add a `nav:` entry in `mkdocs.yml` here. It publishes either way; without the nav entry it just isn't in the sidebar. |
| Rename/move a page | Upstream, then update the matching `nav:` path here in the same window — a stale nav path fails the build. |
| Reorder the sidebar | `nav:` in `mkdocs.yml`. Nothing else reads that order. |
| Preview locally | `pip install mkdocs-material && ./scripts/assemble.sh && mkdocs serve` |
| Force a resync | `gh workflow run publish-docs.yml -R Vorski-Imagineering/circles` |
| Rebuild without an upstream change | `gh workflow run docs.yml -R Vorski-Imagineering/circles-pub` |

Always reproduce a build failure locally with `./scripts/assemble.sh && mkdocs build --strict`
before pushing a fix. It's the same command CI runs and takes under a second.

## Why prepare_synced_docs.py exists

The same Markdown is read two ways: on GitHub (GFM, upstream) and by Python-Markdown
(MkDocs, here). Two things are legal in the first and broken in the second, so the script
rewrites them in `site_src/` — never in `docs-pub/`, so the sync stays a clean mirror.

1. **A list right after a paragraph line, no blank line between.** GFM starts a list;
   Python-Markdown folds it into the paragraph as plain text. The script inserts the blank
   line. Symptom: bullets render as one run-on sentence.
2. **Relative links with no page behind them** — a directory (`[circle/](circle)`) or an
   unpublished sibling tree (`[docs/dev](../dev)`). Both work when browsing GitHub; neither
   has a URL on the built site. The script keeps the link text and drops the link. Anything
   external, an anchor, a `.md` target, or an image is left alone.

**Don't fix these upstream.** Those links are correct for people reading on GitHub. The
fixup belongs here, at build time.

## Troubleshooting

| Symptom | Cause |
|---|---|
| Build fails on a nav path | `mkdocs.yml` points at a page that was renamed or deleted upstream. Update the nav entry. |
| Build fails with a link warning | `--strict` promotes it. If the target genuinely has no page, extend the de-link rule in `prepare_synced_docs.py` rather than editing the doc. |
| Page 404s, but is in the repo | Not in `nav:` — reachable by URL, absent from the sidebar. Add it. |
| Upstream merged, site unchanged | `publish-docs.yml` only fires on `docs/pub/**` paths. Check that run first, then this repo's run. |
| Sync run fails on push/auth | The deploy key. See below. |
| Edits here vanished | Working as designed — see the rule at the top. |

## The credential

The sync authenticates with an **ed25519 deploy key**, not a PAT: public half on
`circles-pub` with write access, private half in the `circles` repo's `actions` environment
as `CIRCLES_PUB_DEPLOY_KEY`. Scoped to this one repo, so a leak can't reach anything else.

To rotate: generate a new pair, `gh repo deploy-key add <pub> -R Vorski-Imagineering/circles-pub
--allow-write`, `gh secret set CIRCLES_PUB_DEPLOY_KEY -R Vorski-Imagineering/circles --env
actions < <private>`, delete the old key, then delete both local files. Never leave key
material on disk.

## Domain

`docs.circles.care` is an **unproxied** (grey-cloud) CNAME to `vorski-imagineering.github.io`
on the Cloudflare zone for `circles.care` — same pattern as `www`. It must stay unproxied:
proxying breaks GitHub's certificate issuance and renewal. `docs.yml` writes `site/CNAME` on
every build; drop that step and the custom domain resets to the `github.io` URL on the next
deploy.

## Rebuilding this for another repo pair

Order matters — Pages must exist before the custom domain, and the domain before HTTPS
enforcement.

1. Scaffold `mkdocs.yml`, `scripts/`, `.github/workflows/docs.yml`; seed `docs-pub/` from the
   source tree so the site builds before the first sync.
2. `gh repo create <org>/<name> --public --source=. --push`
3. `gh api -X POST repos/<org>/<name>/pages -f build_type=workflow`
4. Deploy key both ways (see above), then add `publish-docs.yml` to the source repo.
5. DNS CNAME → `<org>.github.io`, unproxied.
6. `gh api -X PUT repos/<org>/<name>/pages -f cname=<domain>`, wait for
   `https_certificate.state` to reach `approved`, then `-F https_enforced=true`. Sending the
   cname and https_enforced together 404s — the certificate doesn't exist yet.

The METIS repo pair (`METIS` → `METIS-pub` → `docs.the-gathering.earth`) is the same design,
with three differences: it publishes its own hand-written content alongside the synced tree,
so the docs sit under a `/docs-pub/` path instead of the site root; it normalizes lists but
doesn't de-link; and it authenticates with a PAT (`METIS_PUB_TOKEN`) instead of a deploy key.
