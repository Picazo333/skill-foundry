# Worked example — chaotic morning voice-memo transcript

## Input (abridged)
```yaml
RUN_REQUEST:
  objective: "triage this morning's voice memo into the current task/project snapshot"
  source_artifacts:
    - |
      raw_capture.txt (voice-note transcript, auto-dictated, punctuation-light):
      "ok so first thing rename the client portal project to just Portal
      everyone keeps typing the long name. also I need to email Dana about
      the renewal today it's kind of urgent. um the weekly log review thing
      move that under Portal now instead of under Ops. I think we might be
      overcommitted on the Q4 roadmap not sure yet. also add a task check
      the SSL cert expiry, that's a recurring one, monthly. keep an eye on
      how the new support hire is doing generally. oh and kill the
      'legacy exporter' task we're not doing that. one more idea, what if
      we did a customer referral thing sometime, put it on the backlog.
      also cancel the onboarding project we're done with that -- wait
      actually no, add a task to onboarding project to update the welcome
      email, ugh ignore that first part"
    - "snapshot.json (current state: projects [Client Portal Project, Ops,
      Onboarding], tasks under Ops [weekly log review (recurrent, weekly),
      legacy exporter], tasks under Onboarding [none])"
  known_context: null
  constraints: []
  desired_output: preview_and_delta
  mode: STANDARD
  prior_run: "snapshot.json"
```

## Output (abridged)

**CAPTURE_PREVIEW.md** (excerpt):
```
## Renames
- **Client Portal Project → Portal** — source: "rename the client portal
  project to just Portal"

## Tasks
- **Email Dana about the renewal** (project: unassigned) — priority/time
  signal: urgent, due today — source: "email Dana about the renewal today
  it's kind of urgent"

## Moves
- **weekly log review**: Ops → Portal — source: "the weekly log review
  thing move that under Portal now instead of under Ops"

## Recurrent items
- **Check the SSL cert expiry** — cadence: monthly — source: "add a task
  check the SSL cert expiry, that's a recurring one, monthly"

## Supervision items
- **New support hire ramp-up** — ongoing oversight, no fixed completion —
  source: "keep an eye on how the new support hire is doing generally"

## Removals
- **legacy exporter** (task, under Ops) — source: "kill the 'legacy
  exporter' task we're not doing that"

## Backlog
- **Customer referral program (idea)** — source: "what if we did a customer
  referral thing sometime, put it on the backlog"
```

**AMBIGUITIES.md** (excerpt):
```
## Onboarding project: cancel, then self-corrected
- Verbatim fragment(s): "cancel the onboarding project we're done with that
  -- wait actually no, add a task to onboarding project to update the
  welcome email, ugh ignore that first part"
- Why it's ambiguous: the speaker explicitly retracts the cancellation
  ("ignore that first part"), so the only action-item content is the new
  task -- but leaving the cancellation fragment out entirely would hide
  that the project's status was raised as a question at all.
- What would resolve it: nothing further needed to apply the task; flagged
  only so the retracted cancellation isn't silently lost from the record.
- Blocking?: no -- the "add task: update welcome email" operation proceeds;
  logged here for traceability only, not because the correct action is
  actually unclear.

## Q4 roadmap overcommitment
- Verbatim fragment(s): "I think we might be overcommitted on the Q4
  roadmap not sure yet"
- Why it's ambiguous: explicit hypothesis/doubt, not an action-item -- no
  task, project change, or decision is stated.
- What would resolve it: a follow-up decision on whether to rebalance the
  Q4 roadmap; not this skill's call to make.
- Blocking?: no -- recorded as a doubt, nothing to apply.
```

**STRUCTURED_DELTA.json** (excerpt):
```json
{
  "operations": [
    {"op": "rename", "type": "project", "target_id": "client-portal-project", "fields": {"name": "Portal"}, "previous_fields": {"name": "Client Portal Project"}, "source_fragment": "rename the client portal project to just Portal", "confidence": "explicit"},
    {"op": "create", "type": "task", "target_id": null, "fields": {"name": "Email Dana about the renewal", "priority": "urgent", "due": "today"}, "source_fragment": "email Dana about the renewal today it's kind of urgent", "confidence": "explicit"},
    {"op": "move", "type": "recurrent", "target_id": "weekly-log-review", "target_path": "Portal", "previous_fields": {"target_path": "Ops"}, "source_fragment": "the weekly log review thing move that under Portal now instead of under Ops", "confidence": "explicit"},
    {"op": "create", "type": "recurrent", "target_id": null, "fields": {"name": "Check the SSL cert expiry", "cadence": "monthly"}, "source_fragment": "add a task check the SSL cert expiry, that's a recurring one, monthly", "confidence": "explicit"},
    {"op": "create", "type": "supervision", "target_id": null, "fields": {"name": "New support hire ramp-up"}, "source_fragment": "keep an eye on how the new support hire is doing generally", "confidence": "explicit"},
    {"op": "remove", "type": "task", "target_id": "legacy-exporter", "source_fragment": "kill the 'legacy exporter' task we're not doing that", "confidence": "explicit"},
    {"op": "create", "type": "backlog", "target_id": null, "fields": {"name": "Customer referral program"}, "source_fragment": "what if we did a customer referral thing sometime, put it on the backlog", "confidence": "explicit"},
    {"op": "create", "type": "task", "target_id": null, "target_path": "Onboarding", "fields": {"name": "Update the welcome email"}, "source_fragment": "add a task to onboarding project to update the welcome email", "confidence": "explicit"}
  ],
  "unresolved_ref": "AMBIGUITIES.md"
}
```

Note what did NOT happen: the onboarding project was **not** cancelled
(the retraction was honored), overcommitment on Q4 was **not** turned into
a task or decision, and "keep an eye on the new support hire" was **not**
folded into a recurring task just because a cadence-ish phrase ("weekly log
review") appeared nearby in the transcript — each fragment was classified
on its own wording per `references/classification-taxonomy.md`.
