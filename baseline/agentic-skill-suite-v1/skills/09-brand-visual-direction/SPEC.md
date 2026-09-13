# SPEC — Brand Visual Direction

## Identity
**ID:** `brand-visual-direction`  
**Category:** brand

## Purpose
Translate strategy into distinct visual territories and a chosen visual grammar before identity assets are systematized.

## Trigger when
- Brand Strategy exists.
- Need art direction/moodboard logic.
- Need to avoid generic AI-generated design.

## Do not use for
- Final brand book.
- Producing every asset.
- Decorative moodboarding with no strategic rationale.

## Minimum inputs
- BRAND_STRATEGY.md

## Optional inputs
- visual references
- anti-references
- existing identity
- media constraints

## Required outputs
- `VISUAL_TERRITORIES.md`
- `APPROVED_VISUAL_DIRECTION.md`
- `VISUAL_ANTI_PATTERNS.md`
- `GENERATION_LANGUAGE.md`

## Procedure
1. Extract visual implications from strategic attributes without literalizing adjectives.
2. Generate 3–5 materially distinct territories covering composition, materiality, type logic, color behavior, image language, motion, density and UI implications.
3. Map references to principles rather than copying style.
4. Identify category clichés and AI-slop risks.
5. Compare territories by differentiation, strategic fit, extensibility, production feasibility and cross-media behavior.
6. Select/recommend direction and preserve discarded territories for audit.
7. Define canonical visual grammar and anti-patterns.
8. Produce promptable generation language describing principles, not one-off scenes.

## Quality gates
- Territories truly distinct.
- Selected direction traces to strategy.
- Anti-patterns explicit.
- Works beyond hero imagery.
- Avoids generic AI aesthetics.

## Handoffs
- `brand-identity-system`
- `creative-brief-generator`
- `brand-quality-auditor`

## Required eval scenarios
- Radiotomography-inspired finance product.
- Doré/codex-inspired personal OS.
- Rose/ivory dental identity.

## Sonnet implementation requirements
- Convert this into executable `SKILL.md`.
- Define required/optional/do-not-load context.
- Add compact I/O schemas, failure modes, stop conditions.
- Add 3+ evals plus an edge/failure case.
- Keep shared rules in `/shared`.
- Generate thin generic/ChatGPT/Codex/Claude/Gemini/Cursor adapters.
- Support artifact/checkpoint resume without prior chat memory.
