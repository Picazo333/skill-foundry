# Research Architect

Transforms a raw idea/problem into an exhaustive, decision-oriented research
architecture — a weighted, interconnected domain map plus a validated
≥200-iteration research program — and stops before any deep research
execution.

- Canonical definition: [`SKILL.md`](./SKILL.md)
- Specification this was built from: [`SPEC.md`](./SPEC.md)
- Non-negotiable methodology: [`/docs/RESEARCH_ARCHITECT_V2_INVARIANTS.md`](../../docs/RESEARCH_ARCHITECT_V2_INVARIANTS.md)
- Input/output contracts: [`schemas/`](./schemas/)
- Worked example: [`examples/`](./examples/)
- Eval cases: [`evals/`](./evals/)
- Platform adapters: [`adapters/`](./adapters/)

Typically follows `canonical-context-builder` in a workflow (see
`/WORKFLOW_MAP.md` if present) when a project's canon is unclear, and hands
off to `ai-resource-router` when specific research sub-tasks need routing.
It never performs deep research itself — that is a separate, future
Research Executor skill; this skill produces the package that skill would
consume.
