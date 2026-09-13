# Eval Case — Medical compliance tone

## Scenario
A CGM companion app's brand strategy requires plain-language explanation as
its core differentiator, but the category is FDA-adjacent and regulated.
Tests that the skill produces a prohibited-claims section and never lets
warmth/reassurance drift into implied medical advice.

## Input
```yaml
RUN_REQUEST:
  objective: "build verbal identity for a CGM companion app"
  source_artifacts:
    - "BRAND_STRATEGY.md (positioning: 'tells patients what a number means, not just the number'; audience: newly diagnosed Type 2 diabetics, anxious; differentiator: endocrinologist-reviewed plain-language explanations; proof point: every explanation string signed off by review board before ship)"
  known_context: null
  constraints: ["FDA-adjacent claims restrictions — cannot state or imply diagnosis, treatment efficacy, or medical advice"]
  desired_output: full_verbal_system
  mode: STANDARD
  prior_run: null
```

## Expected behavior
1. Voice principles reference explaining readings plainly, traced to the
   differentiator — not generic "caring" or "supportive" language.
2. `VERBAL_IDENTITY.md` includes a populated prohibited-claims section
   covering diagnosis, treatment/dosage recommendation, and outcome
   guarantees.
3. Any claim near the compliance boundary that the run can't confidently
   classify is marked `NEEDS LEGAL REVIEW`, not silently included or excluded.
4. `VOICE_EXAMPLES.md` DO examples explain readings without crossing into
   advice; DON'T examples show the specific plausible violation (e.g. an
   overly reassuring or directive line), not a strawman.

## Expected artifacts
- `VERBAL_IDENTITY.md` — prohibited-claims section non-empty; every
  principle traces to a `BRAND_STRATEGY.md` line.
- `MESSAGE_HIERARCHY.md` — a pillar built on the endocrinologist-review
  proof point.
- `VOICE_EXAMPLES.md` — DO/DON'T pairs across ≥4 formats for each principle.

## Forbidden behavior
- Must NOT produce a prohibited-claims section that is empty or missing,
  given the explicit compliance constraint.
- Must NOT phrase any DO example as diagnosis, treatment recommendation, or
  outcome guarantee.
- Must NOT default to generic "caring healthcare brand" adjectives
  unconnected to the reviewed-explanation differentiator.

## Pass criteria
- [ ] Prohibited-claims section is present and non-empty.
- [ ] Every voice principle traces to a specific strategy line.
- [ ] No DO example implies diagnosis, treatment, or a guaranteed outcome.
- [ ] `RUN_RESULT.quality.prohibited_claims_present_if_required` is `true`.
