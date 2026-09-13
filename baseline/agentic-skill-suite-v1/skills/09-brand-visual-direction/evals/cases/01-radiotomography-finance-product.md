# Eval Case — Radiotomography-inspired finance product

## Scenario
A B2B forecasting product's strategy centers on process-transparency
("shows its work") against competitors who present a single confident
number. The client supplied "radiotomography" as an inspirational
reference word. Tests that a reference word is converted into a
structural principle (translucency/layering, progressive reveal) rather
than copied as literal X-ray imagery or colors, and that the category
default (navy + hero line chart) is correctly flagged and avoided.

## Input
```yaml
RUN_REQUEST:
  objective: "generate visual territories from locked strategy"
  source_artifacts:
    - "BRAND_STRATEGY.md (positioning: 'the forecast that shows its work'; differentiation: method-transparency, not accuracy claims; audience: skeptical numerate CFOs)"
  known_context: "reference word supplied: 'radiotomography' — client note: 'we like that it shows what's underneath, not what it looks like on the outside'"
  constraints: []
  desired_output: full_territory_set
  mode: STANDARD
  prior_run: null
```

## Expected behavior
1. Step 1 derives a tension from "shows its work" (process-legibility vs.
   hero-result) rather than jumping to a palette.
2. Step 5 maps "radiotomography" to a structural principle (translucency/
   layered reveal) attributed to color-behavior and/or motion axes — not
   to literal scan colors, X-ray subject matter, or medical imagery.
3. Step 2 produces territories that set all 8 axes each.
4. Step 3's divergence audit is actually run and any collision is
   rebuilt or discarded, not silently kept.
5. Step 4 flags "navy + single trust-accent + hero line chart" as the
   finance category default; the selected territory either avoids it or
   records an explicit strategic override.
6. Step 7 selects a territory and preserves discarded/runner-up
   territories with stated reasons.

## Expected artifacts
- `VISUAL_TERRITORIES.md` — 3+ territories, each with complete 8-axis
  definitions, divergence-audit matrix, and scores; no territory is a
  color-only variant of another.
- `APPROVED_VISUAL_DIRECTION.md` — color logic stated as a *rule* tied to
  confidence/assumption-encoding, not a decorative palette; compositional
  principle requires a layer beneath the headline number by default.
- `VISUAL_ANTI_PATTERNS.md` — explicitly rules out single-hero-number/
  line-chart as primary visual, and the navy+accent finance default.
- `GENERATION_LANGUAGE.md` — principle-level language reusable across
  asset types (not one scene description of "an X-ray chart").

## Forbidden behavior
- Must not render "radiotomography" as literal medical/X-ray imagery,
  colors, or subject matter in the grammar.
- Must not select a territory whose primary visual is a single confident
  number/line chart — this directly contradicts positioning.
- Must not present territories that differ only in accent color as
  "materially distinct."
- Must not skip the divergence audit or cliché-flag check.

## Pass criteria
- [ ] The reference word is transferred as a principle, not copied as
      literal surface (subject/color).
- [ ] At least 3 territories survive the divergence audit with ≤3 axis
      matches vs. any other survivor.
- [ ] The finance-category default is explicitly flagged in step 4 and
      addressed (avoided or overridden with stated rationale) in the
      selected direction.
- [ ] `APPROVED_VISUAL_DIRECTION.md` traces its color logic and
      composition principle to the "shows its work" strategy attribute.
- [ ] All four required artifacts exist with the content properties above.
