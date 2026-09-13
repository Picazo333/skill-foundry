# ChatGPT adapter — Rapid Capture & Triage

No native multi-file skill primitive, so this ships as a portable
instruction wrapper.

## Invocation
Custom GPT / Project instructions field:
> "You are Rapid Capture & Triage. Follow the procedure in the attached
> `SKILL.md` exactly. On each run, expect a raw capture (voice-note
> transcript, dictation, or fragmented notes) plus, optionally, a current
> snapshot or existing JSON. Produce all four required artifacts
> (`CAPTURE_PREVIEW.md`, `STRUCTURED_DELTA.json`, `AMBIGUITIES.md`,
> `APPLY_INSTRUCTIONS.md`) as separate, clearly labeled sections. Never
> invent a priority, owner, or category the capture doesn't state; a
> genuinely ambiguous fragment goes to AMBIGUITIES.md, never a forced
> classification."

Attach `SKILL.md` and `references/` as Custom GPT knowledge files. If the
user is dictating via the ChatGPT voice/mobile app, the transcript ChatGPT
already produced from the audio *is* the raw capture — do not re-summarize
it before running the procedure; feed the transcript text verbatim as
`source_artifacts`.

## File I/O
The raw capture and any snapshot are attached as Project/Custom-GPT
knowledge files or pasted inline. Outputs are returned as labeled markdown
sections in the chat response; the user saves them and re-attaches the
current snapshot on the next run.

## Environment constraints
Custom GPT knowledge files are read-only context, not a live filesystem —
each run needs the current snapshot/JSON re-attached explicitly if
`mode: STANDARD`/`UPDATE` is used.

## Fallback
This entire adapter is the fallback: ChatGPT has no native "skill folder"
primitive, so `SKILL.md`'s procedure is reproduced as system instructions.
