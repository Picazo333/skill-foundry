# Gemini adapter — Rapid Capture & Triage

No native multi-file skill primitive in Gems/consumer Gemini, so this ships
as a portable instruction wrapper, same pattern as `adapters/chatgpt.md`.

## Invocation
Gem system instructions / API system prompt:
> "You are Rapid Capture & Triage. Follow the procedure in the attached
> SKILL.md exactly. Expect a raw capture (voice-note transcript, dictation,
> or fragmented notes) plus optionally a current snapshot/JSON, and produce
> all four required artifacts as separate labeled sections. Never invent a
> priority, owner, or category the capture doesn't state; log genuinely
> ambiguous fragments in AMBIGUITIES.md rather than forcing a
> classification."

Attach `SKILL.md` content in the Gem's knowledge/context files, or in the
system instruction directly if the deployment has no file-attachment step.
If the capture originates from Gemini's own voice transcription (e.g. a
Recorder/Assistant transcript fed in), use that transcript verbatim as the
raw capture — do not let Gemini's own summarization step run on it first,
since that would pre-flatten ambiguity before this skill's classification
pass ever sees it.

## File I/O
The raw capture and optional snapshot are pasted or uploaded per the host
surface (Gem file upload, or inline in the API call). Outputs are returned
as labeled markdown/JSON sections for the user to save; re-supply the
current snapshot on the next `STANDARD`/`UPDATE` run — no persistent memory
is assumed.

## Environment constraints
When called via the API with a large context window, prefer passing the
full current snapshot + raw capture in one call over multi-turn incremental
triage, to avoid the model losing track of which fragments were already
classified.

## Fallback
This entire adapter is the fallback, same reasoning as the ChatGPT adapter.
