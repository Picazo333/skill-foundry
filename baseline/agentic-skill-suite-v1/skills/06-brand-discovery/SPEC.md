# SPEC — Brand Discovery

## Identity
**ID:** `brand-discovery`  
**Category:** brand

## Purpose
Turn fragmented founder/client/business information into a canonical brand discovery brief separating facts, aspirations, hypotheses, references and constraints.

## Trigger when
- Starting or repositioning a brand.
- Client discovery data exists.
- Need foundation before strategy/design.

## Do not use for
- Final positioning.
- Logo design.
- Generic moodboard generation.

## Minimum inputs
- raw client/project/business context

## Optional inputs
- interviews
- analytics
- competitor notes
- existing identity
- references/anti-references

## Required outputs
- `BRAND_DISCOVERY_BRIEF.md`
- `DISCOVERY_GAPS.md`
- `REFERENCE_MAP.md`

## Procedure
1. Inventory business, offer, customer, market, founder and operational context.
2. Separate FACTS / CLAIMS / ASPIRATIONS / HYPOTHESES / NON-NEGOTIABLES.
3. Extract customer language, desired perception, current perception and business objective.
4. Map references and anti-references by underlying quality, not superficial similarity.
5. Identify contradictions such as premium vs accessible or expressive vs clinical.
6. Identify only discovery gaps that materially block strategy.
7. Produce canonical discovery brief and compact gap list.
8. Stop before strategic or visual decisions.

## Quality gates
- Facts/hypotheses separated.
- Anti-references captured.
- Business objective explicit.
- No premature design.
- Gap list is decision-relevant only.

## Handoffs
- `brand-strategy`
- `research-architect`
- `canonical-context-builder`

## Required eval scenarios
- Dental clinic discovery.
- Streetwear brand with aggressive references.
- B2B automation agency with unclear offer.

## Sonnet implementation requirements
- Convert this into executable `SKILL.md`.
- Define required/optional/do-not-load context.
- Add compact I/O schemas, failure modes, stop conditions.
- Add 3+ evals plus an edge/failure case.
- Keep shared rules in `/shared`.
- Generate thin generic/ChatGPT/Codex/Claude/Gemini/Cursor adapters.
- Support artifact/checkpoint resume without prior chat memory.
