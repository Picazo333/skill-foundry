# SPEC — Brand Book Builder

## Identity
**ID:** `brand-book-builder`  
**Category:** brand

## Purpose
Assemble validated strategy, verbal and identity artifacts into a coherent brand manual without reopening upstream decisions.

## Trigger when
- Strategy + verbal/visual/identity artifacts exist.
- Need client-facing or operational brand book.

## Do not use for
- Doing discovery.
- Reinventing positioning.
- Silently fixing poor upstream strategy.

## Minimum inputs
- brand canon artifacts

## Optional inputs
- brand-book audience
- format constraints
- examples/assets

## Required outputs
- `BRAND_BOOK.md`
- `BRAND_BOOK_OUTLINE.md`
- `BRAND_BOOK_ASSET_CHECKLIST.md`

## Procedure
1. Validate upstream artifacts and flag missing/contradictory inputs.
2. Choose book depth: executive, operational or full.
3. Build narrative sequence: essence → strategy → voice → visual system → applications → governance.
4. Deduplicate repeated rationale while preserving necessary rules.
5. Insert DO/DON’T examples and application guidance.
6. Separate immutable canon from optional inspiration.
7. Create asset checklist for missing examples/visuals.
8. Run usability test: can a designer/writer/agent execute from the book?
9. Stop without silently changing upstream canon.

## Quality gates
- No contradictory rules.
- No filler for page count.
- Operational examples clear.
- Upstream problems surfaced.
- Book works without original chat.

## Handoffs
- `brand-quality-auditor`
- `creative-brief-generator`
- `brand-content-system`

## Required eval scenarios
- Compact startup brand book.
- Full client manual.
- Brand book with conflicting upstream artifacts.

## Sonnet implementation requirements
- Convert this into executable `SKILL.md`.
- Define required/optional/do-not-load context.
- Add compact I/O schemas, failure modes, stop conditions.
- Add 3+ evals plus an edge/failure case.
- Keep shared rules in `/shared`.
- Generate thin generic/ChatGPT/Codex/Claude/Gemini/Cursor adapters.
- Support artifact/checkpoint resume without prior chat memory.
