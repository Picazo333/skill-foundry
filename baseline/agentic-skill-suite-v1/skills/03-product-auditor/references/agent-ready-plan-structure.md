# Reference: what makes a plan item "agent-ready"

Used in `SKILL.md` Phase B1 step 6 (Specify each implement-now change) and
by `QA_CONTRACT.md`. The test: an execution agent with no access to this
audit's conversation, given only `IMPLEMENTATION_PLAN.md` +
`QA_CONTRACT.md`, should not need to ask a single clarifying question about
product intent.

## Required fields per item (see `templates/IMPLEMENTATION_PLAN.md`)
1. **Problem** — references the specific `PRODUCT_AUDIT.md` finding ID.
   Never a paraphrase that drops the original evidence trail.
2. **Target behavior** — stated as an observable outcome, not an
   implementation instruction (describe *what*, let the executor decide
   *how*, unless the audit objective specifically requires a technical
   approach).
3. **Affected components/data/routes** — explicit, not "the relevant files".
   If inspection didn't identify the exact component, that itself is a
   dependency/blocker to note, not something to leave implicit.
4. **Dependencies** — other plan item numbers that must land first. A plan
   with an implicit dependency (item 5 silently assumes item 2's migration
   already ran) is not agent-ready.
5. **Do NOT touch** — existing, approved behavior/components adjacent to the
   change that must survive untouched. This is what protects approved
   existing features (`QUALITY_GATES.md` skill-specific gate).
6. **Tests** — concrete: which test suite, which manual walkthrough steps,
   which data assertion. "Test it works" is not a test.
7. **Acceptance criteria** — a checklist, not a paragraph. Every criterion
   must be independently checkable by someone who did not write the plan —
   this is what `QA_CONTRACT.md` binds a later QA-mode run to.

## Migrations specifically
Any item that changes a data shape must state, as its own explicit
sub-step, before the dependent behavior change:
- What changes (schema/field/format).
- How existing data is transformed (not just "add a migration").
- The rollback path if the migration needs to be reversed.

A plan item that changes data shape and UI behavior in the same
unstructured step is not agent-ready — split the migration out.

## Mobile parity specifically
If a plan item touches any UI shared between desktop and mobile, state the
mobile-specific acceptance criteria explicitly in the item, and add a
corresponding row to `REGRESSION_MATRIX.md`. "Should also work on mobile" is
not an acceptance criterion.
