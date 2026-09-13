# Gemini adapter — Canonical Context Builder

No native multi-file skill primitive in Gems/consumer Gemini, so this ships
as a portable instruction wrapper, same pattern as `adapters/chatgpt.md`.

## Invocation
Gem system instructions / API system prompt:
> "You are the Canonical Context Builder. Follow the procedure in the
> attached SKILL.md exactly. Expect a RUN_REQUEST (objective, source
> artifacts, mode) and produce all five required artifacts as separate
> labeled sections. Never invent facts; log unresolved conflicts in
> OPEN_LOOPS.md rather than resolving them."

Attach `SKILL.md` content in the Gem's knowledge/context files, or in the
system instruction directly if the deployment has no file-attachment step.

## File I/O
Source artifacts are pasted or uploaded per the host surface (Gem file
upload, or inline in the API call). Outputs are returned as labeled markdown
sections for the user to save; re-supply prior canon on the next `UPDATE`
run — no persistent memory is assumed.

## Environment constraints
When called via the API with a large context window, prefer passing the
full prior canon + new sources in one call over multi-turn incremental
building, to avoid drift across turns.

## Fallback
This entire adapter is the fallback, same reasoning as the ChatGPT adapter.
