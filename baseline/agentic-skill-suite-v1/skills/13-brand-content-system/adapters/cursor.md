# Cursor adapter — Brand Content System

## Invocation
Lives as a `.cursor/rules` entry or project doc pointing at
`skills/13-brand-content-system/SKILL.md`. Unlike Codex's explicit per-task
mention, a rule can auto-attach when the agent is working inside the brand
project's canon/content directories, or be invoked explicitly ("use the
brand-content-system skill on this project's canon").

## File I/O
Repo working tree, same as `adapters/codex.md`. Source canon is read from
the repo's brand canon files; the five required artifacts are written as
real files in the project (commonly beside the canon or in a `content/`
directory), not returned only in chat.

## Environment constraints
Same precedence rule as Codex: repo files are the source of truth over a
chat restatement of strategy. If the rule auto-attaches on files that
aren't actually approved canon (e.g. a draft strategy doc mid-edit), verify
approval status per `SKILL.md` step 1 before treating it as valid input —
auto-attachment is a convenience for invocation, not a waiver of the canon-
approval check.

## Fallback
N/A — repo file + rule/mention is the native pattern for this platform.
