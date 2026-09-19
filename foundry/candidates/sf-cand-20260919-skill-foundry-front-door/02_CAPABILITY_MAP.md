# G2 Capability Map — Skill Foundry Front Door

candidate_id: `sf-cand-20260919-skill-foundry-front-door`

| Capability | Recurrence | Depth | Actor | Reuse scope | Proposed treatment |
|---|---|---|---|---|---|
| Recognize Foundry-relevant intent | high | moderate semantic | agentic | transversal | candidate core |
| Classify Foundry intent | high | moderate semantic | agentic | Foundry meta | candidate core |
| Catalog preflight | high | deep boundary reasoning | agentic + registry | Foundry meta | candidate core |
| Execute G0–G10 methodology | high | deep | existing workflow | Foundry | REUSE workflow, not embed |
| Noema context routing | high | deterministic/project governance | Noema | cross-project | REUSE Noema |
| Executor routing | high | deterministic | Noema | cross-project | REUSE Noema |
| Schema/reference validation | high | deterministic | utility | Foundry | REUSE tooling |
| Factory portfolio manufacturing | future | deep | workflow/system | Foundry | NOT part of G4 front door |
| Maintenance lifecycle | future | deep | workflow/system | Foundry | NOT part of G4 front door |

## Rejected micro-Skills
- separate “mode detector” Skill;
- separate “catalog loader” Skill;
- separate “Noema context router” Skill;
- separate “ask one question” Skill.

These are responsibilities or reused infrastructure, not justified standalone Skills.
