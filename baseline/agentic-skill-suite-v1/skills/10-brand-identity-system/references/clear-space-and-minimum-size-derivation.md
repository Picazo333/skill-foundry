# Clear-Space and Minimum-Size Derivation

Used in `SKILL.md` step 1. Governs how logo clear-space and minimum-size
values are *derived from the mark's own geometry* rather than picked as a
round, arbitrary number ("looks about right at 24px").

## Why derivation, not assertion
An arbitrary clear-space value (e.g. "leave 20px around the logo") breaks
the moment the mark is scaled — 20px of clear space around a mark shown at
400px is cramped; around a mark shown at 24px it dwarfs the mark itself.
Clear space and minimum size must scale *with* the mark, which requires
defining them in a mark-relative unit first, then stating the absolute
equivalent at the reference size for convenience.

## 1. Define the mark-relative unit ("X")
Pick a fixed, unambiguous feature of the mark itself as the unit:
- The height of a defining stroke or counter (the enclosed/negative-space
  area inside a letterform or symbol), or
- The stroke width of the mark's dominant line weight, or
- The cap-height of the wordmark, if the lockup is wordmark-led.

Name which feature was used and why (pick the feature most resistant to
optical distortion at small sizes — usually the dominant stroke width for
symbol marks, cap-height for wordmark-led lockups).

## 2. Derive clear space
State clear space as a multiple of X on every side of the mark's bounding
box (commonly 0.5X–1.5X depending on how enclosed/dense the mark is —
denser marks need more relief; simple geometric marks can hold less).
State both:
- **Mark-relative:** e.g. "1X on all sides, where X = the mark's dominant
  stroke width."
- **Absolute-at-reference-size:** e.g. "at the mark's reference size of
  120px tall (X = 10px), clear space = 10px on all sides."

## 3. Derive minimum size
Minimum size is the smallest size at which every defining detail of the
mark still resolves — i.e. the thinnest stroke, smallest gap, or smallest
enclosed counter does not fall below roughly 1px at the target device
pixel ratio (use 1px at 1x as the floor; note that at 2x/3x device pixel
ratios the same logical px is still crisp, so 1 logical px at 1x is the
binding constraint, not the physical pixel count).
- Identify the mark's thinnest stroke or smallest gap as a proportion of
  its full height (e.g. "the gap between the two strokes is 1/12th of the
  mark's total height").
- Minimum size = the height at which that proportion equals ~1px, i.e.
  `minimum_height ≈ 1px / (thinnest_feature_proportion)`.
- State separate minimum sizes for **digital** (favicon/app-icon floor,
  usually smaller because it's a single-purpose square context) and
  **print** (business-card/stationery floor, in mm, accounting for typical
  print resolution).
- If the primary mark cannot resolve legibly below a usable size (common
  for detailed marks), define a **simplified/monogram variant** explicitly
  scoped to small-format use only, rather than shipping the primary mark
  below its legibility floor.

## 4. What to do when no mark geometry is available
If this skill runs before a mark exists in vector form (e.g. the direction
specifies a wordmark-only lockup with no drawn symbol yet), clear-space and
minimum-size values cannot be derived — record this as a blocking gap in
`unresolved` per `SKILL.md`'s stop conditions rather than inventing a
placeholder "20px" that has no relationship to the eventual mark.

## Worked example
Mark: a geometric monogram where the dominant stroke width is 1/12 of the
mark's total height, and the smallest enclosed counter gap is also
approximately 1/12 of total height (the binding constraint).
- X = dominant stroke width.
- Clear space = 1X on all sides (moderately dense mark → 1X, not 0.5X).
- Minimum size (digital) ≈ 1px / (1/12) = 12px total height as an absolute
  floor for the *full-detail* mark; below that, use the simplified
  monogram/favicon variant. State the reference size too, e.g. "at the
  144px reference size, X = 12px, so clear space = 12px on all sides."
- Minimum size (print) — convert the same logical floor to mm at standard
  print resolution (300dpi ⇒ 1px ≈ 0.085mm at that resolution baseline;
  state the resulting mm floor rather than reusing the digital px number
  unchanged).
