# Worked example — Responsive brand site audit (AUDIT mode)

## Input (abridged)
```yaml
RUN_REQUEST:
  objective: "full audit of marketing site ahead of launch: desktop looks final, need mobile parity + simplification pass"
  source_artifacts:
    - "repo: brandsite (Next.js, responsive breakpoints at 768px/1024px)"
    - "screenshots: desktop (approved by stakeholder), mobile (informal, flagged 'looks off')"
    - "PROJECT_CANON.md (locked: hero section copy + CTA text, approved visual direction v3)"
  known_context: "desktop visual direction v3 is locked; mobile has not been formally reviewed"
  constraints: ["do not alter locked hero copy or CTA text"]
  desired_output: full_artifact_set
  mode: AUDIT
  prior_run: null
```

## Output (abridged)

**PRODUCT_AUDIT.md** (excerpt):
```
## Confirmed findings
| C1 | Hero CTA button overlaps subheading text below 480px width |
      mobile-parity | reproduced at 375px viewport | P1 |
| C2 | Three near-identical "Get started" CTAs stacked on the pricing
      section (nav, hero, footer) all point to the same URL | simplification
      | code inspection: all three <a href> identical | P2 |

## Suspected findings
| S1 | Font may be loading a fallback on some mobile browsers (text
      renders visually different from desktop screenshot) | mobile-parity |
      inconsistent screenshot vs. live render, not yet isolated to a
      specific browser/OS | needs cross-browser screenshot diff to confirm |
```

**IMPLEMENTATION_PLAN.md** (excerpt):
```
### Item 1 — Fix hero CTA/subheading overlap below 480px
- Problem: C1.
- Target behavior: CTA and subheading maintain minimum 16px clearance at
  all widths down to 320px.
- Affected components/data/routes: `Hero.tsx`, mobile breakpoint styles
  only.
- Do NOT touch: locked hero copy/CTA text (PROJECT_CANON.md), desktop
  layout (already approved v3).
- Tests: visual regression snapshot at 320/375/414/768/1024px.
- Acceptance criteria: [ ] no overlap at any tested width [ ] desktop
  snapshot unchanged.

## Backlog
- C2 (duplicate CTAs) — deferred: cosmetic simplification, P2 low urgency,
  not blocking launch; revisit post-launch.

## Discarded
(none this pass — no reported item was dropped)
```

**REGRESSION_MATRIX.md** (excerpt):
```
| P1 | Hero renders correctly | Item 1 | pass (existing, unchanged) | fail →
       target after fix | tracked for QA-mode follow-up |

## Mobile applicability
Product has a mobile web surface (responsive breakpoints, no native app) —
all rows above apply to mobile web viewport widths.
```

Note what did NOT happen: S1 (font fallback) was not treated as confirmed
and did not get an implement-now plan item — it stayed in
`PRODUCT_AUDIT.md` as suspected, with the specific evidence needed to
confirm it, per the confirmed-vs-suspected quality gate.
