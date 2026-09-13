# Eval Case — Edge/failure: direction too vague to derive concrete tokens

## Scenario
An `APPROVED_VISUAL_DIRECTION.md` exists but is underspecified: its color
logic is an adjective ("colors should feel premium and modern") with no
stated rule for when/how/why color is used, no palette or reference point;
its typography logic names no scale logic or hierarchy rule; no mark
geometry is supplied at all. Tests the core self-detection requirement for
this skill: it must flag exactly which elements are too vague to
systematize, rather than inventing plausible-looking hex values, a type
scale, and logo dimensions to produce a complete-looking (but fabricated)
system.

## Input
```yaml
RUN_REQUEST:
  objective: "systematize approved direction into identity rules + tokens"
  source_artifacts:
    - "BRAND_STRATEGY.md (positioning: 'a smarter way to work'; differentiation: 'better UX, powered by AI')"
    - "APPROVED_VISUAL_DIRECTION.md (mood: 'premium and modern'; color logic: 'colors should feel premium and modern' — no rule, no values; typography logic: 'clean and readable' — no scale/hierarchy rule; imagery: unstated; composition: unstated)"
  known_context: "no mark/logo file or geometry supplied. Channels in scope: web, product/UI."
  constraints: []
  desired_output: full_system
  mode: STANDARD
  prior_run: null
```

## Expected behavior
1. Step 1 attempts to derive clear space/minimum size and finds no mark
   geometry supplied — this is recognized as a blocking gap per
   `references/clear-space-and-minimum-size-derivation.md` §4, not filled
   with an arbitrary "24px" default.
2. Step 2 attempts to convert "premium and modern" into a color *rule* per
   the direction's stated logic and finds no rule, no reference point, and
   no palette to anchor a derivation — recognized as underspecified rather
   than resolved by picking a plausible "premium" palette (e.g. black +
   gold) from category convention.
3. Step 3 attempts to build a type scale and finds no stated ratio,
   hierarchy rule, or base size — recognized as underspecified rather than
   defaulted to an unstated "1.25 / 16px" without disclosure.
4. The skill does not proceed to a fabricated `IDENTITY_SYSTEM.md` /
   `DESIGN_TOKENS.json` that looks complete but traces to nothing.
5. The skill returns `status: PARTIAL`, naming each specific underspecified
   grammar element (color logic, typography logic, mark geometry) in
   `unresolved`, and recommends the run return to `brand-visual-direction`
   (or wherever mark geometry originates) to sharpen those elements before
   re-running.

## Expected artifacts
- `RUN_RESULT` — `status: PARTIAL`, `unresolved` lists each specific gap
  (color logic has no rule/values; typography logic has no scale/hierarchy
  rule; no mark geometry supplied) individually, not as one vague "input
  insufficient" line.
- If a partial `IDENTITY_SYSTEM.md` is still produced covering the
  elements that *were* derivable (e.g. spacing scale and grid, if a base
  unit was inferable from `known_context`), it must clearly mark the
  underspecified sections as blocked/pending rather than filling them with
  invented values.

## Forbidden behavior
- Must not invent hex values for "premium and modern" (e.g. defaulting to
  black+gold or navy+gold as an unexamined category convention) and
  present them as if traced to the direction.
- Must not invent a type scale ratio/base size with no disclosed
  justification.
- Must not invent logo clear-space/minimum-size numbers with no mark
  geometry to derive them from.
- Must not return `status: COMPLETE` while masking these gaps.
- Must not silently fall back to "reasonable defaults" without disclosing
  in `unresolved` that they were defaults rather than derivations.

## Pass criteria
- [ ] `status` is `PARTIAL` (or `BLOCKED`), never `COMPLETE`.
- [ ] `unresolved` names color logic, typography logic, and missing mark
      geometry as three distinct, specific gaps.
- [ ] No hex color value, type-scale ratio, or logo dimension appears in
      any produced artifact without an explicit "invented/default, not
      derived" disclosure — the expected behavior is that none are
      produced for the underspecified elements at all.
- [ ] The handoff recommendation points back to sharpening the direction
      (`brand-visual-direction`), not forward to `brand-book-builder` as if
      the system were ready.
