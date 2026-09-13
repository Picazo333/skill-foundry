# Eval Case — Multi-rename project

## Scenario
A project (like the "Regula" example) went through 3 names and 2 pivots
across a year of chats, with one signed-off brief locking the final
direction. Tests whether the skill correctly identifies the current
canonical name/direction and files the earlier ones as deprecated rather
than as still-live alternatives.

## Input
```yaml
RUN_REQUEST:
  objective: "rebuild canon from scratch"
  source_artifacts:
    - initial pitch chat (name A, angle A)
    - pivot note (name B, angle B)
    - signed brief (name C, angle C, APPROVED, most recent)
  known_context: null
  constraints: []
  desired_output: full_canon_set
  mode: STANDARD
  prior_run: null
```

## Expected behavior
1. Source inventory ranks the signed brief above the chats (authority),
   and additionally notes it is the most recent.
2. FACTS/LOCKED DECISIONS reflect name C / angle C only.
3. Names A and B and their angles are written to `DEPRECATED_REGISTER.md`
   with what superseded them, not silently dropped.
4. No section presents name A or B as current.

## Expected artifacts
- `PROJECT_CANON.md` — LOCKED DECISIONS names only "C" as current name.
- `DEPRECATED_REGISTER.md` — contains both A and B with supersession reason.
- `DECISION_REGISTER.md` — shows the naming decision history (A→B→C) with
  the final one marked `locked`.

## Forbidden behavior
- Must not list name A or B in FACTS or LOCKED DECISIONS as current.
- Must not omit the deprecated names entirely (losing history is a failure,
  not a simplification).

## Pass criteria
- [ ] Current name/angle in canon matches the signed brief only.
- [ ] Both prior names appear in `DEPRECATED_REGISTER.md` with reasons.
- [ ] `DECISION_REGISTER.md` shows the full naming decision chain.
