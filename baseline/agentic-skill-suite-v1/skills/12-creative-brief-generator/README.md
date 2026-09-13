# Creative Brief Generator

Translates brand canon plus a specific deliverable objective into an
execution-ready creative brief — concrete audience, single-minded message,
canon-cited mandatories, format specs and QA-checkable acceptance criteria
for one named deliverable (landing page, Reel/campaign, deck, packaging,
generated media). Not a restatement of the brand book.

- Canonical definition: [`SKILL.md`](./SKILL.md)
- Specification this was built from: [`SPEC.md`](./SPEC.md)
- Input/output contracts: [`schemas/`](./schemas/)
- Worked examples: [`examples/`](./examples/)
- Eval cases: [`evals/`](./evals/)
- Platform adapters: [`adapters/`](./adapters/)

Sits after `brand-book-builder` (and optionally `brand-content-system`) in
the brand workflow (see `/WORKFLOW_MAP.md`): it consumes compiled brand
canon — plus, optionally, a content brief from `brand-content-system` — and
hands its brief set to `brand-quality-auditor` for production QA.
