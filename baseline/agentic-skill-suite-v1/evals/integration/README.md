# Suite integration walkthroughs

These 7 walkthroughs exercise cross-skill handoffs end to end, per
`START_PROMPT.md` §9. Each is a documented scenario tracing the actual
artifact names each skill produces/consumes (per every skill's real
`manifest.json`), not a hypothetical. They are integration-level evals —
individual skills' own eval cases live in `skills/<n>/evals/`.

| # | Walkthrough | Skills exercised |
|---|---|---|
| 1 | [`01-voice-note-to-canon.md`](./01-voice-note-to-canon.md) | rapid-capture-triage → canonical-context-builder |
| 2 | [`02-new-idea-to-research-package.md`](./02-new-idea-to-research-package.md) | canonical-context-builder → research-architect |
| 3 | [`03-product-audit-to-handoff.md`](./03-product-audit-to-handoff.md) | canonical-context-builder → product-auditor → ai-resource-router |
| 4 | [`04-new-brand-zero-to-book.md`](./04-new-brand-zero-to-book.md) | brand-discovery → brand-strategy → (brand-verbal-identity + brand-visual-direction) → brand-identity-system → brand-book-builder → brand-quality-auditor |
| 5 | [`05-existing-brand-content-to-qa.md`](./05-existing-brand-content-to-qa.md) | brand-content-system → creative-brief-generator → brand-quality-auditor |
| 6 | [`06-multi-tool-workload-routing.md`](./06-multi-tool-workload-routing.md) | ai-resource-router (standalone, multi-task) |
| 7 | [`07-orchestrator-resumes-partial-brand.md`](./07-orchestrator-resumes-partial-brand.md) | brand-skill-orchestrator resuming mid-workflow without restarting finished stages |

## How to read a walkthrough
Each file states: the starting state, the sequence of skill runs, the exact
artifact each run consumes and produces (cross-checked against that skill's
own `manifest.json`), and what would make the walkthrough fail (a broken
handoff — wrong artifact name expected, a skill re-deriving what upstream
already decided, or silently dropping an unresolved item).
