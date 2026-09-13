---
name: brand-strategy
description: Converts a brand discovery brief and its evidence into a defensible strategy — category, audience, positioning, promise, differentiation and guardrails — specific enough to constrain verbal and visual work downstream; use once a discovery brief exists and positioning is needed, not for writing the brand book/verbal system or choosing fonts, colors or visual system.
---

# Brand Strategy

> Canonical skill definition. Adapters in `adapters/` are thin wrappers over
> this file — they may not change purpose, procedure, outputs, quality gates
> or stop conditions. See `/PORTABILITY.md` and `/shared/adapters/README.md`.

## Identity
- **ID:** `brand-strategy`
- **Category:** brand
- **Version:** `1.0.0`
- **Purpose:** Convert a brand discovery brief and its evidence into a
  defensible strategy — category, audience, positioning, promise, value
  proposition, differentiation, proof and guardrails — that is specific
  enough to constrain both verbal and visual work downstream.

## Trigger
Use this skill when:
- A `BRAND_DISCOVERY_BRIEF.md` exists and is adequate (has audience
  evidence, a competitive frame, and at least some distinguishing facts).
- A positioning/strategy decision is needed before identity (verbal or
  visual) work can start.
- An existing brand is being repositioned and needs a new/updated strategy.

## Non-trigger
Do not use this skill for:
- Writing the brand book (voice, verbal system, tone-of-voice rules) — that
  is `brand-verbal-identity`.
- Choosing fonts, colors, logo direction, or any visual system — that is
  `brand-visual-direction`.
- Generating social posts, ad copy, or other production content — that is
  `brand-content-system` / `creative-brief-generator`.
- Building the discovery brief itself from raw research/interviews — that is
  `brand-discovery`, which this skill consumes.

## Context policy
- **REQUIRED_CONTEXT:** `BRAND_DISCOVERY_BRIEF.md`.
- **OPTIONAL_CONTEXT:** research findings, a competitor map, voice-of-customer
  (VoC) evidence, business model documentation, and — in `mode: UPDATE` — the
  prior `BRAND_STRATEGY.md` / `POSITIONING_SYSTEM.md` as `prior_run`.
- **DO_NOT_LOAD_BY_DEFAULT:** any verbal-identity or visual-direction drafts
  (downstream artifacts — loading them biases positioning toward an
  executional answer instead of a strategic one), the full raw discovery
  conversation once `BRAND_DISCOVERY_BRIEF.md` exists, and unrelated brand
  projects' canon.

Prefer canonical artifacts over conversational memory (`ARCHITECTURE.md`).

## Inputs

### Minimum inputs
- `BRAND_DISCOVERY_BRIEF.md`

### Optional inputs
- Research findings
- Competitor map
- Voice-of-customer (VoC) evidence
- Business model documentation
- Prior `BRAND_STRATEGY.md` / `POSITIONING_SYSTEM.md` (required as
  `prior_run` when `mode: UPDATE`)

### RUN_REQUEST envelope
```yaml
RUN_REQUEST:
  objective:            # e.g. "define initial strategy" | "reposition after category shift"
  source_artifacts:      # must include BRAND_DISCOVERY_BRIEF.md; optionally research/competitor map/VoC/business model
  known_context:         # anything already established outside the brief, if relevant
  constraints:           # e.g. "regulated category — no comparative claims", "no repositioning of the name"
  desired_output:        # full_strategy_set | specific_artifact
  mode: STANDARD          # STANDARD (new strategy) | UPDATE (repositioning against prior strategy)
  prior_run:              # path to prior BRAND_STRATEGY.md/POSITIONING_SYSTEM.md, required when mode: UPDATE
```

## Procedure
Numbered, executable steps. Two independent runs against the same discovery
brief should converge on materially the same strategic recommendation.

1. **Verify inputs.** Confirm `BRAND_DISCOVERY_BRIEF.md` is present and
   check it has: (a) some audience/customer evidence, (b) some competitive
   or category frame, (c) at least one fact that could support
   differentiation. If any of these is entirely absent and no optional
   input fills the gap, stop — go to the BLOCKED stop condition rather than
   inventing the missing evidence. In `mode: UPDATE`, also load `prior_run`
   as the baseline to reposition against.
2. **Identify the strategic decision and constraints.** State in one or two
   sentences the actual decision this run must resolve (e.g. "position a
   new entrant in a commoditized category" / "reposition after a pivot").
   Pull hard constraints from the discovery brief and any business model
   doc (regulatory limits, category conventions that can't be broken,
   budget-driven scope limits, naming/legal constraints).
3. **Define audience/ICP at useful resolution.** Derive the audience
   description directly from evidence in the discovery brief and VoC (if
   supplied). State confidence per attribute. Where evidence is thin, mark
   the gap explicitly as an assumption requiring validation — do not
   manufacture demographic or psychographic detail the brief never
   supported (see `references/audience-and-differentiation-evidence.md`,
   and the fictional-persona failure mode below).
4. **Map category, alternatives and competitive frame.** List direct
   competitors, indirect/substitute alternatives, and "do nothing" as a
   competitor. Note the category's dominant conventions/clichés — these are
   what a distinctive position must depart from. Use a supplied competitor
   map if available; otherwise derive a minimal frame from the discovery
   brief alone and flag it as minimal.
5. **Generate positioning territories.** Generate 3–5 genuinely distinct
   positioning territories — different strategic bets, not restatements of
   one idea. Score each on distinctiveness, credibility, relevance,
   extensibility and business fit per
   `references/positioning-territory-scoring.md`. Every score must cite the
   evidence or constraint it's based on.
6. **Recommend and document rejection.** Select the highest-scoring
   territory that no constraint blocks. Write the recommendation rationale
   tied explicitly to its scores and evidence. Document every discarded
   territory in `POSITIONING_SYSTEM.md` with the specific reason it lost
   (tied to its own scores — never a generic "didn't fit").
7. **Define the strategy payload.** From the recommended territory, define:
   value proposition, brand promise, 3–5 strategic pillars, reasons-to-believe
   (RTBs — each traceable to a discovery-brief fact), a differentiation
   statement, and the desired perception (how the audience should describe
   the brand unprompted).
8. **Define anti-goals and strategic guardrails.** State what the brand must
   never claim, imply, or do; which category conventions it deliberately
   breaks vs. deliberately conforms to (and why); and the boundaries that
   verbal and visual work must operate inside. Every guardrail must be
   operational — testable against a real downstream output — not a mood
   word. See `references/category-and-commoditization-test.md`.
9. **Run the contradiction/commoditization test.** Check the recommended
   strategy doesn't contradict any discovery-brief fact or constraint from
   step 2. Then run the swap test: could a direct competitor's name replace
   this brand's name in the positioning statement without it reading as
   wrong? If yes, the position is commoditized — return to step 5/6 and
   regenerate/re-score rather than shipping it.
10. **Stop when the strategy is usable.** Stop once the strategy is specific
    enough that it could visibly rule out an obviously wrong verbal or
    visual direction (i.e. it constrains, not just describes). Produce
    `RUN_RESULT` with `handoff` to both `brand-verbal-identity` and
    `brand-visual-direction`.

### Checkpoints
For a `DEEP`/multi-territory run, checkpoint after step 5 (territories
generated and scored, before recommendation) recording the territory list,
scores and evidence citations so a resumed run doesn't regenerate territories
from scratch — it resumes at step 6 (recommend/reject) with the existing
scoring table.

## Outputs

### Required output artifacts
- `BRAND_STRATEGY.md` — strategic decision, audience, category frame, value
  proposition, promise, pillars, RTBs, differentiation statement, desired
  perception.
- `POSITIONING_SYSTEM.md` — all generated territories with their five-axis
  scores and evidence citations, the recommended territory with rationale,
  and every discarded territory with its specific rejection reason.
- `STRATEGIC_GUARDRAILS.md` — anti-goals, conventions kept vs. broken, and
  operational boundaries for verbal and visual work.

### RUN_RESULT envelope
```yaml
RUN_RESULT:
  status:      # COMPLETE | PARTIAL | BLOCKED
  summary:
  artifacts:   # [BRAND_STRATEGY.md, POSITIONING_SYSTEM.md, STRATEGIC_GUARDRAILS.md] on COMPLETE
  decisions:   # the recommended territory + why, and any constraint-driven calls
  unresolved:  # evidence gaps, assumptions flagged for validation
  handoff:     # next_skill(s) + reason — brand-verbal-identity and brand-visual-direction
  quality:     # gate results (see Quality gates below)
```

### Output schema
See `schemas/output.schema.json` for the machine-checkable shape of the
artifact set / RUN_RESULT.

## Handoffs
- → `brand-verbal-identity` — receives `BRAND_STRATEGY.md` +
  `STRATEGIC_GUARDRAILS.md` as the strategic foundation for tone of voice,
  verbal system and messaging; must not need to re-derive positioning.
- → `brand-visual-direction` — receives the same two artifacts in parallel
  as the strategic foundation for visual territory exploration; must not
  need to re-derive positioning. These two handoffs happen from the same
  completed run (they branch, per `routing-graph.json` / `WORKFLOW_MAP.md`)
  — this skill does not sequence or wait between them.
- → `brand-skill-orchestrator` — when this run is part of a routed
  multi-stage brand workflow and the orchestrator needs to decide the next
  step.

## Failure modes
Concrete ways this skill can go wrong, and what to do instead:
- **Generic/commoditized positioning.** Detect: the swap test in step 9
  passes (a competitor's name fits as well as this brand's). Fix: reject the
  territory, regenerate, and re-score — never ship a position that reads as
  category-generic to hit a deadline.
- **Differentiation not connected to evidence.** Detect: a claim in
  `BRAND_STRATEGY.md` (value prop, RTB, differentiation statement) has no
  traceable source in the discovery brief or optional inputs. Fix: cut the
  claim, or find the supporting evidence — never assert unsupported
  differentiation.
- **Fictional persona invention.** Detect: the audience section states
  specific demographic/psychographic detail the discovery brief never
  described. Fix: state it as a flagged assumption in `unresolved`, not as
  fact — audience resolution follows evidence, not narrative convenience.
- **Visual or verbal execution leakage.** Detect: `BRAND_STRATEGY.md` or
  `POSITIONING_SYSTEM.md` specifies colors, typography, logo direction, or
  actual tone-of-voice copy/word choices. Fix: strip it — this skill defines
  the *what and why*; *how it sounds* is `brand-verbal-identity`, *how it
  looks* is `brand-visual-direction`.
- **Discarded alternatives omitted.** Detect: `POSITIONING_SYSTEM.md` shows
  only the recommended territory. Fix: regenerate the full 3–5 territory set
  and document every rejection with its specific reason — this is required
  so the decision isn't re-litigated later without new evidence.
- **Guardrails too vague to test.** Detect: a guardrail reads as a mood
  word ("feel premium") rather than a checkable rule. Fix: rewrite as an
  operational boundary (e.g. "never lead with price in any headline claim").
- **Forcing a COMPLETE status on thin evidence.** Detect: the discovery
  brief lacks audience evidence, competitive frame, or any distinguishing
  fact, and none of the optional inputs fill the gap. Fix: stop at BLOCKED
  (see Stop conditions) — do not invent evidence to force a complete-looking
  strategy.

## Quality gates
Skill must satisfy `/QUALITY_GATES.md` skill-level gates 1–10, plus the
SPEC-level gates:
- Positioning is not generic (passes the commoditization swap test).
- Differentiation connects to evidence/choice — every RTB and differentiation
  claim traces to a discovery-brief or optional-input fact.
- Discarded alternatives are documented with specific, not generic, reasons.
- Guardrails are operational (each is checkable against a real downstream
  output).
- No visual-execution or verbal-execution leakage into strategy artifacts.

## Stop conditions
- **Normal completion:** all three required artifacts produced, the
  contradiction/commoditization test passed, discarded territories
  documented, guardrails operational → `status: COMPLETE`.
- **Blocked (insufficient input):** the discovery brief (plus any optional
  inputs supplied) lacks audience evidence, a competitive frame, or any
  distinguishing fact needed to support a differentiated position →
  `status: BLOCKED`, state exactly what discovery-level evidence is
  missing, and recommend re-running `brand-discovery` to gather it. This is
  the expected outcome for a weak/generic discovery brief — not a failure
  to work around.
- **Never continue past:** shipping a positioning that fails the
  commoditization swap test, or inventing audience/differentiation facts
  the discovery brief does not support, just to reach `status: COMPLETE`.

## Examples
See `examples/` for one worked input → output pair per required eval
scenario (orthodontic brand, AI consulting agency, consumer apparel brand).

## Evals
See `evals/` — 3 core scenarios (orthodontic brand, AI consulting agency,
consumer apparel brand, per `SPEC.md`) + 1 edge/failure case (weak/generic
discovery input), using `/shared/templates/EVAL_TEMPLATE.md`.
