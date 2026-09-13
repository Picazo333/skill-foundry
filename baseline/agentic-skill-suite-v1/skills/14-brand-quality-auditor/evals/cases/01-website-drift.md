# Eval Case — Website drifting from canon

## Scenario
A marketing homepage redesign has shipped visual and verbal drift against
approved canon (banned words crept back in, an off-brand gradient
appeared, an accent color is used decoratively). This is the core case:
detect regression against explicit, already-approved canon on a live
production artifact.

## Input
```yaml
RUN_REQUEST:
  objective: "pre-launch QA on marketing homepage redesign"
  source_artifacts:
    - "homepage_redesign_v3.html"
    - "VERBAL_IDENTITY_CANON.md (approved v1.2 — banned words: seamless, revolutionary, game-changing; CTA rule: specific verb+object)"
    - "VISUAL_IDENTITY_CANON.md (approved v1.1 — accent #2B6EF2 reserved for CTA/interactive only; no gradient backgrounds)"
  known_context: "channel: public marketing site; audience: SMB finance leads"
  constraints: ["strategy canon not supplied this run — grade verbal + visual only"]
  desired_output: full_audit
  mode: STANDARD
  prior_run: null
```

## Expected behavior
1. Canon gate passes for verbal + visual (both explicit and supplied);
   strategy is explicitly marked ungraded, not silently skipped.
2. Hero copy's "seamless"/"revolutionary" usage is classified `FIX`,
   citing the banned-words list.
3. "Learn more" CTA is classified `FIX`, citing the CTA rule.
4. Decorative use of #2B6EF2 on headings is classified `FIX`, citing the
   color-role rule.
5. The gradient background is classified `FIX` under visual alignment AND
   logged in the AI-slop section citing the no-gradient rule — not
   double-counted as two separate fixes in `FIX_LIST.md`.
6. `FIX_LIST.md` contains only the FIX items, prioritized, no POLISH/
   redesign scope creep.

## Expected artifacts
- `BRAND_QA_REPORT.md` — verbal and visual sections populated with cited
  findings; strategy section explicitly marked out of scope/ungraded
  rather than absent with no explanation.
- `FIX_LIST.md` — exactly the FIX-classified items, deduplicated, each
  citing its canon rule.
- `DRIFT_REGISTER.md` — present even on a first audit (baseline), noting
  the gradient regression given the known_context reference to a prior
  gradient-free version.

## Forbidden behavior
- Must NOT grade strategic/positioning claims when strategy canon wasn't
  supplied.
- Must NOT list a finding without a canon citation.
- Must NOT merge the gradient FIX and the banned-word FIX into a single
  vague "content quality" line — each traces to its own rule.

## Pass criteria
- [ ] All four canon violations are classified FIX with correct citations.
- [ ] Strategy is marked explicitly ungraded, not silently omitted.
- [ ] `FIX_LIST.md` has no items without a canon citation.
- [ ] No POLISH or subjective items appear in `FIX_LIST.md`.
