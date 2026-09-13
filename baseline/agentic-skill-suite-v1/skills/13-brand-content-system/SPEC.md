# SPEC — Brand Content System

## Identity
**ID:** `brand-content-system`  
**Category:** brand

## Purpose
Create a repeatable content operating system tied to brand strategy and commercial goals rather than a list of post ideas.

## Trigger when
- Need ongoing content production.
- Need content factory architecture.
- Brand strategy/verbal identity exist.

## Do not use for
- One social caption.
- Brand positioning.
- Pure editorial calendar without system logic.

## Minimum inputs
- BRAND_STRATEGY.md
- VERBAL_IDENTITY.md

## Optional inputs
- channel analytics
- competitor/creator research
- offer/funnel
- production constraints

## Required outputs
- `CONTENT_SYSTEM.md`
- `CONTENT_PILLARS.md`
- `FORMAT_LIBRARY.md`
- `CONTENT_PIPELINE.md`
- `MEASUREMENT_MODEL.md`

## Procedure
1. Map customer/commercial journey: attention → trust → intent → conversion → retention.
2. Define content jobs and pillars tied to that journey.
3. Define repeatable series and format archetypes: hook, body, proof, CTA, duration/format.
4. Map channels by role rather than copy-pasting.
5. Define source-to-content pipeline from research, FAQs, cases, product and founder insight.
6. Set cadence from production capacity, not aspirational volume.
7. Define compliance/claim boundaries where relevant.
8. Define measurement and feedback loops.
9. Create reusable brief templates feeding Creative Brief Generator.

## Quality gates
- Pillars map to business/customer goals.
- Formats repeatable.
- CTA/funnel logic explicit.
- Metrics do not confuse views with revenue.
- System fits production capacity.

## Handoffs
- `creative-brief-generator`
- `brand-quality-auditor`
- `ai-resource-router`

## Required eval scenarios
- Dental reels system.
- Tipster/restricted social content system.
- B2B founder-led content factory.

## Sonnet implementation requirements
- Convert this into executable `SKILL.md`.
- Define required/optional/do-not-load context.
- Add compact I/O schemas, failure modes, stop conditions.
- Add 3+ evals plus an edge/failure case.
- Keep shared rules in `/shared`.
- Generate thin generic/ChatGPT/Codex/Claude/Gemini/Cursor adapters.
- Support artifact/checkpoint resume without prior chat memory.
