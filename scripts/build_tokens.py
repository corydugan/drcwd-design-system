#!/usr/bin/env python3
"""
build_tokens.py  ·  colors_and_type.css  ->  tokens.json

tokens.json is GENERATED. Never edit it by hand. Edit colors_and_type.css and
run this script.

Why this exists
---------------
On 2026-08-12 an audit found seven files independently defining the brand
palette, and the retirement of DM Serif Display (commit 605ee77) had landed in
exactly one line of one file. tokens.json, sitting in the same repo and the
same commit, still named DM Serif Display as the display face, and its
categorical data-viz ramp still carried #797A80, the pre-WCAG ink-500 that was
corrected on 2026-07-27. Its own header already said "Generated from
colors_and_type.css", but no generator existed, so "generated" meant
"retyped when someone remembered".

Per ~/.claude/CLAUDE.md rule 2: anything that must always happen is a script,
not an instruction.

What it does
------------
1. Parses the :root and [data-surface="ink"] blocks of colors_and_type.css.
2. Rebuilds the token tree, resolving var(--x) into {alias.path} references
   and into literal hex where an array of values is required.
3. Carries forward every $description from the existing tokens.json by path,
   so the reasoning written by hand is never lost.
4. Rebuilds $meta.locked from the "Locked constraints:" line in the CSS header,
   which is what went stale last time.
5. Writes tokens.json. Emits the SAME sections the file already had, so a diff
   shows only corrected drift, not a reshaped file.

Usage
-----
    python3 scripts/build_tokens.py           # write tokens.json
    python3 scripts/build_tokens.py --check   # exit 1 if out of date, write nothing
"""

from __future__ import annotations

import json
import re
import sys

sys.path.insert(0, str(__import__('pathlib').Path(__file__).resolve().parent))

from css_guard import CssGuardError, check as guard_css
from css_parse import find_block, declarations as parse_declarations
from collections import OrderedDict
from pathlib import Path


REPO = Path(__file__).resolve().parent.parent
CSS = REPO / "colors_and_type.css"
TOKENS = REPO / "tokens.json"

# --- CSS var name -> token path -------------------------------------------------
# Only names listed here reach tokens.json. Anything else in the CSS is web-only
# plumbing (motion, z-index, containers) that no downstream tool consumes yet.

def _color_paths() -> dict[str, tuple[str, ...]]:
    m: dict[str, tuple[str, ...]] = {}
    for step in ("900", "800", "700", "600", "500", "200", "100", "050"):
        m[f"grape-{step}"] = ("color", "grape", step)
    for step in ("max", "1000", "900", "700", "500", "400", "300", "200", "100", "050"):
        m[f"ink-{step}"] = ("color", "ink", step)
    m["paper"] = ("color", "paper")
    for s in ("up", "down", "warn"):
        m[f"status-{s}"] = ("color", "status", s)
    return m


COLOR_PATHS = _color_paths()

SURFACE_KEYS = OrderedDict([
    ("surface", "field"),
    ("surface-fg", "fg"),
    ("surface-fg-muted", "fgMuted"),
    ("surface-fg-subtle", "fgSubtle"),
    ("surface-rule", "rule"),
    ("surface-stroke", "stroke"),
    ("surface-accent", "accent"),
    ("surface-on-accent", "onAccent"),
    ("surface-eyebrow", "eyebrow"),
    ("surface-logo", "logo"),
    ("surface-track", "track"),
    ("surface-baseline", "baseline"),
])

FONT_KEYS = OrderedDict([
    ("font-serif", "serif"),
    ("font-sans", "sans"),
    ("font-figures", "figures"),
    ("font-mono", "mono"),
    ("font-mono-asset", "monoAsset"),
])

FS_ORDER = ["display-xl", "display-lg", "display-md", "display-sm", "stat",
            "heading-lg", "heading-md", "heading-sm",
            "body-lg", "body", "body-sm", "meta", "micro"]
FW_ORDER = ["light", "regular", "medium", "semibold", "bold"]
SPACE_ORDER = ["1", "2", "3", "4", "5", "6", "8", "10", "12", "16", "20", "24", "32", "40"]
RADIUS_ORDER = ["xs", "sm", "md", "lg", "xl", "pill"]

DECL = re.compile(r"--([a-z0-9-]+)\s*:\s*([^;]+);", re.I)
VAR_REF = re.compile(r"var\(\s*--([a-z0-9-]+)\s*\)", re.I)


def block(css: str, selector: str) -> str:
    """Comment- and string-aware. A comment mentioning the selector
    used to hijack this and hand back the wrong block."""
    return find_block(css, selector)


def declarations(body: str):
    """Comment-blind parsing is what let a comment quoting an old hex
    overwrite a live token. Strict: a missing semicolon now raises."""
    return parse_declarations(body)


def resolve_hex(name: str, decls: dict[str, str], seen: set[str] | None = None) -> str:
    """Follow var() chains until a literal lands. Raises on a cycle or a miss."""
    seen = seen or set()
    if name in seen:
        raise ValueError(f"circular var reference at --{name}")
    seen.add(name)
    value = decls.get(name)
    if value is None:
        raise KeyError(f"--{name} is referenced but never declared in colors_and_type.css")
    ref = VAR_REF.search(value)
    if ref:
        return resolve_hex(ref.group(1).lower(), decls, seen)
    return value.strip()


def alias_or_literal(value: str) -> str:
    """var(--ink-1000) -> {color.ink.1000}; a literal stays literal."""
    ref = VAR_REF.search(value)
    if not ref:
        return value.strip()
    target = ref.group(1).lower()
    path = COLOR_PATHS.get(target)
    if path is None:
        raise KeyError(f"--{target} has no tokens.json path; add it to COLOR_PATHS")
    return "{" + ".".join(path) + "}"


def primary_family(stack: str) -> str:
    """'Instrument Serif', 'DM Serif Display', Georgia  ->  Instrument Serif"""
    first = stack.split(",")[0].strip()
    return first.strip("'\"")


def locked_constraints(css: str) -> list[str]:
    """Rebuild $meta.locked from the CSS header. This is the line that went stale."""
    m = re.search(r"Locked constraints:(.*?)\*/", css, re.S)
    if not m:
        raise ValueError("no 'Locked constraints:' line in the colors_and_type.css header")
    text = " ".join(m.group(1).split())
    text = re.sub(r"\s*=+\s*$", "", text).strip()
    parts = [p.strip(" .") for p in text.split("·")]
    return [p for p in parts if p]


def collect_descriptions(node, path=(), out=None):
    """Every $description already written, keyed by its token path."""
    out = {} if out is None else out
    if isinstance(node, dict):
        if "$description" in node and isinstance(node["$description"], str):
            out[path] = node["$description"]
        for k, v in node.items():
            if not k.startswith("$"):
                collect_descriptions(v, path + (k,), out)
    return out


def leaf(value, ttype=None, path=(), descriptions=None):
    node: "OrderedDict[str, object]" = OrderedDict()
    if ttype:
        node["$type"] = ttype
    node["$value"] = value
    desc = (descriptions or {}).get(path)
    if desc:
        node["$description"] = desc
    return node


def build() -> "OrderedDict":
    guard_css(CSS)          # refuse to generate from a stylesheet that will not parse
    css = CSS.read_text(encoding="utf-8")
    root = declarations(block(css, ":root"))
    ink = declarations(block(css, '[data-surface="ink"]'))

    previous = json.loads(TOKENS.read_text(encoding="utf-8")) if TOKENS.exists() else {}
    desc = collect_descriptions(previous)

    def L(value, ttype, *path):
        return leaf(value, ttype, tuple(path), desc)

    out: "OrderedDict[str, object]" = OrderedDict()
    out["$schema"] = previous.get("$schema", "https://design-tokens.org/format")
    out["$description"] = (
        "Dr. Cory Dugan brand design tokens. Tool-agnostic source for Figma "
        "(Tokens Studio), Canva, Tailwind, Style Dictionary. GENERATED from "
        "colors_and_type.css by scripts/build_tokens.py. Do not edit this file "
        "by hand: edit the CSS and re-run the script."
    )
    meta: "OrderedDict[str, object]" = OrderedDict()
    prev_meta = previous.get("$meta", {})
    meta["brand"] = prev_meta.get("brand", "Dr. Cory Dugan (drCWDugan)")
    meta["version"] = prev_meta.get("version", "3.0.0")
    meta["supersedes"] = prev_meta.get("supersedes", "")
    meta["generatedFrom"] = "colors_and_type.css"
    meta["locked"] = locked_constraints(css)
    out["$meta"] = meta

    # ---- color ----
    color: "OrderedDict[str, object]" = OrderedDict()
    grape: "OrderedDict[str, object]" = OrderedDict()
    for step in ("900", "800", "700", "600", "500", "200", "100", "050"):
        grape[step] = L(root[f"grape-{step}"], "color", "color", "grape", step)
    color["grape"] = grape

    inkc: "OrderedDict[str, object]" = OrderedDict()
    for step in ("max", "1000", "900", "700", "500", "400", "300", "200", "100", "050"):
        inkc[step] = L(root[f"ink-{step}"], "color", "color", "ink", step)
    color["ink"] = inkc

    color["paper"] = L(root["paper"], "color", "color", "paper")

    status: "OrderedDict[str, object]" = OrderedDict()
    for s in ("up", "down", "warn"):
        status[s] = L(root[f"status-{s}"], "color", "color", "status", s)
    color["status"] = status

    dataviz: "OrderedDict[str, object]" = OrderedDict()
    dataviz["categorical"] = L(
        [resolve_hex(f"dv-cat-{i}", root) for i in range(1, 6)],
        "array", "color", "dataviz", "categorical")
    dataviz["sequential"] = L(
        [resolve_hex(f"dv-seq-{i}", root) for i in range(1, 5)],
        "array", "color", "dataviz", "sequential")
    color["dataviz"] = dataviz
    out["color"] = color

    # ---- gradient (a rule, not a value; carried forward verbatim) ----
    if "gradient" in previous:
        out["gradient"] = previous["gradient"]

    # ---- font ----
    font: "OrderedDict[str, object]" = OrderedDict()
    for css_name, key in FONT_KEYS.items():
        if css_name in root:
            font[key] = L(primary_family(root[css_name]), "fontFamily", "font", key)
    out["font"] = font

    # ---- fontSize / fontWeight ----
    fs: "OrderedDict[str, object]" = OrderedDict()
    for k in FS_ORDER:
        if f"fs-{k}" in root:
            fs[k] = L(" ".join(root[f"fs-{k}"].split()), "dimension", "fontSize", k)
    out["fontSize"] = fs

    fw: "OrderedDict[str, object]" = OrderedDict()
    for k in FW_ORDER:
        fw[k] = leaf(int(root[f"fw-{k}"]), None, ("fontWeight", k), desc)
    out["fontWeight"] = fw

    # ---- spacing / radius ----
    spacing: "OrderedDict[str, object]" = OrderedDict()
    for k in SPACE_ORDER:
        spacing[k] = L(root[f"space-{k}"], "dimension", "spacing", k)
    out["spacing"] = spacing

    radius: "OrderedDict[str, object]" = OrderedDict()
    for k in RADIUS_ORDER:
        radius[k] = L(root[f"radius-{k}"], "dimension", "radius", k)
    out["radius"] = radius

    # ---- surface: two peers, paper from :root, ink from the override block ----
    surface: "OrderedDict[str, object]" = OrderedDict()
    if ("surface",) in desc:
        surface["$description"] = desc[("surface",)]
    for peer, decls in (("paper", root), ("ink", ink)):
        peer_node: "OrderedDict[str, object]" = OrderedDict()
        if ("surface", peer) in desc:
            peer_node["$description"] = desc[("surface", peer)]
        for css_name, key in SURFACE_KEYS.items():
            if css_name in decls:
                peer_node[key] = leaf(
                    alias_or_literal(decls[css_name]), "color",
                    ("surface", peer, key), desc)
        surface[peer] = peer_node
    out["surface"] = surface

    return out


def main() -> int:
    check = "--check" in sys.argv
    try:
        built = build()
    except CssGuardError as e:
        print(str(e), file=sys.stderr)
        return 2
    rendered = json.dumps(built, indent=2, ensure_ascii=False) + "\n"

    if check:
        current = TOKENS.read_text(encoding="utf-8") if TOKENS.exists() else ""
        if current == rendered:
            print("tokens.json is up to date with colors_and_type.css")
            return 0
        print("tokens.json is STALE. Run: python3 scripts/build_tokens.py", file=sys.stderr)
        return 1

    TOKENS.write_text(rendered, encoding="utf-8")
    print(f"wrote {TOKENS.relative_to(REPO)}")
    print(f"  locked constraints: {built['$meta']['locked']}")
    print(f"  display face:       {built['font']['serif']['$value']}")
    print(f"  categorical ramp:   {built['color']['dataviz']['categorical']['$value']}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
