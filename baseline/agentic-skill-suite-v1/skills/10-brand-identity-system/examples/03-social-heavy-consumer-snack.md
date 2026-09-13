# Worked Example — Social-Heavy Consumer Brand (snack/beverage)

`APPROVED_VISUAL_DIRECTION.md` (abbreviated): a consumer snack brand's
direction is "loud shelf, quiet ingredients" — high-saturation primary
surface color to win shelf/feed attention, near-black ink for all
ingredient/nutrition information (deliberately unadorned, contrasting the
loud packaging), bold geometric type, no motion budget (static-first,
print/packaging-led).

## Step 1 — architecture (excerpt)
Symbol + wordmark lockup, symbol usable standalone at small social/app-icon
sizes. X = dominant stroke width = 1/9 of mark height. Clear space = 1.25X
(busy, high-contrast mark needs more relief to avoid feed clutter) at the
120px reference size (X=13px) = 16px. Minimum size: 32px digital (social
avatar floor) / 10mm print (packaging floor, converted from the same
logical-px constraint at 300dpi baseline).

## Step 2 — color roles (excerpt)
| Role | Token | Value | Usage rule | Approved pairing (computed) |
|---|---|---|---|---|
| Primary/shelf color | `color.brand.primary` | `#FFC933` (sunshine yellow) | Dominant packaging/feed surface | ink `#1A1A1A` on yellow: **11.32:1** — clears AAA, approved for all text on primary surface |
| Accent | `color.brand.accent` | `#E8368F` (hot pink) | Callout/limited-drop signaling | on `#FFFFFF`: **3.92:1** — fails 4.5:1, clears 3:1; **approved for large headline text (≥24px) and UI only, not body copy** |
| Ink | `color.neutral.900` | `#1A1A1A` | All nutrition/ingredient copy — deliberately unadorned | on `#FFFFFF`: [computed per method, clears 4.5:1 easily at this darkness] |

The accent's narrowed approval (large-text/UI only) is exactly why the
ingredient panel — which strategy calls "quiet" and is set in body-size
type — uses ink-on-white/yellow, never pink-on-white: pink at body size
would both violate the accessibility threshold and contradict the "quiet
ingredients" principle it's supposed to visually reinforce.

## Step 3 — typography (excerpt)
Base 16px, ratio 1.333 (perfect fourth — widest step-up of the three
examples, matching "loud shelf"). Display steps (`type.scale.700/800`) use
a bold geometric display face; body/ingredient copy uses a plain grotesk at
a smaller, consistent scale step — the direction's "loud shelf, quiet
ingredients" split is a *type-family* split, not just a size split.

## Step 4 — grid/spacing/shape (excerpt)
Radius: `radius.sm`=0px (packaging/print-led, sharp die-cut edges, opposite
pole from the app example) for primary packaging elements; social crops
use platform-default corner masking, not a brand radius token. Iconography:
minimal use (mostly wordmark/symbol-led), 20px grid where icons appear.

## Step 5 — motion
Explicitly out of scope: `IDENTITY_SYSTEM.md` states "no motion budget —
static-first, per direction" rather than leaving the section silently
absent.

## Step 6 — application rules (5 surfaces)
Packaging/print (primary channel — die-cut radius, ink panel placement),
social (Instagram/TikTok static posts — yellow-dominant crops, pink
reserved for limited-drop callout stickers only), retail/point-of-sale,
web/e-commerce product pages, and email (order confirmations — ink-on-white
body, yellow header band only).

## Step 9 — audit result
Pink's large-text/UI-only restriction is consistent across §2, the
ingredient-panel rule, and the exceptions section; radius choice states
its materiality-axis pole explicitly (sharp/die-cut) same as the other two
examples state theirs, each independently derived rather than copied
across examples; motion section states the explicit out-of-scope status;
5 surfaces covered. `status: COMPLETE`.
