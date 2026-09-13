# Codex adapter — Rapid Capture & Triage

## Invocation
Reference this skill from the repo's agent-instructions file (e.g.
`AGENTS.md`) as: "For triaging raw capture (dictated notes, dropped-in
transcripts) into structured task/project updates, read
`skills/04-rapid-capture-triage/SKILL.md` and follow it exactly." The
coding agent loads `SKILL.md` on demand when it encounters a raw-capture
style input (e.g. a `NOTES.md`/`INBOX.md` scratch file, or a
pasted-in-conversation dump) rather than keeping it permanently in context.

## File I/O
Reads the raw capture from the repo working tree (a scratch/inbox file, or
text pasted into the session) and the current snapshot from wherever the
project tracks tasks/issues (a `TASKS.json`, a project board export, or
similar tracked file). Writes the four required artifacts as real files,
typically alongside the raw capture (e.g. a `capture/<date>/` directory).

## Environment constraints
Prefer an existing tracked snapshot file in the repo over asking the user
to restate current state — if the repo has a canonical task/project file,
that is the `prior_run`/snapshot input for `mode: STANDARD`/`UPDATE`. Treat
`STRUCTURED_DELTA.json` as a proposed patch to review, not something to
auto-apply to the tracked snapshot without the human seeing
`CAPTURE_PREVIEW.md` and `AMBIGUITIES.md` first.

## Fallback
N/A — repo filesystem access covers this skill's I/O needs directly.
