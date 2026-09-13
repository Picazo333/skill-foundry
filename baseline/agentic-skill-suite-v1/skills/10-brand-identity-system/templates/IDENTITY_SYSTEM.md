# Identity System — [Brand Name]

Built from: `APPROVED_VISUAL_DIRECTION.md` ([territory name/date]).
Traces to strategy via the direction's own trace-to-strategy table; this
document does not re-derive strategy, only systematizes the approved
grammar.

## 1. Identity architecture
- **Primary mark:** [description; vector source reference]
- **Wordmark:** [typeface/treatment]
- **Lockups:** [horizontal — default context; stacked — default context]
- **Monochrome / reversed versions:** [when each is used]
- **Clear space:** [N]X on all sides, where X = [defining feature] =
  [value] at reference size [value]. Absolute-at-reference-size: [value].
  (Method: `references/clear-space-and-minimum-size-derivation.md`.)
- **Minimum size:** digital [value]px (full-detail mark) / [value]px
  (simplified variant, if applicable); print [value]mm.
- **Forbidden alterations:** [stretch / recolor outside palette / rotate /
  add effects / place below required contrast — list explicitly]

## 2. Color roles
Core rule (from direction): [state the direction's color-logic rule].

| Role | Token | Value | Usage rule | Approved pairings (computed contrast) |
|---|---|---|---|---|
| Primary | `color.brand.primary` | `#______` | [...] | on `#______`: [ratio]:1 — [threshold cleared] |
| Accent | `color.brand.accent` | `#______` | [...] | on `#______`: [ratio]:1 — [threshold cleared] |
| Neutral-50…900 | `color.neutral.*` | [...] | [...] | [...] |
| Success | `color.semantic.success` | `#______` | [...] | [...] |
| Warning | `color.semantic.warning` | `#______` | [...] | [...] |
| Error | `color.semantic.error` | `#______` | [...] | [...] |
| Info | `color.semantic.info` | `#______` | [...] | [...] |

Contrast method: `references/contrast-verification-method.md`. Any pairing
below 4.5:1 is restricted to large-text/UI use (≥3:1) or dropped — state
which, never assert "accessible" without the number.

## 3. Typography
- **Primary family:** [name] — fallback stack: `[font-stack]`
- **Secondary family (if any):** [name] — fallback stack: `[font-stack]`
- **Scale:** base [value]px, ratio [named ratio, e.g. 1.25 / major third]

| Step | Role | Size | Line-height | Weight |
|---|---|---|---|---|
| `type.scale.100` | Caption/label | [...] | [...] | [...] |
| `type.scale.200` | Body | [...] | [...] | [...] |
| `type.scale.300` | Lead/body-lg | [...] | [...] | [...] |
| `type.scale.400`–`800` | H4–Display | [...] | [...] | [...] |

- **Voice vs. structure:** [from direction]
- **Tracking/casing rules:** [...]
- **Responsive behavior:** [fluid clamp formula or breakpoint steps]

## 4. Grid, spacing, shape, imagery, iconography
- **Spacing scale:** base unit [value]px — `space.1`…`space.n`: [values]
- **Grid:** [columns] / [gutter] / [margin] per breakpoint: [...]
- **Radius scale:** `radius.sm/md/lg/full` = [values] (materiality axis:
  [sharp/precise or soft/approachable] — why: [...])
- **Border/stroke widths:** `border.width.*` = [values]
- **Imagery treatment:** crop ratios [...]; color treatment [...]; subject
  convention [...]; deliberately absent: [...]
- **Iconography:** grid [value]px on [value]px stroke; corner style
  [rounded/square, consistent with radius scale]; fill vs. outline default:
  [...]

## 5. Motion
[State explicitly if out of scope.]
- **Duration tokens:** `motion.duration.fast/base/slow` = [ms values]
- **Easing:** `motion.easing.standard` = [cubic-bezier]
- **Trigger logic:** [state-change-driven / decorative — from direction]
- **Restraint rule:** [what motion never does]

## 6. Exceptions and forbidden combinations
- [Forbidden logo/background pairing — reason]
- [Forbidden type pairing — reason]
- [Any contrast-failing pairing restricted/dropped in §2 — reason]
- [Any request-driven exception granted — owner + reason]

## Grammar-element trace table
| Direction grammar element | Operational rule(s) here |
|---|---|
| Mood | [...] |
| Color logic | [...] |
| Typography logic | [...] |
| Imagery language | [...] |
| Compositional principles | [...] |
| Motion principles (if in scope) | [...] |
