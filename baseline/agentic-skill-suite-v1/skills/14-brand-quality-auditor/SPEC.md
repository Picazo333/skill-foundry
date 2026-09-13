# SPEC — Brand Quality Auditor

## Identity
**ID:** `brand-quality-auditor`  
**Category:** brand

## Purpose
Audit any brand output against canonical strategy/verbal/visual rules and detect drift, regression, genericity and AI-slop.

## Trigger when
- Need QA on web/copy/deck/campaign/brand book/content.
- Need compare implementation to approved canon.

## Do not use for
- Creating canon when none exists.
- Subjective aesthetic critique with no criteria.
- Replacing upstream strategy without escalation.

## Minimum inputs
- artifact to audit
- brand canon

## Optional inputs
- specific objective
- channel
- prior audit
- known exceptions

## Required outputs
- `BRAND_QA_REPORT.md`
- `FIX_LIST.md`
- `DRIFT_REGISTER.md`

## Procedure
1. Load only canon sections relevant to the artifact.
2. Check strategic alignment: audience, positioning, promise, claims.
3. Check verbal alignment: voice, vocabulary, message hierarchy.
4. Check visual alignment: composition, typography, color roles, imagery, UI/motion where relevant.
5. Check objective/channel fitness and usability.
6. Detect AI-slop, genericity and over-decoration.
7. Classify PASS / FIX / POLISH / DEFER.
8. Separate canon violation from subjective preference.
9. Generate smallest fix list that restores compliance.

## Quality gates
- Every issue traces to canon/objective.
- No aesthetic fiat.
- Fix list prioritized.
- Approved strategy not casually reopened.
- AI-slop detection operationalized with examples.

## Handoffs
- `brand-book-builder`
- `creative-brief-generator`
- `product-auditor`

## Required eval scenarios
- Website drifting from canon.
- AI-generated social creative.
- Brand book self-audit.

## Sonnet implementation requirements
- Convert this into executable `SKILL.md`.
- Define required/optional/do-not-load context.
- Add compact I/O schemas, failure modes, stop conditions.
- Add 3+ evals plus an edge/failure case.
- Keep shared rules in `/shared`.
- Generate thin generic/ChatGPT/Codex/Claude/Gemini/Cursor adapters.
- Support artifact/checkpoint resume without prior chat memory.
