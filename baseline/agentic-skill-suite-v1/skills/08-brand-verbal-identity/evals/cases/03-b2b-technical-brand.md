# Eval Case — B2B technical brand

## Scenario
A database migration tool for senior platform engineers, with an explicit
"no basic explaining" constraint and a differentiator around showing failure
modes/rollback plans upfront. Tests that the skill resists adding a default
warmth/approachability principle that the audience/constraint actively
argue against.

## Input
```yaml
RUN_REQUEST:
  objective: "build verbal identity for a database migration tool"
  source_artifacts:
    - "BRAND_STRATEGY.md (positioning: 'shows you the rollback plan before you run anything'; audience: senior platform engineers burned by tools hiding failure modes; differentiator: dry-run diff + generated rollback script; proof point: zero silent-failure incidents across 400+ production migrations)"
  known_context: null
  constraints: ["audience is expert-level; no explaining basic database concepts"]
  desired_output: full_verbal_system
  mode: STANDARD
  prior_run: null
```

## Expected behavior
1. At least one principle centers on surfacing failure modes/technical facts
   plainly rather than softening them, traced to the "burned before" audience
   signal.
2. Syntax/rhythm conventions state a high jargon tolerance, traced to the
   "expert-level, no basic explaining" constraint.
3. No principle introduces a warmth/approachability rule that isn't traced to
   strategy — this scenario's signal argues against defaulting to one.

## Expected artifacts
- `VERBAL_IDENTITY.md` — a principle about disclosing technical facts/risk
  without softening, plus syntax conventions naming high jargon tolerance.
- `MESSAGE_HIERARCHY.md` — a pillar built on the rollback-before-run
  differentiator with the 400+ migrations proof point.
- `VOICE_EXAMPLES.md` — an error/empty-state DO/DON'T pair showing a
  disclosed failure mode vs. a softened generic error message.

## Forbidden behavior
- Must NOT add an "approachable/friendly" principle with no strategy trace,
  just because B2B brand voice guides often default to one.
- Must NOT explain basic database concepts in any DO example, per the
  explicit constraint.
- Must NOT soften a DO example's technical fact into reassurance language.

## Pass criteria
- [ ] A principle exists that discloses risk/failure modes plainly, traced
      to the "burned before" signal.
- [ ] No untraced warmth/approachability principle is present.
- [ ] Jargon tolerance is stated explicitly and matches the constraint.
