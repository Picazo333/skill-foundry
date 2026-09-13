# Reference: the real artifact/handoff contracts this skill routes against

Built directly from the 14 finished skills' `manifest.json` files (not
imagined). If any skill's `manifest.json` changes, this file and
`references/stage-detection-rules.md` must be updated together — they are
the orchestrator's routing table, not decoration.

| Skill ID | Minimum inputs | Required outputs | Hands off to |
|---|---|---|---|
| `canonical-context-builder` | project materials or current canonical artifact; objective | `PROJECT_CANON.md`, `DECISION_REGISTER.md`, `OPEN_LOOPS.md`, `DEPRECATED_REGISTER.md`, `NEXT_START_PROMPT.md` | research-architect, product-auditor, brand-discovery, brand-skill-orchestrator, rapid-capture-triage |
| `research-architect` | raw project/research objective | `PROJECT_RESEARCH_BRIEF.md`, `MASTER_RESEARCH_PROGRAM.md`, `DOMAIN_MAP.md`, `COVERAGE_DEBT.md`, `GAP_LEDGER.md`, `CHECKPOINT.md`, `EXECUTOR_START_PROMPT.md` | canonical-context-builder, ai-resource-router |
| `product-auditor` | repo/app/artifacts (AUDIT) or delivered work (QA); audit objective or prior plan | `PRODUCT_AUDIT.md`, `IMPLEMENTATION_PLAN.md`, `REGRESSION_MATRIX.md`, `QA_CONTRACT.md`, `HANDOFF_PROMPT.md` | ai-resource-router, canonical-context-builder |
| `rapid-capture-triage` | raw capture (transcript/dictation/notes) | `CAPTURE_PREVIEW.md`, `STRUCTURED_DELTA.json`, `AMBIGUITIES.md`, `APPLY_INSTRUCTIONS.md` | canonical-context-builder, ai-resource-router, product-auditor |
| `ai-resource-router` | tasks/projects to route; capacity snapshot | `ROUTING_PLAN.md`, `DISPATCH_QUEUE.json`, `PROMPTS/`, `CAPACITY_RISK.md` | product-auditor, research-architect, brand-skill-orchestrator |
| `brand-discovery` | raw client/project/business context | `BRAND_DISCOVERY_BRIEF.md`, `DISCOVERY_GAPS.md`, `REFERENCE_MAP.md` | brand-strategy, research-architect, canonical-context-builder |
| `brand-strategy` | `BRAND_DISCOVERY_BRIEF.md` | `BRAND_STRATEGY.md`, `POSITIONING_SYSTEM.md`, `STRATEGIC_GUARDRAILS.md` | brand-verbal-identity, brand-visual-direction, brand-skill-orchestrator |
| `brand-verbal-identity` | `BRAND_STRATEGY.md` (locked positioning + value prop) | `VERBAL_IDENTITY.md`, `MESSAGE_HIERARCHY.md`, `VOICE_EXAMPLES.md` | brand-book-builder, brand-content-system, creative-brief-generator, brand-quality-auditor |
| `brand-visual-direction` | `BRAND_STRATEGY.md` | `VISUAL_TERRITORIES.md`, `APPROVED_VISUAL_DIRECTION.md`, `VISUAL_ANTI_PATTERNS.md`, `GENERATION_LANGUAGE.md` | brand-identity-system, creative-brief-generator, brand-quality-auditor |
| `brand-identity-system` | `BRAND_STRATEGY.md`, `APPROVED_VISUAL_DIRECTION.md` | `IDENTITY_SYSTEM.md`, `DESIGN_TOKENS.json`, `APPLICATION_RULES.md` | brand-book-builder, creative-brief-generator, brand-quality-auditor |
| `brand-book-builder` | `VERBAL_IDENTITY.md`, `MESSAGE_HIERARCHY.md`, `VOICE_EXAMPLES.md`, `IDENTITY_SYSTEM.md`, `DESIGN_TOKENS.json`, `APPLICATION_RULES.md` | `BRAND_BOOK.md`, `BRAND_BOOK_OUTLINE.md`, `BRAND_BOOK_ASSET_CHECKLIST.md` | creative-brief-generator, brand-content-system, brand-quality-auditor, brand-verbal-identity, brand-identity-system (on coherence-gap PARTIAL) |
| `creative-brief-generator` | brand canon (strategy + verbal minimum; + visual for visual deliverables); deliverable objective | `CREATIVE_BRIEF.md`, `ASSET_REQUIREMENTS.md`, `PRODUCTION_HANDOFF.md` | brand-quality-auditor, brand-content-system |
| `brand-content-system` | `BRAND_STRATEGY.md` (or `BRAND_BOOK.md`); `VERBAL_IDENTITY.md` (or `BRAND_BOOK.md`) | `CONTENT_SYSTEM.md`, `CONTENT_PILLARS.md`, `FORMAT_LIBRARY.md`, `CONTENT_PIPELINE.md`, `MEASUREMENT_MODEL.md` | creative-brief-generator, brand-quality-auditor, ai-resource-router |
| `brand-quality-auditor` | artifact to audit; brand canon covering its relevant dimensions | `BRAND_QA_REPORT.md`, `FIX_LIST.md`, `DRIFT_REGISTER.md` | brand-book-builder, creative-brief-generator, product-auditor |

## Notes for routing
- `brand-book-builder`'s minimum inputs are the full six-artifact set from
  verbal identity + identity system — do not route to it until both exist.
- `creative-brief-generator` and `brand-content-system` can be satisfied by
  `BRAND_STRATEGY.md`/`VERBAL_IDENTITY.md` alone (no compiled book
  required) when the objective doesn't need the full manual — don't force a
  `brand-book-builder` run onto every content-only engagement.
- `brand-quality-auditor` will itself `BLOCK` if canon is missing/unapproved
  — the orchestrator should predict this from the inventory and avoid
  routing to it when the relevant canon plainly isn't there yet, rather than
  waiting for it to bounce back.
