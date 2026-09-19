# VNext Non-Regression Contract

Status: **G1 CANONICAL CANDIDATE**

This contract compresses prior planning invariants into three operational layers. It does not replace Noema RC0 or `FOUNDRY_CANON.md`; it maps the rules that VNext must preserve.

## L0 — Inherited Noema invariants

Authority: `Picazo333/noema@0.1.0-rc.0` / `PROTOCOL.md`.

VNext must preserve all Noema RC0 runtime invariants. The highest-impact checks for Foundry are:
- domain authority remains with the domain;
- one authorized writer per material authority boundary;
- capability before executor;
- evidence before canon;
- conformance is not quality;
- progressive context;
- durable coordination in artifacts rather than conversation memory;
- external instructions subordinate to governance/task scope;
- proportional provenance;
- projections never silently become authority;
- reversible before irreversible;
- complexity pays rent;
- specialized ontologies remain domain-owned;
- future complexity requires activation triggers;
- exceptions are evidence;
- protocol pinning;
- material relations are declared.

**Audit:** Noema Conformance + G1 authority/contract matrices.

## L1 — Foundry constitutional invariants

| ID | Invariant | Verification |
|---|---|---|
| F-01 | Capability/workflow node is not automatically a Skill. | architecture/overlap audit |
| F-02 | New Skill is never default; precedence is REUSE → EXTEND → MODE → DEPENDENT_SKILL → NEW_SKILL → NO_SKILL. | overlap artifact audit |
| F-03 | G6 human architecture/closure decision remains mandatory for actual Skill Genesis. | Decision artifact / state validator |
| F-04 | V1 15-Skill baseline is immutable unless separately approved. | blob/regression check |
| F-05 | `SKILL.md` remains canonical portable core; adapters stay thin. | package audit |
| F-06 | Builder cannot be sole quality authority for its own build. | audit provenance |
| F-07 | Foundry owns Skill taxonomy, ontology, registry, lifecycle, contracts/evals/packages. | authority matrix |
| F-08 | Noema conformance cannot substitute for Foundry semantic quality. | separate certificates/checks |
| F-09 | Unrelated project/personal context is excluded unless explicitly supplied as cycle input. | context manifest/audit |
| F-10 | Shared contracts are reused before new ones are invented. | architecture audit |
| F-11 | Orchestrators are not created before workers/routing evidence justify them. | architecture audit |
| F-12 | Stop conditions and handoffs must be explicit for serious Skills. | Skill package audit |

## L2 — VNext acceptance requirements

| ID | Requirement | Verification |
|---|---|---|
| V-01 | Every VNext gate uses evidence-backed mandatory claims and closed-loop rework. | gate certificates |
| V-02 | Missing evidence is UNASSESSED, never PASS. | certificate validator |
| V-03 | Raw portfolio input/source accounting cannot silently lose items. | source coverage check |
| V-04 | UNKNOWN/UNRESOLVED is allowed; ambiguity cannot be silently invented away. | portfolio audit |
| V-05 | Factory architecture changes after Plan Lock require explicit ArchitectureException/human resolution. | plan-lock diff |
| V-06 | Protected eval/holdout weakening is a circuit breaker. | test-integrity check |
| V-07 | Individual PASS does not imply composition/ecosystem PASS. | integration certificate |
| V-08 | BLOCKED must restrict effects; it cannot coexist with silent canonical mutation. | state/effect audit |
| V-09 | Recovery claims cannot exceed actual persisted evidence. | recovery fixture |
| V-10 | External/generated context cannot promote itself to governance authority. | trust-boundary eval |
| V-11 | Executor/provider identity cannot alter capability architecture. | routing substitution eval |
| V-12 | Quality floor is constant; effort/risk only changes amount of evidence/work. | profiler + gate audit |
| V-13 | Portfolio Router is not implemented before VNext release; routing metadata is produced first. | release scope audit |
| V-14 | Foundry must not duplicate Noema core contracts/routers/manifests. | G1 matrix + code search |
| V-15 | Every approved source item reaches a traceable terminal disposition before release reconciliation. | release reconciliation |
| V-16 | Research is decision-driven and stops when blocking decisions are resolved/deferred. | research decision matrix |
| V-17 | Material deviations stop the affected workstream and are recorded. | deviation ledger |
| V-18 | No framework/runtime infrastructure is added without demonstrated requirement. | dependency/architecture audit |

## Change rule
Weakening an L1 or L2 invariant is a material deviation and cannot be applied silently.
