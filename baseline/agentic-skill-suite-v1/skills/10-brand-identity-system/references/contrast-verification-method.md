# Contrast Verification Method

Used in `SKILL.md` step 2 (and re-checked in step 9). Governs how every
approved text/UI color pairing gets a computed WCAG contrast ratio instead
of an asserted "meets AA" claim.

## 1. Thresholds (WCAG 2.x)
- **4.5:1** — normal text (below 24px, or below 18.66px if bold).
- **3:1** — large text (≥24px, or ≥18.66px bold) and UI components /
  graphical objects (icon strokes, focus indicators, input borders).
- **7:1 / 4.5:1** — AAA equivalents, optional; state if a pairing clears
  AAA as a bonus, never require it unless the brief asks for it.

A pairing that fails 4.5:1 but clears 3:1 is approved for large-text/UI
use only — state that scope explicitly rather than dropping the pairing
outright or rounding up to "passes."

## 2. Relative luminance formula
For an sRGB color with 8-bit channels `R, G, B` (0–255):

```
for each channel c in {R, G, B}:
  c_srgb = c / 255
  c_lin  = c_srgb / 12.92                          if c_srgb <= 0.03928
         = ((c_srgb + 0.055) / 1.055) ^ 2.4         otherwise

L = 0.2126 * R_lin + 0.7152 * G_lin + 0.0722 * B_lin
```

## 3. Contrast ratio
```
ratio = (L_lighter + 0.05) / (L_darker + 0.05)
```
where `L_lighter` is the greater of the two colors' luminance.

## 4. Worked example (used in `IDENTITY_SYSTEM.md` templates/examples)
`#14213D` (ink navy) on `#FFFFFF` (white):
- R=20,G=33,B=61 → linearized: R_lin≈0.00700, G_lin≈0.01522, B_lin≈0.04671
- L ≈ 0.2126(0.00700) + 0.7152(0.01522) + 0.0722(0.04671) ≈ **0.01575**
- White L = 1.0 (all channels linearize to 1.0)
- ratio = (1.0 + 0.05) / (0.01575 + 0.05) ≈ **15.97:1** — clears 4.5:1 and
  7:1; safe for normal body text.

`#FCA311` (amber accent) on `#14213D` (ink navy):
- L(amber) ≈ 0.2126(0.97335) + 0.7152(0.3663) + 0.0722(0.00560) ≈ **0.4694**
- ratio = (0.4694 + 0.05) / (0.01575 + 0.05) ≈ **7.90:1** — clears 4.5:1;
  approved for text/UI on the dark surface.

`#FCA311` on `#FFFFFF`:
- ratio = (1.0 + 0.05) / (0.4694 + 0.05) ≈ **2.02:1** — fails both
  thresholds. This pairing is **not** approved for text or UI components;
  amber-on-white is fills/graphics/large decorative use only, and that
  restriction must be stated in `IDENTITY_SYSTEM.md`, not silently omitted.

## 5. How to apply this in the procedure
For every role pairing you intend to approve in step 2:
1. Compute the ratio using the formula above (or a verified contrast
   calculator implementing the same formula — never eyeball it).
2. State the ratio next to the pairing in `IDENTITY_SYSTEM.md`.
3. State which threshold it clears (large-text/UI only at 3:1, or full
   normal-text approval at 4.5:1).
4. If it clears neither, either drop the pairing from approved usage or
   restrict it to non-text decorative use, and log it as an exception in
   step 7 rather than silently omitting the failing pairing from the
   document.
