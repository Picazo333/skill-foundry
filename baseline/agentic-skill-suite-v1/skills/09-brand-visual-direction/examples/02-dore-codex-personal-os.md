# Worked Example — Doré/Codex-Inspired Personal OS

## Input (abbreviated `BRAND_STRATEGY.md`)
- **Category:** Consumer "personal operating system" app (notes, tasks,
  journal, and habit tracking unified).
- **Positioning:** "A life, illuminated" — against competitors positioned
  as productivity/efficiency tools, this product treats a person's data as
  a personal record worth dwelling in, not optimizing.
- **Differentiation:** Reflective, archival quality vs. competitors'
  dashboard-and-metrics framing.
- **Audience:** People fatigued by quantified-self apps who want their own
  history to feel meaningful, not gamified.
- **References supplied:** Gustave Doré engravings (dramatic
  black-and-white illustration, dense linework, high contrast); illuminated
  manuscript/codex page structure (marginalia, hand-set feel, text as
  artifact).

## Step 1 — tension derivation (excerpt)
| Attribute | Tension | Rules out |
|---|---|---|
| "A record worth dwelling in" | Archival permanence vs. live/editable data | Real-time dashboard widgets, streak counters, gamified progress bars |
| "Reflective, not optimizing" | Density-as-richness vs. density-as-noise | Metric-dense analytics screens |

## Step 5 — reference-to-principle mapping
Doré engravings → principle: *high-contrast linework builds weight and
permanence without color* → color behavior axis: near-grayscale by
default, so entries read as etched rather than logged. Illuminated
manuscript/codex → principle: *marginalia as a structural device, not
decoration* → compositional axis: annotations/tags live in a persistent
margin structure rather than a modal/overlay, echoing a page you keep
returning to rather than a screen you dismiss.

## Territories generated (summary)
1. **"Etched Ledger"** (selected) — grayscale/high-contrast linework
   textures on entries; persistent margin column for tags/annotations
   (never a modal); serif text-as-artifact typography with generous
   line-height; near-zero motion (entries "settle," they don't animate in);
   dense-but-calm — density from accumulated history, not simultaneous
   widgets.
2. **"Living Index"** (runner-up) — codex-page structural logic but warmer
   materiality (cream paper tone vs. grayscale ink), diverges on
   materiality, color behavior, and motion (gentle page-turn transitions)
   from Territory 1.
3. **"Marginal Notes"** (discarded — collided with Territory 1 on
   composition and type logic; distinguishing color alone was judged
   insufficient differentiation, so folded into Territory 1 rather than
   kept as a separate false-variety option).

## Selection
Territory 1, "Etched Ledger" — scored highest on strategic fit (directly
answers "reflective, not optimizing") and differentiation from
quantified-self competitors (no progress bars, no streaks, no color-coded
metrics).

## Output excerpt — `GENERATION_LANGUAGE.md`
> **Principle: weight without color.** Any new visual element signals
> importance through line weight and contrast, never through added color.
> Applications — app icon: rendered in the grayscale linework system, no
> accent color introduced for "pop"; empty-state illustration: dense
> linework rather than a flat pastel graphic.

## Output excerpt — `VISUAL_ANTI_PATTERNS.md`
> Ruled out: streak counters, progress rings, gamified completion
> percentages — the single most direct contradiction of "reflective, not
> optimizing" positioning; any of these appearing in downstream design
> should be rejected on sight.
> Ruled out: color-coded category tagging (a wellness/productivity-app
> default) — this system encodes distinction through linework density and
> margin placement instead.
