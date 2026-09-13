# Brand Visual Direction

Translates a locked brand strategy into 3–5 materially distinct creative
territories, audits them for false variety and AI-slop/category clichés,
scores them, and selects a single visual grammar — mood, color logic,
typography logic, imagery language, compositional principles — before any
identity assets are produced.

- Canonical definition: [`SKILL.md`](./SKILL.md)
- Specification this was built from: [`SPEC.md`](./SPEC.md)
- Input/output contracts: [`schemas/`](./schemas/)
- Worked examples: [`examples/`](./examples/)
- Eval cases: [`evals/`](./evals/)
- Platform adapters: [`adapters/`](./adapters/)

Sits between `brand-strategy` and `brand-identity-system` in the brand
workflow (see `/WORKFLOW_MAP.md`, `/routing-graph.json`), running in
parallel with `brand-verbal-identity`. This skill produces *direction*,
not final production assets — that systemization is `brand-identity-system`.
