# Reference: fragment epistemic status and urgency/priority heuristics

Used in `SKILL.md` step 2 (epistemic status) and step 3 (priority/time
signals).

## Epistemic status categories
- **fact** — a stated state of the world the speaker asserts as already
  true ("the vendor confirmed the contract"). Goes into the preview as
  context/notes, not as an action item.
- **hypothesis** — a belief or guess the speaker is not certain of ("I think
  the launch date might slip"). Record as a `doubt` (see taxonomy reference)
  unless the fragment also contains an explicit action — do not silently
  upgrade a hypothesis into a task ("we might need to push the date" is not
  the same as "push the date").
- **action-item** — an explicit instruction to do, create, change, or remove
  something. This is the only status that produces `create`/`update`/
  `rename`/`move`/`remove` operations in `STRUCTURED_DELTA.json`.
- **genuinely-ambiguous** — resolving the fragment's type, target, or
  operation would require inventing information not present in the
  fragment or its immediate context. This is not a failure state — it is
  the correct classification for input that is actually unclear, and it
  routes straight to `AMBIGUITIES.md`.

## Test for genuinely-ambiguous
Before classifying a fragment as anything else, ask: "Could two careful,
literal readers of this exact wording (with the same snapshot/context)
disagree about its type, target, or operation, with neither reading being
obviously wrong?" If yes, it is `genuinely-ambiguous`. This test exists to
stop the classifier from picking a plausible reading and moving on — a
plausible reading is not the same as a correct one when the wording
supports more than one.

Contradiction is a special case of this: if two fragments in the *same*
capture assert incompatible things about the same item (e.g. "cancel the
onboarding project" ... later "add task X to the onboarding project"),
neither fragment is individually ambiguous, but their combination is —
record it as one ambiguity referencing both fragments, not as two separate,
silently-resolved operations.

## Priority/time-signal detection
Scan each `action-item` fragment for:
- **Explicit priority language:** "urgent", "top priority", "critical",
  "whenever", "low priority", "not important right now".
- **Explicit time signals:** absolute ("by Friday", "March 3rd") or relative
  ("after the launch", "before the client call", "today").
- **Ordering language:** "first... then...", "also", "oh and one more
  thing" — these affect relative order, not priority tier.

## What counts as an inferred (forbidden) priority
Do not assign a priority tier or due date because:
- the item "sounds important" based on general judgment,
- the item was mentioned first or last in the capture (capture order is
  preserved separately from priority — see below),
- a similar existing snapshot item has a priority (a match does not import
  the matched item's priority unless the fragment also restates it).

## Capture order vs. priority
When no explicit priority/time signal exists for an item, preserve its
position in the sequence the fragments were spoken/written (`capture_order`
in `STRUCTURED_DELTA.json`). Capture order is a neutral fact about the
input, not a priority judgment — never present it to the user as if it were
one (e.g. do not label it "Priority 1, 2, 3..."; label it order of mention).
