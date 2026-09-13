# Cursor adapter — Product Auditor

## Invocation
Add as a `.cursor/rules` entry (or project doc referenced from one) that
points at `skills/03-product-auditor/SKILL.md`: "When asked to audit the
product, produce an implementation plan, or QA delivered work against a
prior plan, follow this file's procedure exactly — including its AUDIT/QA
mode boundary." A Cursor rule can auto-attach based on file-path glob or
manual `@`-mention, per the project's rule configuration.

## File I/O
Reads the repo working tree to reproduce findings (same as `codex.md`):
code, tests, prior `IMPLEMENTATION_PLAN.md`/`REGRESSION_MATRIX.md` for QA
mode. Writes the five required artifacts as real files in the repo.

## Environment constraints
Cursor's inline edit affordances make it easy to slide from "audit" into
"just fix it inline" — the rule must explicitly instruct the agent to
resist accepting an inline-edit request while operating under this skill's
`mode: AUDIT` or `mode: QA`. If the user wants the fix applied, that is a
separate, explicit follow-up action outside this skill (typically after
`ai-resource-router` dispatches the plan item), not a continuation of the
same audit turn.

## Fallback
N/A — repo filesystem access covers this skill's I/O needs directly.
