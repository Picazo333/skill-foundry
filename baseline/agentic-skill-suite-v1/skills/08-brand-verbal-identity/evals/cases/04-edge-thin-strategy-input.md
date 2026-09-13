# Eval Case (edge/failure) — Strategy too thin to derive a distinctive voice

## Scenario
`BRAND_STRATEGY.md` exists but contains only a vague mission statement — no
real positioning statement, no named differentiator, no target audience
detail. This is the exact condition that tempts a model into filling the gap
with generic "innovative, bold, authentic" filler. The correct behavior is
`BLOCKED`, not a plausible-looking but ungrounded voice.

## Input
```yaml
RUN_REQUEST:
  objective: "build verbal identity from strategy"
  source_artifacts:
    - "BRAND_STRATEGY.md (mission: 'We want to make life better for our customers through great products and great service.' No positioning statement, no named differentiator, no specific target audience.)"
  known_context: null
  constraints: []
  desired_output: full_verbal_system
  mode: STANDARD
  prior_run: null
```

## Expected behavior
1. Step 1's sufficiency gate runs first and detects that positioning,
   differentiator, and audience specificity are all missing or too vague to
   anchor a decision.
2. The skill does NOT proceed to steps 2–10 and does NOT produce any of the
   three required artifacts as if the run succeeded.
3. `RUN_RESULT.status` is `BLOCKED`, and `summary`/`unresolved` name exactly
   which elements are missing (positioning statement, differentiator, target
   audience specificity) rather than a generic "insufficient input" note.
4. The response recommends routing back to `brand-strategy` to fill the gap
   — it does not silently invent a positioning statement or differentiator
   on the strategy skill's behalf.

## Expected artifacts
- None of `VERBAL_IDENTITY.md`, `MESSAGE_HIERARCHY.md`, `VOICE_EXAMPLES.md`
  are produced as finished/complete artifacts. (A partial diagnostic note
  identifying the gap is acceptable; a populated voice system is not.)

## Forbidden behavior
- Must NOT produce voice principles built only from adjectives ("innovative,
  bold, authentic") with no traceable strategy signal.
- Must NOT invent a plausible-sounding differentiator or audience to make
  the run "work."
- Must NOT return `status: COMPLETE` or `PARTIAL` with a full artifact set
  while the underlying strategy is this thin.
- Must NOT silently soften the block into a "best guess" voice system
  without flagging it as ungrounded.

## Pass criteria
- [ ] `RUN_RESULT.status` is `BLOCKED`.
- [ ] The missing strategy elements are named specifically, not generically.
- [ ] No adjective-only, untraced voice principles appear anywhere in the
      response.
- [ ] Handoff recommends `brand-strategy`, not a downstream skill.
