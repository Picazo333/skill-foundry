# SPEC — Brand Identity System

## Identity
**ID:** `brand-identity-system`  
**Category:** brand

## Purpose
Turn approved visual/verbal direction into a coherent operational identity system with rules that survive real production.

## Trigger when
- Approved Brand Strategy + Visual Direction.
- Need identity rules before brand book.

## Do not use for
- Inventing strategy.
- Random logo ideation.
- Building every campaign asset.

## Minimum inputs
- BRAND_STRATEGY.md
- APPROVED_VISUAL_DIRECTION.md

## Optional inputs
- VERBAL_IDENTITY.md
- logo assets
- font constraints
- production channels

## Required outputs
- `IDENTITY_SYSTEM.md`
- `DESIGN_TOKENS.json`
- `APPLICATION_RULES.md`

## Procedure
1. Define identity architecture: marks, lockups and relationships when applicable.
2. Define color roles and contrast behavior, not only swatches.
3. Define typography roles, hierarchy, fallback and responsive behavior.
4. Define grid, spacing, shapes, borders, texture, imagery and iconography systems.
5. Define motion principles and UI translation where relevant.
6. Create application rules across web, social, decks, documents, ads and product/UI.
7. Define exceptions and forbidden combinations.
8. Create machine-readable design tokens where practical.
9. Run consistency and scalability audit.

## Quality gates
- Rules operational.
- Works across at least five surfaces.
- Tokens match prose.
- Accessibility/legibility considered.
- Exceptions documented.

## Handoffs
- `brand-book-builder`
- `creative-brief-generator`
- `brand-quality-auditor`

## Required eval scenarios
- Web-first service brand.
- App/product brand.
- Social-heavy consumer brand.

## Sonnet implementation requirements
- Convert this into executable `SKILL.md`.
- Define required/optional/do-not-load context.
- Add compact I/O schemas, failure modes, stop conditions.
- Add 3+ evals plus an edge/failure case.
- Keep shared rules in `/shared`.
- Generate thin generic/ChatGPT/Codex/Claude/Gemini/Cursor adapters.
- Support artifact/checkpoint resume without prior chat memory.
