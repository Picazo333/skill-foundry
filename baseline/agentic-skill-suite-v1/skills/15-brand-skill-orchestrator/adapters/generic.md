# Generic adapter — Brand Skill Orchestrator

For any chat-based LLM interface with file upload or paste support.

## Invocation
Paste/reference `SKILL.md` (plus `references/routed-skill-contracts.md` and
`references/stage-detection-rules.md`) as a system/instruction message. On
each run, supply the current artifact inventory (what exists, what's
approved) as the `RUN_REQUEST`. If no persistent memory, re-supply
`BRAND_WORKFLOW_STATE.md` from the prior run on every `RESUME` call.

## File I/O
Source artifacts are referenced by name/summary (not necessarily full
content — this skill reads existence/version/approval state, not full
artifact bodies, except when resolving a named conflict). Outputs
(`BRAND_WORKFLOW_STATE.md`, `NEXT_SKILL_RUN.json`, handoff package contents,
`COMPLETION_REPORT.md`) are returned as separate labeled blocks for the user
to save and carry into the next routed skill's own session.

## Environment constraints
This adapter cannot itself invoke other skills — the user manually runs the
recommended `next_skill` in a separate session/tab and brings its output
back on the next orchestrator run.

## Fallback
N/A — baseline all other adapters specialize.
