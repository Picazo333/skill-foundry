# Brand Verbal Identity

Converts a locked brand strategy into an operational verbal identity system —
behavioral voice principles, tone modulation by context, vocabulary rules, a
message hierarchy, and DO/DON'T examples — precise enough that a writer who
never met the founder can reproduce the voice correctly.

- Canonical definition: [`SKILL.md`](./SKILL.md)
- Specification this was built from: [`SPEC.md`](./SPEC.md)
- Input/output contracts: [`schemas/`](./schemas/)
- Worked examples: [`examples/`](./examples/)
- Eval cases: [`evals/`](./evals/)
- Platform adapters: [`adapters/`](./adapters/)

Takes `brand-strategy`'s output. Runs in parallel with `brand-visual-direction`
(see `/WORKFLOW_MAP.md`); both feed `brand-book-builder`. Also hands off to
`brand-content-system`, `creative-brief-generator`, and
`brand-quality-auditor` (see `/routing-graph.json`).
