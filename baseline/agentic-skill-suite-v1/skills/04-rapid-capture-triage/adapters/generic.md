# Generic adapter — Rapid Capture & Triage

For any chat-based LLM interface with file upload or paste support.

## Invocation
Paste or reference `SKILL.md` as a system/instruction message, then supply
the raw capture as the `RUN_REQUEST` (objective, the capture text itself as
`source_artifacts`, mode). The raw capture is usually pasted directly —
dictation apps and phone voice-memo transcripts are plain text, so no
special upload handling is needed for the minimum-input case.

## File I/O
- **Reading sources:** paste the raw capture as text; upload the current
  snapshot/existing JSON if the interface supports file upload, or paste it
  inline for `mode: STANDARD`/`UPDATE`.
- **Writing outputs:** the assistant returns the four required artifacts as
  separate, clearly delimited blocks — `STRUCTURED_DELTA.json` as a fenced
  `json` block, the three `.md` files as fenced `markdown` blocks — so they
  can be saved as separate files by the user.

## Environment constraints
No filesystem access assumed. The user saves the returned artifacts and
re-supplies the current snapshot on the next run (this skill's runs are
typically one-shot per capture, not a resumed multi-turn session).

## Fallback
N/A — this is the baseline all other adapters specialize.
