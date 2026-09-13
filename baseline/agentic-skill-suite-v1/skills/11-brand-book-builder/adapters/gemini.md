# Gemini adapter — Brand Book Builder

No native multi-file skill primitive in Gems/consumer Gemini, so this ships
as a portable instruction wrapper, same pattern as `adapters/chatgpt.md`.

## Invocation
Gem system instructions / API system prompt:
> "You are the Brand Book Builder skill. Follow the procedure in the
> attached SKILL.md exactly. Expect a RUN_REQUEST (objective, source
> artifacts including all 6 required canon artifacts, mode). Run the
> sufficiency gate first; if any required artifact is missing, return
> BLOCKED and name it and its owning skill. Run the verbal/visual coherence
> check (step 6) using the attached checklist reference and record every gap
> found — never resolve a mismatch by silently editing either source. Every
> rule in the compiled book must trace to one of the 6 source artifacts."

Attach `SKILL.md` and `references/verbal-visual-coherence-checklist.md`
content in the Gem's knowledge/context files, or in the system instruction
directly if the deployment has no file-attachment step.

## File I/O
The 6 canon artifacts and optional `BRAND_STRATEGY.md` are pasted or
uploaded per the host surface. Outputs are returned as labeled markdown
sections for the user to save; re-supply the current canon and the prior
`BRAND_BOOK.md` on the next `UPDATE` run — no persistent memory is assumed.

## Environment constraints
When called via the API with a large context window, prefer passing all 6
canon artifacts plus `BRAND_STRATEGY.md` in one call over multi-turn
incremental compilation, so the coherence check (step 6) sees the full
picture at once rather than comparing artifacts pasted across separate
turns.

## Fallback
This entire adapter is the fallback, same reasoning as the ChatGPT adapter.
