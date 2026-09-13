# Brand Strategy

Converts a brand discovery brief and its evidence into a defensible
strategy — category, audience, positioning, promise, value proposition,
differentiation, proof and guardrails — specific enough to constrain both
verbal and visual identity work downstream.

- Canonical definition: [`SKILL.md`](./SKILL.md)
- Specification this was built from: [`SPEC.md`](./SPEC.md)
- Input/output contracts: [`schemas/`](./schemas/)
- Output templates: [`templates/`](./templates/)
- Framework references: [`references/`](./references/)
- Worked examples: [`examples/`](./examples/)
- Eval cases: [`evals/`](./evals/)
- Platform adapters: [`adapters/`](./adapters/)

Sits between `brand-discovery` and the parallel branch of
`brand-verbal-identity` / `brand-visual-direction` (see `/WORKFLOW_MAP.md`
and `/routing-graph.json`): it consumes `BRAND_DISCOVERY_BRIEF.md` and its
output is the shared strategic foundation both downstream skills build
from. It defines the *what and why*; it never writes voice/tone copy or
visual direction — those are the downstream skills' job.
