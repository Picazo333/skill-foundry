# Eval Case — Partial brand, approved strategy but no visual system

## Scenario
An existing project already has an approved `BRAND_STRATEGY.md` and a
complete `VERBAL_IDENTITY.md` set, but no visual work has started. Tests
that the orchestrator correctly resumes mid-workflow rather than restarting
from discovery, and routes only to what's actually missing.

## Input
```yaml
RUN_REQUEST:
  objective: "continue this brand project toward a complete brand book"
  source_artifacts:
    - {artifact: BRAND_DISCOVERY_BRIEF.md, owning_skill: brand-discovery, approval_state: approved}
    - {artifact: BRAND_STRATEGY.md, owning_skill: brand-strategy, approval_state: approved}
    - {artifact: VERBAL_IDENTITY.md, owning_skill: brand-verbal-identity, approval_state: approved}
    - {artifact: MESSAGE_HIERARCHY.md, owning_skill: brand-verbal-identity, approval_state: approved}
    - {artifact: VOICE_EXAMPLES.md, owning_skill: brand-verbal-identity, approval_state: approved}
  mode: STANDARD
```

## Expected behavior
1. Inventory correctly identifies discovery, strategy, and verbal identity
   as complete/approved.
2. Does NOT route to `brand-discovery`, `brand-strategy`, or
   `brand-verbal-identity` — those stages are skipped with a stated reason
   ("already complete and approved").
3. Routes to `brand-visual-direction` as the single next action.

## Expected artifacts
- `BRAND_WORKFLOW_STATE.md` — inventory table shows discovery/strategy/verbal
  as `exists: yes, approved`; visual/identity-system/book as `exists: no`.
  "Skipped stages" section explicitly lists discovery/strategy/verbal with
  reasons.
- `NEXT_SKILL_RUN.json` — `next_skill: brand-visual-direction`.

## Forbidden behavior
- Must not re-route to any of the three already-complete stages.
- Must not skip ahead to `brand-identity-system` (visual direction isn't
  approved yet, so identity-system's minimum input isn't satisfied).

## Pass criteria
- [ ] `NEXT_SKILL_RUN.json.next_skill == "brand-visual-direction"`.
- [ ] `BRAND_WORKFLOW_STATE.md` lists exactly 3 skipped stages with reasons.
- [ ] No routing decision touches discovery, strategy, or verbal identity.
