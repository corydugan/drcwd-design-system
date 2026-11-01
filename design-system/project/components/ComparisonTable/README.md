# ComparisonTable

A plain ruled table comparing options row by row, with the favourable cells in accent and the unfavourable ones faint.

Lifted from `preview/components.html` in the repository; one of the v3 layout patterns.

- `table.cmp`: full width, collapsed borders, `fs-body-sm`, cells padded `space-3` by `space-4` over a 1px `color-rule`.
- `thead th`: `fw-semibold` in `surface-fg` over a 2px `surface-fg` rule.
- `td.yes`: `surface-accent`, semibold. `td.no`: `color-fg-faint`.

## What the consumer provides

A `<table class="cmp">` with a header row and short cells; mark cells `yes` or `no` only where the comparison is binary.

## Do and don't

- `color-fg-faint` is 2.63:1 on paper, below the 4.5:1 text floor. The repository sets it this way; keep the word in the cell (Yes, No, Partial) so the meaning never rests on the colour.
- Never use red, amber or green to grade a person's result.
