# Brand Quality Auditor

Audits a delivered creative/content artifact against explicit brand canon
(strategy, verbal identity, visual identity) to detect drift, regression,
and generic "AI slop" — and refuses to audit (returns `BLOCKED`) if the
canon it needs is missing or incomplete, rather than grading against
assumed taste.

`SKILL.md` is the canonical implementation contract. `SPEC.md` is the
original design spec it was built from. Adapters in `adapters/` are thin
platform wrappers over `SKILL.md` — see `/PORTABILITY.md` and
`/shared/adapters/README.md`.

## Folder contents
- `SKILL.md` — canonical procedure, I/O contract, quality gates.
- `manifest.json` — portable machine-readable summary
  (`/shared/contracts/skill-manifest.schema.json`).
- `schemas/` — `input.schema.json` / `output.schema.json` for
  `RUN_REQUEST` / `RUN_RESULT`.
- `templates/` — blank templates for the three required output artifacts.
- `references/` — `ai-slop-checklist.md` (operationalized genericity
  detection) and `drift-comparison-method.md` (how to compare an artifact
  to canon without inventing standards).
- `examples/` — worked input → output pairs.
- `evals/` — eval cases per `/shared/templates/EVAL_TEMPLATE.md`.
- `adapters/` — per-platform thin wrappers (generic, ChatGPT, Codex,
  Claude, Gemini, Cursor).
