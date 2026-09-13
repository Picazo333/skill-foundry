# Reference: target-type classification taxonomy

Used in `SKILL.md` step 2 (classify each fragment — target type).

## Content types (what kind of thing the fragment describes)
- **project** — a bounded body of work with an end state ("build the new
  onboarding flow"). Creates or refers to a project-level entity.
- **process** — a repeatable way of doing something, not a single deliverable
  ("our intake process should always start with a call"). Distinct from a
  project: a process has no completion date, only a definition/procedure.
- **task** — a single, concrete, closeable unit of work ("email the vendor
  about the contract").
- **recurrent** — a task-shaped item that repeats on a stated or implied
  cadence ("check the server logs every Monday"). The defining feature is a
  cadence and a completable action each cycle.
- **supervision** — an ongoing oversight/monitoring responsibility with **no**
  fixed completion and **no** cadence of discrete completable actions ("keep
  an eye on the new hire's ramp-up", "watch how the client reacts to the
  pricing change"). The defining feature is standing attention, not a
  repeating checklist item.
- **doubt** — an open question or reservation the speaker raised but did not
  resolve into a decision or action ("not sure the new pricing is right").
  Never promote a doubt to a decision or a task on the skill's own
  initiative — that's inventing certainty the capture didn't provide.
- **idea** — a possibility floated without commitment ("what if we tried a
  referral program").
- **backlog** — an explicitly deferred item ("put that on the backlog for
  later", or an idea/task the speaker explicitly says not to act on now).

## Operations (what to do to an existing or new item)
- **remove** — explicit instruction to delete/cancel an existing item. Must
  be explicit; "that's not important anymore" is a demotion signal (maybe
  → backlog), not necessarily a removal — check the exact wording before
  choosing `remove` over `move`/`backlog`.
- **rename** — explicit instruction that an existing item's name/label
  changes, with the old and new name both identifiable.
- **move** — explicit instruction that an existing item's parent (which
  project/process it lives under) changes.
- **preserve** — the fragment confirms an item is unchanged (this happens
  when a user reviews and explicitly re-confirms something already
  correct); record it so the confirmation is visible, but it alters nothing.

## The recurrent vs. supervision distinction (quality gate)
This is the single most commonly conflated pair — treat it as a required
check, not a judgment call to skip:

| Signal in the fragment | Classify as |
|---|---|
| A cadence word/phrase ("weekly", "every morning", "each sprint") plus a discrete action that gets marked done each cycle | `recurrent` |
| "keep watching", "keep an eye on", "make sure X doesn't happen", "stay on top of" with no cadence and no single completable action | `supervision` |
| A cadence word but the action described is open-ended monitoring, not a discrete completable step ("check in on morale weekly") | Still ambiguous — cadence alone does not make it `recurrent` if there's no discrete completable action per cycle. If genuinely unclear, use `genuinely-ambiguous` (see the epistemic-status reference) rather than defaulting to either type. |

## Disambiguating type from a bare noun phrase
A short fragment naming only a thing ("the Q3 budget") without a verb
carries no operation and often no clear type. Do not default it to `task`.
Check surrounding fragments for a verb that supplies the operation/type; if
none exists, it is `genuinely-ambiguous`, not a task by default.
