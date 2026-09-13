# Territory Generation Framework

Used in `SKILL.md` steps 1–3. Governs how strategy becomes territories
without collapsing into adjective-literalism or false variety.

## 1. Attribute → tension → ruled-out (step 1)

Never map a strategic word directly to a visual object. Instead, ask what
*behavior* or *tension* the attribute demands, then what it rules out.

| Strategic attribute | Wrong (adjective-literalism) | Right (tension → rules out) |
|---|---|---|
| "Precise, clinical accuracy" (finance/health) | Thin sans-serif, lots of whitespace, blue | Tension: *legibility under scrutiny vs. warmth*. Demands: information hierarchy survives at small scale; color is functional (state, not mood). Rules out: decorative type, color used for vibe rather than meaning. |
| "Trustworthy" | Navy blue, serif logo | Tension: *authority vs. approachability*. Demands: consistency (same visual promise every time) over any specific palette. Rules out: novelty-driven variation between touchpoints — trust is broken by inconsistency, not by the wrong hue. |
| "Personal, almost intimate" (consumer/wellness) | Hand-lettering, pastel, rounded shapes | Tension: *individual voice vs. scalable system*. Demands: a grammar flexible enough to feel authored per-context without becoming inconsistent. Rules out: a single rigid template applied everywhere unchanged. |
| "Category-disrupting / non-conformist" | Bold color-blocking, brutalist type | Tension: *legible difference vs. incoherence*. Demands: the disruption reads as intentional against the category's actual defaults (requires knowing those defaults). Rules out: difference for its own sake with no category-comparison anchor. |

The output of step 1 is a table like the above, specific to the loaded
`BRAND_STRATEGY.md` — not a lookup from this reference. This reference
exists to demonstrate the *method* (attribute → tension → rules-out), not
to supply answers to reuse verbatim.

## 2. The 8 axes (step 2)

Every territory must set a position on all 8. A territory with an unset
axis is incomplete, not "focused."

1. **Composition** — grid discipline vs. asymmetry; centered vs.
   off-center; how negative space carries meaning (or doesn't).
2. **Materiality** — flat vs. dimensional; matte vs. glossy; printed-object
   feel vs. screen-native feel; texture vocabulary (paper grain, scan
   artifact, glass, none).
3. **Type logic** — not "which typeface" but the *rule*: contrast strategy
   (weight/size pairing), how hierarchy is built, whether type is a voice
   element or a structural element, justified/ragged, tracking behavior.
4. **Color behavior** — not a palette but a *rule* for when color appears,
   how much, and what it signals (state, category, mood, nothing). A
   monochrome-by-default territory with color reserved for one functional
   purpose is a valid, often more distinct, answer than a 5-color palette.
5. **Image language** — photography vs. illustration vs. data-driven/
   generative vs. none; subject distance and framing convention; how
   people (if any) are depicted or deliberately absent.
6. **Motion** — restrained/functional vs. expressive; what triggers motion
   (state change vs. decoration); or explicitly "no motion" if out of
   scope — state this rather than leaving it silent.
7. **Density** — information density tolerance; how much white space is
   structural vs. incidental; how the system behaves when content is dense
   (a form, a dashboard) vs. sparse (a hero moment).
8. **UI/system implications** — how the grammar survives into interface
   states (buttons, forms, error states, empty states) and small formats
   (favicon, app icon), not just hero imagery.

## 3. Divergence audit (step 3)

Build an 8×N matrix (axes as rows, territories as columns). For each pair
of columns, count matching axis positions. Two territories that match on
4+ of 8 are not distinct — they are a palette-swap of the same idea
wearing different colors. This is the single most common failure mode in
AI-assisted direction work: multiple "options" that all use the same
composition, same image language, same density, and differ only in hue.

**Rebuild rule:** when a collision is found, do not tweak the collided
territory's color axis alone. Re-open step 1's tension table, pick a
different, still-strategy-grounded tension to lead with, and re-derive at
least 3 axes (composition, image language, and one more) from that
tension. If no second strategy-grounded tension exists to anchor a
genuinely different territory, that is a signal the strategy itself may be
too thin to support 3–5 distinct territories — say so in `unresolved`
rather than manufacturing fake distinctness.

## 4. Reference-to-principle mapping (step 5)

When a reference is supplied (an artifact, movement, discipline — e.g.
"radiotomography," "Doré engravings," "brutalist wayfinding signage"),
extract structural principles, not surface. Ask: what does this reference
*do* mechanically that could transfer?

Example — "radiotomography" (X-ray/scan imagery) for a finance product:
- Surface (wrong to copy): black backgrounds, cyan/green scan-line color,
  bone-white line art.
- Principle (right to transfer): *translucency reveals structure otherwise
  hidden* → color behavior axis: use layered opacity to show
  data-beneath-data (e.g. a projection revealed under an actual figure,
  not two solid-color layers). *Scan-line rhythm as a time signal* →
  motion axis: progressive reveal instead of instant appearance, echoing a
  scan pass. The finance product's actual palette can be anything the
  strategy demands — the reference contributes *mechanism*, not *mood
  board colors*.
