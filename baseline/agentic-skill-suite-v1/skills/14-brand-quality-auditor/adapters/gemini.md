# Gemini adapter — Brand Quality Auditor

No native multi-file skill primitive in Gems/consumer Gemini, so this
ships as a portable instruction wrapper, same pattern as
`adapters/chatgpt.md`.

## Invocation
Gem system instructions / API system prompt:
> "You are the Brand Quality Auditor. Follow the procedure in the
> attached SKILL.md exactly, including the canon gate: if explicit,
> approved brand canon is not supplied for the dimension you're asked to
> check, return `status: BLOCKED` and name what's missing rather than
> auditing against general taste or best practice. Expect a RUN_REQUEST
> (artifact under audit, canon, objective, mode) and produce all three
> required artifacts as separate labeled sections, each finding citing its
> specific canon rule."

Attach `SKILL.md` and `references/ai-slop-checklist.md` in the Gem's
knowledge/context files, or in the system instruction directly if the
deployment has no file-attachment step.

## File I/O
The artifact under audit and canon are pasted or uploaded per the host
surface (Gem file upload, or inline in the API call). Outputs are
returned as labeled markdown sections for the user to save; re-supply
canon plus the prior audit on the next `UPDATE` run — no persistent
memory is assumed.

## Environment constraints
When called via the API with a large context window, prefer passing the
full canon + the artifact under audit in one call over multi-turn
incremental review, so a later turn doesn't drift away from the
originally supplied canon.

## Fallback
This entire adapter is the fallback, same reasoning as the ChatGPT
adapter.
