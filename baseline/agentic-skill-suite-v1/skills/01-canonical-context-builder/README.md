# Canonical Context Builder

Reconstructs and maintains the single canonical truth of a project — facts,
locked decisions, hypotheses, constraints, deprecated directions and open
loops — from fragmented conversations, files, renames and prior outputs.

- Canonical definition: [`SKILL.md`](./SKILL.md)
- Specification this was built from: [`SPEC.md`](./SPEC.md)
- Input/output contracts: [`schemas/`](./schemas/)
- Worked example: [`examples/`](./examples/)
- Eval cases: [`evals/`](./evals/)
- Platform adapters: [`adapters/`](./adapters/)

First skill in most workflows (see `/WORKFLOW_MAP.md`): raw input normally
passes through `rapid-capture-triage` first, then here, before branching to
`research-architect`, `product-auditor`, or `brand-discovery`.
