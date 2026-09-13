# Walkthrough 7 — Brand Orchestrator resumes a partially completed brand without restarting finished stages

## Starting state
Same as `skills/15-brand-skill-orchestrator/evals/cases/02-partial-brand-approved-strategy-no-visual.md`:
`BRAND_DISCOVERY_BRIEF.md`, `BRAND_STRATEGY.md`, and the full verbal identity
set already exist and are approved. No visual work has started. This
walkthrough extends that eval case through to a full resume-and-complete
sequence, demonstrating suite-level gate 9 ("every workflow can resume from
artifacts/checkpoints").

## Sequence
1. **`brand-skill-orchestrator`** run with `mode: STANDARD`,
   `source_artifacts` listing the three approved artifact sets.
   - Inventory (step 1 of `SKILL.md`) marks discovery/strategy/verbal as
     complete/approved.
   - Stage detection (step 2, using `references/stage-detection-rules.md`)
     determines current stage is VISUAL — not DISCOVERY.
   - `RUN_RESULT.status: PARTIAL`, `handoff.next_skill: brand-visual-direction`.
   - `BRAND_WORKFLOW_STATE.md`'s "Skipped stages" section names discovery,
     strategy, and verbal identity with "already complete and approved."
2. *(external)* `brand-visual-direction` runs, producing
   `APPROVED_VISUAL_DIRECTION.md`.
3. **`brand-skill-orchestrator`** run again with `mode: RESUME`,
   `prior_run: BRAND_WORKFLOW_STATE.md` from step 1, plus the new visual
   artifact.
   - Does NOT re-inventory from scratch by re-reading discovery/strategy/
     verbal content — it updates the existing state with the new visual
     artifact and re-applies stage detection.
   - Routes to `brand-identity-system` next.
4. Sequence continues (identity-system → brand-book-builder) exactly as in
   `examples/zero-to-brand-book-example.md` runs 5–7, arriving at
   `status: COMPLETE`.

## What must hold
- Step 1 never routes to `brand-discovery` or `brand-strategy` despite this
  being technically "early" in the overall workflow — the artifact inventory,
  not workflow position, drives routing.
- Step 3's `RESUME` mode genuinely resumes from `BRAND_WORKFLOW_STATE.md`
  rather than rebuilding the inventory from raw artifacts each time — this
  is the literal meaning of the suite-level "resume cleanly" quality gate.
- No skill is routed to twice across the whole sequence.

## Failure signature
If step 1 recommends `brand-discovery` (a completed, approved stage) as the
next action, the orchestrator has failed its single most important
quality gate: never re-running a completed stage without cause.
