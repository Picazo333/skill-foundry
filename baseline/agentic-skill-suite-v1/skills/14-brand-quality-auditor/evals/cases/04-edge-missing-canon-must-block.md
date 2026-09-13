# Eval Case (edge/failure) — Canon missing/incomplete, must return BLOCKED

## Scenario
A stakeholder asks for a "brand quality check" on a new landing page but
supplies only the page itself — no verbal identity doc, no visual
identity doc, no positioning/strategy doc, nothing labeled as approved
canon. This is the case the skill must refuse to guess through: grading
against "general good landing page practice" or the auditor's own taste
would violate the suite-level gate "Brand Quality Auditor requires
explicit canon" (`QUALITY_GATES.md`).

## Input
```yaml
RUN_REQUEST:
  objective: "brand quality check on new landing page before launch"
  source_artifacts:
    - "new_landing_page.html"
  known_context: null
  constraints: []
  desired_output: full_audit
  mode: STANDARD
  prior_run: null
```

## Expected behavior
1. Step 1 (canon gate) runs before any comparison work: the skill checks
   for explicit, approved canon covering strategy/verbal/visual and finds
   none supplied.
2. The skill does NOT proceed to grade the landing page against generic
   best-practice heuristics, competitor norms, or the auditor's own sense
   of good design/copy.
3. The skill does NOT produce any `PASS`/`FIX`/`POLISH` classifications.
4. The run stops and returns `status: BLOCKED`, naming exactly what's
   missing: verbal identity canon, visual identity canon, and
   strategy/positioning canon (or whichever subset is actually absent),
   so the requester knows precisely what to supply next.

## Expected artifacts
- No `BRAND_QA_REPORT.md` findings table populated with graded items (the
  file may exist stating the block reason, or may simply not be produced
  — either way it must not contain graded PASS/FIX/POLISH rows).
- `RUN_RESULT.artifacts` may be empty.
- `RUN_RESULT.unresolved` explicitly lists the missing canon artifacts.

## Forbidden behavior
- Must NOT invent an implicit standard ("well-designed landing pages
  generally...") and grade against it.
- Must NOT partially proceed and quietly label the ungraded-canon
  situation as a footnote while still issuing FIX/POLISH verdicts as if
  backed by real canon.
- Must NOT return `status: COMPLETE` — a run with no canon to check
  against cannot complete an audit.
- Must NOT ask the user a single vague clarifying question and then
  proceed anyway on assumption — it must actually block until canon is
  supplied.

## Pass criteria
- [ ] `RUN_RESULT.status` is `BLOCKED`.
- [ ] No PASS/FIX/POLISH classification appears anywhere in the output.
- [ ] `RUN_RESULT.unresolved` (or equivalent) names the specific missing
      canon artifacts (verbal, visual, strategy).
- [ ] No aesthetic or "best practice" judgment substitutes for canon
      anywhere in the response.
