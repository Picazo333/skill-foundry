---
name: brand-content-system
description: Turns approved brand canon into a repeatable content operating system — pillars traceable to strategy, format/channel rules, production cadence and reusable templates — for ongoing content production; use when recurring content output is needed and canon already exists and is approved, not for a single one-off deliverable or for defining brand positioning, promise or audience.
---

# Brand Content System

> Canonical skill definition. Adapters in `adapters/` are thin wrappers over
> this file — they may not change purpose, procedure, outputs, quality gates
> or stop conditions. See `/PORTABILITY.md` and `/shared/adapters/README.md`.

## Identity
- **ID:** `brand-content-system`
- **Category:** brand
- **Version:** `1.0.0`
- **Purpose:** Turn approved brand canon into a repeatable content operating
  system — pillars traceable to strategy, format/channel rules, production
  cadence and reusable templates — for ongoing content production, not a
  one-off brief or a generic posting calendar.

## Trigger
Use this skill when:
- Ongoing/recurring content production is needed (a "content factory"), not a
  single deliverable.
- Brand strategy and verbal identity (or a compiled brand book) already exist
  and are approved.
- A team needs a structure that keeps producing on-strategy content without
  re-deriving pillars/formats from scratch every time.

## Non-trigger
Do not use this skill for:
- A single social caption, post, or one-off creative deliverable — that is
  `creative-brief-generator`, which this skill feeds.
- Defining brand positioning, promise or audience — that is `brand-strategy`
  / `brand-discovery`. This skill consumes strategy, it does not create it.
- A plain editorial calendar (dates + topics) with no system logic behind
  it — a calendar without pillars/formats/measurement tied to the journey is
  not this skill's output.
- Auditing existing content against canon — that is `brand-quality-auditor`.

## Context policy
- **REQUIRED_CONTEXT:** approved brand canon — at minimum `BRAND_STRATEGY.md`
  (positioning, promise, differentiators, audience) and `VERBAL_IDENTITY.md`
  (voice, vocabulary, banned topics/claims). If `BRAND_BOOK.md` exists, it
  satisfies both.
- **OPTIONAL_CONTEXT:** channel analytics/history, competitor or creator
  research, the offer/funnel definition, production constraints (team size,
  budget, tooling), prior `CONTENT_SYSTEM.md` (for `mode: UPDATE`).
- **DO_NOT_LOAD_BY_DEFAULT:** the full brand-discovery conversation history,
  unrelated skills' canon (e.g. product-audit findings), individual past
  social posts (use analytics summaries, not raw post archives).

Prefer canonical artifacts over conversational memory.

## Inputs

### Minimum inputs
- `BRAND_STRATEGY.md` (or `BRAND_BOOK.md` covering strategy)
- `VERBAL_IDENTITY.md` (or `BRAND_BOOK.md` covering voice)

### Optional inputs
- Channel analytics / performance history
- Competitor or creator research
- Offer/funnel definition
- Production constraints (team size, cadence capacity, budget, tooling)
- Regulatory/compliance constraints for the vertical (e.g. health claims,
  gambling/betting advertising rules)

### RUN_REQUEST envelope
```yaml
RUN_REQUEST:
  objective:            # e.g. "build initial content system" | "revise pillars after Q3 offer change"
  source_artifacts:      # [BRAND_STRATEGY.md, VERBAL_IDENTITY.md, ...]
  known_context:         # offer/funnel, channels in use, team capacity, vertical constraints
  constraints:            # e.g. "1 editor, 2hr/week", "no medical claims", "18+ jurisdiction rules"
  desired_output:         # full_system | specific_artifact
  mode: STANDARD          # STANDARD (build) | UPDATE (delta against prior system) | AUDIT (capacity/compliance check only)
  prior_run:              # path to prior CONTENT_SYSTEM.md, if mode: UPDATE
```

## Procedure
Numbered, executable steps. Two independent runs against the same canon
should converge on materially the same pillar set and system structure.

1. **Verify canon is stable.** Confirm `BRAND_STRATEGY.md` and
   `VERBAL_IDENTITY.md` (or `BRAND_BOOK.md`) exist and are marked
   approved/locked, not draft. If canon is missing or explicitly in-review →
   `status: BLOCKED` (see Stop conditions). Never build a content system on
   canon that could still change under it.
2. **Map the customer/commercial journey.** For the audience defined in
   strategy, state the real question/objection at each stage:
   - Attention — "does this brand know my specific problem?"
   - Trust — "can I believe what they claim?"
   - Intent — "why this brand over the alternative I'm also considering?"
   - Conversion — "what happens, concretely, if I act now?"
   - Retention — "did I make the right call, and is there more here for me?"
3. **Derive content pillars from strategy, not from a generic list.** For
   each journey stage, identify the specific differentiator, proof point, or
   positioning claim in `BRAND_STRATEGY.md` that answers that stage's
   question for *this* brand. That claim — named in the brand's own
   vocabulary from `VERBAL_IDENTITY.md` — is a candidate pillar. Merge
   candidates that trace to the same underlying claim across stages (one
   pillar can serve more than one stage). **Reject any candidate that does
   not trace to a specific line in strategy** — "tips", "behind the scenes",
   "testimonials" are not pillars unless the strategy names a specific
   reason *this* brand's tips/BTS/testimonials matter (e.g. proprietary
   method, founder credibility, regulated-industry proof requirement).
   Target 3–5 pillars; more than 5 usually means pillars weren't merged
   properly or capacity won't sustain them (see step 6).
4. **Define format archetypes per pillar.** For each pillar, specify
   repeatable series: hook pattern, body structure, proof element, CTA, and
   target duration/length — concrete enough that a producer can execute
   without reinventing the format each time. A format is not repeatable if
   it depends on a one-off idea; it must be a structure other content in the
   same pillar can reuse.
5. **Map channels by role, not by copy-paste.** For each channel in scope,
   state which pillar(s) it carries, which journey stage(s) it serves, and
   how the *same* pillar's format changes for that channel's constraints
   (length, algorithm behavior, native format). Never assume one asset
   ships unmodified across channels.
6. **Define the source-to-content pipeline.** Name the recurring inputs that
   feed content without requiring net-new ideation each time: research
   findings, FAQs/objections from sales or support, customer cases, product
   changelog/roadmap, founder/SME insight. Map each source to the pillar(s)
   it feeds.
7. **Set cadence from stated production capacity — never aspirational
   volume.** If `known_context`/`constraints` state team size, hours/week,
   or budget, compute a cadence per pillar/channel that fits it explicitly
   (show the arithmetic: e.g. "2hr/week ÷ ~45min per piece ≈ 2 pieces/week
   sustainably"). If capacity is not stated, do not invent a number — mark
   cadence as `capacity_unknown` in `CONTENT_PIPELINE.md`, propose a
   conservative starting cadence explicitly labeled as an assumption, and
   list confirming production capacity as an unresolved item.
8. **Define compliance/claim boundaries.** Pull from `VERBAL_IDENTITY.md`
   banned claims/topics and any stated regulatory constraints (health,
   financial, gambling/betting, age-gating, etc.). List them as hard
   boundaries per pillar/channel, not a generic disclaimer.
9. **Define measurement and feedback loops.** Assign each pillar a metric
   appropriate to the journey stage(s) it serves (e.g. attention → reach/
   watch-time/completion; trust → saves/shares/comment sentiment; intent →
   profile visits/link clicks; conversion → attributed leads/sales;
   retention → repeat engagement/LTV signal). Explicitly state which metrics
   must NOT be read as revenue proxies (views/reach are not conversion).
   Define the review cadence (e.g. monthly) and what triggers a pillar
   revision (e.g. two review cycles of a pillar underperforming its stage
   metric).
10. **Create reusable brief templates for `creative-brief-generator`.** For
    each pillar/format pair, produce a fillable brief skeleton (objective,
    pillar, format archetype, channel variant, mandatory proof, CTA,
    compliance boundary) so a specific-deliverable brief can be generated
    without re-deriving system logic each time.
11. **Delta mode.** If `mode: UPDATE` and a prior `CONTENT_SYSTEM.md` exists,
    diff against it: only revise pillars/formats/cadence that the new
    context actually changes (e.g. a new offer, a capacity change, a
    consistently underperforming pillar from step 9's review trigger); leave
    stable sections untouched and record what changed and why.
12. **Stop** when a producer or `creative-brief-generator` could generate an
    on-strategy piece using only the five required artifacts — no need to
    re-read brand discovery conversations or re-derive pillar logic.

### Checkpoints
For large/multi-channel systems, checkpoint after step 3 (pillars locked,
each with its traced strategy source) and after step 7 (cadence set against
stated capacity), recording pillar list + sources + cadence so a resumed run
does not re-derive pillars from scratch.

## Outputs

### Required output artifacts
- `CONTENT_SYSTEM.md` — the system overview: journey map, pillar summary,
  channel-role map, review cadence; the top-level document that ties the
  other four together.
- `CONTENT_PILLARS.md` — each pillar with its traced strategy source, the
  journey stage(s) it serves, and why it is specific to this brand (not
  generic).
- `FORMAT_LIBRARY.md` — repeatable format archetypes per pillar (hook/body/
  proof/CTA/duration), with per-channel variants.
- `CONTENT_PIPELINE.md` — source-to-content map, cadence (with capacity
  arithmetic or explicit `capacity_unknown` flag), and compliance boundaries.
- `MEASUREMENT_MODEL.md` — metric per pillar/stage, review cadence, revision
  triggers, and an explicit list of metrics that must not be read as
  revenue.

### RUN_RESULT envelope
```yaml
RUN_RESULT:
  status:      # COMPLETE | PARTIAL | BLOCKED
  summary:
  artifacts:   # [CONTENT_SYSTEM.md, CONTENT_PILLARS.md, FORMAT_LIBRARY.md, CONTENT_PIPELINE.md, MEASUREMENT_MODEL.md]
  decisions:   # pillar set, cadence, channel-role assignments locked this run
  unresolved:  # e.g. capacity not confirmed, compliance question needing legal review
  handoff:     # recommended next skill + why
  quality:     # gate results
```

### Output schema
See `schemas/output.schema.json` for the machine-checkable shape of the
artifact set / RUN_RESULT.

## Handoffs
- → `creative-brief-generator` — passes `CONTENT_PILLARS.md` +
  `FORMAT_LIBRARY.md` (the brief skeletons from step 10) so each specific
  piece is briefed from the system instead of ad hoc.
- → `brand-quality-auditor` — passes the full artifact set as the canon
  against which produced content is later audited for pillar/format/
  compliance drift.
- → `ai-resource-router` — when production needs a model/tool dispatch
  recommendation for executing the format library at the set cadence.

## Failure modes
- **Building pillars as a generic content-category list.** Detect: a pillar
  in `CONTENT_PILLARS.md` has no traceable line from `BRAND_STRATEGY.md`.
  Fix: cut it or re-derive it from an actual differentiator/proof point.
- **Building on unstable canon.** Detect: strategy/verbal identity is marked
  draft, or a required source artifact is missing. Fix: `status: BLOCKED`,
  name the exact missing/unstable artifact — do not proceed on "reasonable"
  assumptions about strategy.
- **Copy-pasting one format across channels.** Detect: `FORMAT_LIBRARY.md`
  shows identical structure/length across channels with different native
  constraints. Fix: define the per-channel variant explicitly (step 5).
- **Aspirational cadence.** Detect: `CONTENT_PIPELINE.md` cadence has no
  capacity arithmetic behind it and capacity was stated in input. Fix:
  recompute cadence from stated capacity; if capacity was never stated, flag
  `capacity_unknown` rather than picking a number.
- **Confusing views with revenue.** Detect: `MEASUREMENT_MODEL.md` treats a
  reach/view metric as a conversion or revenue signal. Fix: reclassify to
  the correct journey stage and add it to the "not a revenue proxy" list.
- **Silently dropping a compliance boundary.** Detect: a regulated claim/
  topic from `VERBAL_IDENTITY.md` or stated constraints is absent from
  `CONTENT_PIPELINE.md`'s boundaries. Fix: add it explicitly per pillar/
  channel, never as one generic disclaimer line.
- **Duplicating `creative-brief-generator`'s job.** Detect: this skill's
  output includes a fully written, deliverable-ready brief for one specific
  piece (with concrete copy) instead of a reusable skeleton. Fix: keep
  step 10's output at the skeleton level; hand specifics to
  `creative-brief-generator`.

## Quality gates
Skill must satisfy `/QUALITY_GATES.md` skill-level gates 1–10, plus:
- Every pillar in `CONTENT_PILLARS.md` traces to a named line in
  `BRAND_STRATEGY.md` or `VERBAL_IDENTITY.md`.
- Every format in `FORMAT_LIBRARY.md` is repeatable (a structure, not a
  one-off idea) and has at least one per-channel variant where more than one
  channel is in scope.
- `CONTENT_PIPELINE.md` cadence is either arithmetic-backed or explicitly
  flagged `capacity_unknown` — never an unexplained number.
- `MEASUREMENT_MODEL.md` never presents a reach/view/impression metric as a
  revenue or conversion signal.
- CTA/funnel logic in `CONTENT_SYSTEM.md` is explicit per pillar, not
  implied.

## Stop conditions
- Normal completion: all five required artifacts produced, every pillar
  traced to strategy, cadence resolved or explicitly flagged, `status:
  COMPLETE`.
- Blocked: `BRAND_STRATEGY.md`/`VERBAL_IDENTITY.md` (or `BRAND_BOOK.md`) is
  missing, or exists only in draft/unapproved form → `status: BLOCKED`,
  name exactly what must be approved/supplied first (see
  `evals/cases/04-edge-canon-not-approved.md`).
- Never continue past producing pillars that read as a generic content
  checklist detachable from this specific brand's strategy.

## Examples
See `examples/` for at least one worked input → output pair.

## Evals
See `evals/` — minimum 3 scenarios + 1 edge/failure case, using
`shared/templates/EVAL_TEMPLATE.md`.
