# DataTile

A bordered tile holding one method label and one stat, set in a responsive grid of tiles.

Lifted from `preview/components.html` in the repository; one of the v3 layout patterns.

- `.tiles` is the grid: `repeat(auto-fit, minmax(200px, 1fr))`, gap `space-4`.
- `.tile` is the card: 1px `color-border`, `radius-lg`, padding `space-6`, `shadow-xs`.
- Inside: `.method-label` then `.stat` at `fs-display-sm`; add `.stat--grape` to one tile at most.

## What the consumer provides

Each tile's label (the threshold or method, in the label) and its sourced number.

## Do and don't

- A tile states one number. A sentence belongs in an EvidenceBlock.
- A prevalence tile names its cut-off in the label.
