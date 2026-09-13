# Apply Instructions

> How to apply `STRUCTURED_DELTA.json` to the real target system, and what
> to do about anything left open in `AMBIGUITIES.md`.

**Source capture:** <path/description of the raw capture>
**Run date:** <date>

## 1. Apply now (non-blocking, unambiguous operations)
Apply every operation in `STRUCTURED_DELTA.json` whose `target_id`/fields
are not referenced by any entry in `AMBIGUITIES.md`. Suggested order:
1. `remove` operations (explicit removals first, so nothing downstream
   references a removed item).
2. `rename` / `move` operations (so later operations can reference items by
   their new identity).
3. `create` operations (new projects/processes/tasks/recurrent/supervision/
   doubt/idea/backlog items).
4. `update` operations on existing items.
5. `preserve` operations need no action — they confirm no change.

## 2. Hold (blocking ambiguities)
Do not apply any operation tied to a `Blocking?: yes` entry in
`AMBIGUITIES.md` until it is resolved. List them here explicitly:
- <ambiguity label> — holds operation(s): <operation id(s)/description>

## 3. Non-blocking ambiguities
These can be applied provisionally, or the whole delta can proceed while
these stay open for follow-up — call out which was chosen:
- <ambiguity label> — <applied provisionally as X / left entirely open>

## 4. Resolving and re-running
Once a human answers the open questions in `AMBIGUITIES.md`:
1. Update `known_context` / `prior_run` with the resolution.
2. Re-run `rapid-capture-triage` in `mode: UPDATE` against the current
   snapshot plus the resolution, rather than re-triaging the original raw
   capture from scratch.
3. Confirm the newly-applied operations no longer appear in
   `AMBIGUITIES.md`.

## 5. Recommended next skill
<e.g. "canonical-context-builder — this capture touched project-level
facts/decisions, fold CAPTURE_PREVIEW.md + STRUCTURED_DELTA.json into
canon." or "none — task-level only, delta is self-contained.">
