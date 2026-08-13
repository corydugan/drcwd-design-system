# Dr. Cory Dugan: Brand Design System · v3 "Authority"

**Single source of truth** for every drCWDugan asset: logos, websites, prototypes, decks, social, screening-tool UIs. Faithful to the existing grape brand, elevated to read as a serious **healthcare-AI consultant + founder** (not a wellness coach).

> **Edit only `colors_and_type.css` and `tokens.json`.** Everything else (Claude Design, the website, Canva, Figma) inherits *from here*. This file is the contract.

**Locked constraints:** grape `#352051` · Instrument Serif + DM Sans + IBM Plex Sans figures · white-dominant editorial.
**Supersedes:** v2 grape (2026-06-12) and the retired v1 teal system.

---

## 0 · Non-negotiables

The short card. These are the rules a tool needs before it builds anything, and
they live here rather than in a second file so there is only one copy of them.
`scripts/build_brand_card.py` extracts everything between the CARD markers into
`PASTE-INTO-TOOLS.md` and injects the live token values beneath it.

<!-- CARD:START -->
## The rules

1. **Grape is accent and ink only, never a page fill.** Neutrals carry 90%+ of
   every layout.
2. **Two peer surfaces, not a dark mode.** `paper` is the default workhorse.
   `ink` is a full peer, used when the message wants weight rather than clinical
   calm. Set it on the card root, never per component. Grape is still never the
   field: the dark field is `--ink-max`.
3. **A component never hard-codes a colour and never reads a raw palette token.**
   It reads `--surface-*`. Reading `var(--grape-200)` directly is the bug that
   makes an asset unportable between surfaces.
4. **Reference tokens by name**, never a raw hex inline. This includes render
   scaffolding outside the artboard.
5. **The lockup reads `--surface-logo`, never `--surface-fg`.** `--surface-fg`
   is text.
6. **Field-dominant: 35 to 40% clear field minimum**, measured as layout
   negative space (content-block occupancy on a coarse grid), NOT as a count of
   background-coloured pixels. A pixel count scores the inside of every letter
   as whitespace and can never fail.
7. **Minimum readable size.** A 1080px canvas renders near 400 CSS px in a phone
   feed. Anything intended to be READ, including every confidence interval and
   every citation, sits at 32px minimum on a 1080px canvas. Below that it is
   decoration: cut it rather than shrink it.
8. **No gradient. No emoji. No exclamation marks.**

## Voice

First-person singular, Australian English, plain-confident, always cites the
number.

- **No em dashes and no en dashes as prose punctuation.** Use a comma,
  parentheses, or a full stop. Universal rule.
- **Banned words, no exceptions: prove, proven, fact, absolute.** This binds
  rendered card text, not only captions. Machine-check it.
- **Never state a prevalence without its threshold.** The same cohort gives 17%,
  39% or 78% for iron deficiency depending only on where the ferritin cut-off
  sits. Name the cut-off or do not name the number.
- **Name the population the source names.** If the paper says "females aged 12
  to 21", the asset does not say "women".
- **Write micrograms per litre as `ug/L`, never the micro sign.**
  `text-transform: uppercase` maps the micro sign to a capital Greek mu, so it
  renders as a 1000-fold unit error that is invisible in the source.

Worked example of the voice:

> "In 3,490 US females aged 12 to 21, 38.6% were iron deficient at a ferritin
> below 25 ug/L. At below 50, the same blood gives 77.5%."

## Show it, do not only say it

Where a claim is about data, a process, a relationship, a sequence or a
threshold, SHOW it as a minimal visualisation rather than describing it.

```
a hidden layer under a surface .... iceberg · layers
a status range, low to optimal .... reference-range bar · spectrum
this vs that ...................... versus split · before and after
branching options ................. decision tree · two-path fork
a mechanism or causal chain ....... cascade · chain · flow
how big the gap is ................ funnel · waffle · icon array
a sequence with real order ........ timeline · step flow · pipeline
a single striking number .......... big-number hero + annotation
```

Line art only: strokes read `--surface-stroke`, labels read
`--surface-fg-muted`. ONE element filled with `--surface-fill`, and that
element is the insight; everything else is a hairline. Labels, not sentences.
Every diagram carries a `.method-label` above and a `.citation` below naming
the population. Numbers use `--font-figures`. Use a shape only where the shape
carries information: a numbered list that is not a sequence is decoration.

## The authority signature

Lead with data on display: a big tabular `.stat`, a small-caps `.method-label`
above it, a thin `.data-baseline` rule beneath, mono `.evidence` for the
supporting figure, and `.citation` for the source.

Charts: the fill reads `--surface-accent`, the track reads `--surface-track`.
Use ONE fill colour when bar length and a printed number already carry the
value. Never let the same value take different sequential-ramp steps on two
slides of one carousel.
<!-- CARD:END -->


---

## 1 · Color tokens
Brand grape is **accent + ink only, never a page fill.** Neutrals carry 90%+ of every layout.

| Token | Hex | Use |
|---|---|---|
| `--grape-800` | `#352051` | **PRIMARY**: links, numerals, key marks |
| `--grape-700` | `#4a2f70` | hovers, mid-strength fills |
| `--grape-600` `--grape-500` | `#6b4f9e` `#8a6fb8` | illustration, chart secondary/tertiary |
| `--grape-200`→`050` | `#d8cfe7`→`#f6f4fa` | data baseline, chart fills, soft tints |
| `--ink-max` | `#0B0B0C` | **v3** near-black. The **ink surface** field (§1b), and stat displays on paper. Not stats only. |
| `--ink-1000`/`700`/`500` | `#1C1C1E`/`#4A4A4F`/`#6E6F75` | body / secondary / muted (ink-500 darkened 2026-07-27 for WCAG AA: 4.28:1 → 5.01:1) |
| `--ink-200` `--ink-100` `--ink-050` | `#E4E5E7` `#EFEFEF` `#F7F7F6` | hairlines / dividers / off-white |
| `--paper` | `#FFFFFF` | the **paper surface** field (§1b). Default and workhorse, and a peer of ink. |
| `--status-up/down/warn` | `#4a2f70` `#B5524A` `#B58A3A` | data-viz + form states only |

**Data-viz ramp (v3):** categorical = grape-800 · grape-500 · ink-500 · warn · down. Sequential = grape-100 → grape-500 → grape-600 → grape-800. Charts inherit the brand; no rainbow.
**Gradient:** none, by design.

## 1b · Surfaces (added 2026-08-05)
**Two peer surfaces. Not a light mode and a dark mode.** Documented here 2026-08-10; the layer had lived only in `colors_and_type.css` and `tokens.json`, and this file still called paper "the dominant surface".

- **paper** `#FFFFFF`, the default and still the workhorse. Clinical, calm, what evidence-led work is set on.
- **ink** `#0B0B0C`, a full peer. Reach for it when the message wants weight rather than calm: a hook, a quote, a launch, one hard claim.

A component never hard-codes a colour. It reads `--surface-*` and inherits whatever surface it sits on. Set the surface on the card root: `<div class="slide">` is paper, `<div class="slide" data-surface="ink">` is ink.

| token | paper | ink | role |
|---|---|---|---|
| `--surface` | `--paper` | `--ink-max` | the field |
| `--surface-fg` | `--ink-1000` | `--paper` | headline, primary text |
| `--surface-fg-muted` | `--ink-700` | `--ink-200` | labels, body, citations |
| `--surface-fg-subtle` | `--ink-500` | `--ink-300` | micro-caps, meta |
| `--surface-rule` | `--ink-200` | `--ink-900` | hairline dividers |
| `--surface-eyebrow` | `--grape-700` | `--grape-500` | tracked micro-caps kicker |
| `--surface-stroke` | `--grape-600` | `--ink-200` | load-bearing line art |
| `--surface-accent` | `--grape-800` | `--grape-500` | the ONE solid element |
| `--surface-on-accent` | `--paper` | `--paper` | text reversed out of accent |
| `--surface-logo` | `--grape-800` | `--paper` | delta + wordmark lockup (§3) |
| `--surface-track` | `--ink-100` | `--ink-900` | bar-chart 0-100 track |
| `--surface-baseline` | `--grape-200` | `--grape-500` | chart baseline / axis rule |

Grape is still never a page fill. The dark field is `ink-max`, not grape.
**Contrast on ink `#0B0B0C`, measured (rounded, not truncated):** fg 19.67:1 · fg-muted 15.61:1 · fg-subtle 11.99:1 · stroke 15.61:1 · accent 4.73:1. White on `--surface-on-accent` is **4.16:1**, so it is LARGE TEXT ONLY (≥24px, or ≥18.66px bold). Never set small text in it.

**Measure a chart fill against its neighbour, not against the field.** A bar sitting in a `--surface-track` is judged against the track. On paper the three sequential fills read 3.62:1 / 5.64:1 / 12.37:1 against `--ink-100`, not the 4.16 / 6.49 / 14.22 they score against paper. All clear the 3:1 non-text floor; the margin on the lightest is thinner than it looks.

## 2 · Typography
- **Serif** **Instrument Serif**, display/headlines + signature italic emphasis. Changed 2026-08-12: DM Serif Display carries 491 kern pairs against Instrument Serif's 3,805, has one weight and no optical-size axis, and sits on the Google Fonts default carousel, which is the single strongest signal that a card was built from a template.
- **Sans** DM Sans, body, UI, eyebrows. **NOT stats.**
- **Figures** **IBM Plex Sans** (`--font-figures`) for every stat, CI, `n =` and evidence string. DM Sans has **no `tnum` table**: `font-variant-numeric: tabular-nums` on it is a silent no-op, and its digit `1` renders at 0.517 the width of its `0`, so every figure containing a 1 has a visible hole. Measured in the render path 2026-08-12, not read off a spec sheet. IBM Plex Sans is monospaced in the figures by default and needs no feature flag.
- **Mono** the **evidence voice** (n=, p-values, CIs). Two tokens, and the split matters: `--font-mono` is `ui-monospace` for the **web**, `--font-mono-asset` is pinned **IBM Plex Mono** for anything **rendered to a file**. A system stack makes an exported PNG render differently per machine, which is drift by construction. Ratified 2026-08-12; before that the mono was a fourth typeface smuggled in under a private alias.
- Scale: display-xl→sm (serif) · `.stat` tabular (v3) · heading-lg/md · body-lg/body/sm · meta (eyebrow) · micro (tags, method labels).
- Display tracking `-0.02em`; body line-height `1.6`.

## 3 · Logo usage
- **Mark:** the **Δ delta**, symbol for change/difference, and an upward data peak. Equilateral. The single signature across icon + wordmark.
- **Lockup colour is a token, never a literal.** Components read `--surface-logo`; they must not read `--surface-fg`, which is text. Resolves to **grape-800** on paper / ink-050 / grape-050, and **paper** on grape and on ink-max.
- **Primary lockup:** delta + "Dr. Cory Dugan" wordmark in **DM Serif Display**, outlined to paths. **This is deliberate and settled, not drift.** Cory's call 2026-08-12: when Instrument Serif replaced DM Serif Display for display TYPE, the lockups were reviewed at four treatments and DM Serif Display was kept for the MARK. So the two are split on purpose: Instrument Serif sets every headline, the wordmark stays as it is. Do not "correct" the lockups to Instrument Serif, and do not regenerate them from `.build/outline.py` unless that call is reversed (`logo/lockup-primary-delta-outlined.svg`).
- **Credential lockup:** + "PhD" + eyebrow "HEALTH-SCREENING AI" (`logo/lockup-credential-delta-outlined.svg`). **Stacked:** `logo/wordmark-stacked-delta-outlined.svg`.
- **Icon:** grape delta tile, brand xl radius (`logo/icon-delta.svg` + `-inverse` for light). Scales to a 24px favicon.
- Clearspace ≥ the delta's height; min wordmark width 150px / 25mm. Approved grounds: paper, ink-050, grape-050, and **ink-max** (added 2026-08-12, closing the gap left when the surface layer landed in `759ec62` after this section was written).
- **Don't:** stretch/rotate the delta, add a gradient, place on an un-scrimmed photo, recolor outside grape/ink/paper, or re-add the baseline rule under the name.
- Wordmark SVGs are **outlined to paths** (print-safe, no font dependency). Regenerate from `.build/outline.py` if the wordmark text changes. The retired "cd" monogram + baseline-wordmark explorations live in `logo/options/`.

## 4 · Motif: the evidence signature (v3 center of gravity)
Kept: hairline rules as structure · generous whitespace (35–40% min) · squared editorial cards · serif-italic grape numerals.
**New, evidence on display:**
- tabular grape/near-black **stat blocks** as hero elements (`.stat`)
- small-caps **method label** above data (`.method-label`, "METHOD" / "n =" / "EVIDENCE")
- thin grape **data-baseline** rule under stats (`.data-baseline`)
- **citation/footnote** style for sources (`.citation`), visible rigor.

## Show it, do not only say it

**Added 2026-08-13, Cory's call.** Where a claim is about data, a process, a
relationship, a sequence or a threshold, the asset SHOWS it as a minimal
visualisation rather than describing it in a sentence. A number without its
shape is an assertion; the shape is the argument.

This is the same visual language as the concept diagrams, not a second one.
`BRAND/drCWD Concept-Diagram Visual Language_CD.md` holds the full 14-group
library and the message-to-shape matching guide. It applies on the web too,
drawn as inline SVG or CSS rather than rendered to PNG.

**The matching guide, short form:**

```
a hidden layer under a surface .... iceberg · layers · concentric rings
a status range, low to optimal .... reference-range bar · spectrum
this vs that, two choices ......... versus split · before and after
one idea into branching options ... decision tree · two-path fork
a mechanism or causal chain ....... cascade · chain · flow
how big the gap or loss is ........ funnel · waffle · icon array
a depleting resource .............. battery · hourglass
a sequence with real order ........ timeline · step flow · pipeline
a single striking number .......... big-number hero + annotation
prevalence storytelling ........... natural-frequency tree · waffle
```

**On brand, every time:**

1. **Line art, not chrome.** Strokes read `--surface-stroke`, labels read
   `--surface-fg-muted`. No gradients, no shadows, no 3D.
2. **ONE element filled with `--surface-fill`.** That element is the insight.
   Everything else is a hairline. If two things are filled, neither reads.
3. **The structure IS the content.** Labels, not sentences. If it needs a
   paragraph to make sense, it is the wrong shape.
4. **It carries its own evidence.** A `.method-label` above, a `.citation`
   below naming the population. A diagram without a source is decoration.
5. **Numbers use `--font-figures`.** Never the sans, which has no tnum table.
6. **Only where it earns its place.** A sequence gets a timeline only if the
   order carries information the reader needs. Numbered markers on a list that
   is not a sequence are decoration, and decoration is the thing this brand
   is against.

## 5 · Voice
First-person singular · **Australian English** · no emoji · no exclamation marks.
Traits: authoritative · evidence-precise · plain-confident · **cites the number**.
- **Do:** "In 3,490 US females aged 12 to 21, 38.6% were iron deficient at a ferritin below 25 ug/L. At below 50, the same blood gives 77.5%." (⛔ **NO EM DASHES, ever.** Use commas, parentheses, or a full stop. This is a universal rule across every surface: brand copy, outreach, manuscripts, chat, filenames. This line previously read "em dashes welcome" and was the source of repeated leaks into outreach copy. Corrected 2026-07-27 to match `~/.claude/CLAUDE.md`.)
- **Don't:** hedge, hype, diet-culture, or claim without a figure/source behind it.
- ⛔ **Banned words, no exceptions: prove, proven, fact, absolute.** This binds RENDERED CARD TEXT, not only captions. Added 2026-08-12 after a banned word shipped in the largest type on a carousel slide: the voice check that ran on that pack enumerated em dashes, emoji, exclamation marks and claim-without-a-number, and silently omitted this list. Machine-check it, and check the HTML, not just the caption.
- **Never state a prevalence without its threshold.** The same cohort gives 17%, 39% or 78% for iron deficiency depending only on where the ferritin cut-off sits. Name the cut-off or do not name the number.
- ⛔ **Write micrograms per litre as `ug/L`, never `µg/L`.** Cory's call, 2026-08-12. `text-transform: uppercase` maps the micro sign to a capital Greek mu, so it renders as `MG/L`, a 1000-fold unit error that is invisible in the source. It shipped twice in one day, once in a hand-built card and once out of Claude Design. `u` is immune and costs nothing.
- **Name the population the source names.** If the paper says "females aged 12 to 21, median age 16", the asset does not say "women". Check the median age before reaching for a population noun.

## 6 · Layout rules
- Containers: narrow 760 (prose) · default 1120 · wide 1280 · gutter `clamp(20px,4vw,48px)`.
- Spacing: 4px base scale (`--space-1`…`40`). Radius: 0 default (editorial), 8/12/16 interactive + data tiles, 999 pills.
- Borders: 1px hairline / 2px strong. Shadows: extremely restrained, cards lean on borders.
- Patterns (v3): stat-bar · data-tile · evidence/methodology block · comparison table.
- **How to measure the 35 to 40% minimum.** It is layout negative space: content-block occupancy on a coarse grid (32px or 64px cells on a 1080px canvas). It is NOT a count of pixels equal to the background colour. That count scores the inside of every letter as whitespace and cannot fail: a slide carrying a large solid grape block still scored 87.3% on it. Added 2026-08-12 after a pack shipped with the pixel-count method reported as if it were the rule.
- **On ink the field is dark**, so state the rule as "field share on ink, whitespace on paper". The metric is the same; the field colour is not.
- **Minimum readable size.** A 1080px canvas renders at roughly 400 CSS px in a phone feed, a factor of 0.37. Anything intended to be READ, including **every confidence interval and every citation**, sits at **32px minimum on a 1080px canvas** (12px effective). Below that it is decoration. Cut it rather than shrink it.
- **Charts:** the fill reads `--surface-accent`, the track reads `--surface-track`. Use ONE fill colour when bar length and a printed number already carry the value. Never let the same value take different sequential-ramp steps on two slides of one carousel; that reintroduces the distortion a shared axis removes.

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
| **GitHub** (this repo) | version control, the fix for brand drift | ✅ |
| **Web / Netlify** | CSS custom properties drop into drcorydugan.com | native |
| **Canva** | push palette + fonts as a Brand Kit (MCP) | optional, high-value for content |
| **Figma** | import `tokens.json` via Tokens Studio plugin | supported if a collaborator needs it; not stood up |

---

### History
- **v3 Authority** (2026-06-18): added `--ink-max` + data-viz ramp, `.stat` tabular display + mono evidence voice, evidence motif (method label / data baseline / citation), wordmark + PhD lockup, layout patterns, integrations block. Built to read as healthcare-AI authority. Grape + DM type + white-dominant unchanged.
- **v2 grape** (2026-06-12): teal → grape `#352051` rebrand.
- **v1 teal**: retired.
