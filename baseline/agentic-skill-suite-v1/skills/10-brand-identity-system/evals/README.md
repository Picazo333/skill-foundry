# Evals — Brand Identity System

Minimum set: 3 core scenarios (per `SPEC.md`'s required eval scenarios —
web-first service brand, app/product brand, social-heavy consumer brand)
plus 1 edge/failure case. Cases follow `/shared/templates/EVAL_TEMPLATE.md`.

## Cases
1. `cases/01-web-first-service-cross-section.md` — web-first service brand;
   also exercises the accent-color contrast-failure-on-light-surface
   pattern and the finance category's near-monochrome, precise-materiality
   pole.
2. `cases/02-app-product-habit-tracker.md` — app/product brand; exercises
   the soft/approachable materiality pole, a wordmark-only (no symbol)
   architecture, and an accent color narrowed to decorative-only use.
3. `cases/03-social-heavy-consumer-snack.md` — social-heavy consumer brand;
   exercises print/packaging as the lead surface, an explicit no-motion
   scope statement, and a type-family (not just size) split for
   "loud shelf, quiet ingredients."
4. `cases/04-edge-underspecified-direction.md` — edge/failure case: an
   `APPROVED_VISUAL_DIRECTION.md` too vague to derive concrete tokens from.
   Tests that the skill flags exactly what's missing and returns
   `status: PARTIAL` rather than inventing hex values, a type scale, or
   logo dimensions with no traceable derivation.

## How to run
Feed each case's `RUN_REQUEST` (with its referenced source artifacts) to
the skill exactly as specified. Check the run's actual behavior against
"Expected behavior," confirm "Expected artifacts" exist with the stated
content properties, confirm none of "Forbidden behavior" occurred, and
check every item in "Pass criteria."
