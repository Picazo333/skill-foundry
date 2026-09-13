# Eval Case — Sports betting / tipster market

## Scenario
A founder wants to launch a paid sports-betting tipster subscription and
picks `mode: AUTONOMOUS`. Tests domain-native lens discovery in a market
with real, non-generic mechanics (bookmaker limiting, odds compression,
affiliate economics), correct tagging of primary-evidence triggers where
secondary sources genuinely can't answer the question, and — since this is
the AUTONOMOUS case — that the run proceeds through all phases without
pausing for "continue?" while still checkpointing after logical blocks.
See `examples/tipster-market-example.md` for a fuller worked version of
this same scenario.

## Input
```yaml
RUN_REQUEST:
  objective: "We want to launch a paid sports-betting tipster subscription service. Should we build it, and if so, what model (pure tips vs. tips+community vs. copy-betting) and what market first?"
  source_artifacts: []
  known_context: "Founders have built two prior subscription products (unrelated niches). No existing betting/gambling operating experience. Budget: bootstrapped, ~$40k runway."
  constraints: ["must remain compliant with gambling-advertising law in target market", "no in-house odds/trading desk planned"]
  desired_output: full_architecture_package
  mode: AUTONOMOUS
  prior_run: null
```

## Expected behavior
1. Domain discovery surfaces domain-native mechanics (bookmaker account
   limiting, odds-compression dynamics, affiliate/referral economics,
   track-record verification/trust signals) distinct from generic "market
   sizing" filler; a generic-only domain list is a failure.
2. Regulatory/advertising-compliance domain is weighted high given the
   stated constraint, and interconnects explicitly with the distribution/
   acquisition-channel domain.
3. Questions that cannot be answered from secondary sources (e.g. actual
   bookmaker limiting thresholds, revealed — not stated — subscriber trust
   behavior) are tagged as primary-evidence triggers, not left to default
   to a secondary-source assumption.
4. In AUTONOMOUS mode, the run does not pause to ask "should I continue" /
   "Siguiente" / "y" between iterations or phases; it produces
   `CHECKPOINT.md` updates after each logical block (Phase 1 lock, every
   ~25 expansion iterations, the 150 threshold, every ~25 polishing
   iterations, the 50 threshold, each QA pass).
5. Run still stops before deep research despite AUTONOMOUS mode — no
   bookmaker limiting thresholds or subscriber WTP figures are actually
   asserted as findings.

## Expected artifacts
- `DOMAIN_MAP.md` — contains domain-native lenses named above, each with
  interconnections.
- `GAP_LEDGER.md` — primary-evidence triggers section non-empty, each
  citing why secondary sources are insufficient.
- `CHECKPOINT.md` — shows multiple checkpoint entries across the run (not
  only a single end-of-run checkpoint), consistent with checkpointing after
  every logical block in AUTONOMOUS mode.
- `RUN_RESULT.mode: AUTONOMOUS`, `quality.stopped_before_execution: true`.

## Forbidden behavior
- Must not produce only generic/universal lenses (market size, competitors,
  financials) with no domain-native mechanics specific to betting/tipster
  markets.
- Must not silently default a primary-evidence-only question to a
  secondary-source answer.
- Must not emit any "continue?"/"Siguiente"/"y" style pause absent a
  genuine blocker.
- Must not answer any research question (e.g. state an actual bookmaker
  limiting threshold) — that is execution-stage work.

## Pass criteria
- [ ] Domain-native lenses (limiting, odds compression, affiliate economics,
      trust/verification) are present and distinct from generic lenses.
- [ ] Primary-evidence triggers are tagged with a stated reason, not silently
      defaulted.
- [ ] No confirmation-seeking pause appears anywhere in the AUTONOMOUS run.
- [ ] `CHECKPOINT.md` reflects multiple block-level checkpoints, not one.
- [ ] No research question is actually answered; package stops before
      execution.
