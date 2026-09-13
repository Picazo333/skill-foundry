# Cursor adapter — Rapid Capture & Triage

## Invocation
Add as a `.cursor/rules` entry (or project doc referenced from one) that
points at `skills/04-rapid-capture-triage/SKILL.md`: "When the user pastes
or drops in a raw capture (voice-note transcript, dictation, scratch notes)
and asks to triage/structure it, follow this file's procedure exactly."
Unlike Codex's explicit-mention pattern, a Cursor rule can auto-attach when
the user pastes unstructured text into a task/inbox-shaped file, per the
project's rule configuration.

## File I/O
Reads the raw capture from the repo working tree (a scratch/inbox file, or
pasted chat content) and the current snapshot from the project's tracked
task/project file, same as `codex.md`. Writes the four required artifacts
as real files in the repo.

## Environment constraints
Same as `codex.md`: treat the tracked snapshot file as authoritative for
matching, and treat `STRUCTURED_DELTA.json` as a proposed patch for human
review before it's applied to that tracked file.

## Fallback
N/A — repo filesystem access covers this skill's I/O needs directly.
