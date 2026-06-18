# SKILL — Generate drCWDugan assets on the v3 "Authority" brand

Paste this (with `colors_and_type.css` + `tokens.json`) into any tool to make assets inherit the Dr. Cory Dugan brand exactly. This is the drCWDugan **personal/business** brand — distinct from HolisticHer (HolisticHer = gradient + Montserrat; never mix them).

## Non-negotiables
1. **Grape `#352051` is accent + ink only — never a page fill.** Backgrounds are white/off-white.
2. **DM Serif Display** for display/headlines (+ italic emphasis); **DM Sans** for body/UI/stats; **mono** for evidence (n=, p, CIs).
3. **White-dominant, 35–40% whitespace minimum.** Hairlines and whitespace do the structural work — not boxes, color, or shadow.
4. **No gradient. No emoji. No exclamation marks.** (Gradient/emoji = HolisticHer or off-brand.)
5. Always reference tokens **by name** (`var(--grape-800)`, `--space-8`), never raw hex inline.

## The authority signature (what makes v3 "improved")
Lead with **data on display**:
- Big tabular numerals via `.stat` (use `--ink-max` or `.stat--grape`).
- A small-caps `.method-label` above the number ("METHOD" / "n =" / "EVIDENCE").
- A thin `.data-baseline` grape rule beneath it.
- Mono `.evidence` for the supporting figure; `.citation` for the source.
- Stats and citations make Cory read as a researcher-founder, not a coach.

## Voice
First-person singular, **Australian English**, plain-confident, **always cites the number**. Em dashes welcome.
> "One in three women is iron deficient — here's what the data shows."

## Quick recipe
- Hero: serif `display-xl` headline with one italic emphasis word + `.stat` proof point.
- Sections: `--section-y` rhythm, eyebrow (`--color-accent`) → serif heading → 18px lead.
- Services: serif-italic grape numerals `01 / 02 / 03`.
- Data/decks: `data-tile` + `stat-bar` patterns, data-viz ramp for charts.
- CTA: grape-800 fill (the rare place grape fills), paper text, pill radius.

See `README.md` for the full 8-block spec. Source of truth = `colors_and_type.css` + `tokens.json` — edit only those.
