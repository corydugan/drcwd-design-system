#!/usr/bin/env python3
"""
sync_website.py  ·  colors_and_type.css  ->  drcwd-website/styles/brand.css

The website's brand.css is a BUILD ARTIFACT. Never edit it. Edit
colors_and_type.css here and run this script.

Why this exists
---------------
On 2026-08-12 an audit found drcwd-website/styles/brand.css was a hand-made
fork, not an import: 285 lines against the canonical 356, missing the entire
surface layer (12 tokens, added 2026-08-05), --font-figures and
--font-mono-asset. It carried the ink-500 WCAG fix but not the rest, so it was
selectively out of date, which is the kind nobody spots. Fourteen live pages
and 54 tokens consumed by site.css were sitting on it.

A structural diff at the time showed the fork contained exactly ONE rule of its
own, `a:focus-visible`, which has been moved to site.css where site-specific
rules belong. brand.css therefore has no exceptions left and can be overwritten
wholesale, which is what makes this script safe.

The @import
-----------
colors_and_type.css opens with an @import for the Google Fonts stack. That is
correct for the design system, where the CSS is loaded standalone. It is wrong
for the website, where an @import inside a stylesheet is render-blocking and
serialises behind the CSS request. The site loads the same families through a
<link rel=preconnect/stylesheet> in each page head instead, so this script
strips the @import and prints the canonical <link> href for the pages to carry.
Run with --fonts to print just that href.

Usage
-----
    python3 scripts/sync_website.py            # write brand.css
    python3 scripts/sync_website.py --check    # exit 1 if the site is stale
    python3 scripts/sync_website.py --fonts    # print the canonical font href
    python3 scripts/sync_website.py --website /path/to/drcwd-website
"""

from __future__ import annotations

import argparse
import re
import subprocess
import sys
from pathlib import Path

from css_guard import CssGuardError, check as guard_css

sys.path.insert(0, str(Path(__file__).resolve().parent))

REPO = Path(__file__).resolve().parent.parent
CSS = REPO / "colors_and_type.css"
DEFAULT_WEBSITE = REPO.parent / "drcwd-website"
TARGET_REL = Path("styles/brand.css")

IMPORT_RE = re.compile(r"^@import\s+url\((['\"])(.+?)\1\);\s*$", re.M)
MARKER = "GENERATED FILE, DO NOT EDIT"


def source_stamp() -> str:
    """Short sha of the design system, plus a dirty flag when it matters."""
    try:
        sha = subprocess.run(
            ["git", "-C", str(REPO), "rev-parse", "--short", "HEAD"],
            capture_output=True, text=True, check=True).stdout.strip()
    except (subprocess.CalledProcessError, FileNotFoundError):
        return "unknown"
    dirty = subprocess.run(
        ["git", "-C", str(REPO), "status", "--porcelain", "--", "colors_and_type.css"],
        capture_output=True, text=True).stdout.strip()
    return f"{sha}-dirty" if dirty else sha


def font_href(css: str) -> str | None:
    m = IMPORT_RE.search(css)
    return m.group(2) if m else None


def header(stamp: str, href: str | None) -> str:
    lines = [
        "/* =====================================================================",
        f"   {MARKER}.",
        "",
        "   Source:    drcwd-design-system/colors_and_type.css",
        f"   Generated: scripts/sync_website.py from design-system {stamp}",
        "",
        "   Edits made here are overwritten on the next sync and will silently",
        "   diverge the live site from the brand in the meantime. That is exactly",
        "   what happened before 2026-08-12: this file was a hand-made fork that",
        "   had fallen 14 tokens behind without anyone being able to tell.",
        "",
        "   To change the brand: edit colors_and_type.css in the design system,",
        "   run scripts/sync_website.py, then commit BOTH repos.",
        "   Site-specific rules belong in styles/site.css, never here.",
    ]
    if href:
        lines += [
            "",
            "   The @import from the source was stripped: the site loads these",
            "   families through a <link> in each page head instead, which is not",
            "   render-blocking behind the stylesheet request. Canonical href:",
            f"   {href}",
        ]
    lines += ["   ===================================================================== */", "", ""]
    return "\n".join(lines)


def build(css: str, stamp: str) -> str:
    href = font_href(css)
    body = IMPORT_RE.sub("", css, count=1).lstrip("\n")
    return header(stamp, href) + body


def body_of(text: str) -> str:
    """Everything after the generated header, for a stamp-insensitive compare."""
    end = text.find("*/")
    return text[end + 2:].strip() if MARKER in text[:2000] and end != -1 else text.strip()


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("--check", action="store_true")
    ap.add_argument("--fonts", action="store_true")
    ap.add_argument("--website", type=Path, default=DEFAULT_WEBSITE)
    args = ap.parse_args()

    try:
        guard_css(CSS)      # never sync a stylesheet that will not parse
    except CssGuardError as e:
        print(str(e), file=sys.stderr)
        return 2
    css = CSS.read_text(encoding="utf-8")

    if args.fonts:
        href = font_href(css)
        if not href:
            print("no @import found in colors_and_type.css", file=sys.stderr)
            return 1
        print(href)
        return 0

    target = args.website / TARGET_REL
    if not args.website.exists():
        print(f"website repo not found at {args.website}", file=sys.stderr)
        print("pass --website /path/to/drcwd-website", file=sys.stderr)
        return 2

    rendered = build(css, source_stamp())

    if args.check:
        if not target.exists():
            print(f"{target} does not exist", file=sys.stderr)
            return 1
        current = target.read_text(encoding="utf-8")
        if MARKER not in current[:2000]:
            print(f"{target} is NOT a generated file. Someone forked it again.", file=sys.stderr)
            return 1
        if body_of(current) == body_of(rendered):
            print(f"{target} matches colors_and_type.css")
            return 0
        print(f"{target} is STALE. Run: python3 scripts/sync_website.py", file=sys.stderr)
        return 1

    target.parent.mkdir(parents=True, exist_ok=True)
    target.write_text(rendered, encoding="utf-8")
    print(f"wrote {target}")
    print(f"  from design-system {source_stamp()}")
    print(f"  {len(rendered.splitlines())} lines")
    href = font_href(css)
    if href:
        print("\n  pages must load this font href:")
        print(f"  {href}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
