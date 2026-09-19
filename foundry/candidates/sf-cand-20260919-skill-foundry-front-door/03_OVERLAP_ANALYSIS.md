# G3 Registry / Overlap Analysis — Skill Foundry Front Door

candidate_id: `sf-cand-20260919-skill-foundry-front-door`

## Relevant existing Skills
- Canonical Context Builder — constructs canonical truth; does not provide Foundry entry/routing.
- Research Architect — architects research; does not provide Foundry entry/routing.
- AI Resource Router — routes work to AI/tools; overlaps executor selection conceptually, but Noema now owns executor routing and the proposed front door routes Foundry intent, not providers.
- Brand Skill Orchestrator — orchestrates Brand workers; domain-specific and depends on an established Brand family.

## Decision precedence

### REUSE
No existing Skill provides a universal Skill Foundry entry surface.

### EXTEND
Extending AI Resource Router would conflate capability/workflow routing with resource/executor routing and duplicate Noema boundaries. Rejected.

### MODE
No existing Skill has a coherent parent responsibility for “Foundry entry”. Rejected.

### DEPENDENT_SKILL
The front door depends on Foundry canon/registry/Noema context contracts, but is not naturally a child of an existing Skill.

### NEW_SKILL
**Recommended**: `skill-foundry` as a thin meta/router Skill whose responsibility is detect → preflight → delegate/mediate.

### NO_SKILL
Rejected because without a portable entry Skill the user must know repo-specific mechanics and internal workflows, undermining the approved UX/portability goal.

## Boundary
The Skill must remain thin. It does not own G0–G10, Noema routing, Factory implementation, or downstream capability work.
