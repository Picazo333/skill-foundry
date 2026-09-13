# AI-Slop / Genericity Detection Checklist

Operationalized patterns for step 7 of `SKILL.md`. This list makes
"detect AI-slop" checkable instead of a vague instruction. Every hit
against this checklist is only a valid finding when it also traces to a
specific canon rule (see `SKILL.md` Failure modes and Quality gates) —
this file tells you *what to look for*; the canon tells you *whether it's
actually a violation here*. A checklist hit with no canon rule to pin it
to is an out-of-scope observation, not a `FIX`/`POLISH` item.

## Verbal patterns

### Generic filler adjectives
Words that could describe any brand in any category, doing no
differentiating work: "innovative", "seamless", "cutting-edge",
"world-class", "revolutionary", "game-changing", "next-level",
"transformative", "robust", "holistic", "empower", "elevate", "unlock",
"unleash", "journey" (as a generic metaphor), "seamlessly", "effortlessly".
- **How to flag:** the word appears and, if swapped for a competitor's
  name, the sentence remains equally true. Cite the verbal canon's
  approved-vocabulary or banned-words list if one exists; if canon is
  silent on vocabulary entirely, this dimension can't be graded (log as
  out-of-scope, don't invent a banned-word list).

### Hedge-y / non-committal copy
Copy that avoids a specific, falsifiable claim: "can help you...",
"may improve...", "designed to...", "aims to...", stacked qualifiers
("in many cases, users may see..."), passive voice hiding the actor.
- **How to flag:** compare against verbal canon's stated voice
  confidence/directness rules and message hierarchy (what should be
  asserted plainly vs. hedged).

### Triplet padding
Rule-of-three noun/adjective stacking with no added meaning: "fast,
reliable, and scalable"; "simple, powerful, and flexible" — each word
addable/removable without changing what's said.
- **How to flag:** cite verbal canon's message-hierarchy or clarity rule;
  flag when the triplet doesn't map to three distinct, canon-defined
  message pillars.

### Uniform sentence rhythm
Every sentence the same length/structure (subject-verb-object, ~8-12
words), no variation — a common LLM-default cadence.
- **How to flag:** only a finding if verbal canon specifies rhythm/voice
  texture; otherwise log as observation.

### Generic CTA language
"Get started today", "Learn more", "Discover the difference" with no
brand-specific verb or promise.
- **How to flag:** cite verbal canon's CTA/vocabulary conventions if
  defined.

## Visual patterns

### Gradient-blob / abstract-shape backgrounds
Purple-to-blue (or similarly ubiquitous) mesh gradients, blurred organic
blobs, or generic abstract shape clusters used as decoration with no
message function — a strong signal of default AI-generation or template
output.
- **How to flag:** cite visual canon's decoration-has-function rule or
  approved background/texture system. If visual canon doesn't address
  backgrounds at all, this can't be graded as a violation — log as
  observation.

### Isometric/3D stock-style illustration
Generic isometric-perspective icon sets or 3D-rendered "tech" illustration
style not defined anywhere in the visual canon's illustration system.
- **How to flag:** cite the canon's defined illustration/iconography style;
  absence of a defined style means this stays an observation, not a FIX.

### Off-role color use
Colors technically on-palette but used outside their canonical role (e.g.
an accent color used as a body-text color, or a warning color used
decoratively).
- **How to flag:** cite the specific color-role definition in visual canon.

### Over-decoration with no hierarchy function
Excess ornament, drop shadows, glows, or layered effects that don't
support the visual hierarchy defined in canon.
- **How to flag:** cite visual canon's hierarchy/composition rules.

### Stock photography mismatch
Generic stock imagery (interchangeable smiling professionals, unbranded
handshake/lightbulb metaphors) where canon specifies a defined photography
style, subject matter, or treatment.
- **How to flag:** cite the canon's imagery/photography guidelines.

## Structural patterns

### Interchangeable-with-any-brand test
Read the artifact with the brand name/logo removed. If nothing else in
the copy or visuals identifies which brand it is, that is a strong
genericity signal.
- **How to flag:** this is a diagnostic test, not itself a citable rule —
  use it to locate candidate findings, then trace each one to the specific
  verbal/visual canon rule it fails.

### Template symmetry with no brand-specific deviation
Layout/copy structure that exactly matches an unbranded generic template
(hero + three feature cards + testimonial + CTA) with zero brand-specific
structural choice.
- **How to flag:** cite visual/verbal canon's composition or content-
  structure guidance if one exists.

## How to use this list
1. Scan the artifact against every pattern above.
2. For each hit, find the canon rule it violates (strategy, verbal, or
   visual canon). If none exists, it's an observation, not a finding.
3. Record hits with canon citations in `BRAND_QA_REPORT.md`'s AI-slop
   section; carry forward trend data into `DRIFT_REGISTER.md`.
