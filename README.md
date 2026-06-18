# Dr. Cory Dugan — Brand Design System · v3 "Authority"

**Single source of truth** for every drCWDugan asset: logos, websites, prototypes, decks, social, screening-tool UIs. Faithful to the existing grape brand, elevated to read as a serious **healthcare-AI consultant + founder** (not a wellness coach).

> **Edit only `colors_and_type.css` and `tokens.json`.** Everything else (Claude Design, the website, Canva, Figma) inherits *from here*. This file is the contract.

**Locked constraints:** grape `#352051` · DM Serif Display + DM Sans · white-dominant editorial.
**Supersedes:** v2 grape (2026-06-12) and the retired v1 teal system.

---

## 1 · Color tokens
Brand grape is **accent + ink only — never a page fill.** Neutrals carry 90%+ of every layout.

| Token | Hex | Use |
|---|---|---|
| `--grape-800` | `#352051` | **PRIMARY** — links, numerals, key marks |
| `--grape-700` | `#4a2f70` | hovers, mid-strength fills |
| `--grape-600` `--grape-500` | `#6b4f9e` `#8a6fb8` | illustration, chart secondary/tertiary |
| `--grape-200`→`050` | `#d8cfe7`→`#f6f4fa` | data baseline, chart fills, soft tints |
| `--ink-max` | `#0B0B0C` | **v3** near-black — stat displays only |
| `--ink-1000`/`700`/`500` | `#1C1C1E`/`#4A4A4F`/`#797A80` | body / secondary / muted |
| `--ink-200` `--ink-100` `--ink-050` | `#E4E5E7` `#EFEFEF` `#F7F7F6` | hairlines / dividers / off-white |
| `--paper` | `#FFFFFF` | canvas (dominant surface) |
| `--status-up/down/warn` | `#4a2f70` `#B5524A` `#B58A3A` | data-viz + form states only |

**Data-viz ramp (v3):** categorical = grape-800 · grape-500 · ink-500 · warn · down. Sequential = grape-100 → grape-500 → grape-600 → grape-800. Charts inherit the brand; no rainbow.
**Gradient:** none, by design.

## 2 · Typography
- **Serif** DM Serif Display — display/headlines + signature italic emphasis.
- **Sans** DM Sans — body, UI, eyebrows, and **tabular stats**.
- **Mono** ui-monospace — code + the **evidence voice** (n=, p-values, CIs).
- Scale: display-xl→sm (serif) · `.stat` tabular (v3) · heading-lg/md · body-lg/body/sm · meta (eyebrow) · micro (tags, method labels).
- Display tracking `-0.02em`; body line-height `1.6`.

## 3 · Logo usage
- **Wordmark:** "Dr. Cory Dugan" in DM Serif Display, grape-800 / ink-1000.
- **Credential lockup:** "Dr. Cory Dugan, PhD" + optional eyebrow "HEALTH-SCREENING AI".
- Clearspace ≥ cap-height of the "D"; min 150px / 25mm. Approved on paper, ink-050, grape-050.
- **Don't:** place on grape fills, un-scrimmed photos, or recolor outside grape-800 / ink-1000 / paper.
- *(No mark file ships yet — this is the spec to hold to.)*

## 4 · Motif — the evidence signature (v3 center of gravity)
Kept: hairline rules as structure · generous whitespace (35–40% min) · squared editorial cards · serif-italic grape numerals.
**New — evidence on display:**
- tabular grape/near-black **stat blocks** as hero elements (`.stat`)
- small-caps **method label** above data (`.method-label` — "METHOD" / "n =" / "EVIDENCE")
- thin grape **data-baseline** rule under stats (`.data-baseline`)
- **citation/footnote** style for sources (`.citation`) — visible rigor.

## 5 · Voice
First-person singular · **Australian English** · no emoji · no exclamation marks.
Traits: authoritative · evidence-precise · plain-confident · **cites the number**.
- **Do:** "One in three women is iron deficient — here's what the data shows." (em dashes welcome)
- **Don't:** hedge, hype, diet-culture, or claim without a figure/source behind it.

## 6 · Layout rules
- Containers: narrow 760 (prose) · default 1120 · wide 1280 · gutter `clamp(20px,4vw,48px)`.
- Spacing: 4px base scale (`--space-1`…`40`). Radius: 0 default (editorial), 8/12/16 interactive + data tiles, 999 pills.
- Borders: 1px hairline / 2px strong. Shadows: extremely restrained — cards lean on borders.
- Patterns (v3): stat-bar · data-tile · evidence/methodology block · comparison table.

## 7 · Imagery
- **Art direction:** documentary-real, natural light, desaturated-warm. Founder-in-context (talks/panels/lab) + clean screening/lab/data detail. No stock-gloss, no AI faces.
- **Generated images:** abstract data/organic forms only (no synthetic people). Grape lives in the UI *around* the image, never recolors the photo.
- **Approved bank:** headshot · lab-testing · iron-screening · pennington-talk · panel-discussion · abc-radio.
- **Which where:** headshot → About/Hero · lab/iron-screening → Services/products · talk/panel/radio → Credentials / Featured-in / social proof.

## 8 · Integrations & portability
One source format; everything else is **generated**, never hand-maintained in parallel.

```
SOURCE OF TRUTH:  colors_and_type.css  +  tokens.json
        │ inherit / generate ↓
 Claude Design · Claude Code · GitHub (this repo) · Web/Netlify · Canva · Figma(optional)
```

| Target | How | Status |
|---|---|---|
| **Claude Design** (claude.ai/design) | preview cards via `/design-sync` | live v3 project |
| **Claude Code** | paste `SKILL.md` / `tokens.json` as context | every asset inherits by name |
| **GitHub** (this repo) | version control — the fix for brand drift | ✅ |
| **Web / Netlify** | CSS custom properties drop into drcorydugan.com | native |
| **Canva** | push palette + fonts as a Brand Kit (MCP) | optional, high-value for content |
| **Figma** | import `tokens.json` via Tokens Studio plugin | supported if a collaborator needs it; not stood up |

---

### History
- **v3 Authority** (2026-06-18): added `--ink-max` + data-viz ramp, `.stat` tabular display + mono evidence voice, evidence motif (method label / data baseline / citation), wordmark + PhD lockup, layout patterns, integrations block. Built to read as healthcare-AI authority. Grape + DM type + white-dominant unchanged.
- **v2 grape** (2026-06-12): teal → grape `#352051` rebrand.
- **v1 teal**: retired.
