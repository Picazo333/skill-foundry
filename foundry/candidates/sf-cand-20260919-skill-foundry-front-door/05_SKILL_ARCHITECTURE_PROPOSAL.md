# G5 Skill Architecture Proposal — Skill Foundry Front Door

candidate_id: `sf-cand-20260919-skill-foundry-front-door`

## Recommendation
Create one new thin Skill:

`skill-foundry`

## Purpose
Provide a portable single entry point that recognizes Skill Foundry intent, performs catalog preflight and routes to the canonical Foundry workflow without embedding or redefining it.

## Supported in G4
- GENESIS
- MINING

## Detected but explicitly blocked until later VNext
- FACTORY
- MAINTENANCE

## Dependencies
- FOUNDRY_OPERATING_MODEL.md / SF-WF-001
- Skill Registry
- Noema project/context governance when operating in repo
- existing Foundry validator/eval contracts

## Shared contracts
Reuse:
- Noema WorkOrder/Handoff/EvalResult/Artifact/StorageRef where coordination/evidence requires them.
- Existing Foundry candidate/spec/manifest contracts.

Do not invent a second executor/context router.

## Handoffs
handoffs_from:
- user/operator request

handoffs_to:
- Genesis workflow
- capability mining path
- later Factory/Maintenance workflow when implemented

## Tier / role
- scope: meta
- capability class: router
- priority: S

## Orchestrator assessment
Not an orchestrator over worker Skills. It is a thin entry/router over Foundry workflows.

## Quality constraint
Success is correct routing/preflight/mediation, not completion of the downstream Skill-building goal.
