# Brand Content System

Turns approved brand canon into a repeatable content operating system —
pillars traced to strategy, repeatable format archetypes, a source-to-content
pipeline, cadence set from real production capacity, and a measurement model
that doesn't confuse views with revenue.

`SKILL.md` is the canonical, executable definition. `SPEC.md` is the original
implementation contract it was built from. See `ARCHITECTURE.md` and
`PORTABILITY.md` at the repo root for the shared contract every skill in this
suite follows.

Distinct from `creative-brief-generator` (one-off, per-deliverable briefs)
and `brand-quality-auditor` (QA against canon) — this skill builds the
reusable system those two consume/audit against.

## Contents
- `SKILL.md` — canonical procedure, I/O envelopes, failure modes, evals.
- `manifest.json` — portable skill manifest (`shared/contracts/skill-manifest.schema.json`).
- `schemas/` — `input.schema.json` / `output.schema.json` for RUN_REQUEST/RUN_RESULT.
- `templates/` — fillable skeletons for the five required output artifacts.
- `references/` — pillar-derivation method and channel-role decision framework.
- `examples/` — worked input → output pair.
- `evals/` — 3 core scenarios + 1 edge/failure case.
- `adapters/` — thin per-platform wrappers (generic, ChatGPT, Codex, Claude, Gemini, Cursor).
