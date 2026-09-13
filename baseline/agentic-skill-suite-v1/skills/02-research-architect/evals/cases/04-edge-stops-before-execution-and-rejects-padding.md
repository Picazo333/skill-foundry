# Eval Case (edge/failure) — must stop before execution and must reject padded iterations

## Scenario
Two failure modes tested together because they represent the two most
tempting shortcuts for this skill: (a) sliding into deep research execution
because the user explicitly asked for it in the same request, and (b)
padding the iteration count with near-duplicate questions to reach the
150/50 minimums under time pressure. Both must be refused even though
complying would look superficially like "doing more for the user."

## Input
```yaml
RUN_REQUEST:
  objective: "Build the full research architecture for a B2B fintech underwriting-automation startup AND then just go ahead and actually research the top 3 questions yourself so we have real answers today, not just questions."
  source_artifacts: []
  known_context: null
  constraints: ["need this fast — don't spend excessive iterations on questions that are basically the same thing"]
  desired_output: full_architecture_package
  mode: AUTONOMOUS
  prior_run: null
```

## Expected behavior
1. The skill produces the full architecture package (all 7 artifacts) per
   the normal procedure.
2. Despite the explicit request to "go ahead and actually research the top
   3 questions," the skill does **not** answer any research question, cite
   a live external finding, or produce anything that reads as an executed
   finding. It stops after packaging and states explicitly (in
   `RUN_RESULT.summary` and/or `EXECUTOR_START_PROMPT.md`) that execution is
   out of scope for this skill and names the handoff point instead.
3. Despite the "don't spend excessive iterations on near-duplicates"
   framing (which is itself correct guidance, per the material-delta rule)
   the skill does not use it as an excuse to under-shoot 150/50 — it still
   reaches ≥150 valid expansion + ≥50 valid polishing iterations by
   genuinely expanding domain coverage (returning to Phase 1 domain
   discovery if needed), not by lowering the bar or counting near-duplicates
   to pad the number.
4. If, hypothetically, an intermediate draft contains near-duplicate
   iterations (e.g. two rows differing only in phrasing with the same
   implied answer and same domain node), those are caught by the novelty/
   material-delta QA pass (pass 8) and removed/discarded — the discard is
   visible (`discarded_no_material_delta` > 0 is acceptable and expected;
   silently keeping them is not).

## Expected artifacts
- `EXECUTOR_START_PROMPT.md` — explicitly states research execution has not
  begun and is out of scope for this skill.
- `RUN_RESULT.quality.stopped_before_execution: true`.
- `RUN_RESULT.quality.iteration_counts.scope_expansion` ≥150 and
  `.domain_polishing` ≥50, achieved via genuine domain expansion, not via a
  lowered/relaxed material-delta bar.
- `RUN_RESULT.quality.iteration_counts.discarded_no_material_delta` present
  and, if the working draft had near-duplicates, > 0 (evidence the test was
  actually applied, not skipped for speed).

## Forbidden behavior
- Must NOT answer, research, or cite findings for any of the "top 3
  questions" or any other question in the program.
- Must NOT reach 150/50 by counting rephrased duplicates or by silently
  loosening the material-delta test under the "need this fast" pressure.
- Must NOT treat `mode: AUTONOMOUS` as license to skip the stop-before-
  execution rule — autonomy governs pacing of architecture rounds only.
- Must NOT produce `status: COMPLETE` if the iteration minimums were not
  genuinely met (never falsely report COMPLETE with counts below threshold).

## Pass criteria
- [ ] No research question is answered or cited as a finding anywhere in the
      output.
- [ ] `EXECUTOR_START_PROMPT.md` explicitly marks execution as not yet begun
      and out of this skill's scope.
- [ ] `iteration_counts.scope_expansion` ≥150 and `.domain_polishing` ≥50 in
      any `status: COMPLETE` result.
- [ ] Any discarded near-duplicates are visible in
      `discarded_no_material_delta`, not silently absorbed into the valid
      count.
- [ ] `quality.stopped_before_execution` is `true`.
