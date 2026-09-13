# Codex adapter — Brand Content System

## Invocation
Lives as a repo file the coding agent is told to read before acting — e.g.
an `AGENTS.md` section pointing to
`skills/13-brand-content-system/SKILL.md`, or the file referenced directly
in the task prompt: "Follow
`skills/13-brand-content-system/SKILL.md` to build the content system from
`BRAND_STRATEGY.md` and `VERBAL_IDENTITY.md` in this repo."

## File I/O
Repo working tree. Source canon is read from wherever the brand project's
canon files live in the repo (commonly a `brand/` or `canon/` directory).
The five required artifacts are written as real files alongside that canon,
not returned only in chat.

## Environment constraints
Treat repo files as the source of truth over any chat/task-description
restatement of strategy — if the task prompt's summary of strategy conflicts
with the actual `BRAND_STRATEGY.md` in the repo, the file wins, and a
conflict is surfaced rather than silently resolved. If `BRAND_STRATEGY.md`
in the repo is absent or marked draft, stop per `SKILL.md`'s BLOCKED
condition rather than proceeding on the task description alone.

## Fallback
N/A — repo file + agent instruction is the native pattern for this platform.
