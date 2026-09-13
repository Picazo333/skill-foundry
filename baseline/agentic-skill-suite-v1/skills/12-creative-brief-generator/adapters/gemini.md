# Gemini adapter — Creative Brief Generator

No native multi-file skill primitive in Gems/consumer Gemini, so this ships
as a portable instruction wrapper, same pattern as `adapters/chatgpt.md`.

## Invocation
Gem system instructions / API system prompt:
> "You are the Creative Brief Generator. Follow the procedure in the
> attached SKILL.md exactly. Expect a RUN_REQUEST (objective, canon source
> artifacts, known_context, constraints, mode) and produce all three
> required artifacts as separate labeled sections. Go BLOCKED if canon
> doesn't cover the deliverable rather than inventing brand rules; flag any
> conflict between the request and locked canon explicitly rather than
> silently complying or silently dropping it."

Attach `SKILL.md` content (and `templates/`/`references/`) in the Gem's
knowledge/context files, or in the system instruction directly if the
deployment has no file-attachment step.

## File I/O
Canon artifacts are pasted or uploaded per the host surface (Gem file
upload, or inline in the API call). Outputs are returned as labeled markdown
sections for the user to save; re-supply the prior brief set and current
canon on the next `UPDATE` run — no persistent memory is assumed.

## Environment constraints
When called via the API with a large context window, prefer passing the
full relevant canon + deliverable request in one call over multi-turn
incremental briefing, to avoid the message/CTA drifting across turns.

## Fallback
This entire adapter is the fallback, same reasoning as the ChatGPT adapter.
