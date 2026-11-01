Faithful to the existing grape brand, elevated to read as a serious **healthcare-AI consultant and founder** (not a wellness coach). Editorial, ink-first on feed cards, grape accent only. Authority is held by data rigour, not decoration.

**Locked constraints:** grape `#352051` (`grape-800`) · DM Serif Display + DM Sans + IBM Plex Sans figures · ink-first on cards; paper on the website, documents and letters.

## The rules

1. **Grape is accent and ink only, never a page fill.** Neutrals carry 90%+ of every layout. A grape box is an outline with the field showing through, never a filled block.
2. **Two peer surfaces, not a dark mode.** `ink` is the default for feed cards; `paper` is a full peer. One carousel may mix them when it helps. Set the surface on the card root, never per component. Grape is still never the field: the dark field is `ink-max`.
3. **A component never hard-codes a colour and never reads a raw palette token.** It reads `surface-*`. Reading `grape-200` directly is the bug that makes an asset unportable between surfaces.
4. **Reference tokens by name**, never a raw hex inline. This includes render scaffolding outside the artboard.
5. **The lockup reads `surface-logo`, never `surface-fg`.** `surface-fg` is text.
6. **Field-dominant: 35 to 40% clear field minimum**, measured as layout negative space (content-block occupancy on a coarse grid), NOT as a count of background-coloured pixels. A pixel count scores the inside of every letter as whitespace and can never fail.
7. **Minimum readable size.** A 1080px card shows about 390 points wide in a phone feed. The smallest text on a card is the population line at 24px, about 8.7 points on a phone; the footer is 26px. Below 24px it is decoration: cut it rather than shrink it.
8. **No gradient. No emoji. No exclamation marks.**
9. **Nothing ships to the website unseen.** Any visual built for drcorydugan.com is rendered to a PNG and opened locally for Cory to approve BEFORE it lands in a page or a commit.
10. **The colour rule covers words and text visuals.** Icons from the library keep their own colours. Red appears only inside an icon, never in a chart. A video may use colour when its text and mark are on brand.
11. **When the colour is in doubt, ask Cory.**
12. **Context decides the drawing, and Cory decides by seeing it.** Drawing type, drawing size, animation, organs and people depend on the card. Show two to four options drawn on the real card, with the same title, numbers and caption, and let Cory pick. Never ask it as a text question.

## Content fundamentals

Voice, terminology, names, numbers and channel rules are governed by **Brand voice guidelines v2.1** (`CAREER/Business/BRAND/Brand voice guidelines_09292026_CD.md`). It is the single voice authority; where anything here disagrees with it, it wins. The rules a visual most often breaks:

First-person singular · **Australian English** · no emoji · no exclamation marks. Traits: authoritative · evidence-precise · plain-confident · **cites the number**. A stranger should read it in one second as clinical and calm, warm and on her side, scientific and precise.

- **No em dashes and no en dashes as prose punctuation.** Use a comma, parentheses, or a full stop. Ranges are "15 to 30".
- **The banned words** in the voice guidelines' Never-use table bind rendered card text, not only captions. Machine-check with `style_gate.py`, and check the HTML, not just the caption.
- **Channels** (hashtag counts, disclaimers, acronyms in captions, tone per platform) live in the voice guidelines, version 2.2 of 31 October 2026.
- **Never state a prevalence without its threshold.** The same cohort gives 17%, 39% or 78% for iron deficiency depending only on where the ferritin cut-off sits. Name the cut-off or do not name the number.
- **Name the population the source names.** If the paper says "females aged 12 to 21", the asset does not say "women".
- **Write micrograms per litre as `ug/L`, never the micro sign.** `text-transform: uppercase` maps the micro sign to a capital Greek mu, so it renders as a 1000-fold unit error that is invisible in the source.
- **Don't:** hedge, hype, diet-culture, or claim without a figure or source behind it.
- From the voice guidelines: "Numbers that report evidence are required. Numbers that pass judgement on a person are refused." "Dr" takes no full stop. Headings and titles name the thing, as a noun phrase.

Worked example of the voice:

> "In 3,490 US females aged 12 to 21, 38.6% were iron deficient at a ferritin below 25 ug/L. At below 50, the same blood gives 77.5%."

## Colour

Brand grape is **accent and ink only, never a page fill.** Neutrals carry 90%+ of every layout.

| Token | Hex | Use |
|---|---|---|
| `grape-800` | `#352051` | **PRIMARY**: links, numerals, key marks |
| `grape-700` | `#4a2f70` | hovers, mid-strength fills |
| `grape-600` `grape-500` | `#6b4f9e` `#8a6fb8` | illustration, chart secondary and tertiary |
| `grape-200` to `grape-050` | `#d8cfe7` to `#f6f4fa` | data baseline, chart fills, soft tints |
| `ink-max` | `#0B0B0C` | near-black. The **ink surface** field, and stat displays on paper. Not stats only. |
| `ink-1000` / `ink-700` / `ink-500` | `#1C1C1E` / `#4A4A4F` / `#6E6F75` | body / secondary / muted |
| `ink-200` `ink-100` `ink-050` | `#E4E5E7` `#EFEFEF` `#F7F7F6` | hairlines / dividers / off-white |
| `paper` | `#FFFFFF` | the **paper surface** field. Default for the website, documents and letters; a full peer of ink on cards. |
| `status-up` `status-down` `status-warn` | `#4a2f70` `#B5524A` `#B58A3A` | data viz and form states only |

**Data-viz ramp:** categorical = `dv-cat-1` to `dv-cat-5` (grape-800 · grape-500 · ink-500 · warn · down; maximum five series). Sequential = `dv-seq-1` to `dv-seq-4` (grape-100 to grape-500 to grape-600 to grape-800). Charts inherit the brand; no rainbow. Status colours never grade a person's health result, and never carry meaning without a label.

**Gradient:** none, by design.

## Surfaces

**Two peer surfaces. Not a light mode and a dark mode.** Here they are the two themes, Paper and Ink; in code the surface is set on the card root: `<div class="slide">` is paper, `<div class="slide" data-surface="ink">` is ink.

- **paper** `#FFFFFF`, the default for the website, documents and letters, and a full peer on cards. Clinical, calm, what evidence-led work is set on.
- **ink** `#0B0B0C`, the default for feed cards.

**Where colour goes on a card.** The accent (`surface-accent`) shows on the title's key word and the number. The payoff line reads `surface-fg`, white on ink. The population line and the footer read `surface-fg-muted`, soft grey on ink.

| token | paper | ink | role |
|---|---|---|---|
| `surface` | `paper` | `ink-max` | the field |
| `surface-fg` | `ink-1000` | `paper` | headline, primary text |
| `surface-fg-strong` | `ink-max` | `paper` | stat displays, the hero number |
| `surface-fg-muted` | `ink-700` | `ink-200` | labels, body, citations |
| `surface-fg-subtle` | `ink-500` | `ink-300` | micro-caps, meta |
| `surface-rule` | `ink-200` | `ink-900` | hairline dividers |
| `surface-eyebrow` | `grape-700` | `grape-500` | tracked micro-caps kicker |
| `surface-stroke` | `grape-600` | `ink-200` | load-bearing line art |
| `surface-accent` | `grape-800` | `grape-500` | a TYPE colour: eyebrows, links, tags, the one solid element's text |
| `surface-on-accent` | `paper` | `ink-max` | text reversed out of accent |
| `surface-fill` | `grape-800` | `grape-800` | a BLOCK colour: button and card backgrounds |
| `surface-fill-edge` | `grape-900` | `grape-600` | a fill needs a visible edge |
| `surface-on-fill` | `paper` | `paper` | text reversed out of a fill |
| `surface-logo` | `grape-800` | `paper` | delta and wordmark lockup |
| `surface-track` | `ink-100` | `ink-900` | bar-chart 0 to 100 track |
| `surface-baseline` | `grape-200` | `grape-500` | chart baseline and axis rule |
| `surface-footer` | `ink-1000` | `ink-900` | footer field |

The `color-*` tokens are semantic aliases of this layer (`color-fg` is `surface-fg`, `color-link` is `surface-accent`, and so on), kept because the site, the diagrams and the previews read them by those names.

**Fill and accent are split.** `surface-accent` is a type colour; `surface-fill` is a block colour. On paper both are grape-800 and the split is invisible. On ink they diverge, because grape-800 is 1.39:1 as text on the field (unreadable) and 14.22:1 as a fill with white on it.

**Contrast on ink `#0B0B0C`, measured:** fg 19.67:1 · fg-muted 15.61:1 · fg-subtle 11.99:1 · stroke 15.61:1 · accent 4.73:1 · baseline 4.73:1. White on grape-500 is **4.16:1**, so it is LARGE TEXT ONLY (24px or more, or 18.66px bold). Never set small text in it.

**Measure a chart fill against its neighbour, not against the field.** A bar sitting in a `surface-track` is judged against the track. The sequential ramp has FOUR steps. Against `ink-100` they read 1.05:1 / 3.62:1 / 5.64:1 / 12.37:1, and against paper 1.21:1 / 4.16:1 / 6.49:1 / 14.22:1. `dv-seq-1` clears nothing against either field, so it cannot carry meaning on its own and needs a label, an outline or a darker neighbour beside it.

## Typography

- **Display** `font-serif`: DM Serif Display for headlines. On cards the whole title is italic and its key word takes the accent. Instrument Serif is kept in the stack as the first fallback. Display tracking `tracking-display` (-0.02em), weight 400.
- **Sans** `font-sans`: DM Sans, body, UI, eyebrows, and any number inside a sentence. **Not a number standing on its own.**
- **Figures** `font-figures`: IBM Plex Sans regular for a number standing on its own: the stat, a label, the counter, a table, a confidence interval, `n =` and evidence strings. A number inside a sentence stays in the sentence's font, DM Sans. DM Sans has **no `tnum` table**: `font-variant-numeric: tabular-nums` on it is a silent no-op, and its digit `1` renders at 0.517 the width of its `0` in bold (narrower still in lighter weights), so every figure containing a 1 has a visible hole. IBM Plex Sans is monospaced in the figures by default and needs no feature flag.
- **Mono** the **evidence voice** (n =, p values, confidence intervals). Two tokens, and the split matters: `font-mono` is a system stack for the **web**, `font-mono-asset` is pinned **IBM Plex Mono** for anything **rendered to a file**. A system stack makes an exported PNG render differently per machine, which is drift by construction.
- Scale: `display-xl` to `display-sm` (serif, fluid) · `stat` · `heading-lg` to `heading-sm` · `lead` / `body` / `body-sm` · `meta` and `eyebrow` · `tag` and `method-label` (micro, uppercase, tracked). Body line height `lh-body` (1.6).
- **Card scale**, the `Card` type group, for the 1080 canvas: cover title 72 · title 48 · series label 24 · population line 24 · data label 24 · number 96 · number label 28 · payoff 34 · footer 26 · counter 24. Nothing on a card is under 24.
- All three faces are Google Fonts; no font files ship with this system.

## Cards

- **Format:** 1080 × 1350, square corners, no border, `ink` by default.
- **Margins and spacing:** 88 all round, 40 between parts. Left aligned; text runs the full width.
- **Order, top to bottom:** series label and slide counter · title · population line · data label · the drawing · the number box · the payoff · the footer.
- **The drawing leads.** The number sits under it.
- **The number box:** a 2px `surface-accent` outline with the field showing through, the number (`card-number`) with its label (`card-number-label`) beside it.
- **How much:** title, drawing and one number by default. More numbers only when the data has them.
- **Crowded:** split into two slides. The confidence interval goes in the caption, never on the card.
- **Footer:** a hairline (`surface-rule`) above it with a 40 gap; the short citation left (Weyand et al., 2023); the delta + drCWDugan lockup bottom right. The handle is not on cards.
- **Payoff:** `card-payoff`, italic, centred, `surface-fg`.
- **Never on a card:** a call to action, a photo on a data card, emoji, the delta as decoration.
- **Disclaimer:** in the caption, and only when a post discusses supplements or treatment options.

## Carousels

- **Cover:** the grape series label (`card-series`) and the title (`card-cover-title`, 72) only, left aligned, centred top to bottom. No counter, no footer, no mark.
- **Length:** set by the content.
- **Last slide:** the sources, always.
- **One finding:** a single card for Facebook and LinkedIn, a carousel for Instagram.
- **A series** (the Iron Panel) uses the same system as everything else; the series name is the only difference, with real icons from the library.

## Google Business Profile

- **The still:** landscape 1200 × 900, the same card style.

## Video

- **Top label:** the series label, "The Iron Panel · 01".
- **Narration:** Kore for explainers; Cory's own voice for podcasts.
- **Numbers on screen:** freely, and every one passes the evidence check first.
- **Ending:** the 1.5 s delta + drCWDugan sign-off, small, at the bottom right of the area TikTok and Instagram keep clear of their buttons and captions, not the frame's corner. No web address, no handle, nothing spoken over it (the Motion group).
- **The detail:** the opening card, the sign-off's beats and pixels, the screen rules and the voice are in the Video spec section (`video-spec.md`).

## Logo

- **Mark:** the **Δ delta**, symbol for change and difference, and an upward data peak. Equilateral. The single signature across icon and wordmark.
- **Lockup colour is a token in code** (`surface-logo`: grape-800 on paper, white on ink); components never read `surface-fg` for it. Image files carry their ink literally, one file per surface (the Logos group).
- **drCWDugan lockup:** delta + "drCWDugan" in DM Serif Display, outlined. Cards (bottom right of the footer) and the video sign-off. Grape-800 on paper, white on ink (Claude's call at Cory's request, 31 October 2026, matching the sign-off already on every reel).
- **Dr Cory Dugan lockup:** delta + "Dr Cory Dugan", no full stop (Cory, 29 September 2026). The website, documents and letters to clients. Grape-800 on paper, grape-200 on ink (Cory, 27 October 2026). It replaces the "Dr. Cory Dugan" primary lockup.
- **Credential lockup:** + "PhD", no eyebrow. Workplaces and proposals. **Stacked:** the stacked wordmark, for square and narrow spaces. Both redrawn without the full stop on 31 October 2026, grape-800 on paper, grape-200 on ink.
- **Cory's name as text**, on profiles: Dr Cory Dugan.
- **Icon:** grape delta tile, rounded square (`icon-delta.svg`, and `icon-delta-inverse.svg` for light). Scales to a 24px favicon.
- Clearspace ≥ the delta's height; minimum wordmark width 150px / 25mm. Approved grounds: paper, ink-050, grape-050, and **ink-max**.
- **Don't:** stretch or rotate the delta, add a gradient, place on an un-scrimmed photo, recolour outside grape, ink or paper, or re-add the baseline rule under the name.
- Video: every reel closes on the 1.5 s delta + drCWDugan sign-off, bottom right of the apps' clear area (see Video).

## Motif: the evidence signature

Kept: hairline rules as structure · generous whitespace (35 to 40% minimum) · squared editorial cards. On cards the number is `card-number`, IBM Plex Sans regular; the serif-italic grape numeral (`numeral`) stays on the website.

Evidence on display: lead with data, a big tabular `stat`, a small-caps `method-label` above it, a thin `data-baseline` rule beneath (2px, `surface-baseline`), mono `evidence` for the supporting figure, and `citation` for the source. See the EvidenceSignature component.

Charts: the fill reads `surface-accent`, the track reads `surface-track`. Use ONE fill colour when bar length and a printed number already carry the value. Never let the same value take different sequential-ramp steps on two slides of one carousel; that reintroduces the distortion a shared axis removes.

## Show it, do not only say it

Where a claim is about data, a process, a relationship, a sequence or a threshold, the asset SHOWS it as a minimal visualisation rather than describing it in a sentence. A number without its shape is an assertion; the shape is the argument. The full 14-group library lives in `BRAND/drCWD Concept-Diagram Visual Language_CD.md`.

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

1. **Line art, not chrome.** Strokes read `surface-stroke`, labels read `surface-fg-muted`. No gradients, no shadows, no 3D.
2. **What carries the finding is filled.** The dots that matter are filled `surface-accent`; the rest are thin rings. Bars are all filled.
3. **The structure IS the content.** Labels, not sentences. If it needs a paragraph to make sense, it is the wrong shape.
4. **It carries its own evidence.** A `method-label` above, a `citation` below naming the population. A diagram without a source is decoration.
5. **A number standing on its own uses `font-figures`.** A number inside a sentence stays in DM Sans.
6. **Only where it earns its place.** Numbered markers on a list that is not a sequence are decoration, and decoration is the thing this brand is against.

Cory's choices for cards:

- **The curve card is the favourite.** A hidden problem: two curves with the gap shaded. A cut-off: one curve and a threshold line.
- **Counting women:** the dot field, or woman icons when a better icon exists.
- **A body process:** coloured icons with arrows, small, nothing behind them.
- **Medium line weight** (4 at 1080). Minimal axes: only what the point needs.
- **Labels sit on the drawing**, never over a line.
- **A series reuses one drawing as its motif.** Before and after sit side by side.
- **Drawing size, type, animation, organs and people** are chosen per card from drawn options (rule 12).

## Layout

- Containers: `container-narrow` 760 (prose) · `container` 1120 · `container-wide` 1280 · `gutter` clamp(20px, 4vw, 48px). Section rhythm `section-y` and `section-y-tight`.
- Spacing: 4px base scale (`space-1` to `space-40`). Radius: `radius-0` default (editorial), `radius-md` / `radius-lg` / `radius-xl` (8 / 12 / 16) for interactive elements and data tiles, `radius-pill` (999) for pills.
- Borders: `bw-hair` 1px hairline / `bw-strong` 2px. Shadows: extremely restrained (`shadow-0` default, `shadow-xs` on a data tile); cards lean on borders.
- Patterns: stat bar · data tile · evidence and methodology block · comparison table (the Data components).
- **How to measure the 35 to 40% minimum.** It is layout negative space: content-block occupancy on a coarse grid (32px or 64px cells on a 1080px canvas). It is NOT a count of pixels equal to the background colour.
- **On ink the field is dark**, so state the rule as "field share on ink, whitespace on paper". The metric is the same; the field colour is not.
- Motion (code only, not a token family here): `ease-out` cubic-bezier(0.22, 1, 0.36, 1) · `ease-in-out` cubic-bezier(0.65, 0, 0.35, 1) · `ease-standard` cubic-bezier(0.4, 0, 0.2, 1) · `dur-fast` 120ms · `dur-base` 200ms · `dur-slow` 320ms · `dur-slower` 600ms.

## Imagery

- **Art direction:** documentary-real, natural light, desaturated-warm. Founder-in-context (talks, panels, lab) + clean screening, lab and data detail. No stock-gloss, no AI faces.
- **Generated images:** abstract data and organic forms only (no synthetic people). Grape lives in the UI *around* the image, never recolours the photo.
- **Approved bank:** headshot · lab-testing · iron-screening · pennington-talk · panel-discussion · abc-radio.
- **Which where:** headshot to About and Hero · lab and iron-screening to Services and products · talk, panel and radio to Credentials, Featured-in and social proof.

## Iconography

- **Source:** Cory's icon and clip-art library first (`~/Documents/icons-and-clip-art` on his Mac), then a matching set.
- **Colour:** icons keep their own colours (rule 10). Coloured clip art is fine on `ink`.
- **Size:** small, beside the text. Mixing icon families is fine if it reads.
- **Organs** default to realistic illustration; people and symptoms are chosen per card (rule 12).
- **An icon beside a number** depends on the card.
- **Never:** emoji, or the delta used as decoration. The delta is the mark (and the favicon tile, under Logo).
