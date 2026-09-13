# Handoff package — <target skill-id>

Placed at `HANDOFF_PACKAGES/<skill-id>/`. Contains exactly what the target
skill's `manifest.json.minimum_inputs` + `optional_inputs` need — canonical
artifacts, the relevant decisions from `BRAND_WORKFLOW_STATE.md`, any
unresolved items the target skill should know about, and constraints.

Never include the full workflow state or unrelated skills' artifacts — see
`ARCHITECTURE.md`'s handoff rule: pass artifacts + decisions + unresolved +
constraints + next-skill recommendation, not the whole project.

## Contents of this package
- `<artifact>.md` / `.json` — copied or referenced from its owning skill's output.
- `DECISIONS.md` — the subset of `BRAND_WORKFLOW_STATE.md` decisions relevant to this run.
- `CONSTRAINTS.md` — constraints carried from the original RUN_REQUEST.
