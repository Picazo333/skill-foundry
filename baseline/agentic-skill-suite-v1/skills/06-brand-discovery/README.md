# Brand Discovery

Turns fragmented founder/client/business information — interviews, existing
materials, market signals, raw notes — into a canonical brand discovery
brief that separates FACTS, CLAIMS, ASPIRATIONS, HYPOTHESES and
NON-NEGOTIABLES, maps references and anti-references by the underlying
quality they signal, and surfaces only the discovery gaps and contradictions
that materially block strategy. It documents; it does not decide.

- Canonical definition: [`SKILL.md`](./SKILL.md)
- Specification this was built from: [`SPEC.md`](./SPEC.md)
- Input/output contracts: [`schemas/`](./schemas/)
- Discovery templates: [`templates/`](./templates/)
- Discovery question bank + fact-vs-opinion rubric: [`references/`](./references/)
- Worked examples: [`examples/`](./examples/)
- Eval cases: [`evals/`](./evals/)
- Platform adapters: [`adapters/`](./adapters/)

First stage of the brand workflow (see `/WORKFLOW_MAP.md`): follows
`canonical-context-builder` (or raw client intake), hands off to
`brand-strategy`, which is where positioning and directional decisions
actually get made. Never do that decision work here — see `SKILL.md`'s
Non-trigger and Failure modes sections.
