---
status: APPROVED_FOR_BUILD
candidate_id: sf-cand-20260919-skill-foundry-factory-mode
skill_id: skill-foundry
change_kind: EXTEND
target_skill_id: skill-foundry
---
# Approved Skill Spec — Skill Foundry Factory Mode Extension

## Identity
- **Target Skill:** `skill-foundry`
- **Change:** EXTEND existing thin front door with operational FACTORY routing.
- **Purpose:** Route portfolio-scale Foundry requests to the canonical Factory workflow after G5 without creating a second Factory Skill.

## Trigger
Existing trigger remains unchanged. Requests involving many capabilities/Skills, portfolio architecture, batch capability mining/manufacturing, or explicit Factory use classify as FACTORY.

## Non-trigger
Existing non-trigger remains unchanged. Do not invoke Factory for ordinary single-domain execution or a simple single-capability Genesis need.

## Inputs
Same as current front door plus optional multi-item portfolio/corpus/architecture input.

## Context policy
- Reuse current front-door progressive loading.
- On FACTORY, load `SF-WF-003_PORTFOLIO_FACTORY.md` plus current portfolio artifacts only.
- Do not load full portfolio raw material into every work unit.
- Noema remains context/executor coordination authority.

## Procedure
1. Classify FACTORY when the request is portfolio-scale or explicitly Factory-oriented.
2. Route to `foundry/workflows/SF-WF-003_PORTFOLIO_FACTORY.md`.
3. Preserve F0–F5 discovery before manufacturing.
4. Require explicit Portfolio Review / Plan Lock for real portfolio architecture.
5. After Plan Lock, permit routine autonomous Factory execution within locked architecture.
6. Architecture-changing findings create explicit exceptions; do not silently mutate Plan Lock.
7. Re-overlap pending items after every publication wave.
8. MAINTENANCE remains blocked until separately implemented.

## Autonomy
May execute Factory discovery, normalization, dedup, architecture analysis and post-Plan-Lock routine manufacturing within approved scope. Must stop affected items for architecture exceptions requiring human authority.

## Outputs
- portfolio source ledger;
- normalized PortfolioItems;
- dedup/family/contract/dependency views;
- Portfolio Proposal;
- Plan Lock decision/plan;
- dependency-safe wave plan;
- evidence/certificates;
- final portfolio reconciliation.

## Quality gates
- 100% source accounting;
- no invented UNKNOWN interpretation;
- mandatory catalog overlap before NEW_SKILL;
- Plan Lock before build;
- dependency DAG valid;
- no illegal wave order;
- no builder shared-canon writes;
- architecture exceptions explicit;
- serialized canonical publication;
- no critical false PASS.

## Failure modes
- unknown item → quarantine UNRESOLVED rather than invent;
- source not accounted → Factory FAIL;
- dependency cycle → Factory FAIL/BLOCKED;
- post-lock architecture change → ArchitectureException;
- critical circuit breaker → stop affected workstream;
- missing executor → Noema routing returns blocked rather than changing architecture.

## Stop conditions
Factory run ends only when all sources are accounted and every PortfolioItem has a justified terminal or explicitly unresolved/deferred disposition, with no open critical architecture exception or unaudited canonical publication.

## Dependencies
- `SF-WF-003_PORTFOLIO_FACTORY.md`
- Factory schemas and validator
- Skill Registry
- Noema coordination contracts
- VNext gate-eval/circuit-breaker contracts

## handoffs_from
- existing `skill-foundry` intent router;
- supplied portfolio/corpus/Skill architecture.

## handoffs_to
- per-item Genesis/spec/build/audit work;
- serialized steward/publication path;
- final reconciliation.

## Token/context strategy
Portfolio discovery may inspect broad source material once; work units receive only WorkOrder-specific context, dependencies, contracts and relevant registry entries. Derived views replace repeated raw-context loading.

## Portability
No platform/provider is encoded in Factory semantics. Executors remain replaceable behind Noema capability requirements.

## Compatibility / migration impact
Backward compatible extension of `skill-foundry`. GENESIS/MINING behavior is unchanged. FACTORY changes from honest blocked state to supported routing. MAINTENANCE remains blocked.

## Evals
- FACTORY request routes to SF-WF-003.
- Single-skill request remains GENESIS.
- unknown items remain unresolved.
- source loss fails.
- duplicate aliases do not create duplicate Skills.
- Plan Lock required before build.
- dependency cycle fails.
- downstream item cannot enter same/earlier wave than dependency.
- shared-canon builder write fails.
- architecture change after Plan Lock creates explicit exception.

## Explicit out-of-scope
- Maintenance implementation;
- Portfolio Router;
- learned executor routing;
- database/graph/runtime framework;
- Noema protocol changes;
- automatic human architecture approval.
