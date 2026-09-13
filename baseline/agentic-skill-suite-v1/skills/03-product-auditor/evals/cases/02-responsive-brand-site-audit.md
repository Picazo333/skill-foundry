# Eval Case — Responsive brand site audit

## Scenario
A marketing site's desktop layout is locked/approved (v3 visual direction,
specific hero copy), but mobile has never been formally reviewed and has a
real layout bug plus a cosmetic duplication issue. Tests whether the skill
protects locked/approved content while still surfacing and prioritizing a
real mobile-parity bug, and makes mobile applicability explicit rather than
assumed.

## Input
```yaml
RUN_REQUEST:
  objective: "audit marketing site ahead of launch: desktop approved, need mobile parity + simplification pass"
  source_artifacts:
    - "repo: brandsite"
    - "desktop screenshots (approved)"
    - "mobile screenshots (informal, flagged 'looks off')"
    - "PROJECT_CANON.md (locked hero copy/CTA text, approved visual direction v3)"
  known_context: "desktop v3 locked; mobile not yet formally reviewed"
  constraints: ["do not alter locked hero copy or CTA text"]
  desired_output: full_artifact_set
  mode: AUDIT
  prior_run: null
```

## Expected behavior
1. Phase A reproduces the mobile CTA/subheading overlap at narrow viewport
   widths and confirms it.
2. The duplicate-CTA finding is classified as simplification/P2 and
   deferred to backlog (not implement-now) with a stated reason, since it
   is not launch-blocking.
3. Every implement-now plan item touching shared UI states explicit mobile
   acceptance criteria and states "do not touch" for the locked hero
   copy/CTA text and the already-approved desktop layout.
4. `REGRESSION_MATRIX.md` explicitly states mobile applicability (present,
   with viewport widths) rather than leaving it implicit.
5. Any finding that could not be fully verified (e.g. a font-rendering
   inconsistency without a controlled cross-browser diff) stays tagged
   `suspected` and does not enter the implement-now plan.

## Expected artifacts
- `PRODUCT_AUDIT.md` — mobile overlap bug `confirmed`/P1; font-rendering
  concern (if present in the run) tagged `suspected` with what would confirm
  it.
- `IMPLEMENTATION_PLAN.md` — overlap-fix item has "do not touch" covering
  locked hero copy/CTA text and desktop layout; duplicate-CTA item is in
  Backlog, not Implement-now.
- `REGRESSION_MATRIX.md` — explicit desktop/mobile columns with viewport
  widths, mobile applicability stated.

## Forbidden behavior
- Must NOT alter or propose altering the locked hero copy/CTA text.
- Must NOT state a font-rendering concern as confirmed without a controlled
  reproduction.
- Must NOT leave `REGRESSION_MATRIX.md`'s mobile applicability implicit or
  blank without a stated reason.
- Must NOT write/edit any site code during the run.

## Pass criteria
- [ ] Mobile overlap bug is `confirmed`, has an implement-now plan item with
      explicit mobile acceptance criteria.
- [ ] Locked hero copy/CTA text and desktop layout are explicitly protected
      ("do not touch") in the relevant plan item.
- [ ] Duplicate-CTA item is Backlog with a stated reason, not implement-now.
- [ ] `REGRESSION_MATRIX.md` states mobile applicability explicitly.
