# Eval Case — Task reprioritization with renames

## Scenario
A user reviews an existing task list out loud, renaming one task, reordering
priority on another, and confirming a third is unchanged. This simulates
`mode: STANDARD` snapshot matching, where duplicate/rename detection and
"preserve unmentioned fields" are the core behaviors under test.

## Input
```yaml
RUN_REQUEST:
  objective: "reconcile my task list after this review pass"
  source_artifacts:
    - |
      raw_capture.txt: "rename 'draft blog post' to 'draft launch blog
      post' and bump it to top priority. the 'update pricing page' task
      is still fine as is no changes there. also new task reach out to
      the beta testers for feedback"
    - |
      snapshot.json: tasks: [
        {id: "t1", name: "draft blog post", priority: "medium", project: "Launch"},
        {id: "t2", name: "update pricing page", priority: "low", project: "Launch", due: "2026-09-20"},
        {id: "t3", name: "schedule launch tweet", priority: "medium", project: "Launch"}
      ]
  known_context: null
  constraints: []
  desired_output: preview_and_delta
  mode: STANDARD
  prior_run: "snapshot.json"
```

## Expected behavior
1. "draft blog post" matches existing `t1` by name (step 4); the operation
   is `rename` + priority `update`, not a `create` of a new task.
2. `t2`'s `due: "2026-09-20"` field is untouched — the fragment ("still fine
   as is no changes there") is classified `preserve`, and no field on `t2`
   is altered (step 5).
3. `t3` ("schedule launch tweet") is not mentioned anywhere in the capture
   and must remain fully unchanged and absent from `STRUCTURED_DELTA.json`
   operations entirely — it is not implicitly deprioritized just because
   two sibling tasks were discussed.
4. "reach out to the beta testers for feedback" has no match in the
   snapshot and is a `create`, `target_id: null`.
5. Step 8 consistency check: 3 preview-line-backed operations (rename+
   update on t1, preserve on t2, create for beta testers) all appear
   identically in both `CAPTURE_PREVIEW.md` and `STRUCTURED_DELTA.json`.

## Expected artifacts
- `CAPTURE_PREVIEW.md` — a `Renames` line for t1 showing old/new name and
  new priority; a `Preserved` line for t2; a `Tasks` line for the new beta
  testers task; no line at all for t3.
- `STRUCTURED_DELTA.json` — `previous_fields.name` set for the t1 rename;
  `t2`'s `due` field does not appear anywhere in the delta (nothing to
  patch); no operation references `t3`.
- `AMBIGUITIES.md` — empty or states so explicitly; this scenario has no
  genuine ambiguity.
- `APPLY_INSTRUCTIONS.md` — ordered application: rename/update t1 before
  anything depending on its new name, create the beta-tester task.

## Forbidden behavior
- Must NOT create a new task instead of matching t1 by name.
- Must NOT alter `t2.due` or any other unmentioned `t2` field.
- Must NOT touch, reorder, or mention `t3` in the delta.
- Must NOT infer that t1's "top priority" bump implies t3 should be
  deprioritized (nothing in the capture says that).

## Pass criteria
- [ ] t1 operation is `rename`+`update` against `target_id: "t1"`, not a
      new create.
- [ ] t2's `due` field is absent from every operation in the delta.
- [ ] t3 does not appear anywhere in `CAPTURE_PREVIEW.md` or
      `STRUCTURED_DELTA.json`.
- [ ] Delta operation count matches preview line count exactly.
