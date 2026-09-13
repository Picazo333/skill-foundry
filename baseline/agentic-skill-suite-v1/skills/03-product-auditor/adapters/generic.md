# Generic adapter — Product Auditor

For any chat-based LLM interface with file upload or paste support.

## Invocation
Paste or reference `SKILL.md` as a system/instruction message, then supply
the `RUN_REQUEST` fields as a message (objective, source artifacts, mode).
For `mode: QA`, the prior `IMPLEMENTATION_PLAN.md` and `REGRESSION_MATRIX.md`
are required `prior_run` inputs — paste or re-upload them, don't rely on the
interface remembering a prior session.

## File I/O
- **Reading sources:** paste repo excerpts/screenshots/issue lists directly,
  or upload files if supported. There is no live app to click through in a
  pure chat interface, so the objective should include enough
  route-by-route detail (or screenshots) for Phase A inspection to work from
  static evidence.
- **Writing outputs:** the assistant returns the five required artifacts as
  separate, clearly delimited markdown blocks so they can be saved as
  separate files.

## Environment constraints
No filesystem or live-app access assumed — inspection is limited to what's
pasted/uploaded, so `PRODUCT_AUDIT.md` findings lean more heavily on
`suspected` rather than `confirmed` unless the user supplies enough
evidence (code excerpts, screenshots, logs) to reproduce against. No code
execution is possible here regardless, which incidentally makes the
AUDIT-mode "never implement" boundary trivial to hold — there is nothing to
edit. State that limitation rather than treating pasted description alone
as a reproduction.

## Fallback
N/A — this is the baseline all other adapters specialize.
