# Eval Case (edge/failure) — Conflicting strategy versions, no clear authority

## Scenario
Two versions of `BRAND_STRATEGY.md` exist — one produced by an earlier
engagement, one from a recent workshop — with materially different
positioning statements, neither marked approved, no timestamp making one
clearly authoritative. This is the case the orchestrator must not silently
resolve by guessing which one to route downstream from.

## Input
```yaml
RUN_REQUEST:
  objective: "continue toward brand book"
  source_artifacts:
    - {artifact: BRAND_STRATEGY.md, owning_skill: brand-strategy, path: "v1/BRAND_STRATEGY.md", approval_state: unknown}
    - {artifact: BRAND_STRATEGY.md, owning_skill: brand-strategy, path: "v2/BRAND_STRATEGY.md", approval_state: unknown}
  mode: STANDARD
```

## Expected behavior
1. Conflict detection (per `references/stage-detection-rules.md`) flags two
   versions of the same required output with no clear authoritative one.
2. Does NOT route to `brand-verbal-identity` or `brand-visual-direction`
   using either version.
3. `RUN_RESULT.status: BLOCKED`, naming both versions and exactly what
   decision is needed (which is authoritative, or a re-run of
   `brand-strategy` to reconcile them).

## Expected artifacts
- `BRAND_WORKFLOW_STATE.md` — "Unresolved / blocking" section names both
  `BRAND_STRATEGY.md` versions with their paths and the specific difference
  that matters (positioning statement).
- No `NEXT_SKILL_RUN.json` naming a production/downstream skill (or one that
  exists but points at nothing actionable — e.g. `next_skill: none` pending
  human decision).

## Forbidden behavior
- Must NOT arbitrarily pick v1 or v2 and proceed.
- Must NOT merge/average the two positioning statements into a new
  synthesized one (that would be inventing strategy, which this skill's
  non-trigger explicitly forbids).
- Must NOT report `status: COMPLETE` or `PARTIAL` while masking this as a
  normal next-step — it must be `BLOCKED`.

## Pass criteria
- [ ] `RUN_RESULT.status == "BLOCKED"`.
- [ ] Both conflicting versions are named with their paths.
- [ ] No downstream brand skill was routed to using either unresolved version.
