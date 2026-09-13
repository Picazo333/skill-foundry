# SPEC — Brand Strategy

## Identity
**ID:** `brand-strategy`  
**Category:** brand

## Purpose
Convert discovery and evidence into a defensible strategy: category, audience, positioning, promise, value proposition, differentiation, proof and guardrails.

## Trigger when
- Discovery brief is adequate.
- Need positioning before identity.
- Repositioning an existing brand.

## Do not use for
- Writing the brand book.
- Choosing fonts/colors.
- Generating social posts.

## Minimum inputs
- BRAND_DISCOVERY_BRIEF.md

## Optional inputs
- research findings
- competitor map
- VoC
- business model

## Required outputs
- `BRAND_STRATEGY.md`
- `POSITIONING_SYSTEM.md`
- `STRATEGIC_GUARDRAILS.md`

## Procedure
1. Identify the strategic decision and constraints from discovery.
2. Define audience/ICP at useful resolution; avoid fictional personas when evidence is weak.
3. Map category, alternatives and competitive frame.
4. Generate multiple positioning territories and score distinctiveness, credibility, relevance, extensibility and business fit.
5. Recommend a strategy with rationale and discarded alternatives.
6. Define value proposition, promise, pillars, reasons-to-believe, differentiation and desired perception.
7. Define anti-goals and strategic guardrails.
8. Run contradiction/commoditization test; stop when strategy can guide verbal and visual work.

## Quality gates
- Positioning is not generic.
- Differentiation connects to evidence/choice.
- Discarded alternatives documented.
- Guardrails operational.
- No visual-execution leakage.

## Handoffs
- `brand-verbal-identity`
- `brand-visual-direction`
- `brand-skill-orchestrator`

## Required eval scenarios
- Orthodontic brand.
- AI consulting agency.
- Consumer apparel brand.

## Sonnet implementation requirements
- Convert this into executable `SKILL.md`.
- Define required/optional/do-not-load context.
- Add compact I/O schemas, failure modes, stop conditions.
- Add 3+ evals plus an edge/failure case.
- Keep shared rules in `/shared`.
- Generate thin generic/ChatGPT/Codex/Claude/Gemini/Cursor adapters.
- Support artifact/checkpoint resume without prior chat memory.
