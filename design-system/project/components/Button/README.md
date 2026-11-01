# Button

Pill buttons in three weights: a grape fill for the one primary action, an outline for the secondary, and an underlined text link for the quietest.

Lifted from `preview/components.html` in the repository (hand-written there, no component code).

| Class | Look | Reads |
|---|---|---|
| `.btn .btn-primary` | grape fill, white text, pill | `surface-fill`, `surface-on-fill`, `surface-fill-edge`, `radius-pill` |
| `.btn .btn-secondary` | outline, accent text | `surface-accent`, `color-border-strong` |
| `.btn .btn-ghost` | text with an underline, no pill | `surface-accent` |

Type is `font-sans` at `fs-body-sm`, `fw-medium`; padding `space-3` by `space-6`.

## What the consumer provides

An `<a>` or `<button>` with the classes, and a label that names the action in plain words.

## Do and don't

- One primary button per view.
- No exclamation marks in a label.
- The focus ring is a 2px `surface-accent` outline, offset 2px.
