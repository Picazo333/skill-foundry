# SF-WF-001 — SKILL GENESIS

Status: **CANONICAL**  
Purpose: convert a recurrent human workflow/capability need into the smallest justified solution: reuse, extension/mode, dependent/new Skill, or explicit no-Skill closure.

```text
HUMAN WORKFLOW / NEED
        |
        v
G0 INTAKE
        |
        v
G1 WORKFLOW RECONSTRUCTION
        |
        v
G2 CAPABILITY MINING
        |
        v
G3 REGISTRY / OVERLAP ANALYSIS
        |
        v
G4 CONDITIONAL RESEARCH (or documented skip)
        |
        v
G5 ARCHITECTURE / CLOSURE PROPOSAL
        |
        v
G6 HUMAN DECISION
   | buildable approved       | reuse/no-skill approved      | reject/research/correct
   v                          v                              +----> appropriate earlier gate
G7 SURGICAL SPECS          G10 CLOSE
   |
   v
G8 BUILD (CURSOR)
   |
   v
G9 AUDIT (ANTIGRAVITY)
   | PASS          | REWORK
   v               +-------> G8
G10 PUBLISH + CANON UPDATE
   |
   v
 STOP
```

## Candidate artifact bundle
`foundry/candidates/<candidate_id>/`
- `00_INTAKE.md`
- `01_WORKFLOW_RECONSTRUCTION.md`
- `02_CAPABILITY_MAP.md`
- `03_OVERLAP_ANALYSIS.md`
- conditional `04_RESEARCH_PLAN.md` / `04_RESEARCH_FINDINGS.md`
- `05_SKILL_ARCHITECTURE_PROPOSAL.md`
- `DECISION.md`

Approved specs: `foundry/specs/<skill_id>.md`  
Builds: `catalog/skills/<skill_id>/`  
Audits: `foundry/reviews/<skill_id>_AUDIT.md`

## Gate semantics
- G0→G5 autonomous except indispensable missing process information.
- G6 always human.
- G7→G10 autonomous professional/mechanical execution except hard blocker or destructive ambiguity.
- A workflow stage is not automatically a Skill.
- An orchestrator is not created until worker boundaries and routing need are proven.

## Success criterion
Success is **correct routing with evidence**, not number of Skills created.
