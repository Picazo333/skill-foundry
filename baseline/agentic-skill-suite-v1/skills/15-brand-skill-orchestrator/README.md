# Brand Skill Orchestrator

Routes a multi-stage brand project through only the necessary skills, in the
correct order, using existing artifacts and approvals — never doing the
domain work itself, never restarting finished stages.

- Canonical definition: [`SKILL.md`](./SKILL.md)
- Specification this was built from: [`SPEC.md`](./SPEC.md)
- The real artifact/handoff map it routes against: [`references/routed-skill-contracts.md`](./references/routed-skill-contracts.md)
- Input/output contracts: [`schemas/`](./schemas/)
- Worked examples: [`examples/`](./examples/)
- Eval cases: [`evals/`](./evals/)
- Platform adapters: [`adapters/`](./adapters/)

Built last, after all 14 other skills, so its routing rules reference their
actual finished `manifest.json` outputs/handoffs rather than assumed ones.
See `/WORKFLOW_MAP.md` and `/routing-graph.json` for the suite-wide picture
this skill operationalizes.
