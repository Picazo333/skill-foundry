# Eval Case — AI-generated social creative

## Scenario
A content team used a generative image/copy tool to produce a batch of
social posts under time pressure. The output is generic ("AI slop") even
though it's technically within brand colors. This tests the skill's
ability to operationalize genericity detection and tie every hit to a
specific canon rule, rather than issuing a vague "this feels AI-generated"
verdict.

## Input
```yaml
RUN_REQUEST:
  objective: "QA batch of 5 social posts before scheduling"
  source_artifacts:
    - "social_batch_sept_2026/post_1.png ... post_5.png"
    - "social_batch_sept_2026/captions.txt"
    - "VERBAL_IDENTITY_CANON.md (approved — voice is 'direct, specific, no filler adjectives'; banned: 'unlock', 'elevate', 'empower')"
    - "VISUAL_IDENTITY_CANON.md (approved — illustration style: flat geometric line icons only; no 3D/isometric renders; imagery: real customer photos only, no stock)"
  known_context: "channel: Instagram/LinkedIn; produced via AI image generator + AI copy draft"
  constraints: []
  desired_output: full_audit
  mode: STANDARD
  prior_run: null
```
Artifact detail: posts use isometric 3D icon renders (not in canon's
illustration system), generic stock-style "smiling professional at
laptop" imagery, and captions containing "unlock your potential" and
"elevate your workflow."

## Expected behavior
1. Isometric 3D renders are flagged citing the illustration-style rule
   (flat geometric line icons only) — not a generic "looks AI-made"
   comment.
2. Stock-style imagery is flagged citing the real-customer-photos-only
   rule.
3. "Unlock"/"elevate" are flagged citing the banned-words list.
4. Each of the 5 posts is assessed individually in `BRAND_QA_REPORT.md`
   (not one blended verdict for the whole batch) so per-post fixes are
   traceable.
5. AI-slop section explicitly cross-references the checklist entries used
   (isometric/3D stock-style illustration; stock photography mismatch;
   generic filler adjectives).

## Expected artifacts
- `BRAND_QA_REPORT.md` — per-post breakdown, each finding cites specific
  canon rule.
- `FIX_LIST.md` — prioritized, e.g. regenerate/replace imagery ranked
  above caption word-swaps if imagery affects more posts.
- `DRIFT_REGISTER.md` — notes this as a new AI-slop pattern tied to the
  new generation tool, useful for trend tracking across future batches.

## Forbidden behavior
- Must NOT issue a single "this feels off-brand" verdict without
  per-element canon citations.
- Must NOT flag the isometric icons as wrong without an actual defined
  illustration-style rule to cite (canon does define one here, so this
  is a valid FIX — contrast with case 04 where no such rule exists).
- Must NOT treat "produced by AI" itself as a violation — only the
  concrete canon-violating properties of the output are gradable.

## Pass criteria
- [ ] Every AI-slop hit cites a specific canon rule (illustration style,
      imagery style, or banned words).
- [ ] Findings are broken out per post, not blended.
- [ ] The fact the content was AI-generated is never itself cited as the
      violation — only concrete canon mismatches are.
