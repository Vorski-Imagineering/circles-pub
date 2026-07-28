#!/usr/bin/env python3
"""
Fix up Markdown synced from the Circles repo so it renders correctly under
MkDocs (Python-Markdown), which is stricter than GitHub's renderer.

Two passes, both in place over every *.md under the given directories:

1. Blank line before lists. GitHub (GFM/CommonMark) lets a list interrupt a
   paragraph with no blank line between; Python-Markdown does not — it silently
   folds the list into the preceding paragraph as plain text.

2. De-link relative links that don't resolve to a page. Browsing on GitHub, a
   link to a directory (`[circle/](circle)`) or to an unpublished sibling tree
   (`[docs/dev](../dev)`) works; on the built site neither has a URL, so they
   would 404. Anything relative that isn't a `*.md` target is reduced to its
   link text — the sidebar nav covers section browsing.

Usage: prepare_synced_docs.py <dir> [<dir> ...]
"""
import re
import sys
from pathlib import Path

LIST_RE = re.compile(r'^(\s*)([-*+]\s+|\d+[.)]\s+)')
FENCE_RE = re.compile(r'^\s*(```|~~~)')
# [text](target); kept only when target is external, an anchor, or a .md page
LINK_RE = re.compile(r'(?<!!)\[([^\]]*)\]\(([^)\s]+)\)')
KEEP_RE = re.compile(r'^(https?:|mailto:|#|[^)]*\.md(#.*)?$)')


def normalize_lists(text):
    lines = text.split('\n')
    out = []
    in_fence = False
    in_list = False
    for line in lines:
        if FENCE_RE.match(line):
            in_fence = not in_fence
            in_list = False
            out.append(line)
            continue
        if not in_fence and LIST_RE.match(line):
            if not in_list and out and out[-1].strip() != '':
                out.append('')
            in_list = True
        elif line.strip() == '':
            in_list = False
        elif not line.startswith((' ', '\t')):
            in_list = False
        out.append(line)
    return '\n'.join(out)


def delink_unresolvable(text, path):
    def replace(match):
        if KEEP_RE.match(match.group(2)):
            return match.group(0)
        print(f"  de-linked {match.group(0)!r} in {path}")
        return match.group(1)
    return LINK_RE.sub(replace, text)


def main(argv):
    if not argv:
        print(__doc__)
        return 1
    changed = 0
    for root in argv:
        for path in sorted(Path(root).rglob('*.md')):
            original = path.read_text()
            fixed = delink_unresolvable(normalize_lists(original), path)
            if fixed != original:
                path.write_text(fixed)
                changed += 1
                print(f"prepared: {path}")
    print(f"{changed} file(s) changed")
    return 0


if __name__ == '__main__':
    raise SystemExit(main(sys.argv[1:]))
