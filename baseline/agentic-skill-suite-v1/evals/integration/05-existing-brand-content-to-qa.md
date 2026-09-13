# Walkthrough 5 — Existing brand → Content System → Creative Brief → QA

## Starting state
A brand already has an approved `BRAND_STRATEGY.md` and `VERBAL_IDENTITY.md`
(no full `BRAND_BOOK.md` required — per both skill 12 and skill 13's
manifests, their minimum inputs are satisfiable by strategy + verbal canon
directly). The engagement is content-only.

## Sequence
1. **`brand-content-system`** (input: `BRAND_STRATEGY.md`, `VERBAL_IDENTITY.md`) →
   `CONTENT_SYSTEM.md`, `CONTENT_PILLARS.md`, `FORMAT_LIBRARY.md`,
   `CONTENT_PIPELINE.md`, `MEASUREMENT_MODEL.md`. Per skill 13's design,
   pillars trace to specific strategy/verbal-identity lines, not generic
   listicle categories.
2. **`creative-brief-generator`** (input: brand canon + `CONTENT_SYSTEM.md`'s
   `BRIEF_SKELETON.md` template, deliverable objective: "Q1 Instagram reel
   batch") → `CREATIVE_BRIEF.md`, `ASSET_REQUIREMENTS.md`,
   `PRODUCTION_HANDOFF.md`. This is a per-piece brief, not a re-derivation of
   the content system itself — skill 12 explicitly guards against
   duplicating skill 13's job.
3. **`brand-quality-auditor`** (input: the delivered reel content as the
   artifact to audit, `VERBAL_IDENTITY.md` + `CONTENT_SYSTEM.md` as the
   standard) → `BRAND_QA_REPORT.md`, `FIX_LIST.md`, `DRIFT_REGISTER.md`.

## What must hold
- Step 1 does not produce a one-off brief (that's step 2's job); step 2 does
  not produce a reusable pillar/cadence system (that's step 1's job) — the
  two skills' scopes stay distinct per their own non-triggers.
- Step 3's findings each cite a specific canon rule (from verbal identity or
  the content system's own stated rules), never an unbacked taste judgment.

## Failure signature
`CREATIVE_BRIEF.md` re-deriving content pillars from scratch instead of
referencing `CONTENT_PILLARS.md` would mean skill 12 duplicated skill 13's
job — exactly the failure mode both skills were built to avoid.
