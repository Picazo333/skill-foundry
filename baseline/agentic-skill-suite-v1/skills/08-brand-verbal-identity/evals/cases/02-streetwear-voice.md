# Eval Case — Streetwear voice

## Scenario
A small-batch streetwear label's strategy is explicitly anti-hype-cycle (no
restocks, ever). Tests that the skill derives a voice that would actually
contradict a typical competitor's default hype-driven copy, rather than
producing generic "fire drop" streetwear-brand filler.

## Input
```yaml
RUN_REQUEST:
  objective: "build verbal identity for a small-batch streetwear label"
  source_artifacts:
    - "BRAND_STRATEGY.md (positioning: 'made in runs of 200, never restocked, for people who'd rather own something than be seen owning something'; audience: anti-hype-cycle buyers; differentiator: no restock ever, 3-year track record; proof point: zero restocks across 3 years)"
  known_context: null
  constraints: []
  desired_output: full_verbal_system
  mode: STANDARD
  prior_run: null
```

## Expected behavior
1. At least one principle is built around treating "sold out" as final fact,
   not a scarcity-marketing hook — traced to the no-restock differentiator.
2. `VOICE_EXAMPLES.md`'s stress-test note explains specifically why a
   competitor running a restock/hype model could not produce the DO example
   without contradicting their own strategy.
3. No principle relies on generic hype-culture streetwear vocabulary
   ("fire," "don't sleep," "drop alert") as the primary device.

## Expected artifacts
- `VERBAL_IDENTITY.md` — a principle explicitly contrasting with
  restock-hype language.
- `MESSAGE_HIERARCHY.md` — a pillar built on "no restock is the product,"
  with the 3-year track record as proof.
- `VOICE_EXAMPLES.md` — DO/DON'T pairs including at least one social-caption
  format pair.

## Forbidden behavior
- Must NOT include a DON'T example that's a strawman no competent brand
  would write — the DON'T must be the plausible generic default for the
  category.
- Must NOT produce tagline territories that are finished taglines rather
  than directions.
- Must NOT default to adjectives ("bold," "authentic," "edgy") without a
  behavioral rule and DO/DON'T pairing.

## Pass criteria
- [ ] At least one principle traces to the no-restock differentiator with a
      DO/DON'T pair.
- [ ] Stress-test note explains the competitor contradiction concretely.
- [ ] No bare adjective appears as a stated principle without a rule.
