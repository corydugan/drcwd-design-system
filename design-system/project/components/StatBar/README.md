# StatBar

A row of stats between a strong rule above and a hairline below, for a page band that leads with numbers.

Lifted from `preview/components.html` in the repository; one of the v3 layout patterns.

- `.statbar`: flex row, gap `space-10`, padding `space-6` top and bottom, a 2px top rule in `surface-fg` and a 1px bottom rule in `color-rule`.
- Each item: `.method-label`, a line break, then `.stat` at `fs-display-sm`.

## What the consumer provides

Two to four sourced numbers, each with its label.

## Do and don't

- Labels, not sentences.
- Every prevalence carries its threshold in its label.
