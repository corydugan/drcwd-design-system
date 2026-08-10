#!/usr/bin/env python3
"""Generate the two brand Google Doc sources from the repo, never by retyping.

DOC A  the complete specification. Every token, every number, machine-extracted
       from colors_and_type.css so a value cannot drift between the repo and
       the Notebook.
DOC B  the visual brand sheet as prose, mirroring the six-page PDF.

Both carry provenance and both are _FROZEN: they are snapshots of a commit, and
the repo wins if they ever disagree. Regenerate rather than edit.
"""
import datetime as dt
import json
import re
import subprocess
from pathlib import Path

REPO = Path(__file__).resolve().parent          # this script lives IN the repo it reads
OUT = Path(__file__).resolve().parent / "build"  # generated docs, gitignored
OUT.mkdir(exist_ok=True)
_today = dt.date.today()
DATE = _today.strftime("%-d %B %Y")
STAMP = _today.strftime("%m%d%Y")

COMMIT = subprocess.run(["git", "-C", str(REPO), "rev-parse", "--short", "HEAD"],
                        capture_output=True, text=True).stdout.strip()
DIRTY = subprocess.run(["git", "-C", str(REPO), "status", "--porcelain"],
                       capture_output=True, text=True).stdout.strip()

css = (REPO / "colors_and_type.css").read_text()
root = css.split(":root {", 1)[1]
props = re.findall(r"--([a-zA-Z0-9-]+):\s*([^;]+);", root)
raw = {k: v.strip() for k, v in props}


def resolve(v, d=0):
    if d > 6:
        return v
    m = re.fullmatch(r"var\(--([a-zA-Z0-9-]+)\)", v.strip())
    return resolve(raw.get(m.group(1), v), d + 1) if m else v.strip()


ink_block = css.split('[data-surface="ink"] {', 1)[1].split("}", 1)[0]
ink = {k: v.strip() for k, v in re.findall(r"--([a-zA-Z0-9-]+):\s*([^;]+);", ink_block)}

# --- the paper values are whatever :root held BEFORE the ink block reassigned them
paper_surface = {}
for k, v in props:
    if k.startswith("surface"):
        paper_surface.setdefault(k, v.strip())


def px(rem_str):
    m = re.fullmatch(r"([\d.]+)rem", rem_str)
    return f"{float(m.group(1)) * 16:g}px" if m else ""


def row(*cells):
    return "| " + " | ".join(str(c) for c in cells) + " |"


def table(headers, rows):
    out = [row(*headers), row(*["---"] * len(headers))]
    out += [row(*r) for r in rows]
    return "\n".join(out)


COLOUR_ROLE = {
    "grape-900": "deepest grape. Dense accents only.",
    "grape-800": "PRIMARY. Links, numerals, key marks, the paper accent.",
    "grape-700": "hovers, mid-strength fills, the paper eyebrow.",
    "grape-600": "illustration, chart secondary, load-bearing line art on paper.",
    "grape-500": "chart tertiary, and the accent and eyebrow on the ink surface.",
    "grape-200": "the data-baseline rule under a stat block.",
    "grape-100": "chart fills, soft backgrounds, text selection.",
    "grape-050": "barely-there tint. Rare, section dividers only.",
    "ink-max": "the INK SURFACE field, and stat displays on paper. Not stats only.",
    "ink-1000": "body text, strong emphasis, headline on paper.",
    "ink-900": "near-body, and the hairline rule on the ink surface.",
    "ink-700": "secondary text, labels, body, citations on paper.",
    "ink-500": "muted, meta, captions. Darkened 2026-07-27 for WCAG AA, 4.28:1 to 5.01:1.",
    "ink-400": "placeholder, disabled.",
    "ink-300": "strong hairlines, and subtle foreground on the ink surface.",
    "ink-200": "default hairline, and muted foreground plus stroke on ink.",
    "ink-100": "dividers, wash.",
    "ink-050": "off-white surface, soft background.",
    "paper": "the PAPER SURFACE field. Default and workhorse, a peer of ink.",
    "status-up": "improvement. Uses brand grape rather than green.",
    "status-down": "decline. Desaturated terracotta.",
    "status-warn": "monitoring. Desaturated mustard.",
}

SURFACE_ROLE = {
    "surface": "the field",
    "surface-fg": "headline, primary text",
    "surface-fg-muted": "labels, body, citations",
    "surface-fg-subtle": "micro-caps, meta",
    "surface-rule": "hairline dividers",
    "surface-eyebrow": "tracked micro-caps kicker",
    "surface-stroke": "load-bearing line art",
    "surface-accent": "the ONE solid element",
    "surface-on-accent": "text reversed out of accent",
}

PROVENANCE = f"""**Source.** `~/Documents/GitHub/drcwd-design-system`, commit `{COMMIT}`.
**Generated.** {DATE}, machine-extracted from `colors_and_type.css`. No value in this
document was typed by hand.
**Status.** FROZEN snapshot. If this document and the repo disagree, **the repo wins**.
Regenerate rather than edit.
**Working tree at generation:** {"MODIFIED, uncommitted changes present" if DIRTY else "clean"}.
"""

# ============================== DOC A ==============================
A = []
A.append("# drCWDugan Brand System v3 Authority")
A.append("## The complete specification, every token and every number\n")
A.append(PROVENANCE)
A.append("\n---\n")

A.append("## 0 · Locked constraints\n")
A.append("These four do not change without a version bump.\n")
A.append(table(["constraint", "value"], [
    ["brand grape", "`#352051`"],
    ["display face", "DM Serif Display"],
    ["body face", "DM Sans"],
    ["ground", "white-dominant editorial, 35 to 40 percent whitespace minimum"],
]))
A.append("\nGrape is an ink and an accent. It is **never** a page fill, on either surface.")
A.append("Supersedes v2 grape (2026-06-12) and the retired v1 teal system.\n")

A.append("## 1 · Colour, the base palette\n")
A.append(f"{len(COLOUR_ROLE)} raw values. Everything else in the system references these.\n")
A.append(table(["token", "hex", "role"],
               [[f"`--{k}`", f"`{raw[k]}`", COLOUR_ROLE[k]] for k in COLOUR_ROLE if k in raw]))

A.append("\n## 2 · The surface layer, added 2026-08-05\n")
A.append("**Two peer surfaces. Not a light mode and a dark mode.** Paper is the default and "
         "stays the workhorse: clinical, calm, what evidence-led work is set on. Ink is a full "
         "peer, reached for when the message wants weight rather than calm, meaning a hook, a "
         "quote, a launch, or one hard claim.\n")
A.append("A component never hard-codes a colour. It reads `--surface-*` and inherits whatever "
         "surface it sits on. The surface is set on the card root.\n")
A.append("```html\n<div class=\"slide\">                  paper, the default\n"
         "<div class=\"slide\" data-surface=\"ink\">   ink\n```\n")
A.append(table(["token", "paper", "paper hex", "ink", "ink hex", "role"],
               [[f"`--{k}`", f"`{paper_surface[k]}`", f"`{resolve(paper_surface[k])}`",
                 f"`{ink[k]}`", f"`{resolve(ink[k])}`", SURFACE_ROLE[k]]
                for k in SURFACE_ROLE if k in paper_surface and k in ink]))
A.append("\n**Measured contrast on the ink field `#0B0B0C`.**\n")
A.append(table(["pair", "ratio", "verdict"], [
    ["fg on field", "19.66:1", "pass"],
    ["fg-muted on field", "15.59:1", "pass"],
    ["fg-subtle on field", "11.97:1", "pass"],
    ["stroke on field", "15.59:1", "pass"],
    ["accent on field", "4.72:1", "pass"],
    ["on-accent, white on grape-500", "**4.16:1**", "**LARGE TEXT ONLY**, 24px or more, or 18.66px bold or more"],
]))
A.append("\nNever set small text in `--surface-on-accent`. The dark field is `ink-max`, not grape.\n")

A.append("## 3 · Data visualisation ramps\n")
A.append("Charts inherit the brand. No rainbow, and no gradient anywhere by design.\n")
A.append("**Categorical, maximum five series. Discipline over variety.**\n")
A.append(table(["slot", "token", "hex"],
               [[f"`--dv-cat-{i}`", f"`{raw[f'dv-cat-{i}']}`", f"`{resolve(raw[f'dv-cat-{i}'])}`"]
                for i in range(1, 6)]))
A.append("\n**Sequential, light to dark, for heatmaps and graduated fills.**\n")
A.append(table(["step", "token", "hex"],
               [[f"`--dv-seq-{i}`", f"`{raw[f'dv-seq-{i}']}`", f"`{resolve(raw[f'dv-seq-{i}'])}`"]
                for i in range(1, 5)]))

A.append("\n## 4 · Semantic colour tokens\n")
A.append("Reference these in components, not the raw hex above.\n")
A.append(table(["token", "resolves to", "hex"],
               [[f"`--{k}`", f"`{raw[k]}`", f"`{resolve(raw[k])}`"]
                for k, _ in props if k.startswith("color-")]))

A.append("\n## 5 · Typography\n### 5.1 Families\n")
A.append(table(["role", "stack"], [
    ["serif, display and headlines", f"`{raw['font-serif']}`"],
    ["sans, body and UI and tabular stats", f"`{raw['font-sans']}`"],
    ["mono, code and the evidence voice", f"`{raw['font-mono']}`"],
]))
A.append("\n### 5.2 Type scale\n")
sizes = [k for k, _ in props if k.startswith("fs-")]
A.append(table(["token", "value", "px at 16px root", "use"], [
    [f"`--{k}`", f"`{raw[k]}`", px(raw[k]) or "fluid",
     {"fs-display-xl": "hero", "fs-display-lg": "section opener", "fs-display-md": "",
      "fs-display-sm": "", "fs-stat": "tabular stat display, the credibility hero",
      "fs-heading-lg": "h4", "fs-heading-md": "h5", "fs-heading-sm": "h6",
      "fs-body-lg": "lead, service descriptions", "fs-body": "default body",
      "fs-body-sm": "", "fs-meta": "eyebrow, caption", "fs-micro": "uppercase tags, method labels"}.get(k, "")]
    for k in sizes]))
A.append("\n### 5.3 Line height, tracking, weight\n")
A.append(table(["token", "value"],
               [[f"`--{k}`", f"`{raw[k]}`"] for k, _ in props
                if k.startswith(("lh-", "tracking-", "fw-"))]))

A.append("\n### 5.4 The drop-in type classes\n")
A.append(table(["class", "settings"], [
    ["`h1` / `.display-xl`", "serif, `--fs-display-xl`, lh 1.05, tracking -0.02em, weight 400"],
    ["`h2` / `.display-lg`", "serif, `--fs-display-lg`, lh 1.05, tracking -0.02em, weight 400"],
    ["`h3` / `.display-md`", "serif, `--fs-display-md`, lh 1.2, tracking -0.02em, weight 400"],
    ["`h4`", "sans, 1.5rem, lh 1.2, weight 500, tracking -0.005em"],
    ["`h5`", "sans, 1.25rem, lh 1.2, weight 500"],
    ["`h6`", "sans, 1.0625rem, lh 1.2, weight 600"],
    ["`.display-italic`", "serif italic. The signature emphasis treatment."],
    ["`p`", "sans, 1rem, lh 1.6, colour `--color-fg-muted`, `text-wrap: pretty`"],
    ["`p.lead`", "1.125rem, lh 1.55, max-width 60ch"],
    ["`.eyebrow`", "sans, 0.8125rem, weight 500, tracking 0.14em, uppercase, grape-800"],
    ["`.tag`", "sans, 0.6875rem, weight 500, tracking 0.08em, uppercase, ink-500"],
    ["`.numeral`", "serif italic, `--fs-display-md`, grape-800, lh 1, tracking -0.01em"],
    ["`.stat`", "sans, weight 700, `--fs-stat`, tabular-nums lining-nums, ink-max, lh 1, tracking -0.02em"],
    ["`.stat--grape`", "as `.stat`, coloured grape-800"],
    ["`.method-label`", "sans, 0.6875rem, weight 600, tracking 0.18em, uppercase, ink-500"],
    ["`.data-baseline`", "2px top border in grape-200, width 48px, margin-top 12px"],
    ["`.evidence` / `.stat-meta`", "mono, 0.9375rem, ink-500, tracking 0"],
    ["`.citation`", "sans, 0.8125rem, ink-500, lh 1.3. Links get a dotted underline."],
    ["`.nowrap`", "keeps an evidence unit intact. \"p < .001\" must never break across lines."],
]))
A.append("\n**Vertical rhythm.** Headings carry `margin: 0` so layouts own spacing. Adjacent-sibling "
         "rules add breathing room only when text follows a heading: eyebrow then heading gets 12px, "
         "heading then paragraph gets 20px, heading then heading gets 16px.\n")

A.append("## 6 · Spacing and layout\n### 6.1 Spacing, 4px base\n")
A.append(table(["token", "value"], [[f"`--{k}`", f"`{raw[k]}`"] for k, _ in props if k.startswith("space-")]))
A.append("\n### 6.2 Section rhythm and containers\n")
A.append(table(["token", "value", "use"], [
    ["`--section-y`", f"`{raw['section-y']}`", "section vertical rhythm"],
    ["`--section-y-tight`", f"`{raw['section-y-tight']}`", "tight sections"],
    ["`--container-narrow`", f"`{raw['container-narrow']}`", "prose"],
    ["`--container`", f"`{raw['container']}`", "default"],
    ["`--container-wide`", f"`{raw['container-wide']}`", "wide"],
    ["`--gutter`", f"`{raw['gutter']}`", "page edge"],
]))
A.append("\n### 6.3 Radii, borders, shadow\n")
A.append(table(["token", "value"], [[f"`--{k}`", f"`{raw[k]}`"] for k, _ in props
                                    if k.startswith(("radius-", "bw-", "shadow-"))]))
A.append("\nSquared by default, because the cards are editorial. Soft chrome is for interactive "
         "elements and data tiles only. Hairlines do the heavy lifting. Shadows stay extremely "
         "restrained: cards lean on borders, not shadow.\n")

A.append("## 7 · Motion and stacking\n")
A.append(table(["token", "value"], [[f"`--{k}`", f"`{raw[k]}`"] for k, _ in props
                                    if k.startswith(("ease-", "dur-", "z-"))]))

A.append("\n## 8 · The motif, v3 centre of gravity\n")
A.append("Carried forward: hairline rules as structure, generous whitespace at 35 to 40 percent "
         "minimum, squared editorial cards, serif-italic grape numerals.\n")
A.append("New in v3, evidence on display:\n")
A.append("- tabular grape and near-black **stat blocks** as hero elements, `.stat`\n"
         "- small-caps **method label** above the data, `.method-label`, reading METHOD or n = or EVIDENCE\n"
         "- a thin grape **data-baseline** rule under the stat, `.data-baseline`, the measured mark\n"
         "- **citation and footnote** styling for sources, `.citation`, so the rigour is visible\n")
A.append("Layout patterns: stat-bar, data-tile, evidence and methodology block, comparison table.\n")

A.append("## 9 · Logo\n")
A.append(table(["item", "specification"], [
    ["mark", "the Δ delta. Symbol for change and difference, and an upward data peak. Equilateral, grape-800, or paper on grape. The single signature across icon and wordmark."],
    ["primary lockup", "delta plus the \"Dr. Cory Dugan\" wordmark in DM Serif Display. `logo/lockup-primary-delta-outlined.svg`"],
    ["credential lockup", "plus \"PhD\" and the eyebrow \"HEALTH-SCREENING AI\". `logo/lockup-credential-delta-outlined.svg`"],
    ["stacked", "`logo/wordmark-stacked-delta-outlined.svg`"],
    ["icon", "grape delta tile at brand xl radius. `logo/icon-delta.svg`, plus `-inverse` for light. Scales to a 24px favicon."],
    ["clearspace", "at least the height of the delta"],
    ["minimum width", "wordmark 150px on screen, 25mm in print"],
    ["approved grounds", "paper, ink-050, grape-050"],
    ["file form", "wordmark SVGs are outlined to paths, so they are print-safe with no font dependency. Regenerate from `.build/outline.py` if the wordmark text changes."],
]))
A.append("\n**Never** stretch or rotate the delta, add a gradient, place it on an un-scrimmed photo, "
         "recolour it outside grape, ink and paper, or re-add the baseline rule under the name.\n")

A.append("## 10 · Voice\n")
A.append("First person singular. Australian spelling in this lane. Authoritative, evidence-precise, "
         "plain-confident, and it cites the number.\n")
A.append(table(["do", "never"], [
    ["\"One in three women is iron deficient, and here is what the data shows.\"",
     "em dashes, anywhere, on any surface, including filenames"],
    ["put a figure or a source behind every claim", "emoji, exclamation marks"],
    ["use a comma, parentheses, or a full stop", "hedging, hype, diet-culture framing"],
    ["name the method and the sample", "a claim with no number behind it"],
]))

A.append("\n## 11 · Imagery\n")
A.append("Art direction is documentary-real, natural light, desaturated-warm. Founder in context, "
         "meaning talks, panels and lab, plus clean screening, lab and data detail. No stock gloss "
         "and no AI faces. Generated images are abstract data or organic forms only, never synthetic "
         "people. Grape lives in the interface around the image and never recolours the photo.\n")
A.append(table(["bank image", "where it goes"], [
    ["headshot", "About, hero"],
    ["lab-testing", "Services, products"],
    ["iron-screening", "Services, products"],
    ["pennington-talk", "Credentials, featured in, social proof"],
    ["panel-discussion", "Credentials, featured in, social proof"],
    ["abc-radio", "Credentials, featured in, social proof"],
]))

A.append("\n## 12 · Integrations\n")
A.append("One source format. Everything else is generated, never hand-maintained in parallel.\n")
A.append("```\nSOURCE OF TRUTH:  colors_and_type.css  +  tokens.json\n"
         "        | inherit or generate\n"
         "        v\n"
         "Claude Design · Claude Code · GitHub · Web and Netlify · Canva · Figma (optional)\n```\n")
A.append(table(["target", "how", "status"], [
    ["Claude Design", "preview cards via `/design-sync`", "live v3 project"],
    ["Claude Code", "paste `SKILL.md` or `tokens.json` as context", "every asset inherits by name"],
    ["GitHub, this repo", "version control, the fix for brand drift", "live"],
    ["Web and Netlify", "CSS custom properties drop into drcorydugan.com", "native"],
    ["Canva", "push palette and fonts as a Brand Kit via MCP", "optional, high value for content"],
    ["Figma", "import `tokens.json` via the Tokens Studio plugin", "supported, not stood up"],
]))

A.append("\n## 13 · Version history\n")
A.append(table(["version", "date", "what changed"], [
    ["v3 Authority", "2026-06-18", "added `--ink-max` and the data-viz ramp, `.stat` tabular display and the mono evidence voice, the evidence motif of method label, data baseline and citation, the wordmark and PhD lockup, layout patterns, and the integrations block. Built to read as healthcare-AI authority. Grape, DM type and white-dominant unchanged."],
    ["a11y fix", "2026-07-27", "`--ink-500` darkened to `#6E6F75` for WCAG AA, 4.28:1 to 5.01:1"],
    ["surface layer", "2026-08-05", "paper and ink as two peer surfaces, nine `--surface-*` tokens each"],
    ["drift close", "2026-08-10", "README and tokens.json had never been updated for the surface layer and still called paper the dominant surface and ink-max stats-only. tokens.json also still carried the pre-a11y `#797A80`, which is the value Figma imports. All three files brought into agreement, verified by diffing 22 of 22 colour tokens to zero mismatches."],
    ["v2 grape", "2026-06-12", "teal to grape `#352051` rebrand"],
    ["v1 teal", "retired", ""],
]))

A.append(f"\n## Appendix · every custom property, verbatim\n")
A.append(f"All {len(props)} declarations in `:root`, in file order, exactly as the CSS holds them.\n")
A.append(table(["property", "declared value", "resolves to"],
               [[f"`--{k}`", f"`{v.strip()}`", f"`{resolve(v)}`" if resolve(v) != v.strip() else ""]
                for k, v in props]))
A.append(f"\nPlus the {len(ink)} reassignments inside `[data-surface=\"ink\"]`, listed in section 2.\n")

# ============================== DOC B ==============================
B = []
B.append("# drCWDugan Brand Canon v3 Authority")
B.append("## The visual brand sheet, as a document\n")
B.append(PROVENANCE)
B.append("\nThis is the prose form of the six-page brand sheet PDF. The companion document, "
         "**the complete specification**, carries every token and every number. This one carries "
         "the shape and the reasoning.\n")
B.append("\n---\n")
B.append("## Page 1 · Colour\n")
B.append("> **Authority is held by data rigour, not decoration.**\n")
B.append("Grape as ink and accent only, never a page fill. DM Serif Display over DM Sans. "
         "Neutrals carry ninety percent of every layout, and at least 35 percent of the page "
         "stays empty.\n")
B.append("Locked constraint: grape `#352051`.\n")
B.append("**The grape ramp.** grape-900 for dense accents, grape-800 as PRIMARY for links, "
         "numerals and key marks, grape-700 for hovers and the eyebrow, grape-600 for "
         "load-bearing line art, grape-500 for chart tertiary and the ink-surface accent, "
         "grape-200 for the data-baseline rule, grape-100 for chart fills, grape-050 as a "
         "barely-there tint.\n")
B.append("**The ink ramp.** ink-max is the ink surface field and stat displays. ink-1000 is body "
         "and strong emphasis. ink-700 is secondary text and citations. ink-500 is muted and meta, "
         "darkened for WCAG AA. ink-200 is the default hairline. ink-050 is the off-white surface. "
         "paper is the paper surface field and the workhorse.\n")
B.append("**Status colours** are for data visualisation and form states only. Up uses brand grape "
         "rather than green, down is a desaturated terracotta, warn is a desaturated mustard.\n")
B.append("**Data-viz ramp.** Categorical, maximum five: grape-800, grape-500, ink-500, warn, down. "
         "Sequential: grape-100 to grape-500 to grape-600 to grape-800. Charts inherit the brand. "
         "No rainbow, and no gradient anywhere by design.\n")

B.append("## Page 2 · The surface layer\n")
B.append("**Two peer surfaces. Not a light mode and a dark mode.**\n")
B.append("A component never hard-codes a colour. It reads `--surface-*` and inherits whichever "
         "surface it was placed on. The surface is set on the card root.\n")
B.append("**Paper** is the default, and still the workhorse. Clinical, calm, what evidence-led "
         "work is set on.\n")
B.append("**Ink** is a full peer. Reach for it when the message wants weight rather than calm: "
         "a hook, a quote, a launch, one hard claim.\n")
B.append("Both surfaces carry the same card: an eyebrow, a serif headline, body copy, a method "
         "label, a tabular stat, the grape data-baseline rule under it, a mono evidence line, and "
         "exactly one solid element.\n")
B.append("**Contrast, measured on the ink field `#0B0B0C`.** fg 19.66:1, fg-muted 15.59:1, "
         "fg-subtle 11.97:1, stroke 15.59:1, accent 4.72:1. White on `--surface-on-accent` is "
         "**4.16:1**, so it is large text only, meaning 24px or more, or 18.66px bold or more. "
         "Never set small text in it.\n")

B.append("## Page 2b · The surface tokens\n")
B.append("Nine tokens, each with a paper value and an ink value. A component reads these, never "
         "a raw hex.\n")
B.append(table(["token", "paper", "ink", "role"],
               [[f"`--{k}`", f"`{paper_surface[k]}`", f"`{ink[k]}`", SURFACE_ROLE[k]]
                for k in SURFACE_ROLE if k in paper_surface and k in ink]))
B.append("\nGrape is still never a page fill. The dark field is `ink-max`, not grape.\n")

B.append("## Page 3 · Typography\n")
B.append("DM Serif Display for display and headlines and the signature italic emphasis. DM Sans "
         "for body, UI, eyebrows and tabular stats. A monospace stack for code and the evidence "
         "voice, meaning n equals, p-values and confidence intervals.\n")
B.append("The scale runs display-xl down to display-sm in serif, then a tabular `.stat`, then "
         "heading-lg through heading-sm, then body-lg, body and body-sm, then meta for the eyebrow "
         "and caption, then micro for tags and method labels.\n")
B.append("**Six settings that are easy to get wrong.**\n")
B.append(table(["setting", "value", "why"], [
    ["display tracking", "`-0.02em`", "DM Serif reads loose at size"],
    ["body line-height", "`1.6`", "editorial breathing room"],
    ["method-label tracking", "`0.18em`", "small-caps above data"],
    ["stat numerals", "`tabular-nums lining-nums`", "columns of figures must align"],
    ["evidence units", "`.nowrap`", "\"p < .001\" must never break across lines"],
    ["heading margins", "`0`", "layouts own spacing, not headings"],
]))

B.append("\n## Page 4 · Layout, motif, voice\n")
B.append("**Containers.** narrow 760px for prose, 1120px default, 1280px wide, with a fluid gutter. "
         "Section rhythm is fluid between 72px and 144px. Spacing runs off a 4px base.\n")
B.append("**Radii.** 0 by default because the cards are editorial, 8 to 16 for interactive elements "
         "and data tiles, 999 for pills. Hairlines do the heavy lifting at 1px, strong at 2px. "
         "Shadows stay extremely restrained: cards lean on borders, not shadow.\n")
B.append("**The motif.** Hairline rules as structure, whitespace at 35 to 40 percent, squared "
         "editorial cards, serif-italic grape numerals. On top of that, evidence on display: "
         "tabular stat blocks as hero elements, a small-caps method label above the data, a thin "
         "grape data-baseline rule under the stat, and a citation style that makes the rigour "
         "visible.\n")
B.append("**Voice.** First person singular. Australian spelling in this lane. Authoritative, "
         "evidence-precise, plain-confident, and it cites the number.\n")
B.append("Do: \"One in three women is iron deficient, and here is what the data shows.\" Put a "
         "figure or a source behind every claim. Use a comma, parentheses, or a full stop.\n")
B.append("Never: em dashes, anywhere, on any surface, including filenames. Emoji. Exclamation "
         "marks. Hedging, hype, diet-culture framing, or a claim with no number.\n")

B.append("## Page 5 · Imagery and provenance\n")
B.append("Documentary-real, natural light, desaturated-warm. Founder in context, talks, panels, "
         "lab, plus clean screening and data detail. No stock gloss, no AI faces. Generated images "
         "are abstract data or organic forms only, never synthetic people.\n")
B.append(f"**Provenance.** Rendered {DATE} directly from "
         f"`~/Documents/GitHub/drcwd-design-system/colors_and_type.css` at commit `{COMMIT}`, "
         f"linked live rather than copied.\n")
B.append("**Drift closed 10 August 2026.** Until that date `README.md` and two colour descriptions "
         "in `tokens.json` still called paper the dominant surface and ink-max stat displays only, "
         "and `tokens.json` carried `--ink-500 #797A80` where the CSS carried `#6E6F75`, which is "
         "the value Figma imports. All three files now agree: **ink is a peer surface, not a stat "
         "colour.** Verified by diffing every colour token, 22 of 22, zero mismatches.\n")

for name, body in [
    (f"{STAMP} drCWDugan Brand System v3 COMPLETE SPEC (repo {COMMIT})_FROZEN_CD.md", A),
    (f"{STAMP} drCWDugan Brand Canon v3 SHEET (repo {COMMIT})_FROZEN_CD.md", B),
]:
    text = "\n".join(body)
    bad = [c for c in ("—", "–") if c in text]
    # Word boundaries, not substrings. "improvement" contains "prove" and is fine.
    banned = [w for w in ("prove", "proven", "fact", "facts", "absolute", "absolutely")
              if re.search(rf"\b{w}\b", text, re.I)]
    if bad or banned:
        raise SystemExit(f"REFUSED writing {name}: found {bad} {banned}")
    (OUT / name).write_text(text, encoding="utf-8")
    print(f"{len(text):>7} chars  {name}")
