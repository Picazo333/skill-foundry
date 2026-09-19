# R8 — Factory Concurrency and Ownership

Decision question: What ownership/wave constraints preserve quality as Factory parallelism grows?

## Evidence
- Anthropic's parallelization guidance is strongest when subtasks are independent; sequential dependencies should remain ordered.
- GitHub supports explicit concurrency control for conflict-prone operations; serialization is a standard defense for deployment/canon-like writes.
- Existing Foundry collaboration already restricts parallelism to independent candidates/stages whose dependencies are canonical.
- G4 demonstrates that audit/evidence should be separated from build authority.

## Decision
Use **wave-bounded parallelism with serialized canon publication**.

Initial limits:
- 2 concurrent builders;
- 1 independent auditor lane;
- 1 serialized steward/publisher.

Rules:
1. Work units in the same wave must have satisfied dependencies and non-overlapping write scopes.
2. Builders get isolated branches/work scopes and shared canon is read-only.
3. Auditor may read build branches but does not mutate builder-owned package files.
4. Registry/taxonomy/ontology/checkpoint publication is serialized.
5. Architecture exceptions pause only affected items unless they invalidate shared upstream architecture.
6. Parallelism may increase only after two consecutive healthy waves with zero critical regressions/ownership collisions.

## Branch convention
- `build/<portfolio>/<item-or-skill>`
- `audit/<portfolio>/<item-or-skill>`
- `publish/<portfolio>/<wave>`

For G5 smoke validation, simulated work-unit ownership is sufficient; large-scale agent spawning is not required.

Confidence: high.

Revisit trigger: two healthy real waves complete and measured queueing dominates runtime without quality degradation.
