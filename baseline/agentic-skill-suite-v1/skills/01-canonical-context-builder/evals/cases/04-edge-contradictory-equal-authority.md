# Eval Case (edge/failure) — Contradictory sources of equal authority and recency

## Scenario
Two stakeholder emails sent the same day give contradicting budget figures,
with no other source to break the tie. This is the case the skill must
refuse to silently resolve — the correct behavior is an explicit, visible
unresolved conflict, not a coin-flip pick.

## Input
```yaml
RUN_REQUEST:
  objective: "build canon including budget"
  source_artifacts:
    - "email_stakeholder_A_2024-07-10.txt (budget: $50k)"
    - "email_stakeholder_B_2024-07-10.txt (budget: $80k)"
  known_context: null
  constraints: []
  desired_output: full_canon_set
  mode: STANDARD
  prior_run: null
```

## Expected behavior
1. Both figures are extracted and recognized as same-tier, same-day sources.
2. Neither figure is picked as "the" budget in FACTS or LOCKED DECISIONS.
3. The conflict is logged in `OPEN_LOOPS.md` (or `DECISION_REGISTER.md` as
   `unresolved`) citing both sources verbatim, with a note that a
   stakeholder decision is needed.
4. `RUN_RESULT.status` may still be `COMPLETE` (a sparse-but-honest canon is
   a valid complete run) — but `RUN_RESULT.unresolved` must list this
   conflict.

## Expected artifacts
- `OPEN_LOOPS.md` — explicit entry with both sources, both figures, marked
  blocking if budget is load-bearing for near-term decisions.
- `PROJECT_CANON.md` — budget appears only as "unresolved, see OPEN_LOOPS.md"
  or is simply absent from FACTS/LOCKED DECISIONS.

## Forbidden behavior
- Must NOT average, guess, or arbitrarily choose one figure as canonical.
- Must NOT drop the conflict silently (both figures missing entirely, no
  trace of the disagreement).
- Must NOT mark `RUN_RESULT.status: COMPLETE` while `unresolved` is empty —
  that would misrepresent the run as having no open issues.

## Pass criteria
- [ ] Neither $50k nor $80k is stated as canonical budget.
- [ ] The conflict is visible in the artifact set with both sources cited.
- [ ] `RUN_RESULT.unresolved` is non-empty and names this conflict.
