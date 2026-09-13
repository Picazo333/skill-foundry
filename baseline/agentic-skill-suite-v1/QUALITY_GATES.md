# QUALITY GATES

## Skill-level
A skill fails if any applicable gate fails:
1. Trigger is clear.
2. Boundary/non-trigger is clear.
3. Minimum inputs are sufficient.
4. Procedure is executable without inventing methodology.
5. Output schema is explicit.
6. Downstream handoff works without chat history.
7. It does not materially duplicate another skill.
8. Shared rules are referenced instead of duplicated.
9. Core works without platform-specific assumptions.
10. Minimum eval set passes.

## Suite-level
1. No circular orchestration loop.
2. Brand Orchestrator never performs child-skill deep work.
3. AI Resource Router routes but does not execute unrelated domain work.
4. Canonical Context Builder never invents missing facts.
5. Research Architect stops before deep research.
6. Product Auditor does not implement in audit mode.
7. Rapid Capture preserves real ambiguity.
8. Brand Quality Auditor requires explicit canon.
9. Every workflow can resume from artifacts/checkpoints.
10. Final ZIP is complete and self-contained.
