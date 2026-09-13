# Eval Case — Zero to brand book

## Scenario
A brand-new project with no existing artifacts, objective is a fully
approved brand book. Tests the complete stage sequence end to end with no
stage skipped or re-run without cause. See `examples/zero-to-brand-book-example.md`
for the full worked sequence this case is based on.

## Input
```yaml
RUN_REQUEST:
  objective: "get this brand project to a published, approved brand book"
  source_artifacts: []
  mode: STANDARD
```
(7 sequential runs, each supplying the prior run's routed skill's completed
output as new `source_artifacts`.)

## Expected behavior
1. Run 1 routes to `brand-discovery` (nothing else could be routed to first).
2. Each subsequent run routes to exactly the next skill per
   `references/stage-detection-rules.md`, never skipping ahead of a missing
   dependency (e.g. never routes to `brand-identity-system` before
   `APPROVED_VISUAL_DIRECTION.md` exists).
3. `brand-verbal-identity` and `brand-visual-direction` are each routed to
   exactly once (parallel-eligible stage, not re-run).
4. Final run (`brand-book-builder` returns COMPLETE) produces
   `COMPLETION_REPORT.md` and stops — does not continue into production
   skills the objective didn't ask for.

## Expected artifacts
- `BRAND_WORKFLOW_STATE.md` updated every run, showing cumulative artifact
  inventory growing correctly.
- `NEXT_SKILL_RUN.json` present on every `PARTIAL` run, absent/null on the
  final `COMPLETE` run.
- `COMPLETION_REPORT.md` only on the final run.

## Forbidden behavior
- Must not route to the same skill twice without a new artifact/decision
  between routings.
- Must not route to `brand-book-builder` before both the verbal and
  identity-system artifact sets are complete.
- Must not continue past brand-book completion into
  `creative-brief-generator`/`brand-content-system` — the objective was
  "a brand book," not ongoing production.

## Pass criteria
- [ ] Exactly 6 distinct skills routed to across the 7 runs (discovery,
      strategy, verbal, visual, identity-system, book).
- [ ] No skill routed to twice.
- [ ] `COMPLETION_REPORT.md` produced only on the final run, `status: COMPLETE`.
