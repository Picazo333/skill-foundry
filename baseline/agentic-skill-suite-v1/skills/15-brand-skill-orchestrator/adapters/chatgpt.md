# ChatGPT adapter — Brand Skill Orchestrator

No native multi-file skill primitive or sub-agent dispatch, so this ships as
a portable instruction wrapper that produces a recommendation, not an
auto-executed routing.

## Invocation
Custom GPT / Project instructions field:
> "You are the Brand Skill Orchestrator. Follow the procedure in the
> attached SKILL.md exactly, using the artifact/handoff map in
> `routed-skill-contracts.md` and the stage rules in
> `stage-detection-rules.md`. You do not perform any routed skill's work
> yourself — you only determine and report the single next skill to run,
> with its RUN_REQUEST, and update BRAND_WORKFLOW_STATE.md."

Attach `SKILL.md` and both reference docs as Custom GPT knowledge files.

## File I/O
The user reports current artifact inventory each run (attached files or
pasted summary). The orchestrator returns `BRAND_WORKFLOW_STATE.md`,
`NEXT_SKILL_RUN.json`, and handoff package contents as labeled sections;
the user manually runs the recommended skill in a separate Custom GPT/chat
and brings its output back on the next orchestrator turn.

## Environment constraints
No persistent memory across sessions — re-attach the latest
`BRAND_WORKFLOW_STATE.md` at the start of every `RESUME` run.

## Fallback
This entire adapter is the fallback: no native orchestration/dispatch
primitive exists on this platform.
