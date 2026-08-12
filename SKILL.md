# SKILL: Generate drCWDugan assets on the v3 "Authority" brand

Paste this (with `colors_and_type.css` + `tokens.json`) into any tool to make
assets inherit the Dr. Cory Dugan brand exactly. This is the drCWDugan
**personal/business** brand, distinct from HolisticHer (HolisticHer = gradient
+ Montserrat; never mix them).

Synced to `README.md` 2026-08-12. If this file and `README.md` disagree,
`README.md` wins and this file is stale: fix it rather than following it.

## Non-negotiables

1. **Grape `#352051` is accent + ink only, never a page fill.**
2. **Two peer surfaces, not a dark mode.** `paper` is the default workhorse.
   `ink` (ink-max `#0B0B0C`) is a full peer, used when the message wants weight
   rather than clinical calm. Set it on the card root, never per component:
   `<div class="slide" data-surface="ink">`. Grape is still never the field.
3. **DM Serif Display** for display/headlines (+ italic emphasis); **DM Sans**
   for body/UI/stats; **mono** for evidence (n=, p, CIs).
4. **Field-dominant: 35 to 40% clear field minimum**, measured as layout
   negative space (content-block occupancy on a coarse grid), NOT as a count of
   background-coloured pixels. A pixel count scores the inside of every letter
   as whitespace and can never fail. On paper the field is white; on ink it is
   ink-max. Hairlines and whitespace do the structural work, not boxes, colour,
   or shadow.
5. **No gradient. No emoji. No exclamation marks.** (Gradient/emoji =
   HolisticHer or off-brand.)
6. Always reference tokens **by name** (`var(--surface-accent)`, `--space-8`),
   never raw hex inline. This includes render scaffolding outside the artboard.
7. **A component never hard-codes a colour and never reads a raw palette
   token.** It reads `--surface-*` and inherits whichever surface it sits on.
   Reading `var(--grape-200)` or `var(--ink-100)` directly is the bug that
   makes an asset unportable between surfaces.
8. **The lockup reads `--surface-logo`, never `--surface-fg`.** `--surface-fg`
   is text. Resolves to grape-800 on paper / ink-050 / grape-050, and paper on
   grape and ink-max.

## The authority signature (what makes v3 "improved")

Lead with **data on display**:
- Big tabular numerals via `.stat` (use `--surface-fg` or `.stat--grape`).
- A small-caps `.method-label` above the number ("METHOD" / "n =" / "EVIDENCE").
- A thin `.data-baseline` rule beneath it, reading `--surface-baseline`.
- Mono `.evidence` for the supporting figure; `.citation` for the source.
- Stats and citations make Cory read as a researcher-founder, not a coach.

**Minimum readable size.** Assets are consumed at roughly 0.37x on a phone
feed, so a 1080px canvas renders near 400 CSS px. Anything intended to be READ,
including every confidence interval and every citation, sits at **32px minimum
on a 1080px canvas**. Below that it is decoration. Cut it rather than shrink it.

## Voice

First-person singular, **Australian English**, plain-confident, **always cites
the number**.

- **No em dashes and no en dashes as prose punctuation.** Use a comma,
  parentheses, or a full stop. (Global rule, `~/.claude/rules/no-em-dashes.md`.)
- **Banned words, no exceptions: prove, proven, fact, absolute.** This applies
  to rendered card text, not only to captions. Machine-check it; the voice
  check that shipped 12 Aug 2026 omitted this list and a banned word reached
  the largest type on a card.
- **Never state a prevalence without its threshold.** "One in three women is
  iron deficient" is not a brand line, it is the error the brand argues
  against: the same cohort gives 17%, 39% or 78% depending only on where the
  ferritin cut-off is drawn. Name the cut-off or do not name the number.
- **Name the population the source names.** If the paper says "females aged 12
  to 21, median age 16", the card does not say "women".

> "In 3,490 US females aged 12 to 21, 38.6% were iron deficient at a ferritin
> below 25 ug/L. At below 50, the same blood gives 77.5%."

## Quick recipe

- Hero: serif `display-xl` headline with one italic emphasis word + `.stat`
  proof point.
- Sections: `--section-y` rhythm, eyebrow (`--surface-eyebrow`), serif heading,
  18px lead.
- Services: serif-italic grape numerals `01 / 02 / 03`.
- Data/decks: `data-tile` + `stat-bar` patterns, data-viz ramp for charts.
- **Charts:** bars read `--surface-track` for the 0-100 track and
  `--surface-accent` for the fill. Use ONE fill colour when bar length and a
  printed number already carry the value. Reserve the sequential ramp for a
  single chart read in isolation, and never let the same value take different
  ramp steps on two slides of one carousel.
- CTA: grape-800 fill (the rare place grape fills), paper text, pill radius.

## Section map for `README.md`

`README.md` is an **8-block** spec. There is no section 9. Cite it correctly:

| Need | Section |
|---|---|
| Colour tokens, the ramps (sequential vs categorical) | §1 |
| Surface layer (paper / ink) | §1b |
| Type scale | §2 |
| Logo usage, approved grounds, lockup colour | §3 |
| Motif, method-label, data-baseline | §4 |
| Voice | §5 |
| Layout rules, patterns | §6 |
| Components | §7 |
| Integrations and portability | §8 |

Source of truth = `colors_and_type.css` + `tokens.json`. Edit only those.
