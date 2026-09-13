# Eval Case

## Scenario
One or two sentences: what real situation this simulates, and why it matters
for this skill specifically (not a generic smoke test).

## Input
The `RUN_REQUEST` (or equivalent minimal input) exactly as it would be given
to the skill, including any source artifacts referenced.

## Expected behavior
The procedure steps that must actually happen, in order, for this input —
specific enough that a reviewer can check them off against a real run.

## Expected artifacts
Which required output artifacts must exist, and the specific content
properties they must have for this scenario (not just "artifact exists").

## Forbidden behavior
Concrete things the skill must NOT do on this input (e.g. invent a fact,
skip a required output, merge with another skill's job, silently drop an
unresolved contradiction).

## Pass criteria
A short checklist. All items must hold for the case to pass.
- [ ] ...
- [ ] ...
