# Evals — Brand Verbal Identity

4 cases in `cases/`: 3 core scenarios (from `SPEC.md`'s required eval
scenarios) + 1 edge/failure case. Each follows
`/shared/templates/EVAL_TEMPLATE.md`.

| Case | Type | Tests |
|---|---|---|
| `01-medical-compliance-tone.md` | core | prohibited-claims section required by compliance constraint; no implied medical advice |
| `02-streetwear-voice.md` | core | voice derived from a real strategic differentiator (no restock), not generic hype-culture adjectives |
| `03-b2b-technical-brand.md` | core | expert-audience jargon tolerance; resists defaulting to untraced warmth/approachability |
| `04-edge-thin-strategy-input.md` | edge/failure | must return `BLOCKED` on a thin strategy rather than producing adjective-only AI-slop filler |
