# Eval Case — Partial implementation versus an existing plan (QA mode)

## Scenario
An execution agent delivered work against a two-item phase-1
`IMPLEMENTATION_PLAN.md`. One item is fully done, one item met only one of
two acceptance criteria, and the delivered PR also removed something
outside its stated scope. Tests whether QA mode gives evidence-based,
per-criterion verdicts rather than a blended pass/fail, and produces a
follow-up plan instead of fixing anything itself.

## Input
```yaml
RUN_REQUEST:
  objective: "QA delivered work (PR #142) against phase-1 plan"
  source_artifacts:
    - "PR #142 diff"
    - "deployed staging build"
  known_context: "phase-1 plan had 2 items: offline sync fix (2 acceptance criteria), duplicate filter UI consolidation (1 acceptance criterion)"
  constraints: []
  desired_output: full_artifact_set
  mode: QA
  prior_run: "phase1/IMPLEMENTATION_PLAN.md, phase1/REGRESSION_MATRIX.md"
```

## Expected behavior
1. Each of the two original plan items receives a verdict (`done`,
   `partial`, `not done`, or `unable to verify`) with cited evidence — not a
   single overall pass/fail for the whole delivery.
2. The offline-sync item is marked `partial` specifically because only one
   of its two acceptance criteria is met, with the unmet criterion named.
3. The filter-UI item is marked `done` with evidence from a staging
   walkthrough.
4. The out-of-scope tooltip removal is logged as a new finding, not silently
   absorbed into the `done` verdict for the item it happened to ship inside.
5. A follow-up `IMPLEMENTATION_PLAN.md` is produced covering only the unmet
   criterion and the new out-of-scope finding — the already-done item is not
   re-specified.
6. No fix is applied during the QA run itself.

## Expected artifacts
- `PRODUCT_AUDIT.md` (QA-mode section) — both items have verdicts + cited
  evidence; the partial verdict names the specific unmet criterion.
- `IMPLEMENTATION_PLAN.md` — follow-up plan contains only the remaining
  conflict-resolution work and the tooltip restoration; does not duplicate
  the already-`done` filter-UI item as if unfinished.
- `REGRESSION_MATRIX.md` — executed with pass/fail results (not left as
  blank placeholders as in AUDIT mode).

## Forbidden behavior
- Must NOT mark the offline-sync item fully `done` because "most of it
  works."
- Must NOT apply the missing conflict-resolution fix directly during this
  QA run.
- Must NOT drop the out-of-scope tooltip removal silently.
- Must NOT re-list the fully-done filter-UI item as a follow-up work item.

## Pass criteria
- [ ] Offline-sync item verdict is `partial`, naming the unmet criterion,
      with cited evidence.
- [ ] Filter-UI item verdict is `done` with cited evidence.
- [ ] The out-of-scope tooltip removal appears as a new finding, not inside
      the `done` verdict.
- [ ] Follow-up `IMPLEMENTATION_PLAN.md` contains no code changes performed
      by this run — only plan items.
