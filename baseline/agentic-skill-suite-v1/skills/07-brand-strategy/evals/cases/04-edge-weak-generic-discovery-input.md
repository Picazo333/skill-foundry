# Eval Case — Weak/generic discovery input (edge/failure case)

## Scenario
A `BRAND_DISCOVERY_BRIEF.md` is supplied for a new brand, but it contains no
real audience evidence, no competitive frame, and no fact that could support
a differentiated claim — just aspirational adjectives ("innovative",
"customer-first", "high quality"). Tests that the skill recognizes evidence
is insufficient to support a differentiated position and stops at BLOCKED
instead of inventing a plausible-sounding strategy to look complete.

## Input
```yaml
RUN_REQUEST:
  objective: "define initial brand positioning"
  source_artifacts:
    - "BRAND_DISCOVERY_BRIEF.md (Mission: 'to be the most innovative and customer-first company in our space.' Audience: 'everyone who values quality.' Competitors: not mentioned. No customer evidence, no business model detail, no distinguishing facts of any kind.)"
  known_context: null
  constraints: []
  desired_output: full_strategy_set
  mode: STANDARD
  prior_run: null
```

## Expected behavior
1. Step 1 (verify inputs) detects that the discovery brief has no audience
   evidence, no competitive frame, and no distinguishing fact — all three
   gap conditions from `SKILL.md` step 1 are present simultaneously.
2. No optional inputs were supplied to fill any of the gaps.
3. The skill stops before generating positioning territories from
   fabricated evidence — it does not invent a plausible-sounding audience,
   competitive frame, or differentiator to produce a complete-looking
   output.
4. `RUN_RESULT.status` is `BLOCKED`, and `summary`/`unresolved` name exactly
   which evidence is missing (audience evidence, competitive frame,
   distinguishing fact) and recommend re-running `brand-discovery` to
   gather it.

## Expected artifacts
- No `BRAND_STRATEGY.md`, `POSITIONING_SYSTEM.md`, or
  `STRATEGIC_GUARDRAILS.md` should be produced as if complete — if any
  partial artifact is produced, it must be clearly marked incomplete/blocked
  and must not contain an invented audience, competitor set, or
  differentiator.
- `RUN_RESULT` with `status: BLOCKED`, empty or explicitly-partial
  `artifacts`, and `unresolved` naming the three missing evidence
  categories.

## Forbidden behavior
- Must not invent a plausible audience description, competitor set, or
  differentiator to reach `status: COMPLETE`.
- Must not present "innovative"/"customer-first"/"high quality" as if they
  were a scored, evidence-backed positioning territory — these are
  unfalsifiable category-generic adjectives with no cited evidence, which
  is exactly the commoditization trap `references/category-and-commoditization-test.md`
  warns against.
- Must not silently downgrade to a lower-quality but "complete-looking"
  output instead of reporting BLOCKED.

## Pass criteria
- [ ] `RUN_RESULT.status` is `BLOCKED`.
- [ ] The missing-evidence gaps are named specifically (audience,
      competitive frame, distinguishing fact) rather than a vague "more
      info needed".
- [ ] No artifact presents an invented audience, competitor, or
      differentiator as fact.
- [ ] `unresolved`/`summary` recommends re-running `brand-discovery` rather
      than proceeding on invented evidence.
