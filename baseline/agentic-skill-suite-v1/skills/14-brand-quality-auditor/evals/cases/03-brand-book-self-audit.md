# Eval Case — Brand book self-audit

## Scenario
The brand book itself (the canon source) is audited for internal
consistency — e.g. checking a newly added campaign template section
against the brand book's own core verbal/visual rules defined earlier in
the same document. This tests that the skill can audit canon-adjacent
material without treating "canon" and "artifact under audit" as
interchangeable, and without silently resolving an internal contradiction
in canon itself.

## Input
```yaml
RUN_REQUEST:
  objective: "self-audit newly added 'Event Campaign Template' section of the brand book against the brand book's own core identity chapters"
  source_artifacts:
    - "BRAND_BOOK.md, section 7: 'Event Campaign Template' (new, drafted this quarter)"
    - "BRAND_BOOK.md, chapters 1-4: core verbal identity, core visual identity, color system (approved, prior quarters)"
  known_context: "the new section was drafted by a different team than the original brand book authors"
  constraints: []
  desired_output: full_audit
  mode: STANDARD
  prior_run: null
```
Detail: chapters 1-4 define the accent color as CTA-only; section 7's
template shows the accent color used as a full-bleed background block in
event graphics. Chapters 1-4 also define voice as "no exclamation points
in headlines"; section 7's sample headlines use exclamation points
throughout.

## Expected behavior
1. Chapters 1-4 are treated as the canon; section 7 is treated as the
   artifact under audit — even though both live in the same document.
2. The accent-color-as-background usage in section 7 is classified `FIX`,
   citing chapter 3's color-role rule.
3. Exclamation points in section 7's sample headlines are classified
   `FIX`, citing chapter 1's voice rule.
4. If any part of section 7 is ambiguous as to whether it's proposing a
   canon *change* (new rule) vs. violating existing canon, that item is
   classified `DEFER` and handed off to `brand-book-builder` to reconcile
   — the audit does not unilaterally decide the brand book's own rules
   have changed.

## Expected artifacts
- `BRAND_QA_REPORT.md` — clearly separates "chapters 1-4 (canon)" from
  "section 7 (artifact)" in its framing so the self-referential setup
  doesn't collapse into treating the whole document as internally
  self-validating.
- `FIX_LIST.md` — the color and exclamation-point fixes.
- Handoff to `brand-book-builder` recorded if any `DEFER` items exist.

## Forbidden behavior
- Must NOT treat section 7 as automatically canonical just because it's
  physically inside `BRAND_BOOK.md`.
- Must NOT silently decide the new section supersedes chapters 1-4 (that
  would be reopening/rewriting canon inside an audit).
- Must NOT skip the audit on the theory that "it's all the same document
  so it must already be consistent."

## Pass criteria
- [ ] Section 7 is audited as the artifact, chapters 1-4 as canon.
- [ ] Both identified inconsistencies are classified FIX with citations
      to the specific chapter/rule.
- [ ] No item resolves itself by assuming section 7 silently updates
      canon; ambiguity is routed to DEFER + handoff.
