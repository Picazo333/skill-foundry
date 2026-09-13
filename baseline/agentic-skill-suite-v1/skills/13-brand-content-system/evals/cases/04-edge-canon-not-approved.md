# Eval Case — Content system requested before canon is approved

## Scenario
A stakeholder asks for a full content system while `BRAND_STRATEGY.md` is
still marked draft/in-review (positioning statement has two competing
options still open, not yet decided). Tests that the skill blocks rather
than building pillars on canon that could still change out from under it —
a content system built on unstable canon would need to be re-derived
entirely once strategy locks, wasting the run and risking shipped content
that no longer matches approved positioning.

## Input
```yaml
RUN_REQUEST:
  objective: "build content system so the team can start posting this week"
  source_artifacts:
    - "BRAND_STRATEGY_DRAFT.md (status: IN REVIEW — two competing
       positioning statements still open, stakeholder decision pending;
       differentiators section has a TBD placeholder)"
    - "VERBAL_IDENTITY.md (approved)"
  known_context:
    channels_in_use: ["Instagram"]
    production_capacity: "1 person, ~2hrs/week"
  constraints: []
  desired_output: full_system
  mode: STANDARD
  prior_run: null
```

## Expected behavior
1. Step 1 (verify canon is stable) detects that the strategy source is
   marked draft/in-review with an explicitly unresolved positioning
   decision.
2. The skill does not proceed to derive pillars from either of the two
   competing (unlocked) positioning options.
3. `status: BLOCKED` is returned, naming exactly what is missing: strategy
   approval / the specific pending decision (which positioning statement is
   locked).
4. The skill does not produce a partial pillar set "just in case one option
   wins" — no content-pillar artifact is generated at all from unstable
   strategy.

## Expected artifacts
- None of the five required artifacts are produced in full; at most a
  `RUN_RESULT` with `status: BLOCKED` and `unresolved` naming the pending
  strategy decision.

## Forbidden behavior
- Must not pick one of the two competing positioning statements on its own
  to "unblock" the run.
- Must not produce `CONTENT_PILLARS.md` derived from the draft, even with a
  caveat — draft strategy is not a valid trace source per `SKILL.md` step 1.
- Must not silently proceed because "the team wants to start this week" —
  urgency is not evidence that canon is approved.
- Must not claim `status: COMPLETE` or `PARTIAL` with pillars attached.

## Pass criteria
- [ ] `RUN_RESULT.status` is `BLOCKED`.
- [ ] The blocking reason names the specific unresolved strategy decision,
      not a generic "insufficient input" message.
- [ ] No `CONTENT_PILLARS.md` (or other required artifact) is generated from
      the draft strategy.
- [ ] The response does not choose a positioning option on the skill's own
      authority.
