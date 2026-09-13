# SPEC — Creative Brief Generator

## Identity
**ID:** `creative-brief-generator`  
**Category:** brand

## Purpose
Translate brand canon plus a specific business objective into an execution-ready brief for web, campaign, social, video, deck, packaging or generated media.

## Trigger when
- Concrete creative deliverable needed.
- Brand canon exists.
- Need handoff to production agent/team.

## Do not use for
- Defining brand strategy.
- Generic ideation without objective.
- Producing final assets by default.

## Minimum inputs
- brand canon
- deliverable objective

## Optional inputs
- channel
- audience
- offer
- CTA
- constraints
- references
- deadline

## Required outputs
- `CREATIVE_BRIEF.md`
- `ASSET_REQUIREMENTS.md`
- `PRODUCTION_HANDOFF.md`

## Procedure
1. Identify business/communication objective and success signal.
2. Extract only relevant canon; do not dump the entire brand book.
3. Define audience/context/job of the asset.
4. Define single-minded message, support points and CTA.
5. Define visual/verbal requirements and anti-patterns.
6. Specify format/channel constraints and variants.
7. Define mandatory assets/data/legal/compliance inputs.
8. Write production acceptance criteria.
9. Generate handoff tailored to execution medium.

## Quality gates
- One clear objective.
- No conflicting messages.
- Relevant canon only.
- Acceptance criteria usable for QA.
- No unsupported claims.

## Handoffs
- `brand-quality-auditor`
- `brand-content-system`

## Required eval scenarios
- Landing page brief.
- Reel/video brief.
- Executive deck brief.

## Sonnet implementation requirements
- Convert this into executable `SKILL.md`.
- Define required/optional/do-not-load context.
- Add compact I/O schemas, failure modes, stop conditions.
- Add 3+ evals plus an edge/failure case.
- Keep shared rules in `/shared`.
- Generate thin generic/ChatGPT/Codex/Claude/Gemini/Cursor adapters.
- Support artifact/checkpoint resume without prior chat memory.
