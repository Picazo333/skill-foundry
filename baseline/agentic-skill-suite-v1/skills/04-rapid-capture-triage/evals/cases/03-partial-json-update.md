# Eval Case — Partial JSON update

## Scenario
A user has an existing JSON project/task state and gives a short capture
with two unrelated changes. This simulates `mode: UPDATE`: the skill must
patch only what's mentioned, scoped tightly against the supplied prior
state, and produce a delta that is a true subset patch rather than a
restatement of the whole snapshot.

## Input
```yaml
RUN_REQUEST:
  objective: "apply this update to the current project state"
  source_artifacts:
    - |
      raw_capture.txt: "move the 'api rate limiting' task from Backend
      project to Platform project. also the 'onboarding survey' process,
      mark it done, we're not using it anymore, remove it."
  known_context: null
  constraints: []
  desired_output: preview_and_delta
  mode: UPDATE
  prior_run: |
    {
      "projects": ["Backend", "Platform", "Growth"],
      "tasks": [
        {"id": "tk1", "name": "api rate limiting", "project": "Backend", "priority": "medium"},
        {"id": "tk2", "name": "cache invalidation", "project": "Backend", "priority": "high"}
      ],
      "processes": [
        {"id": "pr1", "name": "onboarding survey", "project": "Growth"},
        {"id": "pr2", "name": "weekly retro", "project": "Growth"}
      ]
    }
```

## Expected behavior
1. `prior_run` (the supplied JSON) is treated as the base snapshot for
   matching per step 4 — required because `mode: UPDATE`.
2. "move the 'api rate limiting' task" matches `tk1` by name; produces a
   `move` operation with `previous_fields.target_path: "Backend"` and new
   `target_path: "Platform"`; `tk1.priority` is left untouched.
3. "the 'onboarding survey' process... remove it" matches `pr1`; produces a
   `remove` operation. Note: the fragment says both "mark it done" and
   "remove it" — treat this as one explicit removal instruction (the
   "mark it done" phrasing is the user's colloquial framing of retiring the
   process, and "remove it" is the unambiguous explicit instruction that
   governs), not two conflicting operations. If this reading feels forced,
   the correct fallback is to flag it in `AMBIGUITIES.md` rather than
   silently picking `remove` — a run may reasonably do either, but must not
   silently apply both an "update to done" and a "remove" as if they don't
   conflict.
4. `tk2` (cache invalidation) and `pr2` (weekly retro) are not mentioned and
   must not appear in the delta at all.
5. `STRUCTURED_DELTA.json.base_snapshot` references the supplied prior
   state; `mode: "UPDATE"`.

## Expected artifacts
- `CAPTURE_PREVIEW.md` — a `Moves` line for tk1, a `Removals` line for pr1
  (or, if the ambiguity fallback was taken, an entry noting the
  done-vs-remove tension with the operation held per `AMBIGUITIES.md`).
- `STRUCTURED_DELTA.json` — exactly the tk1 move and the pr1 disposition;
  no entries for tk2 or pr2; `base_snapshot` populated.
- `AMBIGUITIES.md` — either explicitly empty, or containing the
  done-vs-remove tension if that fallback was taken — both are valid runs,
  but the choice must be stated and consistent with `APPLY_INSTRUCTIONS.md`.
- `APPLY_INSTRUCTIONS.md` — correctly reflects whichever path was taken for
  pr1.

## Forbidden behavior
- Must NOT restate tk2 or pr2 as `preserve` operations padding out the
  delta — `mode: UPDATE` scopes to what changed, not a full re-emission of
  the snapshot.
- Must NOT silently apply both "mark done" and "remove" as independent,
  unflagged operations on pr1.
- Must NOT drop `tk1.priority` from the record — it must remain implicitly
  intact (absent from the patch, not zeroed out).

## Pass criteria
- [ ] Delta contains operations only for tk1 and pr1 — nothing for tk2/pr2.
- [ ] tk1's `priority` field is not touched anywhere in the delta.
- [ ] The pr1 done/remove tension is either cleanly resolved with a stated
      rationale, or explicitly flagged in `AMBIGUITIES.md` — not silently
      double-applied.
- [ ] `base_snapshot` and `mode: UPDATE` are correctly recorded in the delta.
