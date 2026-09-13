# Product Auditor & Implementation Architect

Inspects an existing app/repo/product, verifies issues and opportunities
against evidence, and produces an implementation plan precise enough for an
execution agent to build from — without implementing during audit mode. Also
runs in QA mode to verify delivered work against a prior plan, without
fixing it.

- Canonical definition: [`SKILL.md`](./SKILL.md)
- Specification this was built from: [`SPEC.md`](./SPEC.md)
- Input/output contracts: [`schemas/`](./schemas/)
- Output artifact templates: [`templates/`](./templates/)
- Scoring/plan-structure references: [`references/`](./references/)
- Worked examples: [`examples/`](./examples/)
- Eval cases: [`evals/`](./evals/)
- Platform adapters: [`adapters/`](./adapters/)

Sits between `canonical-context-builder` and `ai-resource-router` in the
existing-product workflow (see `/WORKFLOW_MAP.md`): Canonical Context →
Product Auditor (AUDIT) → `IMPLEMENTATION_PLAN.md` → AI Resource Router →
Execution Agent (external) → Product Auditor (QA) → Canonical Context
Builder (canon update).

**Load-bearing boundary:** in `mode: AUDIT` this skill never writes or edits
product code, config, or data — it stops at a plan. In `mode: QA` it never
fixes a not-done item — it verifies and reports. This is suite-level
quality gate 6 in `/QUALITY_GATES.md` and is enforced even when explicitly
asked otherwise mid-run (see `evals/cases/04-edge-refuses-to-implement-when-asked.md`).
