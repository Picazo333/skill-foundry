# SF-WF-003 — Portfolio Factory

Status: **VNEXT G5 CANONICAL CANDIDATE**

## Purpose
Process messy multi-item capability/Skill input into the smallest coherent, human-approved portfolio architecture and dependency-safe execution plan without equating input count with Skill count.

## Entry
Input may be text, lists, files, repos, prior research, existing trees or mixed artifacts.

## F0 — RAW PRESERVATION
Persist original input and source references. Raw input is immutable.

## F1 — SOURCE LEDGER
Assign stable source IDs. Every source fragment must end as NORMALIZED, DUPLICATE, IRRELEVANT_WITH_REASON or UNRESOLVED.

## F2 — NORMALIZATION / MINING
Create stable PortfolioItems. Distinguish workflow, capability, Skill candidate, deterministic utility, contract, tool/adapter, human judgment and UNKNOWN.

## F3 — DEDUP / CATALOG PREFLIGHT
Compare items to each other and to the canonical Skill Registry. Apply:
REUSE → EXTEND → MODE → DEPENDENT_SKILL → NEW_SKILL → NO_SKILL.

## F4 — PORTFOLIO ARCHITECTURE
Build minimum useful family map, shared-contract map and dependency DAG. No orchestrator is justified merely because a family exists.

## F5 — PORTFOLIO PROPOSAL
Present dispositions, dependencies, effort/risk and proposed waves. Unknowns remain explicit.

## F6 — PORTFOLIO REVIEW / PLAN LOCK
Human approves/corrects architecture. Persist HumanDecision and a PLAN_LOCKED portfolio plan. No build starts before Plan Lock.

## F7 — WORK UNITS / WAVES
Schedule only dependency-safe items. Builders receive isolated write scopes. Shared canon is read-only to parallel builders. Initial max parallel builders = 2.

## F8 — BUILD / AUDIT / REWORK
Each buildable item uses ordinary Foundry semantics and its own evidence loop. Failures route to the owning stage. Architecture-changing findings become ArchitectureExceptions rather than silent mutations.

## F9 — SERIALIZED PUBLICATION
Passed items merge through a serialized steward/publisher. Registry/taxonomy/ontology/checkpoint writes are never concurrent builder effects.

## F10 — RE-OVERLAP / NEXT WAVE
After publication, pending items are rechecked against the updated catalog before the next wave.

## Terminal portfolio condition
Every source fragment is accounted for and every PortfolioItem has a justified terminal or explicitly unresolved/deferred disposition. No silent lost source, dangling dependency, unreviewed architecture exception or unaudited publication remains.

## Circuit breakers
Use `foundry/evals/vnext/CIRCUIT_BREAKERS.yaml`. Critical false PASS, test tampering, provenance loss, trust-boundary violation, human-gate bypass or canonical corruption stops the affected workstream.

## Noema boundary
Noema owns general context/authority/executor coordination envelopes. Factory owns portfolio semantics and Foundry quality meaning.
