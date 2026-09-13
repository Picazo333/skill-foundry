# Worked example — Partial implementation vs. an existing plan (QA mode)

## Input (abridged)
```yaml
RUN_REQUEST:
  objective: "QA the delivered work from the execution agent against phase-1 plan"
  source_artifacts:
    - "PR #142 diff (delivered work)"
    - "deployed staging build"
  known_context: "IMPLEMENTATION_PLAN.md item 1 (offline sync fix) and item 2
    (duplicate filter UI) were both dispatched"
  constraints: []
  desired_output: full_artifact_set
  mode: QA
  prior_run: "path/to/phase1/IMPLEMENTATION_PLAN.md, path/to/phase1/REGRESSION_MATRIX.md"
```

## Output (abridged)

**PRODUCT_AUDIT.md** (QA-mode section, excerpt):
```
| Plan item | Verdict | Evidence | Notes |
|---|---|---|---|
| Item 1 — offline sync fix | partial | ran offline-create/reconnect test
  harness 10x: entries now persist (criterion 1 met). Attempted concurrent
  offline+server edit conflict scenario: no resolution prompt appears,
  server edit silently wins (criterion 2 NOT met) | conflict-resolution UI
  from acceptance criteria was not implemented |
| Item 2 — consolidate duplicate filter UI | done | walked archive screen
  in staging: single "Status" dropdown present, underlying query logic
  unchanged and verified working | matches acceptance criteria fully |

## New findings surfaced during QA
| Q1 | PR #142 also removed the "Archive Filter" label's tooltip, which was
      not part of item 2's scope | regression (unscoped removal) | staging
      walkthrough, compared to pre-PR screenshot | P3 |
```

**IMPLEMENTATION_PLAN.md** (follow-up, excerpt):
```
### Item 1b — Add conflict-resolution prompt for concurrent offline edits
- Problem: Item 1 criterion 2 not met (PRODUCT_AUDIT.md QA verdict).
- Target behavior: unchanged from original Item 1 spec — concurrent edits
  surface a resolution prompt, never silent overwrite.
- Do NOT touch: the now-working offline-persist path (criterion 1, verified
  done) — do not regress it while adding the conflict UI.
- Tests: same conflict scenario used in QA verification.
- Acceptance criteria: [ ] resolution prompt appears on concurrent
  offline+server edit [ ] criterion 1 (persistence) still passes.

### Item 3 — Restore "Archive Filter" tooltip removed in PR #142
- Problem: Q1 — unscoped removal during item 2's delivery.
- Do NOT touch: the consolidated single-dropdown UI (item 2, verified done).
```

**REGRESSION_MATRIX.md** (executed, excerpt):
```
| R1 | Online-only create/edit still works | any entry screen | pass | n/a | verified in staging |
| P1 | Offline entries persist across reconnect | Item 1 | pass | n/a | verified 10/10 cycles |
```

**HANDOFF_PROMPT.md** (excerpt):
```
## Recommended next skill
ai-resource-router — dispatch Item 1b and Item 3 for a second execution
pass. Item 2 is fully done; no further action needed on it.

## Explicitly NOT done by this run
No not-done/partial item was fixed; only verified. Item 1's missing
conflict-resolution UI was written up as follow-up Item 1b, not implemented
here.
```

Note what did NOT happen: Item 1 being "mostly working" (persistence fixed)
did not get marked `done` — a `partial` verdict was used because one of two
explicit acceptance criteria was unmet, and the missing piece became its own
follow-up plan item rather than being patched directly during QA.
