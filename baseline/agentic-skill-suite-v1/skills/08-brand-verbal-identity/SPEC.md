# SPEC — Brand Verbal Identity

## Identity
**ID:** `brand-verbal-identity`  
**Category:** brand

## Purpose
Create an operational verbal system that governs how a brand sounds across channels, not merely a list of adjectives.

## Trigger when
- Brand Strategy exists.
- Need repeatable voice/copy consistency.

## Do not use for
- Long-form content strategy.
- Final visual system.
- One-off copy request with no reusable need.

## Minimum inputs
- BRAND_STRATEGY.md

## Optional inputs
- existing copy
- customer language
- compliance constraints

## Required outputs
- `VERBAL_IDENTITY.md`
- `MESSAGE_HIERARCHY.md`
- `VOICE_EXAMPLES.md`

## Procedure
1. Translate strategy into 3–5 behavioral voice principles.
2. Define tone modulation by context: sales, support, education, social, crisis, product/UI.
3. Build vocabulary: preferred, avoided and prohibited claims where relevant.
4. Create message hierarchy: master message, pillars, proofs, elevator pitch, descriptions, tagline territories.
5. Write DO/DON’T examples that make boundaries observable.
6. Define syntax/rhythm/complexity conventions where useful.
7. Stress-test voice across at least four channels.
8. Stop when another writer/agent can reproduce voice without imitation prompts.

## Quality gates
- Voice principles behavioral.
- DO/DON’T examples included.
- Compliance boundaries included where relevant.
- Messaging aligns to positioning.
- Not dependent on founder imitation.

## Handoffs
- `brand-book-builder`
- `brand-content-system`
- `creative-brief-generator`
- `brand-quality-auditor`

## Required eval scenarios
- Medical compliance tone.
- Streetwear voice.
- B2B technical brand.

## Sonnet implementation requirements
- Convert this into executable `SKILL.md`.
- Define required/optional/do-not-load context.
- Add compact I/O schemas, failure modes, stop conditions.
- Add 3+ evals plus an edge/failure case.
- Keep shared rules in `/shared`.
- Generate thin generic/ChatGPT/Codex/Claude/Gemini/Cursor adapters.
- Support artifact/checkpoint resume without prior chat memory.
