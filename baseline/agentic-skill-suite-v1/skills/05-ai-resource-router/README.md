# AI Resource Router

Chooses the best available AI tool/account for each task in a batch, using
capability fit, quota/capacity, reset urgency, cost/opportunity and context
constraints — then produces a routing plan and ready-to-use dispatch prompts.
It never performs the routed tasks itself.

- Canonical definition: [`SKILL.md`](./SKILL.md)
- Specification this was built from: [`SPEC.md`](./SPEC.md)
- Input/output contracts: [`schemas/`](./schemas/)
- Decision framework: [`references/`](./references/)
- Worked example: [`examples/`](./examples/)
- Eval cases: [`evals/`](./evals/)
- Platform adapters: [`adapters/`](./adapters/)

Can be invoked at any execution boundary in the suite (see
`/WORKFLOW_MAP.md`) to decide what runs where before dispatching to an
external execution agent, and hands routed tasks off to `product-auditor`,
`research-architect`, or `brand-skill-orchestrator` as appropriate — it does
not do their work for them.
