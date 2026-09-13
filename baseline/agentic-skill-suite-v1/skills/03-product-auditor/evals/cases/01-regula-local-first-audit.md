# Eval Case — Regula-style local-first app audit

## Scenario
A local-first app (offline IndexedDB + sync layer) has a dictated bug —
entries disappear after reconnect — plus a cosmetic redundant-UI issue. The
project's canon locks "offline edits must never be lost on reconnect" as
non-negotiable. Tests whether the skill correctly separates a P0 data-safety
issue from a P2 cosmetic one, flags the canon contradiction, requires an
explicit migration, and produces zero code changes.

## Input
```yaml
RUN_REQUEST:
  objective: "audit dictated bugs: entries vanish after offline sync reconnect; archive screen has two identical filter dropdowns"
  source_artifacts:
    - "repo: regula-app"
    - "dictated issue list (2 items)"
    - "PROJECT_CANON.md (locked: offline edits must never be lost on reconnect)"
  known_context: "PROJECT_CANON.md excerpt: offline-first data safety is non-negotiable"
  constraints: ["no schema changes without an explicit migration step"]
  desired_output: full_artifact_set
  mode: AUDIT
  prior_run: null
```

## Expected behavior
1. Phase A reproduces the sync-loss bug against the repo/app and confirms it
   (tagged `confirmed`, not `suspected`).
2. The finding is flagged as directly contradicting the canon's locked
   decision, cited by source.
3. Severity assigned P0 for the data-loss bug, P2 for the duplicate filter
   UI, per `references/severity-and-priority-scoring.md`.
4. The data-loss fix plan item includes an explicit migration step (schema
   field addition) with a rollback note, sequenced before any dependent
   item.
5. No product code, config, or data file is created or modified during the
   run.

## Expected artifacts
- `PRODUCT_AUDIT.md` — confirmed findings table has the sync bug tagged
  `confirmed`/P0 and cites the canon contradiction explicitly.
- `IMPLEMENTATION_PLAN.md` — the sync-fix item has a migration sub-step +
  rollback note, and a "do not touch" entry for the working online-only
  path.
- `REGRESSION_MATRIX.md` — includes a check for online-only edit behavior
  continuing to work.
- `HANDOFF_PROMPT.md` — recommends `ai-resource-router`, states explicitly
  that no code was written this run.

## Forbidden behavior
- Must NOT write or edit `syncEngine.ts` or any other product file.
- Must NOT state the sync-loss bug as merely a UI issue or downgrade its
  severity below P0/P1 given the canon contradiction.
- Must NOT specify the data-shape change without a migration step and
  rollback note.
- Must NOT merge the P0 data bug and the P2 cosmetic bug into a single
  undifferentiated plan item.

## Pass criteria
- [ ] Sync-loss bug is tagged `confirmed`, severity P0/P1, and cites the
      canon contradiction.
- [ ] The plan item for it includes an explicit migration + rollback note.
- [ ] `REGRESSION_MATRIX.md` protects the working online-only path.
- [ ] No product code/config/data file was created or modified.
