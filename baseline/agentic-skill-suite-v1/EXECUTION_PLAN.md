# EXECUTION PLAN

## Build order

Wave 0 — Foundation (this session, direct):
1. This `EXECUTION_PLAN.md`.
2. Flesh out `shared/` (template, eval template, policies, contracts, adapter
   contract) from blueprint placeholders into real canonical content that
   every skill references instead of duplicating.
3. Build `skills/01-canonical-context-builder/` to the full final contract
   (`SKILL.md, README.md, manifest.json, schemas/, templates/, references/,
   examples/, evals/, adapters/`) as the pilot. This validates the folder
   contract, the `SKILL.md` writing pattern, the manifest/schema shape, the
   eval format and the adapter format for every subsequent skill.
4. Checkpoint, commit, push.

Wave 1 — Cross-functional primitives (skills 02–05, parallel subagents,
pilot skill 01 already done in Wave 0):
- `02-research-architect` (special contract: preserve
  `docs/RESEARCH_ARCHITECT_V2_INVARIANTS.md` verbatim — 200+/150+/50+
  iteration minimums, autonomous architecture mode, stop before deep
  research; kept separate from a future Research Executor).
- `03-product-auditor`
- `04-rapid-capture-triage`
- `05-ai-resource-router`

Wave 2 — Brand foundations (skills 06–09, parallel subagents):
- `06-brand-discovery`, `07-brand-strategy`, `08-brand-verbal-identity`,
  `09-brand-visual-direction`

Wave 3 — Brand production (skills 10–14, parallel subagents):
- `10-brand-identity-system`, `11-brand-book-builder`,
  `12-creative-brief-generator`, `13-brand-content-system`,
  `14-brand-quality-auditor`

Wave 4 — Orchestration (skill 15, built directly, not delegated):
- `15-brand-skill-orchestrator` — built last, after all 14 other skills'
  real manifests/outputs exist, so it routes actual contracts.

Wave 5 — Integration:
- Structural validator over the whole suite (folder contract, manifest
  schema conformance, JSON validity).
- Cross-skill integration walkthroughs (the 7 scenarios in
  `START_PROMPT.md` §9).
- `FINAL_REPORT.md`, real `suite.manifest.json`.
- Package `dist/AGENTIC_SKILL_SUITE_V1.zip` + `dist/AGENTIC_SKILL_SUITE_V1_SHA256.txt`.
- Final checkpoint, commit, push.

## Dependencies

- Every skill depends on `shared/` (contracts/policies/templates) — built
  once in Wave 0, referenced not duplicated.
- `15-brand-skill-orchestrator` depends on all other 14 skills' finished
  manifests.
- `11-brand-book-builder` depends on `08-brand-verbal-identity` and
  `10-brand-identity-system` outputs (per `routing-graph.json`).
- `12-creative-brief-generator` and `13-brand-content-system` depend on
  `11-brand-book-builder`.
- `14-brand-quality-auditor` depends on `12` and `13` outputs.
- Skills within a wave are otherwise independent and safe to build in
  parallel (disjoint folders).

## Checkpoint points

Update `CHECKPOINT.md` and commit/push:
- after Wave 0 (foundation + pilot skill);
- after Wave 1;
- after Wave 2;
- after Wave 3;
- after Wave 4 (orchestrator);
- after Wave 5 (final package).

## QA sequence

1. Per-skill: does the folder match the `ARCHITECTURE.md` contract exactly?
2. Per-skill: does `manifest.json` validate against
   `shared/contracts/skill-manifest.schema.json`? Are `schemas/*.json` valid
   JSON Schema?
3. Per-skill: `QUALITY_GATES.md` skill-level gates 1–10.
4. Suite-level: `QUALITY_GATES.md` suite-level gates 1–10, checked once all
   15 skills and the orchestrator exist.
5. Integration walkthroughs (Wave 5) exercise the routing graph end to end.

## Packaging sequence

1. Run structural validator; fix gaps.
2. Write `FINAL_REPORT.md` and `suite.manifest.json`.
3. Assemble `dist/AGENTIC_SKILL_SUITE_V1.zip` from: `skills/`, `shared/`,
   `docs/`, `START_PROMPT.md`, `MASTER_PLAN.md`, `ARCHITECTURE.md`,
   `WORKFLOW_MAP.md`, `PORTABILITY.md`, `TOKEN_EFFICIENCY.md`,
   `QUALITY_GATES.md`, `routing-graph.json`, `suite.manifest.json`,
   `FINAL_REPORT.md`, `CHECKPOINT.md`.
4. `sha256sum` the zip into `dist/AGENTIC_SKILL_SUITE_V1_SHA256.txt`.
