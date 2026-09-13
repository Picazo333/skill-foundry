# Eval Case (edge/failure) — Contradictory founder input on the same axis

## Scenario
A single founder, in the same interview, states two mutually exclusive
positions on the same axis without noticing the contradiction: early on,
"we need to feel exclusive and premium, like a members-only thing"; later,
"but obviously we want as many people as possible to be able to buy in, no
gatekeeping." Unlike the streetwear case (two co-founders, two documents),
this is one person contradicting themselves within one source. Tests that
the skill does not "average" the two into a middle position, does not treat
the later statement as automatically superseding the earlier one (recency
does not resolve a same-source, same-person self-contradiction the way it
would resolve a genuine authority/timestamp conflict), and does not quietly
drop one side.

## Input
```yaml
RUN_REQUEST:
  objective: "build discovery brief for a boutique fitness studio"
  source_artifacts:
    - "founder_interview_2026-08.txt (single founder; minute 4: 'we need to feel exclusive and premium, like a members-only thing'; minute 31: 'but obviously we want as many people as possible to be able to buy in, no gatekeeping')"
  known_context: null
  constraints: []
  desired_output: full_discovery_set
  mode: STANDARD
  prior_run: null
```

## Expected behavior
1. Both statements are extracted as ASPIRATIONS, each with a timestamp/
   location in the source (minute 4 vs. minute 31) and attributed to the
   same founder.
2. The skill identifies this as a Contradiction (premium/exclusive vs.
   accessible/no-gatekeeping) — the fact that both statements come from the
   same person in the same interview does not exempt it from being logged;
   self-contradiction is still a contradiction `brand-strategy` must
   resolve.
3. The skill does NOT treat "minute 31" as superseding "minute 4" the way a
   later, higher-authority source would supersede an earlier one in
   `canonical-context-builder`-style reasoning — a single person changing
   emphasis mid-interview is not the same as a corrected/updated position,
   and the brief must not silently pick the later statement as final.
4. The skill does NOT synthesize a compromise position (e.g. "premium but
   accessible" or "approachable luxury") on its own authority — that
   synthesis, if it happens at all, is `brand-strategy`'s job, not
   discovery's.
5. Because this is the only source and it's internally contradictory on a
   core axis, the resulting brief is thin; `RUN_RESULT.status` may be
   `PARTIAL` given how much rests on an unresolved core tension, and
   `unresolved` must name this contradiction specifically.

## Expected artifacts
- `BRAND_DISCOVERY_BRIEF.md` — both statements appear in ASPIRATIONS with
  distinct source locations; Contradictions section names the tension
  explicitly, citing both, without picking a side or averaging.
- `DISCOVERY_GAPS.md` — likely contains an entry asking the founder directly
  to resolve or prioritize between the two framings, since this is a single
  founder with no other stakeholder to break the tie.
- `RUN_RESULT.unresolved` — explicitly names the exclusive-vs-accessible
  self-contradiction.

## Forbidden behavior
- Must NOT state a single, unified "desired perception" that blends both
  framings into a compromise the founder never actually said.
- Must NOT treat the minute-31 statement as automatically canonical because
  it came later in the same interview.
- Must NOT drop either statement to make the brief read as more coherent
  than the source material actually is.
- Must NOT mark `RUN_RESULT.status: COMPLETE` with an empty `unresolved`
  list when this contradiction is the central finding of the run.

## Pass criteria
- [ ] Both statements are preserved verbatim/attributed, neither dropped.
- [ ] No synthesized "compromise" position appears anywhere in the outputs.
- [ ] Recency within the same interview is not used to silently pick a
      winner.
- [ ] `RUN_RESULT.unresolved` explicitly names this contradiction.
