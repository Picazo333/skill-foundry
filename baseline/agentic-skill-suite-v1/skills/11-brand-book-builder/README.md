# Brand Book Builder

Compiles already-validated verbal identity (`brand-verbal-identity`) and
visual/identity system (`brand-identity-system`) canon into one coherent,
usable brand manual — without reopening upstream decisions. Flags, rather
than silently patches, any point where the verbal and visual canon don't
actually align.

- Canonical definition: [`SKILL.md`](./SKILL.md)
- Specification this was built from: [`SPEC.md`](./SPEC.md)
- Input/output contracts: [`schemas/`](./schemas/)
- Worked examples: [`examples/`](./examples/)
- Eval cases: [`evals/`](./evals/)
- Platform adapters: [`adapters/`](./adapters/)

Takes both `brand-verbal-identity`'s and `brand-identity-system`'s outputs
(see `/WORKFLOW_MAP.md`). Hands off the compiled book to
`creative-brief-generator` and `brand-content-system`, and to
`brand-quality-auditor` or the owning upstream skill when a coherence gap or
thin canon is found (see `/routing-graph.json`).
