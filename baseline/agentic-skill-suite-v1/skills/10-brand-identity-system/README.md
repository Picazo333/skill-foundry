# Brand Identity System

Turns an approved visual direction into an operational identity system —
logo architecture with derived clear-space/minimum-size rules, color roles
with computed WCAG contrast, a typography scale, spacing/grid/shape rules,
iconography and imagery rules, and motion principles — plus a
machine-readable design-token file. Concrete enough that a designer or a
design-token pipeline can build directly from it, with no invented values.

- Canonical definition: [`SKILL.md`](./SKILL.md)
- Specification this was built from: [`SPEC.md`](./SPEC.md)
- Input/output contracts: [`schemas/`](./schemas/)
- Derivation methods: [`references/`](./references/)
- Worked examples: [`examples/`](./examples/)
- Eval cases: [`evals/`](./evals/)
- Platform adapters: [`adapters/`](./adapters/)

Sits between `brand-visual-direction` and `brand-book-builder` in the brand
workflow (see `/WORKFLOW_MAP.md`, `/routing-graph.json`), running after the
visual direction is selected (not while territories are still being
compared) and in parallel with `brand-verbal-identity`. Its three required
outputs — `IDENTITY_SYSTEM.md`, `DESIGN_TOKENS.json`, `APPLICATION_RULES.md`
— hand off to `brand-book-builder` alongside `brand-verbal-identity`'s
`VERBAL_IDENTITY.md`.
