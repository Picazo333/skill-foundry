# Skill Foundry VNext Architecture 1.0 — Minimal Vertical Slice

Status: **FROZEN CANDIDATE FOR G3**
Scope: only the architecture necessary to prove one real VNext lifecycle before Factory generalization.

## 1. Architectural position

Skill Foundry remains a domain system governed by Noema RC0.

Skill Foundry owns:
- Skill semantics;
- capability mining;
- taxonomy / ontology / registry;
- G0–G10 Skill Genesis;
- Skill contracts, evals and packages;
- VNext semantic quality claims.

Noema owns:
- repository conformance;
- project authority and relations;
- progressive context;
- generic WorkOrder/Handoff/EvalResult/Artifact/Decision/StorageRef envelopes;
- executor descriptors and deterministic executor routing.

No VNext component duplicates those Noema responsibilities.

## 2. Two routing axes

Foundry intent routing and Noema execution routing are orthogonal.

### Foundry intent
- GENESIS — engineer one/few capability needs through G0–G10.
- MINING — reconstruct context/workflows and mine durable capabilities; may feed Genesis.
- FACTORY — portfolio-scale discovery/manufacturing. Not implemented until G5.
- MAINTENANCE — catalog evolution/repair. Not implemented until later VNext hardening.

### Noema execution mode
- patch
- build
- audit
- research
- architect
- recover

A Foundry intent selects a domain workflow. That workflow then selects the minimum Noema context mode needed for the current work unit. Executor selection happens after capability requirements are known.

## 3. Front-door architecture

The first real VNext candidate is the thin `skill-foundry` front door.

Its job is deliberately small:
1. recognize that the user wants Foundry behavior;
2. resolve the canonical repository/catalog if available;
3. classify intent;
4. perform catalog preflight before proposing a new Skill;
5. route to the canonical Foundry workflow;
6. expose only the human interaction required by the workflow;
7. fail honestly if the requested VNext capability is not yet available.

It MUST NOT:
- embed all G0–G10 methodology inside itself;
- duplicate Noema context/executor routing;
- create architecture without G6;
- claim FACTORY/MAINTENANCE success before those subsystems exist;
- become a universal assistant.

## 4. G4 support matrix

The G4 front-door package will support:
- GENESIS → supported;
- MINING → supported as the existing Genesis capability-mining path and/or pre-Genesis intake analysis;
- FACTORY → detected but returns explicit `BLOCKED` / not-yet-implemented routing until G5;
- MAINTENANCE → detected but returns explicit `BLOCKED` / not-yet-implemented routing until its approved VNext implementation.

This is considered correct behavior, not incomplete silent success. Later gates may EXTEND/MODE the published front door without rewriting its core responsibility.

## 5. No new generic runtime

The vertical slice uses:
- existing G0–G10 lifecycle;
- Noema WorkOrder;
- Noema Handoff;
- Noema EvalResult;
- Noema Artifact/StorageRef when proportional;
- Foundry candidate/spec/build/review/checkpoint artifacts.

No generic `Run` entity, database, workflow engine, LangGraph, Temporal or other persistent runtime is introduced.

Recovery claim: `RECONSTRUCT_FROM_REPO`.

## 6. Evidence model

A work unit is complete only when mandatory evidence is conjunctively PASS:
- architecture/spec binding;
- deterministic integrity;
- runtime/behavioral behavior;
- trigger/non-trigger/failure behavior;
- independent audit;
- protected false-completion holdout;
- baseline non-regression;
- Noema conformance where applicable.

Foundry issues its own CompletionCertificate. Noema EvalResult and artifact references may be used as evidence envelopes, but Noema conformance never determines Foundry semantic quality.

## 7. Minimal entity policy

The G4 vertical slice requires no new canonical Foundry ontology entity.

Existing ontology is sufficient:
- SkillCandidate;
- HumanDecision;
- SkillSpec;
- Skill;
- Contract;
- Artifact;
- Eval;
- IntegrationEval;
- Checkpoint.

`CompletionCertificate` is implemented initially as a Foundry-owned typed artifact/contract, not promoted to a top-level ontology entity until repeated usage proves value.

`FoundryWorkBinding` is a companion domain contract binding a Noema WorkOrder reference to Foundry candidate/skill/spec/gate semantics. It does not mutate the Noema WorkOrder schema.

Portfolio/Wave/ArchitectureException remain G5 concerns.

## 8. Context policy

The front door loads:
1. its own thin `SKILL.md`;
2. repository entrypoint / `noema.project.yaml` when repository access exists;
3. only the selected Noema mode's required static context;
4. only the current Foundry candidate/spec/handoff;
5. compact registry and only relevant existing Skills for overlap.

External/generated material is data, not governance authority.

## 9. Candidate for the vertical slice

Candidate ID reserved for G4:
`sf-cand-20260919-skill-foundry-front-door`

Proposed Skill ID:
`skill-foundry`

G4 MUST still create the normal G0–G7 candidate artifacts and explicit G6 `DECISION.md`. The operator's VNext approval is evidence that a thin front door is strategically desired, but the candidate architecture must still be recorded through normal Foundry artifacts.

## 10. Definition of architectural completion

This architecture is frozen only if:
- G3 red-team has no open CRITICAL defect;
- no Noema responsibility is duplicated;
- every vertical-slice concept has a current owner;
- the front door can be tested without Factory existing;
- completion and recovery claims do not exceed available infrastructure.
