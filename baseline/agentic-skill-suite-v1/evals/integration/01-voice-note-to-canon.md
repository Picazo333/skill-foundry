# Walkthrough 1 — Chaotic voice note → Rapid Capture → Canonical Context

## Starting state
A founder records a rambling 4-minute voice memo transcript covering three
unrelated topics: a task reprioritization, a doubt about pricing, and a
rename of a feature. No prior canon exists.

## Sequence
1. **`rapid-capture-triage`** run with `RUN_REQUEST.objective: "structure this voice note"`,
   `source_artifacts: [voice_memo_transcript.txt]`.
   - Output: `CAPTURE_PREVIEW.md`, `STRUCTURED_DELTA.json`, `AMBIGUITIES.md`,
     `APPLY_INSTRUCTIONS.md`. Per skill 04's dual classification, the
     reprioritization and rename become `action-item` operations in
     `STRUCTURED_DELTA.json`; the pricing doubt is classified
     `genuinely-ambiguous` and appears only in `AMBIGUITIES.md`, never as an
     operation.
   - `RUN_RESULT.handoff.next_skill: canonical-context-builder`.
2. **`canonical-context-builder`** run with `mode: UPDATE`,
   `source_artifacts: [STRUCTURED_DELTA.json, AMBIGUITIES.md]` (per skill 04's
   handoff rule — canonical artifacts only, not the raw transcript),
   `prior_run: null` (first canon build, or a prior `PROJECT_CANON.md` if one
   existed).
   - Output: `PROJECT_CANON.md` reflects the rename and reprioritization as
     LOCKED DECISIONS/FACTS; `OPEN_LOOPS.md` carries the pricing doubt
     forward from `AMBIGUITIES.md`, not silently dropped.

## What must hold
- Skill 04 never hands the raw transcript directly to skill 01 as the
  primary artifact — only its structured outputs (per skill 04's own design
  note: "handoff to canonical-context-builder passes only the four
  canonical artifacts, never raw capture/chat history").
- The pricing doubt survives both hops unresolved and visible in
  `OPEN_LOOPS.md` — it must not be silently promoted to a decision by either
  skill, and must not vanish.

## Failure signature
If `OPEN_LOOPS.md` after step 2 contains no trace of the pricing doubt, the
handoff broke skill 04's core anti-false-certainty guarantee.
