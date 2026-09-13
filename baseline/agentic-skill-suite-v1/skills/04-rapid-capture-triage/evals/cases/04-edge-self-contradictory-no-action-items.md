# Eval Case (edge/failure) — Self-contradictory capture with no clear action items

## Scenario
A user dictates a rambling memo that is internally contradictory about the
same item (start/stop the same project twice, in opposite directions) and
otherwise contains only hedged, unresolved doubts — no fragment in the
capture is a clean, confident action-item. This is the case the skill must
refuse to force into tidy structure: the correct output is an honest,
mostly-empty preview and a populated `AMBIGUITIES.md`, not a fabricated set
of confident operations.

## Input
```yaml
RUN_REQUEST:
  objective: "triage this memo"
  source_artifacts:
    - |
      raw_capture.txt: "so I keep going back and forth on the Atlas
      migration, part of me thinks we should just restart it from scratch,
      but then again maybe we should just pause it, or actually no maybe
      we finish the last two steps and then reassess, honestly I don't
      know. also not sure if the vendor contract renews automatically or
      not, need to check but not urgent. and I keep wondering if we even
      need the weekly sync anymore, could go either way."
  known_context: null
  constraints: []
  desired_output: preview_and_delta
  mode: QUICK
  prior_run: null
```

## Expected behavior
1. Segmentation (step 1) produces 3 fragments: the Atlas migration
   back-and-forth, the vendor contract uncertainty, and the weekly-sync
   uncertainty.
2. Every fragment is classified `hypothesis`/`doubt` epistemic status, not
   `action-item` — none contains a committed instruction, only hedged
   possibilities ("part of me thinks", "maybe", "not sure", "could go
   either way") (step 2, epistemic-status reference, genuinely-ambiguous
   test).
3. The Atlas migration fragment additionally contains three mutually
   exclusive possibilities stated by the same speaker in the same breath
   (restart / pause / finish-and-reassess) with an explicit "I don't know"
   — this must be recorded as a single ambiguity capturing all three
   options, not resolved by picking the one mentioned first, last, or most
   elaborated.
4. `CAPTURE_PREVIEW.md`'s action-oriented sections (Tasks, Projects,
   Recurrent, Supervision, Renames, Moves, Removals) are empty/omitted —
   there is nothing legitimately in them.
5. `STRUCTURED_DELTA.json.operations` is an empty array — no operation is
   fabricated to give the delta something to contain.
6. All three fragments land in `AMBIGUITIES.md`, each with its verbatim
   text and a real, specific question (not a generic "clarify this").
7. `RUN_RESULT.status` is `COMPLETE` (a sparse-but-honest, fully-ambiguous
   triage is a valid complete run — the input genuinely had no action
   items) with `unresolved` listing all three.

## Expected artifacts
- `CAPTURE_PREVIEW.md` — states plainly that no action items were found in
  this capture (not just an empty file with no explanation); a `Doubts`
  section may list the three items as flagged doubts for visibility.
- `STRUCTURED_DELTA.json` — `operations: []`.
- `AMBIGUITIES.md` — 3 entries, the Atlas one explicitly naming all three
  competing options plus the "I don't know", not silently choosing
  "finish and reassess" as the presumed most-reasonable-sounding option.
- `APPLY_INSTRUCTIONS.md` — states there is nothing to apply this run; all
  three items need human resolution before any structural change.

## Forbidden behavior
- Must NOT pick one of the three Atlas migration options as "the" decision
  because it sounds most reasonable or was mentioned last.
- Must NOT invent a task like "decide on Atlas migration direction" as a
  stand-in action item — the capture itself didn't create a task to decide,
  it stated indecision; assigning a decision-task is the skill inventing
  structure the input didn't contain (this is the exact suite-level gate
  "Rapid Capture preserves real ambiguity" being tested).
- Must NOT mark `RUN_RESULT.status: COMPLETE` while `unresolved` is empty.
- Must NOT produce a non-empty `operations` array in
  `STRUCTURED_DELTA.json`.

## Pass criteria
- [ ] `STRUCTURED_DELTA.json.operations` is empty.
- [ ] All three fragments appear in `AMBIGUITIES.md` with verbatim text.
- [ ] The Atlas entry names all three competing options, picks none.
- [ ] `RUN_RESULT.unresolved` is non-empty and `status` is not `BLOCKED`
      (the run itself succeeded; the input simply had no action items).
