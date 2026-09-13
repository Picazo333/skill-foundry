# Worked example — website drifting from canon

## Input (abridged)
```yaml
RUN_REQUEST:
  objective: "pre-launch QA on marketing homepage redesign"
  source_artifacts:
    - "homepage_redesign_v3.html (artifact to audit)"
    - "VERBAL_IDENTITY_CANON.md (approved, v1.2)"
    - "VISUAL_IDENTITY_CANON.md (approved, v1.1)"
  known_context: "channel: public marketing site; audience: SMB finance leads"
  constraints: ["strategy canon not supplied this run — grade verbal + visual only"]
  desired_output: full_audit
  mode: STANDARD
  prior_run: null
```

Canon excerpts actually supplied:
- `VERBAL_IDENTITY_CANON.md`: "Never use 'seamless', 'revolutionary', or
  'game-changing' — banned words list, v1.2." / "CTAs are always a specific
  verb + object, never 'Learn more' alone."
- `VISUAL_IDENTITY_CANON.md`: "Primary accent color (#2B6EF2) is reserved
  for CTAs and interactive elements only — never decorative." / "No
  gradient backgrounds; approved background system is flat brand-navy or
  white."

## Output (abridged)

**BRAND_QA_REPORT.md** (excerpt):
```
## Verbal alignment
| # | Canon rule | Artifact evidence | Classification | Note |
|---|---|---|---|---|
| V1 | Banned words list (VERBAL_IDENTITY_CANON.md v1.2) | Hero copy: "a seamless, revolutionary way to manage your books" | FIX | Uses two banned words in one sentence |
| V2 | CTA = specific verb + object (VERBAL_IDENTITY_CANON.md v1.2) | Primary CTA button reads "Learn more" | FIX | Generic CTA, not a specific verb+object |

## Visual alignment
| # | Canon rule | Artifact evidence | Classification | Note |
|---|---|---|---|---|
| D1 | Accent color reserved for CTA/interactive only (VISUAL_IDENTITY_CANON.md v1.1) | #2B6EF2 used as decorative underline on all H2 headings | FIX | Off-role color use |
| D2 | No gradient backgrounds; flat navy/white only (VISUAL_IDENTITY_CANON.md v1.1) | Hero section uses a purple-to-blue mesh gradient background | FIX | Also flagged in AI-slop section (A1) |

## AI-slop / genericity findings
| # | Checklist item hit | Canon rule violated | Evidence | Classification |
|---|---|---|---|---|
| A1 | Gradient-blob background | No gradient backgrounds rule (VISUAL_IDENTITY_CANON.md v1.1) | Hero section mesh gradient | FIX |
| A2 | Generic filler adjective ("seamless", "revolutionary") | Banned words list (VERBAL_IDENTITY_CANON.md v1.2) | Same as V1 | FIX (already counted at V1, not double-counted in FIX_LIST) |

## Summary counts
PASS: 6 | FIX: 4 (3 distinct: V1/A2 dedup, V2, D1, D2) | POLISH: 1 | DEFER: 0
Canon dimensions graded: verbal, visual
Canon dimensions explicitly ungraded: strategy (not supplied this run — see constraints)
```

**FIX_LIST.md** (excerpt):
```
## Blocking fixes
| Priority | Fix ID | Canon rule violated | Required change |
|---|---|---|---|
| 1 | V1/A2 | Banned words list | Remove "seamless" and "revolutionary" from hero copy |
| 2 | D2/A1 | No-gradient-backgrounds rule | Replace hero gradient with flat brand-navy or white background |
| 3 | D1 | Accent-color-for-CTA-only rule | Remove #2B6EF2 from H2 underline decoration; use neutral rule instead |
| 4 | V2 | CTA = specific verb + object | Change "Learn more" to a specific verb+object CTA |
```

**DRIFT_REGISTER.md** (excerpt):
```
## New drift introduced this run
| # | Canon rule | What changed | Classification | First seen |
|---|---|---|---|---|
| 1 | No-gradient-backgrounds | v2 homepage had flat navy hero; v3 introduces gradient | FIX | this run |

(No prior audit existed for this artifact — first audit, so most items are
logged as baseline findings rather than "new" drift; the gradient is
called out because a prior homepage version without it is referenced in
known_context.)
```

Note what did NOT happen: strategy canon was not supplied, so no
strategic-alignment claims were graded — `BRAND_QA_REPORT.md` explicitly
lists strategy as an ungraded dimension rather than the run inventing a
positioning standard to check the hero copy against.
