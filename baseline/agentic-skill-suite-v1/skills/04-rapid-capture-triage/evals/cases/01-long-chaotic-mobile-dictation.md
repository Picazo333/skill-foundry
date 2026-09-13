# Eval Case — Long chaotic mobile dictation

## Scenario
A user dictates a long, unpunctuated stream-of-consciousness voice memo on
their phone covering unrelated projects, a mix of recurring and supervisory
items, and one idea explicitly deferred to backlog. This simulates the
skill's primary use case: Notes-speed capture with no prior formatting.

## Input
```yaml
RUN_REQUEST:
  objective: "triage this voice memo into today's backlog/task list"
  source_artifacts:
    - |
      raw_capture.txt: "need to call the printer about the flyer order
      also remember to check backups every friday that's a recurring thing
      and separately just keep watching the new vendor invoices for
      anything weird no fixed schedule on that one just stay alert also
      idea for later maybe we do a summer promo put that on backlog not
      now also task write the Q3 summary doc high priority needed by
      Wednesday"
  known_context: null
  constraints: []
  desired_output: preview_and_delta
  mode: QUICK
  prior_run: null
```

## Expected behavior
1. The capture is segmented into 5 atomic fragments without paraphrasing
   before classification (step 1).
2. "check backups every friday" is classified `recurrent` (cadence +
   discrete completable action); "keep watching the new vendor invoices...
   no fixed schedule... stay alert" is classified `supervision` (no cadence,
   open-ended monitoring) — the two are not conflated (step 2, taxonomy
   reference).
3. "maybe we do a summer promo" is classified `idea` and explicitly routed
   to `backlog` per the fragment's own instruction ("put that on backlog
   not now"), not treated as an active task.
4. "write the Q3 summary doc" carries an explicit priority ("high
   priority") and explicit due date ("Wednesday") — both captured, not
   invented (step 3).
5. "call the printer about the flyer order" carries no priority/time signal
   and is preserved in capture order rather than assigned an inferred
   priority.
6. Since `mode: QUICK` and no snapshot was supplied, no duplicate/rename
   matching is attempted (step 4 is skipped by design, not silently
   dropped) — `STRUCTURED_DELTA.json` operations all have `target_id: null`.

## Expected artifacts
- `CAPTURE_PREVIEW.md` — separate `Recurrent items` and `Supervision items`
  sections, each with exactly one entry; a `Backlog` section with the
  summer-promo idea; a `Tasks` section with both the flyer call and the Q3
  summary doc, the latter showing explicit priority/due date and the former
  showing no priority field (not a placeholder or default value).
- `STRUCTURED_DELTA.json` — 5 `create` operations, all `target_id: null`
  (no snapshot to match against), each with `source_fragment` set to the
  relevant verbatim text.
- `AMBIGUITIES.md` — may be empty or near-empty; if empty, the file must
  say so explicitly.
- `APPLY_INSTRUCTIONS.md` — states all 5 operations can apply immediately
  (none held on ambiguity).

## Forbidden behavior
- Must NOT classify the vendor-invoice supervision item as `recurrent`.
- Must NOT assign a priority tier or due date to the printer call.
- Must NOT create the summer-promo idea as an active/unscoped task instead
  of `backlog`.
- Must NOT attempt snapshot matching in `mode: QUICK`.

## Pass criteria
- [ ] Recurrent and supervision items are in separate sections with correct
      classification.
- [ ] The Q3 summary doc shows the stated priority/due date; the printer
      call shows none.
- [ ] The summer-promo idea lands in Backlog, not Tasks.
- [ ] `STRUCTURED_DELTA.json` operation count and preview line count match
      (5 and 5).
