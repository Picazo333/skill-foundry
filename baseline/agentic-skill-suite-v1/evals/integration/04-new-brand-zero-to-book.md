# Walkthrough 4 — New brand → Discovery → Strategy → Verbal + Visual → Identity → Brand Book → QA

## Starting state
A brand-new project, no artifacts. This is the same sequence as
`skills/15-brand-skill-orchestrator/examples/zero-to-brand-book-example.md`,
extended one stage further into a QA pass.

## Sequence
1. **`brand-discovery`** → `BRAND_DISCOVERY_BRIEF.md`, `DISCOVERY_GAPS.md`,
   `REFERENCE_MAP.md`.
2. **`brand-strategy`** (input: `BRAND_DISCOVERY_BRIEF.md`) → `BRAND_STRATEGY.md`
   (locked positioning), `POSITIONING_SYSTEM.md`, `STRATEGIC_GUARDRAILS.md`.
3. **`brand-verbal-identity`** (input: `BRAND_STRATEGY.md`) → `VERBAL_IDENTITY.md`,
   `MESSAGE_HIERARCHY.md`, `VOICE_EXAMPLES.md`.
4. **`brand-visual-direction`** (input: `BRAND_STRATEGY.md`, parallel to
   step 3) → `VISUAL_TERRITORIES.md`, `APPROVED_VISUAL_DIRECTION.md`,
   `VISUAL_ANTI_PATTERNS.md`, `GENERATION_LANGUAGE.md`.
5. **`brand-identity-system`** (input: `BRAND_STRATEGY.md`,
   `APPROVED_VISUAL_DIRECTION.md`) → `IDENTITY_SYSTEM.md`, `DESIGN_TOKENS.json`,
   `APPLICATION_RULES.md`.
6. **`brand-book-builder`** (input: all six artifacts from steps 3 and 5) →
   `BRAND_BOOK.md`, `BRAND_BOOK_OUTLINE.md`, `BRAND_BOOK_ASSET_CHECKLIST.md`.
   Per skill 11's design, this is a pure compilation step — no new brand
   decisions are introduced here.
7. **`brand-quality-auditor`** (input: `BRAND_BOOK.md` as the artifact to
   audit, full canon set as the standard) → `BRAND_QA_REPORT.md`,
   `FIX_LIST.md`, `DRIFT_REGISTER.md`.

## What must hold
- Steps 3 and 4 both consume `BRAND_STRATEGY.md` only — neither invents
  positioning of its own.
- Step 6 introduces zero new brand decisions; every rule in `BRAND_BOOK.md`
  traces to one of the six upstream artifacts.
- Step 7 only runs because canon is explicit and complete by this point — if
  any upstream artifact were missing, `brand-quality-auditor` would `BLOCK`
  per its own canon gate rather than audit against assumed standards.

## Failure signature
`BRAND_BOOK.md` containing a stated brand rule that cannot be traced to
`VERBAL_IDENTITY.md`/`IDENTITY_SYSTEM.md`/etc. is exactly the failure mode
skill 11's `SKILL.md` names first.
