# Eval Case — Existing brand, content-only engagement

## Scenario
A brand already has a complete, approved brand book. The new objective is
narrow: build a content system for ongoing social posts. Tests that the
orchestrator does not force the project through irrelevant stages just
because they exist in the general workflow.

## Input
```yaml
RUN_REQUEST:
  objective: "build a repeatable content system for ongoing social content; brand is already fully approved"
  source_artifacts:
    - {artifact: BRAND_BOOK.md, owning_skill: brand-book-builder, approval_state: approved}
    - {artifact: BRAND_STRATEGY.md, owning_skill: brand-strategy, approval_state: approved}
    - {artifact: VERBAL_IDENTITY.md, owning_skill: brand-verbal-identity, approval_state: approved}
  mode: STANDARD
```

## Expected behavior
1. Recognizes discovery/strategy/verbal/visual/identity-system/book are all
   already satisfied and approved — none are re-run.
2. Recognizes the objective is a recurring/systemic content program, not a
   one-off deliverable → routes to `brand-content-system`, not
   `creative-brief-generator`.
3. Does not route to `brand-quality-auditor` yet — no production artifact
   has been delivered to audit.

## Expected artifacts
- `BRAND_WORKFLOW_STATE.md` — "Skipped stages" lists discovery through
  brand-book, each with "already complete and approved for this objective."
- `NEXT_SKILL_RUN.json` — `next_skill: brand-content-system`.

## Forbidden behavior
- Must not route through discovery/strategy/verbal/visual/identity-system/
  book "for completeness."
- Must not route to `creative-brief-generator` (wrong skill for a recurring
  system request).

## Pass criteria
- [ ] `NEXT_SKILL_RUN.json.next_skill == "brand-content-system"`.
- [ ] Six stages listed as skipped with explicit reasons, zero re-run.
- [ ] No routing to `brand-quality-auditor` on this run.
