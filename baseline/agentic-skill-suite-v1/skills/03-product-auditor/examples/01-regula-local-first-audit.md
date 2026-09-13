# Worked example — Regula-style local-first app audit (AUDIT mode)

## Input (abridged)
```yaml
RUN_REQUEST:
  objective: "audit dictated bugs while navigating the Regula app: entries sometimes vanish after offline sync, and the archive filter UI looks duplicated"
  source_artifacts:
    - "repo: regula-app (local-first, IndexedDB + sync layer)"
    - "dictated issue list: 'entries disappear after reconnecting', 'two filter dropdowns do the same thing on the archive screen'"
    - "PROJECT_CANON.md (locked: 'local-first, offline edits must never be lost on reconnect')"
  known_context: "PROJECT_CANON.md LOCKED DECISIONS: offline-first data safety is non-negotiable"
  constraints: ["no schema changes without an explicit migration step"]
  desired_output: full_artifact_set
  mode: AUDIT
  prior_run: null
```

## Output (abridged)

**PRODUCT_AUDIT.md** (excerpt):
```
## Confirmed findings
| C1 | Entries created offline are overwritten (not merged) by server state on
      reconnect sync | data-risk | reproduced: created entry offline, went
      online, entry gone; sync layer does last-write-wins by server
      timestamp only | P0 |
| C2 | Archive screen has two filter dropdowns ("Status" and "Archive
      Filter") that set the same underlying query param | redundant-UI |
      code inspection: both bind to `filterState.status` | P2 |

## Canon/prior-audit contradictions
- C1 directly contradicts PROJECT_CANON.md locked decision "offline edits
  must never be lost on reconnect" — source: PROJECT_CANON.md
```

**IMPLEMENTATION_PLAN.md** (excerpt):
```
### Item 1 — Fix offline-edit loss on sync (data migration required)
- Problem: C1 — last-write-wins sync drops offline edits.
- Target behavior: offline edits merge with server state on reconnect;
  conflicting fields are flagged for user resolution, never silently
  dropped.
- Affected components/data/routes: sync layer (`syncEngine.ts`), local
  IndexedDB entry schema (needs conflict-marker field).
- Dependencies: none (must land first — everything else in this plan
  depends on data safety being fixed first).
- Migration required: yes — add `_conflictState` field to local entry
  schema; existing local entries default to `_conflictState: null`;
  rollback: drop the field, revert to prior sync behavior (data-loss risk
  reintroduced — do not roll back without a data-safety justification).
- Do NOT touch: the online-only edit path, which already works correctly.
- Tests: offline-create → reconnect → assert entry persists; offline-edit +
  concurrent server-edit → reconnect → assert both surfaced as conflict, not
  overwritten.
- Acceptance criteria: [ ] no offline entry is lost across 10 reconnect
  cycles in test harness [ ] conflicting edits produce a visible resolution
  prompt, never silent overwrite.

### Item 2 — Consolidate duplicate archive filter UI
- Problem: C2 — two controls set the same state.
- Dependencies: none.
- Do NOT touch: the underlying `filterState.status` query logic itself
  (works correctly; only the duplicate UI is redundant).
```

**REGRESSION_MATRIX.md** (excerpt):
```
| R1 | Online-only create/edit still works | any entry screen | (blank —
       to be filled at QA) | n/a | product has no mobile build as of this
       audit — mobile column explicitly not-applicable |
```

**HANDOFF_PROMPT.md** (excerpt):
```
## Recommended next skill
ai-resource-router — dispatch Item 1 (data-safety P0) first as its own
execution pass; Item 2 can follow independently.

## Explicitly NOT done by this run
No product code, config, or data was written or changed by this audit.
```

Note what did NOT happen: even though the offline-sync bug is a P0 with an
obvious one-line-sounding fix, the skill did not touch `syncEngine.ts` — it
specified the fix as a plan item with a migration and rollback note, and
stopped.
