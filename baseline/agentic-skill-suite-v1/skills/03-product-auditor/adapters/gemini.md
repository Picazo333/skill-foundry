# Gemini adapter — Product Auditor

No native multi-file skill primitive in Gems/consumer Gemini, so this ships
as a portable instruction wrapper, same pattern as `adapters/chatgpt.md`.

## Invocation
Gem system instructions / API system prompt:
> "You are the Product Auditor & Implementation Architect. Follow the
> procedure in the attached SKILL.md exactly. Expect a RUN_REQUEST
> (objective, source artifacts, mode: AUDIT or QA) and produce all five
> required artifacts as separate labeled sections. In AUDIT mode, never
> write or apply product code changes — only specify them as plan items. In
> QA mode, verify against the prior plan and report verdicts; never apply a
> fix."

Attach `SKILL.md` content in the Gem's knowledge/context files, or in the
system instruction directly if the deployment has no file-attachment step.

## File I/O
Source artifacts (screenshots, code excerpts, issue lists, and for QA mode
the prior `IMPLEMENTATION_PLAN.md`/`REGRESSION_MATRIX.md`) are pasted or
uploaded per the host surface. Outputs are returned as labeled markdown
sections for the user to save; re-supply `prior_run` artifacts explicitly on
any `mode: QA` call — no persistent memory is assumed.

## Environment constraints
When called via the API against a live codebase (e.g. through a tool-use
integration with repo access), the same restriction as `codex.md` applies:
read/reproduce only, never write product files, during AUDIT/QA mode.
Without such integration, treat this as the same paste/attach-only
constraint as the ChatGPT adapter.

## Fallback
This entire adapter is the fallback, same reasoning as the ChatGPT adapter.
