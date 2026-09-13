# Eval Case — Rose/ivory dental identity with a fixed-palette constraint and explicit anti-reference

## Scenario
A boutique dental practice's client has already specified a rose/ivory
palette AND supplied an explicit anti-reference ("not another spa-tooth
brand — every boutique practice in town already looks like a candle
store"). Tests that the skill can still generate materially distinct
territories when one axis (color) is partially constrained by the client,
carrying differentiation through the other 7 axes instead — and correctly
identifies that the client's own palette preference, applied the obvious
way, IS the local category cliché.

## Input
```yaml
RUN_REQUEST:
  objective: "generate visual territories from locked strategy"
  source_artifacts:
    - "BRAND_STRATEGY.md (positioning: 'care that looks like you're a person, not a chart'; differentiation: relational warmth without spa-dentistry sameness; audience: adults avoiding dental visits due to clinical coldness)"
  known_context: "client-requested palette: rose/ivory. Anti-reference: 'not another spa-tooth brand'"
  constraints: ["palette starting point: rose/ivory"]
  desired_output: full_territory_set
  mode: STANDARD
  prior_run: null
```

## Expected behavior
1. Step 1 recognizes the client-supplied palette as a constraint on one
   axis (color hues), not a full territory answer — differentiation must
   come from color *behavior* and the other 7 axes.
2. Step 4 flags "evenly-diffused rose/pastel wash + centered symmetrical
   layout + generic soft-focus smile photography" as both the local
   competitor default AND a direct match to the client's own stated
   anti-reference — this territory, if generated, is explicitly named and
   discarded, not silently omitted or silently selected anyway.
3. Territories differ on composition, image language, and type logic
   while respecting the rose/ivory constraint on hue.
4. Selected direction resolves the "person, not a chart" positioning
   through real-practice imagery / editorial composition rather than
   through the palette (which is fixed and thus not a differentiator).

## Expected artifacts
- `VISUAL_TERRITORIES.md` — includes the ruled-out "spa dentistry" pattern
  as a named, discarded territory with its collision to the anti-reference
  stated, not omitted from the file.
- `APPROVED_VISUAL_DIRECTION.md` — color logic describes rose/ivory used
  in a restrained/asymmetric way (not an even wash); imagery language
  specifies real staff/patients or none, never generic stock smiles.
- `VISUAL_ANTI_PATTERNS.md` — explicitly names the evenly-diffused rose
  wash + centered "spa" layout as ruled out, citing the client's own
  anti-reference.
- `GENERATION_LANGUAGE.md` — principles that hold the palette constant but
  vary composition/imagery rules.

## Forbidden behavior
- Must not treat "client specified rose/ivory" as satisfying the
  differentiation requirement on its own — a fixed palette does not exempt
  the skill from generating materially distinct territories.
- Must not select or leave un-flagged a territory that reproduces the
  "spa dentistry" pattern the client explicitly rejected.
- Must not drop the rose/ivory constraint in the selected direction just
  because it made differentiation harder.

## Pass criteria
- [ ] The client's anti-reference is explicitly checked against generated
      territories, and any match is named and excluded (or the run stops
      to flag the contradiction if it cannot be avoided).
- [ ] At least 3 territories survive the divergence audit while honoring
      the rose/ivory constraint on the color-hue portion of the color axis.
- [ ] Selected direction's differentiation traces to composition/imagery/
      type logic, not to a palette claim.
- [ ] All four required artifacts exist with the content properties above.
