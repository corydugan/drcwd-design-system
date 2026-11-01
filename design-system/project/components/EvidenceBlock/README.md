# EvidenceBlock

A short finding on a whisper-grape field with a grape rule at its left, the claim in body text and its evidence string in the mono voice beneath.

Lifted from `preview/components.html` in the repository; the "evidence/methodology block" among the v3 layout patterns.

- `.evblock`: 2px `grape-800` left rule, `color-bg-accent` (grape-050) field, padding `space-2` by `space-6`.
- Inside: a `<p>` for the claim, then `<p class="evidence">` for n, threshold, p value or confidence interval, each unit in `.nowrap`.
- The block carries its own light field, so its text is set in `ink-700` on either surface.

## What the consumer provides

One claim in one or two sentences, read from a named source, and its evidence string.

## Do and don't

- One block per claim; a page of them is decoration.
- The claim names its population and its threshold.
