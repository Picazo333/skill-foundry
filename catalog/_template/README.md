# Canonical Skill Package Template

Required for a published serious Skill:
- `SKILL.md` — canonical portable capability definition.
- `manifest.json` — compact machine-readable registry/validation surface.
- `schemas/input.schema.json` and `schemas/output.schema.json` when structured contracts add value.
- `evals/` — minimum 3 normal + 1 edge/failure case.
- `adapters/` — only thin wrappers actually required by the approved spec/platform targets.

Optional directories such as `templates/`, `references/`, `examples/` are created only when they add operational value. Do not manufacture boilerplate for symmetry.
