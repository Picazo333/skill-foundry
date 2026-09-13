# Worked Example — Web-First Service Brand ("Cross-Section" forecasting product)

Continues the `brand-visual-direction` worked example (see
`/skills/09-brand-visual-direction/examples/01-radiotomography-finance.md`):
a B2B forecasting product whose
`APPROVED_VISUAL_DIRECTION.md` selected the "Cross-Section" territory —
color reserved to encode confidence in a layered assumption stack, near-
monochrome resting UI, a compositional rule that every forecast surface
shows a layer beneath the headline number.

## Input (abbreviated)
- `BRAND_STRATEGY.md`: "the forecast that shows its work"; audience:
  skeptical, numerate CFOs.
- `APPROVED_VISUAL_DIRECTION.md`: color logic — "color never decorates; it
  exists only to encode confidence level in a layered assumption stack.
  Resting UI is near-monochrome." Compositional principle — "every
  forecast surface shows at least one layer beneath the headline number by
  default." Motion — progressive reveal on drill-down (in scope). Imagery —
  none (data-driven surfaces only, no photography/illustration).
- Mark geometry supplied: a layered-plane symbol; dominant stroke width =
  1/10 of mark height.
- Channels in scope: web app (product/UI), marketing site, decks (investor/
  sales), social (LinkedIn only), no print.

## Step 1 — architecture (excerpt)
X = dominant stroke width = 1/10 of mark height. Clear space = 1X on all
sides (moderately dense layered mark). At the 160px reference size,
X = 16px, so clear space = 16px on all sides. Minimum size: thinnest
resolvable gap between layers ≈ 1/14 of mark height ⇒ minimum digital size
≈ 1px / (1/14) ≈ 14px total height for the full-detail mark; below that,
use the flattened single-plane monogram variant (defined separately, scope:
favicon/app-icon only).

## Step 2 — color roles (excerpt, full method in `references/contrast-verification-method.md`)
| Role | Token | Value | Usage rule | Approved pairing (computed) |
|---|---|---|---|---|
| Primary/ink | `color.brand.primary` | `#14213D` | Body text, structural lines, resting UI | on `#FFFFFF`: **15.97:1** — clears 4.5:1, approved for all text |
| Accent (confidence signal) | `color.brand.accent` | `#FCA311` | Confidence-band fills and interactive state only — never decorative | on `#14213D`: **7.90:1** — approved text/UI on dark surface. On `#FFFFFF`: **2.02:1** — fails both thresholds; **fills/graphics only on light surface, never text or UI on white** |
| Semantic success | `color.semantic.success` | `#1E7A46` | Positive variance | on `#FFFFFF`: **5.35:1** — clears 4.5:1 |
| Semantic error | `color.semantic.error` | `#C0392B` | Negative variance | on `#FFFFFF`: **5.44:1** — clears 4.5:1 |
| Semantic warning | `color.semantic.warning` | `#B45309` | Assumption flagged as stale | on `#FFFFFF`: **5.02:1** — clears 4.5:1 |
| Neutral-50…900 | `color.neutral.*` | `#F7F8FA`…`#14213D` | Backgrounds/structure | — |

## Step 3 — typography (excerpt)
Base 16px, ratio 1.25 (major third). `type.scale.200` (body) = 16px/1.5
line-height/400 weight. `type.scale.700` (h1) = 49px/1.15/700. Primary
family: a numeral-forward grounded sans (structural role); fallback stack
`-apple-system, "Segoe UI", Roboto, sans-serif`. Tracking: numerals use
tabular figures at all sizes (numerate-audience requirement — misaligned
columns undercut "shows its work").

## Step 4 — grid/spacing/shape (excerpt)
Spacing base 8px: `space.1`=4, `space.2`=8, `space.3`=12, `space.4`=16,
`space.5`=24, `space.6`=32. Radius: `radius.sm`=2px, `radius.md`=4px
(sharp/precise pole — dense numerate audience, not soft/approachable).
Iconography: 24px grid, 1.5px stroke, outline (not filled) default —
consistent with the near-monochrome resting-UI rule.

## Step 5 — motion (excerpt)
`motion.duration.base` = 200ms, `motion.easing.standard` =
`cubic-bezier(0.4,0,0.2,1)`. Trigger logic: state-change/drill-down only
(progressive reveal echoing the direction's "layer beneath the headline"
principle) — never decorative/ambient motion.

## Step 6 — application rules (5 surfaces)
Web app (product/UI), marketing site, decks (investor/sales — max
`type.scale.500` on a slide title, `space.6` minimum slide margin),
LinkedIn social (1:1 and 4:5 crops, logo never below `logo.minSize.digital`
in a social crop), and print excluded per `constraints` (recorded as an
explicit channel limitation, not silently dropped).

## Step 9 — audit result
All tokens in `DESIGN_TOKENS.json` trace to this prose; accent-on-white
restriction is recorded both in §2 and in the exceptions section (step 7);
5 surfaces covered including the explicit print exclusion; every grammar
element (color logic, compositional "layer beneath," motion, near-
monochrome mood) has an operational rule. `status: COMPLETE`.
