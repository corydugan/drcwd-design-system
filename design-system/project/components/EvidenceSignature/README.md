# EvidenceSignature

The v3 authority signature: data on display, led by a big tabular stat with its method above, a baseline rule beneath, the supporting figure in the evidence voice and the source underneath.

Built from the classes in `colors_and_type.css`; every one reads the surface layer, so the block works on paper and on ink unchanged.

## Parts, in order

| Class | Role | Reads |
|---|---|---|
| `.method-label` | small-caps label ABOVE the number ("METHOD", "n =", the threshold) | `fs-micro`, `tracking-method`, `surface-fg-subtle` |
| `.stat` | the hero number, IBM Plex Sans bold | `font-figures`, `fs-stat`, `surface-fg-strong` |
| `.stat--grape` | the one stat in accent | `surface-accent` |
| `hr.data-baseline` | 48px, 2px rule under the stat, the "measured" mark | `surface-baseline` |
| `.evidence` | mono voice for n =, p values, confidence intervals | `font-mono-asset`, `surface-fg-muted` |
| `.citation` | the source, naming the population | `fs-meta`, `surface-fg-subtle` |
| `.nowrap` | keeps an evidence unit whole ("p < .001") | |

## What the consumer provides

The number, read from a named source; the threshold that produced it, inside the method label; the population as the source names it, in the citation.

## Do and don't

- Every prevalence carries its threshold. Name the cut-off or do not name the number.
- Write `ug/L`, never the micro sign: the method label is uppercased, and uppercasing turns the micro sign into a capital mu.
- Set every figure in `font-figures`. DM Sans has no tabular figures, so a 1 leaves a hole.
- One `.stat--grape` per group at most.
