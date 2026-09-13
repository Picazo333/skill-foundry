# Reference: severity/priority scoring and complexity

Used in `SKILL.md` Phase B1 step 5 (Prioritize).

## Severity tiers (P0–P3)
- **P0 — breaks or corrupts.** Data loss/corruption risk, broken core flow
  (e.g. checkout, auth), crash on a common path. Always implement-now unless
  blocked by an unmet dependency.
- **P1 — materially degrades.** Confirmed bug or missing capability on a
  primary flow that has a workaround, or a canon contradiction that misleads
  users/stakeholders. Default implement-now.
- **P2 — real but contained.** Confirmed issue on a secondary flow, a
  redundant-UI or simplification opportunity with clear value, a
  non-blocking mobile-parity gap. Implement-now if complexity is low;
  backlog if not.
- **P3 — cosmetic or speculative.** Suspected-only findings, minor polish,
  low-value simplification. Backlog by default; never implement-now while
  still tagged `suspected` — reproduce first.

## Complexity estimate
Rate each implement-now item `low` / `medium` / `high` based on:
- Number of affected components/routes.
- Whether it touches shared state or a data migration.
- Whether it has cross-platform (desktop/mobile) surface.

Complexity does not override severity for sequencing priority, but a
high-complexity item with a data migration always sequences before
lower-complexity items that depend on the same data shape (see `SKILL.md`
Phase B1 step 7).

## Implement-now vs. backlog vs. discard
- **Implement-now:** P0/P1 always; P2 when complexity is low-medium and no
  blocking dependency.
- **Backlog:** approved but deferred — P2 with higher complexity, or P3 with
  clear value once reproduced. State the deferral reason (not just "later").
- **Discard:** not approved for any plan — duplicate of another finding,
  contradicts a locked canon decision with no counter-evidence, or explicitly
  out of the stated audit objective's scope. Always state why; a discard
  with no reason is indistinguishable from a silent drop, which is a failure
  mode.

## Suspected findings and severity
A `suspected` finding may be assigned a provisional severity for triage, but
it cannot enter `IMPLEMENTATION_PLAN.md` as implement-now until it is
reproduced and re-tagged `confirmed` in `PRODUCT_AUDIT.md`.
