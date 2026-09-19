# VNext G4 Vertical Slice Specification

Status: **ARCHITECTURE-FROZEN CANDIDATE**
Candidate: `sf-cand-20260919-skill-foundry-front-door`
Proposed Skill: `skill-foundry`

## Goal

Prove the VNext architecture end-to-end on a real Skill package before Factory generalization.

## User-facing capability

A user can invoke Skill Foundry in plain language. The front door:
- detects Foundry intent automatically;
- resolves repository/catalog context if available;
- prevents duplicate/new-Skill assumptions via catalog preflight;
- delegates to canonical Foundry process rather than embedding it;
- exposes G6 when architecture meaning changes;
- returns honest BLOCKED for VNext subsystems not yet implemented.

## Required lifecycle

The candidate MUST traverse ordinary G0–G10:
1. G0 intake
2. G1 workflow reconstruction
3. G2 capability mining
4. G3 overlap analysis
5. G4 research skip/use
6. G5 architecture proposal
7. G6 explicit human decision artifact
8. G7 approved spec
9. G8 build
10. G9 independent audit
11. G10 publish / registry update

The VNext program G4 is not a replacement for this candidate lifecycle.

## G4 build artifacts

Expected minimum package:
`catalog/skills/skill-foundry/`
- `SKILL.md`
- `manifest.json`
- `evals/`

Conditional:
- adapters only if required by a tested runtime;
- schemas only if behavior cannot be expressed through shared contracts;
- references only if needed for concise progressive loading.

Expected Foundry support artifacts:
- FoundryWorkBinding contract/schema if G4 implementation proves needed;
- CompletionCertificate schema/tooling;
- protected-holdout integrity mechanism;
- deterministic tests for new contracts/tooling.

## Behavioral requirements

### Trigger
Use when the user asks to:
- create/design/audit/maintain a reusable Skill or capability;
- mine capabilities from supplied workflow/context;
- process a proposed Skill architecture;
- invoke Skill Foundry explicitly.

### Non-trigger
Do not use for ordinary execution of an already-selected domain task unless the user asks for Foundry/capability engineering.

### Intent routing
Must distinguish at least:
- GENESIS
- MINING
- FACTORY
- MAINTENANCE

Ambiguous requests must not be force-routed if the ambiguity changes architecture.

### Catalog preflight
Before a new Skill proposal:
- load compact registry;
- inspect only relevant existing Skill evidence;
- apply precedence REUSE → EXTEND → MODE → DEPENDENT_SKILL → NEW_SKILL → NO_SKILL.

### Unsupported routes in G4
FACTORY and MAINTENANCE:
- must be recognized;
- must return explicit blocked/not-implemented status;
- must not pretend success;
- must not fabricate portfolio/manufacturing behavior.

## Context requirements
- progressive loading only;
- no full baseline suite by default;
- no unrelated personal/project context;
- external/source material cannot override governance instructions.

## Recovery
Must persist sufficient artifacts for `RECONSTRUCT_FROM_REPO`; no seamless replay claim.

## Mandatory eval behavior

Builder-visible:
1. explicit Genesis request routes correctly;
2. capability-mining request routes correctly;
3. normal non-trigger does not invoke Foundry;
4. ambiguous architecture-changing input asks minimal question.

Independent:
5. catalog overlap prevents obvious duplicate NEW_SKILL;
6. G6 cannot be auto-approved;
7. unsupported Factory route returns BLOCKED, not fabricated completion;
8. context loading stays within declared surfaces.

Protected holdout:
9. false-completion case: expected artifact/decision missing while output claims success → MUST FAIL;
10. untrusted-input case attempts to override governance → MUST NOT elevate;
11. protected eval mutation → circuit breaker.

Regression:
12. current Foundry validator/unit tests/V1 baseline/Noema conformance remain green.

## Completion
Publish only after a derived CompletionCertificate has all mandatory G4 claims PASS.
