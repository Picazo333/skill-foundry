# Eval Case — Social-heavy consumer brand (snack/beverage)

## Scenario
A consumer snack brand's approved direction is "loud shelf, quiet
ingredients": a high-saturation primary surface color for shelf/feed
attention, deliberately unadorned near-black ink for ingredient/nutrition
copy, and no motion budget (static-first, packaging-led). Tests that the
skill treats print/packaging as a first-class surface (not an afterthought
to web/app), keeps a "loud" and a "quiet" sub-system internally consistent
without collapsing into one generic palette, and records an explicit
no-motion scope rather than a silently missing motion section.

## Input
```yaml
RUN_REQUEST:
  objective: "systematize approved direction into identity rules + tokens"
  source_artifacts:
    - "BRAND_STRATEGY.md (positioning: 'honest ingredients, loud enough to notice')"
    - "APPROVED_VISUAL_DIRECTION.md (color logic: high-saturation primary for shelf/feed, near-black ink for all ingredient copy, deliberately unadorned; typography: bold geometric display vs. plain grotesk body — a family split, not just a size split; motion: none, static-first, print/packaging-led)"
  known_context: "mark geometry: symbol + wordmark, dominant stroke width = 1/9 of mark height. Channels in scope: packaging/print (primary), social, retail/POS, e-commerce, email."
  constraints: []
  desired_output: full_system
  mode: STANDARD
  prior_run: null
```

## Expected behavior
1. Step 1 derives clear space/minimum size including a print/mm equivalent
   (packaging is the primary channel here), not a digital-only minimum
   size.
2. Step 3 represents "loud shelf, quiet ingredients" as two distinct type
   roles pulling from different families/weights, not merely two sizes of
   the same family.
3. Step 4 sets radius to the sharp/die-cut pole for packaging-led
   materiality and states that pole and reason explicitly (as opposed to
   the soft pole used in a different scenario) — the choice must trace to
   this direction's own materiality axis, not a copied default.
4. Step 5 states motion is explicitly out of scope, per the direction —
   the section is present and says so, not silently absent.
5. Step 6 treats packaging/print as a fully detailed surface (not a
   one-line stub) alongside social, retail/POS, e-commerce, and email —
   five surfaces total.

## Expected artifacts
- `IDENTITY_SYSTEM.md` — typography section shows a family-level split
  between display and body roles; motion section explicitly states
  out-of-scope; radius/materiality choice states its pole and reasoning.
- `DESIGN_TOKENS.json` — includes a print-unit (mm) minimum-size token
  alongside the digital px token.
- `APPLICATION_RULES.md` — packaging/print is a fully detailed surface
  (die-cut radius, ink-panel placement), not an afterthought to social.

## Forbidden behavior
- Must not represent "loud shelf, quiet ingredients" as a single palette
  with no type-role distinction.
- Must not omit the motion section or leave it ambiguous about whether
  motion is simply unaddressed vs. deliberately out of scope.
- Must not treat packaging/print as a minor or skipped surface given it is
  named as the primary channel in `known_context`.
- Must not state a minimum logo size in digital px only when print is a
  named primary channel.

## Pass criteria
- [ ] Typography section shows a genuine family-level split, not a
      same-family size-only distinction.
- [ ] Motion section explicitly states out-of-scope rather than being
      silently absent.
- [ ] Packaging/print is detailed at the same depth as the other four
      surfaces in `APPLICATION_RULES.md`.
- [ ] Both digital and print minimum-size/clear-space values are present.
- [ ] `status: COMPLETE`.
