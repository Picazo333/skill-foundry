# Eval Case — Doré/codex-inspired personal OS

## Scenario
A consumer "personal OS" app positions itself as a reflective personal
record against quantified-self/productivity competitors. Two references
are supplied (Doré engravings, illuminated-manuscript/codex structure).
Tests that two distinct references are each mapped to a different
structural principle (not merged into one vague "old-book" mood), and
that the skill actively rules out gamification patterns (streaks,
progress bars) that would contradict the strategy.

## Input
```yaml
RUN_REQUEST:
  objective: "generate visual territories from locked strategy"
  source_artifacts:
    - "BRAND_STRATEGY.md (positioning: 'a life, illuminated'; differentiation: archival/reflective quality vs. dashboard/metrics framing; audience: quantified-self-fatigued users)"
  known_context: "references supplied: Gustave Doré engravings (high-contrast linework); illuminated manuscript/codex page structure (marginalia, hand-set feel)"
  constraints: []
  desired_output: full_territory_set
  mode: STANDARD
  prior_run: null
```

## Expected behavior
1. Step 5 extracts a distinct principle from each reference: Doré →
   high-contrast linework/weight-without-color (color behavior axis);
   codex/manuscript → marginalia as persistent structural device, not
   overlay/modal (composition axis). The two references are not collapsed
   into a single generic "vintage book" treatment.
2. Step 1 derives that "reflective, not optimizing" rules out gamified
   progress mechanics.
3. Step 4 flags any territory reintroducing streaks/progress-bars/
   color-coded metric dashboards as a quantified-self-category default
   working against this strategy.
4. Divergence audit run per step 3; any territory that only changes
   background warmth/paper tone from another must be rebuilt or merged,
   not kept as a false-distinct option (see discarded "Marginal Notes" in
   `examples/02-dore-codex-personal-os.md` for the reference pattern).

## Expected artifacts
- `VISUAL_TERRITORIES.md` — territories show the two reference principles
  applied to different axes, not merged into one axis.
- `APPROVED_VISUAL_DIRECTION.md` — motion principle states near-zero/
  settling motion (not celebratory animation); color logic states
  grayscale/near-monochrome by default.
- `VISUAL_ANTI_PATTERNS.md` — explicitly rules out streak counters,
  progress rings, gamified completion percentages, and color-coded
  category tagging as competitor/category defaults.
- `GENERATION_LANGUAGE.md` — a "weight without color" or equivalent
  principle stated generally enough to apply to icon, empty-state, and
  other asset types.

## Forbidden behavior
- Must not merge the two supplied references into one undifferentiated
  "old book" aesthetic with no axis-level attribution.
- Must not include gamification elements (streaks, progress bars, badges)
  anywhere in the selected direction — this directly contradicts
  "reflective, not optimizing."
- Must not treat "archival" as a license to add heavy skeuomorphic
  decoration disconnected from the marginalia/structural principle.

## Pass criteria
- [ ] Each of the two supplied references maps to a distinct, named
      structural principle on a distinct axis.
- [ ] Gamification patterns are explicitly named and ruled out in
      `VISUAL_ANTI_PATTERNS.md`.
- [ ] Selected direction's motion principle is stated (not left silent)
      and consistent with "reflective, not optimizing."
- [ ] All four required artifacts exist with the content properties above.
