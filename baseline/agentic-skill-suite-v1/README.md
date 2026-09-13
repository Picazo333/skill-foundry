# AGENTIC SKILL SUITE

A self-contained, portable 15-skill agentic suite. Every skill has one
canonical implementation (`SKILL.md`) plus thin adapters for ChatGPT, Codex,
Claude, Gemini, Cursor and a generic fallback — see `PORTABILITY.md`.

Status: **implemented** — all 15 skills complete. See `FINAL_REPORT.md` for
the full build report, `scripts/validate_suite.py` for structural
validation, and `evals/integration/` for cross-skill walkthroughs.

## Cross-functional operating skills
1. [Canonical Context Builder](skills/01-canonical-context-builder/)
2. [Research Architect](skills/02-research-architect/)
3. [Product Auditor & Implementation Architect](skills/03-product-auditor/)
4. [Rapid Capture & Triage](skills/04-rapid-capture-triage/)
5. [AI Resource Router](skills/05-ai-resource-router/)

## Brand & Creative operating skills
6. [Brand Discovery](skills/06-brand-discovery/)
7. [Brand Strategy](skills/07-brand-strategy/)
8. [Brand Verbal Identity](skills/08-brand-verbal-identity/)
9. [Brand Visual Direction](skills/09-brand-visual-direction/)
10. [Brand Identity System](skills/10-brand-identity-system/)
11. [Brand Book Builder](skills/11-brand-book-builder/)
12. [Creative Brief Generator](skills/12-creative-brief-generator/)
13. [Brand Content System](skills/13-brand-content-system/)
14. [Brand Quality Auditor](skills/14-brand-quality-auditor/)
15. [Brand Skill Orchestrator](skills/15-brand-skill-orchestrator/)

## Source of truth
- `START_PROMPT.md` — the original build instructions this suite was built from.
- `MASTER_PLAN.md` — scope and acceptance contract.
- `WORKFLOW_MAP.md` — cross-skill workflows.
- `ARCHITECTURE.md` — universal skill contract every `SKILL.md` follows.
- `PORTABILITY.md` — portability rules for the 6 platform adapters.
- `TOKEN_EFFICIENCY.md` — autonomy/checkpoint/token policy.
- `QUALITY_GATES.md` — suite QA gates.
- `EXECUTION_PLAN.md` — the build order this suite was actually built in.
- `CHECKPOINT.md` — current build phase (recovery-oriented, resumable).
- `skills/*/SPEC.md` — the original surgical specification each `SKILL.md` was built from.
- `shared/` — canonical templates, policies and contracts every skill references instead of duplicating.
- `routing-graph.json` / `suite.manifest.json` — machine-readable suite topology and status.

## Using a skill
Each `skills/<n>-<id>/README.md` points to that skill's `SKILL.md`
(canonical procedure), `schemas/` (I/O contracts), `examples/` (worked
input→output), `evals/` (test scenarios) and `adapters/` (per-platform
invocation notes). Start with `SKILL.md`.

## Final package
`dist/AGENTIC_SKILL_SUITE_V1.zip` (+ `dist/AGENTIC_SKILL_SUITE_V1_SHA256.txt`)
contains all 15 finished skills, shared contracts, adapters, examples,
evals, docs, the workflow map, the suite manifest and the final report.
