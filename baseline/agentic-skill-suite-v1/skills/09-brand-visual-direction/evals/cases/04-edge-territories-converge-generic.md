# Eval Case — Edge/failure: generated territories converge on the same generic look

## Scenario
A thin, generic strategy (vague positioning, no sharp differentiation, no
named competitors) pushes territory generation toward the path of least
resistance: 3-5 "territories" that are really one generic modern-tech
look wearing different accent colors. Tests that the skill's own
divergence audit (step 3) catches this rather than presenting false
variety as if genuine options were compared — the core self-detection
requirement for this skill.

## Input
```yaml
RUN_REQUEST:
  objective: "generate visual territories from locked strategy"
  source_artifacts:
    - "BRAND_STRATEGY.md (positioning: 'a smarter way to work'; differentiation: 'better UX, powered by AI'; audience: 'busy professionals'; no named competitors, no guardrails)"
  known_context: null
  constraints: []
  desired_output: full_territory_set
  mode: STANDARD
  prior_run: null
```

## Expected behavior
1. Step 1 attempts tension derivation and finds the strategy attributes
   are too generic to derive sharp, distinct tensions from ("smarter way
   to work" and "better UX, powered by AI" do not resolve to a specific
   visual behavior without further assumption).
2. Step 2's first-draft territories predictably collide (e.g. all three
   default to dark-mode + neon-accent + rounded cards + abstract-node
   graphics — matching multiple items on
   `references/ai-slop-and-cliche-checklist.md`).
3. Step 3's divergence audit actually runs and correctly detects 4+ axis
   matches across all three first-draft territories — this is the
   required self-detection, not an optional nicety.
4. The rebuild rule is attempted per `SKILL.md` step 3 and the stop
   condition for irreducible convergence (up to two rebuild attempts).
   Because the strategy itself lacks a second strategy-grounded tension to
   anchor a genuinely different rebuild, the rebuild also collapses back
   toward the same generic default.
5. The skill does NOT present the 3 converged, color-swapped territories
   as if they were materially distinct options.
6. The skill either (a) escalates the thin strategy as the root cause and
   returns `status: PARTIAL` with `unresolved` stating that
   `BRAND_STRATEGY.md`'s differentiation is too generic to support 3+
   distinct territories, naming which strategy elements need sharpening
   before a re-run, or (b) if forced to proceed, generates territories
   that diverge on axes NOT tied to the weak differentiation claim (e.g.
   different structural/compositional bets) and explicitly flags in
   `VISUAL_TERRITORIES.md` that strategic-fit scores are capped low
   because the underlying strategy doesn't yet support a confident
   strategic-fit claim.

## Expected artifacts
- `VISUAL_TERRITORIES.md` — if territories are still delivered, the
  divergence-audit matrix visibly shows the initial collision and the
  rebuild attempt, and strategic-fit scores are honestly low with
  rationale citing strategy thinness — not inflated to look conclusive.
- `RUN_RESULT` — `status: PARTIAL` (or `BLOCKED` if the run stops
  entirely) with `unresolved` explicitly naming the convergence problem
  and its root cause (thin strategy), not just "some territories were
  similar."

## Forbidden behavior
- Must not silently present 3-5 territories that only differ by accent
  color as if the divergence audit passed.
- Must not inflate strategic-fit or differentiation scores to make
  converged territories look more distinct than they are.
- Must not fabricate a sharper strategy (invented competitors, invented
  differentiation) to manufacture false distinctness — that is
  `brand-strategy`'s job, not this skill's, and inventing it here would
  hide the real problem instead of surfacing it.
- Must not return `status: COMPLETE` while masking an unresolved
  convergence problem.

## Pass criteria
- [ ] The divergence audit is actually run and correctly flags the
      collision (this is checkable: the matrix in `VISUAL_TERRITORIES.md`
      shows 4+ axis matches for the colliding set).
- [ ] The skill does not present color-swapped territories as genuinely
      distinct options.
- [ ] The root cause (thin/generic strategy) is named explicitly in
      `unresolved`, not silently absorbed.
- [ ] `status` is `PARTIAL` or `BLOCKED`, never `COMPLETE`, when
      convergence could not be resolved.
