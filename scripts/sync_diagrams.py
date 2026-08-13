#!/usr/bin/env python3
"""
sync_diagrams.py  ·  colors_and_type.css  ->  drcwd-concept-diagrams/_diagram.css

The token block of _diagram.css is a BUILD ARTIFACT. The diagram frame rules
below it are hand-authored and are never touched.

Why this exists
---------------
The Concept-Diagram Visual Language doc already says it, at §1:

    "Tokens come from canonical drcwd-design-system/colors_and_type.css.
     _diagram.css MIRRORS it and must never diverge: an audit on 2026-08-05
     found it had drifted (its grape-500 was canonical grape-600, plus an
     invented grape-300). Realigned the same day."

It drifted again. On 2026-08-12 this file still carried:

    --ink-500: #797A80    canonical is #6E6F75 since 2026-07-27
    --ink-300: #B5B6BA    canonical is #C8CACE

#797A80 is the pre-WCAG ink-500 that fails AA at 4.28:1, and --ink-500 is what
--surface-fg-subtle resolves to, so every micro-cap and meta label on all 35
diagrams has been under the floor. A mirror maintained by hand drifts. That is
not a discipline problem, it is a design problem, so the mirror is now generated.

Per ~/.claude/CLAUDE.md rule 2: anything that must always happen is a script.

What is generated, and what is not
----------------------------------
GENERATED   the @import, the palette, both surface peers, and the --serif /
            --sans / --figures aliases the diagrams reference by those names.
UNTOUCHED   everything after the end marker: .slide, .brandbar, .dgm, .pay,
            .foot and their comments. Those carry hard-won layout reasoning
            (the align-self:center fix, the load-bearing 78px footer margin)
            and this script must never rewrite them.

On first run the boundary is detected as the last :root/[data-surface] block,
and markers are written in. After that the markers are authoritative.

Usage
-----
    python3 scripts/sync_diagrams.py           # write the token block
    python3 scripts/sync_diagrams.py --check   # exit 1 if the mirror has drifted
    python3 scripts/sync_diagrams.py --target /path/to/drcwd-concept-diagrams
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
DEFAULT_TARGET = Path.home() / (
    "My Drive/CAREER/Business/CONTENT/2-DRAFT/drcwd-concept-diagrams")
TARGET_REL = Path("_diagram.css")

START = "/* ===== GENERATED TOKEN BLOCK, START. Do not edit by hand. ===== */"
END = "/* ===== GENERATED TOKEN BLOCK, END. Hand-authored frame rules below. ===== */"

DECL = re.compile(r"--([a-z0-9-]+)\s*:\s*([^;]+);", re.I)
IMPORT_RE = re.compile(r"^@import\s+url\((['\"])(.+?)\1\);\s*$", re.M)

# the palette the diagrams actually reference, in the order they read best
PALETTE = [
    ("grape", ["900", "800", "700", "600", "500", "200", "100", "050"]),
    ("ink", ["max", "1000", "900", "700", "500", "400", "300", "200", "100", "050"]),
]
SURFACE_KEYS = ["surface", "surface-fg", "surface-fg-muted", "surface-fg-subtle",
                "surface-rule", "surface-eyebrow", "surface-stroke", "surface-accent",
                "surface-on-accent", "surface-logo", "surface-track", "surface-baseline"]


def block(css: str, selector: str) -> str:
    i = css.index(selector)
    start = css.index("{", i) + 1
    depth, j = 1, start
    while depth:
        if css[j] == "{":
            depth += 1
        elif css[j] == "}":
            depth -= 1
        j += 1
    return css[start:j - 1]


def declarations(body: str) -> dict[str, str]:
    return {n.lower(): v.strip() for n, v in DECL.findall(body)}


def source_stamp() -> str:
    try:
        sha = subprocess.run(["git", "-C", str(REPO), "rev-parse", "--short", "HEAD"],
                             capture_output=True, text=True, check=True).stdout.strip()
    except (subprocess.CalledProcessError, FileNotFoundError):
        return "unknown"
    dirty = subprocess.run(
        ["git", "-C", str(REPO), "status", "--porcelain", "--", "colors_and_type.css"],
        capture_output=True, text=True).stdout.strip()
    return f"{sha}-dirty" if dirty else sha


def wrap(lines: list[str], per_line: int = 4) -> list[str]:
    out = []
    for i in range(0, len(lines), per_line):
        out.append("  " + " ".join(lines[i:i + per_line]))
    return out


def token_block(css: str) -> str:
    root = declarations(block(css, ":root"))
    ink = declarations(block(css, '[data-surface="ink"]'))
    href = IMPORT_RE.search(css)

    L: list[str] = [START]
    L.append(f"/* Source: drcwd-design-system/colors_and_type.css @ {source_stamp()}")
    L.append("   Written by scripts/sync_diagrams.py. Edit the canonical CSS, not this.")
    L.append("   Frame rules below the END marker are hand-authored and never rewritten. */")
    if href:
        L.append(f"@import url('{href.group(2)}');")
    L.append(":root{")
    L.append("  /* palette, inherited from canonical */")
    for family, steps in PALETTE:
        present = [f"--{family}-{s}:{root[f'{family}-{s}']};"
                   for s in steps if f"{family}-{s}" in root]
        L += wrap(present)
    L.append(f"  --paper:{root['paper']};")
    status = [f"--status-{s}:{root[f'status-{s}']};" for s in ("up", "down", "warn")
              if f"status-{s}" in root]
    if status:
        L.append("  /* status, data-viz and form states only */")
        L += wrap(status, 3)
    L.append("")
    L.append("  /* SURFACE LAYER: two peer surfaces. Paper is default;")
    L.append("     set data-surface=\"ink\" on .slide. A diagram reads --surface-*")
    L.append("     and never a raw grape or ink token, or it cannot cross surfaces. */")
    L += wrap([f"--{k}:{root[k]};" for k in SURFACE_KEYS if k in root], 2)
    L.append("")
    L.append("  /* type. The diagrams reference --serif / --sans / --figures by those")
    L.append("     short names, so the canonical stacks are aliased rather than renamed. */")
    for short, canonical in (("serif", "font-serif"), ("sans", "font-sans"),
                             ("figures", "font-figures"), ("mono", "font-mono-asset")):
        if canonical in root:
            L.append(f"  --{short}:{root[canonical]};")
    L.append("}")
    L.append('[data-surface="ink"]{')
    L += wrap([f"--{k}:{ink[k]};" for k in SURFACE_KEYS if k in ink], 2)
    L.append("}")
    L.append(END)
    return "\n".join(L)


def split_target(text: str) -> tuple[str, str]:
    """Return (generated_block, hand_authored_tail)."""
    if START in text and END in text:
        head, rest = text.split(START, 1)
        _, tail = rest.split(END, 1)
        if head.strip():
            raise ValueError("unexpected content before the generated block")
        return "", tail.lstrip("\n")
    # first run: the boundary is the end of the last :root / [data-surface] block
    last = 0
    for m in re.finditer(r"(?::root|\[data-surface=\"ink\"\])\s*\{", text):
        depth, j = 1, text.index("{", m.start()) + 1
        while depth:
            if text[j] == "{":
                depth += 1
            elif text[j] == "}":
                depth -= 1
            j += 1
        last = max(last, j)
    if not last:
        raise ValueError("no :root block found; is this the right file?")
    return "", text[last:].lstrip("\n")


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("--check", action="store_true")
    ap.add_argument("--target", type=Path, default=DEFAULT_TARGET)
    args = ap.parse_args()

    try:
        guard_css(CSS)
    except CssGuardError as e:
        print(str(e), file=sys.stderr)
        return 2

    target = args.target / TARGET_REL
    if not target.exists():
        print(f"not found: {target}", file=sys.stderr)
        return 2

    css = CSS.read_text(encoding="utf-8")
    current = target.read_text(encoding="utf-8")
    _, tail = split_target(current)
    rendered = token_block(css) + "\n" + tail

    if args.check:
        try:
            _, cur_tail = split_target(current)
        except ValueError as e:
            print(f"{target}: {e}", file=sys.stderr)
            return 1
        if START not in current:
            print(f"{target} is not yet generated. Run: python3 scripts/sync_diagrams.py",
                  file=sys.stderr)
            return 1
        cur_block = current.split(START, 1)[1].split(END, 1)[0]
        new_block = rendered.split(START, 1)[1].split(END, 1)[0]
        # ignore the stamp line, which moves with every commit
        strip = lambda s: "\n".join(l for l in s.splitlines() if "@ " not in l)
        if strip(cur_block) == strip(new_block) and cur_tail == tail:
            print(f"{target} matches colors_and_type.css")
            return 0
        print(f"{target} has DRIFTED. Run: python3 scripts/sync_diagrams.py", file=sys.stderr)
        return 1

    target.write_text(rendered, encoding="utf-8")
    print(f"wrote {target}")
    print(f"  from design-system {source_stamp()}")
    print(f"  hand-authored frame rules preserved: {len(tail.splitlines())} lines")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
