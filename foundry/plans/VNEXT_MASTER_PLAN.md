# Skill Foundry VNext — Canonical Execution Program

Status: **OPERATOR-AUTHORIZED PLAN**
Branch of origin: `planning/vnext-canonical-program`
Baseline target: `main@a471a1b9f82faf221eeb3d89aa06a828a9f3a0cc`
Scope: evolve Skill Foundry from V5 + Noema RC0 governance into VNext with a validated single-capability vertical slice, then Factory, then canaries, then release.

This file is the **canonical execution plan** for the VNext program. It does not replace `FOUNDRY_CANON.md`, `FOUNDRY_OPERATING_MODEL.md`, Noema RC0, or the G0–G10 Skill lifecycle. It governs only the VNext migration program.

## 0. Program contract

### 0.1 Invariants
- Noema owns repository conformance, project authority declarations, progressive context, interoperability, executor descriptors/routing, project relations and general provenance/storage references.
- Skill Foundry owns Skill taxonomy, Skill ontology, Skill registry, G0–G10, capability mining, portfolio architecture, Skill contracts/evals/packages and Skill lifecycle semantics.
- Noema PASS never substitutes for Foundry quality PASS.
- Capability is not automatically a Skill.
- Decision precedence remains `REUSE → EXTEND → MODE → DEPENDENT_SKILL → NEW_SKILL → NO_SKILL`.
- The 15-Skill V1 baseline remains immutable unless a separate explicit migration is approved.
- No second context router, executor router, project manifest, generic provenance model, or project relation model may be created inside Foundry.
- No platform/model identity is architecture.
- No VNext phase may merge if its required deterministic validation, behavioral evidence and independent review are incomplete.
- No material plan deviation may be applied silently.

### 0.2 Operator authorization
The operator has authorized this program to be executed end-to-end without routine intermediate confirmation once this plan is canonical in `main`.
This authorization:
- permits intermediate implementation PRs to be merged after their gate conditions pass;
- does **not** waive G6 for actual Skill architecture decisions;
- does **not** permit changing this plan's scope, Noema/Foundry authority boundaries, or acceptance gates without a recorded material deviation;
- requires final operator review after VNext release candidate completion.

### 0.3 Deviation policy
A change is **non-material** only if it:
- does not change authority ownership;
- does not introduce/remove a gate;
- does not change terminal acceptance criteria;
- does not alter public/canonical contracts;
- does not add infrastructure/framework dependencies;
- does not weaken tests, audit or Shadow controls.

Non-material implementation details may be adjusted and recorded in `foundry/plans/VNEXT_DEVIATIONS.md`.

A **material deviation** must stop the affected workstream, be recorded with evidence, and remain unresolved until operator review. Independent unaffected work may continue.

### 0.4 Branch policy
- `main` = stable canon.
- One implementation branch per gate: `vnext/g0-baseline`, `vnext/g1-boundaries`, ..., `vnext/g7-release`.
- Each branch starts from current `origin/main`.
- No force-push.
- Each gate merges only after the gate's acceptance criteria pass.
- Cross-gate dependencies become usable only after merge to `main`.

---

# Gate G0 — Seal V5 + Noema RC0 baseline

## Goal
Create an immutable technical reference before VNext changes.

## Required actions
1. Verify current `main` equals or descends from `a471a1b9f82faf221eeb3d89aa06a828a9f3a0cc`.
2. Run:
   - `python tools/validate_foundry.py`
   - `python -m unittest tests.test_validate_foundry -v`
   - V1 baseline validator already present in repo
   - Noema conformance workflow / equivalent pinned RC0 validation
3. Capture:
   - commit SHA;
   - validation outputs;
   - Noema protocol pin;
   - baseline Skill count;
   - current context-mode measurements if available.
4. Add immutable baseline evidence under:
   - `foundry/analysis/vnext/G0_BASELINE_REPORT.md`
   - `foundry/analysis/vnext/G0_BASELINE_MANIFEST.yaml`
5. Tag/release label: `sf-v5-noema-rc0-baseline` if repository permissions/tooling allow it. If tag creation is unavailable, record the exact commit SHA and treat it as the rollback anchor.

## Forbidden
- taxonomy/ontology changes;
- workflow redesign;
- Factory entities;
- package changes.

## Exit gate
All current V5 + Noema RC0 checks green; rollback anchor recorded.

---

# Gate G1 — Authority, contract and non-regression reconciliation

## Goal
Prevent Noema/Foundry duplication before any new VNext model is introduced.

## Required deliverables
Create:
- `foundry/architecture/VNEXT_AUTHORITY_MATRIX.yaml`
- `foundry/architecture/VNEXT_CONTRACT_REUSE_MATRIX.yaml`
- `foundry/architecture/VNEXT_NON_REGRESSION_CONTRACT.md`
- `foundry/architecture/VNEXT_OPEN_QUESTIONS.yaml`

## Authority matrix must classify every candidate concept as exactly one of
- `NOEMA_CORE`
- `FOUNDRY_DOMAIN`
- `NOEMA_CORE_WITH_FOUNDRY_EXTENSION`
- `DEFERRED_UNRESOLVED`

At minimum classify:
- Project
- ProjectAuthority
- ContextMode
- StorageRef
- Provenance
- ExecutorDescriptor
- ExecutorRouting
- ProjectRelation
- WorkOrder
- Run
- Handoff
- RecoveryState
- EvalEvidence
- Capability
- Skill
- SkillCandidate
- SkillFamily
- SkillSpec
- Portfolio
- PortfolioItem
- PlanDecision
- ArchitectureException
- Wave
- CompletionCertificate

## Contract reuse matrix
For each mixed concept define:
- upstream Noema contract;
- Foundry extension fields;
- ownership of validation;
- versioning authority;
- allowed direction of dependency.

## Non-regression contract
Compress prior NR-001…NR-060 and Noema invariants into three layers:
- L0 inherited Noema invariants;
- L1 Foundry constitutional invariants;
- L2 VNext acceptance requirements.

Every L1/L2 invariant must be testable or auditable.

## Exit gate
No unresolved ownership collision for any concept required by the vertical slice.
Unresolved optional/future concepts may remain `DEFERRED_UNRESOLVED`.

---

# Gate G2 — Targeted research only for surviving unknowns

## Goal
Resolve only architecture questions that G1 cannot settle from current repo/Noema/Shadow evidence.

## Default research tracks
- R1 behavioral completion / false-PASS evidence
- R2 eval layering, holdouts and eval-gaming resistance
- R3 recoverable execution semantics and idempotency
- R4 portfolio semantics at 1→1000 candidate scale
- R5 taxonomy/ontology facets needed for routing/dedup/maintenance
- R6 canonical Skill package and portable exports
- R7 routing metadata required by the future Portfolio Router
- R8 Factory waves, ownership and concurrency

Tracks may be removed if G1 closes them. No track may be added without mapping to a concrete open architecture decision.

## Required output per track
`foundry/research/vnext/Rx_<slug>.md` containing:
- exact decision question;
- repo/Noema/Shadow evidence;
- external evidence if used;
- alternatives;
- trade-offs;
- recommended decision;
- confidence;
- revisit trigger.

Create:
- `foundry/research/vnext/RESEARCH_DECISION_MATRIX.yaml`

## Tool allocation
- primary research: ChatGPT Deep Research;
- independent research: Gemini Deep Research;
- long-corpus interrogation: NotebookLM where useful;
- repo-aware critique: Antigravity;
- adversarial critique: Grok Bot / independent model;
- deterministic checks: Python/CI.

Tool identity is not architecture; substitutions are allowed if capability requirements are met.

## Exit gate
Every open decision needed by the vertical slice is either:
- `DECIDED`, or
- explicitly `DEFERRED` with no vertical-slice dependency.

---

# Gate G3 — Minimal VNext architecture + pre-code red team

## Goal
Freeze only the architecture required to prove one complete VNext lifecycle.

## Required architecture
Create:
- `foundry/architecture/VNEXT_ARCHITECTURE_1_0.md`
- `foundry/architecture/VNEXT_ENTITY_MODEL.yaml`
- `foundry/architecture/VNEXT_STATE_MODEL.yaml`
- `foundry/architecture/VNEXT_VERTICAL_SLICE_SPEC.md`
- `foundry/architecture/VNEXT_FAILURE_MODEL.yaml`

## Vertical slice must cover
```
messy input
→ automatic intent detection
→ capability mining
→ catalog preflight / overlap
→ architecture proposal
→ human architecture decision
→ buildable spec
→ work assignment
→ build
→ deterministic validation
→ independent audit
→ adversarial/holdout check
→ completion evidence
→ canonical publish
```

## Architectural constraints
- use existing G0–G10 wherever applicable rather than inventing a second lifecycle;
- Foundry intent and Noema execution mode are separate axes;
- context routing remains governed by Noema;
- executor selection remains governed by capability-before-executor semantics;
- only add ontology/taxonomy entities that the vertical slice actually requires;
- no Factory-wide UI;
- no database/vector DB/runtime framework dependency;
- no Portfolio Router implementation.

## Pre-code red team
Attack at minimum:
- Noema PASS masquerading as Foundry PASS;
- self-approval;
- duplicate capability with alias;
- malicious/untrusted source text;
- test weakening;
- BLOCKED but mutating state;
- false resume;
- missing dependency reported green;
- context mode omitting required Skill context;
- executor substitution changing architecture;
- architecture drift after human decision;
- provenance loss;
- safe components producing unsafe/invalid chain.

Write:
- `foundry/reviews/VNEXT_ARCHITECTURE_REDTEAM.md`

## Exit gate
No open critical red-team defect.
Architecture required for the vertical slice is frozen as 1.0.

---

# Gate G4 — Implement and prove the single-capability vertical slice

## Goal
Prove VNext end-to-end before generalizing to Factory.

## Implementation rules
- architect produces implementation spec before builder writes code;
- builder cannot redesign architecture;
- deterministic code owns deterministic truth;
- builder evals, independent audit and holdouts remain separated;
- all generated evidence is persisted in repo artifacts;
- completion is derived from evidence, not free-form agent assertion.

## Expected implementation areas
Exact files are determined by G3, but changes may include:
- Foundry protocols/workflows;
- new or extended JSON/YAML schemas;
- deterministic validators;
- test fixtures;
- execution evidence/handoff artifacts;
- completion certificate tooling;
- catalog/package support.

## Required validations
- existing V5 tests remain green;
- Noema conformance remains green;
- new deterministic tests pass;
- behavioral eval passes;
- independent audit verdict = PASS;
- relevant Shadow/holdout attacks pass;
- no baseline mutation;
- no ownership violation.

## Exit gate
One real VNext candidate completes end-to-end and publishes without bypass, paper-PASS or manual repo repair.

---

# Gate G5 — Generalize proven slice into Factory

## Goal
Scale the proven semantics, not unproven abstractions.

## Add Factory discovery
- raw input preservation;
- source ledger;
- normalization;
- contradiction handling;
- UNKNOWN quarantine;
- intra-batch dedup;
- catalog overlap;
- capability/family map;
- shared-contract map;
- dependency DAG;
- portfolio proposal.

## Add Factory execution
- Portfolio Review / Plan Lock;
- execution mandate or approved Noema+Foundry extension determined in G1;
- work units;
- waves;
- architecture exceptions;
- effort profile;
- risk profile;
- isolated ownership;
- serialized canon publication;
- re-overlap after each published wave;
- circuit breakers.

## Scale constraints
- initial concurrency: 2 build work units + 1 independent auditor + serialized publisher;
- no increase until two consecutive waves show no critical regression/ownership collision;
- shared canon files are read-only to parallel builders;
- architecture exceptions do not silently mutate Plan Lock.

## Exit gate
Factory can process a small mixed portfolio and all source items reach a justified state without source loss or architecture drift.

---

# Gate G6 — Double canary + hardening

## Synthetic canary
Use ~10–12 deliberately adversarial items including:
- obvious REUSE;
- obvious NO_SKILL;
- semantic duplicates;
- giant candidate requiring split;
- micro-candidates requiring merge;
- unknown/missing context;
- dependency cycle;
- premature orchestrator;
- malicious reference;
- EXTEND/NEW borderline;
- locked bad assumption;
- shared-contract opportunity.

Expected outcomes are defined before execution.

## Real canary
Use 15–25 representative items from the already-mined real corpus:
- multiple families;
- multiple effort/risk levels;
- overlaps;
- dependencies;
- at least one architecture exception candidate.

## Required metrics
- source coverage = 100%;
- silent lost items = 0;
- undocumented architecture changes = 0;
- critical false PASS = 0;
- holdout/test tampering = 0;
- dependency cycles in published graph = 0;
- canon ownership breaches = 0;
- unrecoverable interrupted runs = 0;
- untraced terminal dispositions = 0;
- critical Noema/Foundry authority collision = 0.

Also record:
- Noema Context Units per work unit;
- rework rate;
- human intervention points;
- executor substitutions;
- token/credit usage where measurable;
- repeated failure patterns.

## Circuit breakers
Immediate stop of the affected wave on:
- human-gate bypass;
- test manipulation;
- critical provenance loss;
- trust-boundary violation;
- canonical corruption;
- critical false PASS.

## Exit gate
Synthetic canary PASS + real canary PASS + no unresolved critical architecture exception.

---

# Gate G7 — VNext 1.0 release + first productive portfolio

## Goal
Release only after the system has demonstrated correctness.

## Release scope
Complete only what is required for a usable VNext:
- thin Skill Foundry front door;
- stable Genesis;
- stable Factory;
- capability mining;
- basic maintenance actions required by first portfolio;
- canonical package/export path needed by current usage;
- documentation and recovery instructions.

Do **not** add:
- Portfolio Router implementation;
- Noema architecture changes without separate evidence/harvest;
- web dashboard;
- DB/vector DB;
- Temporal/LangGraph/runtime framework;
- marketplace;
- exhaustive platform adapters.

## Full portfolio
Process the 80+ mined items only after release candidate gates are green.
Every source item must end in a traceable terminal disposition such as:
- REUSE
- EXTEND
- MODE
- DEPENDENT_SKILL
- NEW_SKILL/PUBLISHED
- MERGED
- NO_SKILL
- DEFERRED
- REJECTED
- UNRESOLVED

## Release evidence
Create:
- `foundry/releases/VNEXT_1_0_RELEASE_REPORT.md`
- `foundry/releases/VNEXT_1_0_ACCEPTANCE.yaml`
- `foundry/releases/VNEXT_1_0_PORTFOLIO_RECONCILIATION.md`

## Final operator intervention
After all release evidence is complete, execution stops for operator review.
No Portfolio Router project begins before this review.

---

# Program-wide acceptance rules

## Required on every gate merge
- branch based on latest `main`;
- no force-push;
- relevant Noema conformance green;
- relevant Foundry validation green;
- no baseline mutation unless explicitly in scope;
- all artifacts required by the gate committed;
- gate status updated in `VNEXT_EXECUTION_MANIFEST.yaml`;
- deviations recorded;
- no unresolved critical defect.

## Evidence priority
1. deterministic validation;
2. runtime/behavioral evidence;
3. independent audit;
4. model judgment;
5. narrative claim.

Narrative claims cannot override missing evidence.

## Done definition
VNext is done only when G0–G7 are terminal PASS and final operator review is the only remaining action.
