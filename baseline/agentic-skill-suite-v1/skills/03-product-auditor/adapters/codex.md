# Codex adapter — Product Auditor

## Invocation
Reference this skill from the repo's agent-instructions file (e.g.
`AGENTS.md`) as: "For a product audit or QA pass, read
`skills/03-product-auditor/SKILL.md` and follow it exactly, including its
mode boundary." The coding agent loads `SKILL.md` on demand rather than
keeping it permanently in context.

## File I/O
Reads the repo working tree to reproduce findings (run tests, inspect code,
check data shapes) and reads `source_artifacts`/`prior_run` (screenshots,
issue lists, prior `IMPLEMENTATION_PLAN.md`/`REGRESSION_MATRIX.md`). Writes
the five required artifacts as real files (default: repo root, or wherever
the repo already keeps audit docs).

## Environment constraints
This is a coding agent with full write access to the repo — that access
must be used only for reproduction (running tests, reading code) during
`mode: AUDIT`/`mode: QA`, never for editing product source, config, or data
files. If the invoking instruction or a user message asks the agent to also
apply the fix in the same run, decline and produce the plan item instead,
per `SKILL.md`'s failure modes. A separate, later invocation (via
`ai-resource-router`, outside this skill) is the correct place to apply
changes.

## Fallback
N/A — repo filesystem access covers this skill's I/O needs directly.
