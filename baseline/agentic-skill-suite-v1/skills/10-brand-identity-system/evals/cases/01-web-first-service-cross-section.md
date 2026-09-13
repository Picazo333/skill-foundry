# Eval Case — Web-first service brand (Cross-Section forecasting product)

## Scenario
A B2B forecasting product has a locked strategy and an *approved* (not
still-compared) visual direction whose color logic ties color strictly to
confidence-encoding and whose composition requires a layer beneath every
headline number. Tests that the skill systematizes a direction with a
strict, narrow color-usage rule into tokens without loosening that rule
into a generic decorative palette, and that it computes real contrast
numbers rather than asserting them.

## Input
```yaml
RUN_REQUEST:
  objective: "systematize approved direction into identity rules + tokens"
  source_artifacts:
    - "BRAND_STRATEGY.md (positioning: 'the forecast that shows its work')"
    - "APPROVED_VISUAL_DIRECTION.md (color logic: color only encodes confidence in a layered assumption stack, near-monochrome resting UI; composition: layer beneath every headline number; motion: progressive reveal on drill-down, in scope; imagery: none/data-driven only)"
  known_context: "mark geometry: layered-plane symbol, dominant stroke width = 1/10 of mark height. Channels in scope: web app, marketing site, decks, LinkedIn social. No print."
  constraints: ["no print"]
  desired_output: full_system
  mode: STANDARD
  prior_run: null
```

## Expected behavior
1. Step 1 derives clear space and minimum size from the supplied stroke-
   width proportion, not an arbitrary round number.
2. Step 2 assigns the accent color a role tied strictly to
   confidence-signaling (per the direction's core color rule) and computes
   its contrast on every surface it's proposed for, including the failing
   on-white case.
3. Step 2's failing pairing (accent-on-white) is narrowed to non-text/
   fills-only use, not dropped silently and not asserted as passing.
4. Step 5 translates the direction's in-scope motion principle into
   duration/easing tokens with state-change-only trigger logic.
5. Step 6 covers the in-scope channels (web app, marketing site, decks,
   LinkedIn) and explicitly records the "no print" limitation rather than
   silently under-covering five surfaces.
6. Step 9's audit confirms token/prose parity and that every grammar
   element (including the "layer beneath the headline" compositional rule)
   has an operational translation.

## Expected artifacts
- `IDENTITY_SYSTEM.md` — color-role table with a computed ratio next to
  every approved pairing; the accent's on-white restriction stated
  explicitly; compositional rule "layer beneath headline" reflected as an
  operational rule (e.g. a component/layout requirement), not dropped.
- `DESIGN_TOKENS.json` — values identical to `IDENTITY_SYSTEM.md`, no
  orphan tokens.
- `APPLICATION_RULES.md` — the four in-scope surfaces detailed, plus the
  explicit print-exclusion note.

## Forbidden behavior
- Must not present the accent color as freely usable for text/UI on every
  surface — the direction's own color rule (and the computed 2.02:1 ratio
  on white) forbids that.
- Must not invent a clear-space/minimum-size value disconnected from the
  supplied stroke-width proportion.
- Must not silently drop the "layer beneath the headline" compositional
  principle from the operational rules.
- Must not present fewer than the four in-scope surfaces without recording
  the print exclusion explicitly.

## Pass criteria
- [ ] Every approved color pairing in `IDENTITY_SYSTEM.md` carries a
      computed ratio and its cleared threshold.
- [ ] The accent-on-white pairing is explicitly narrowed to non-text use,
      not silently omitted or falsely marked as passing.
- [ ] Clear space/minimum size trace to the supplied mark geometry.
- [ ] `DESIGN_TOKENS.json` values match `IDENTITY_SYSTEM.md` exactly.
- [ ] The print-channel exclusion is recorded explicitly in
      `APPLICATION_RULES.md`.
- [ ] `status: COMPLETE` with the audit's quality fields all true/passing.
