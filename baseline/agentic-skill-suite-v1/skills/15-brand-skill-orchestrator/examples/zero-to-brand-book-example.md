# Worked example — zero-to-brand-book routing sequence

## Input (Run 1)
```yaml
RUN_REQUEST:
  objective: "get this brand project to a published, approved brand book"
  source_artifacts: []   # nothing exists yet
  mode: STANDARD
```

## Output (Run 1, abridged)
```yaml
RUN_RESULT:
  status: PARTIAL
  summary: "No artifacts exist yet. Routing to brand-discovery first."
  handoff:
    next_skill: brand-discovery
    reason: "BRAND_DISCOVERY_BRIEF.md missing and objective requires full brand book, which requires strategy, which requires discovery."
```
`BRAND_WORKFLOW_STATE.md` records stage `DISCOVERY`, no artifacts yet,
next action = run `brand-discovery`.

## Subsequent runs (summarized)
1. **Run 2** (after `brand-discovery` delivers `BRAND_DISCOVERY_BRIEF.md`,
   no material gaps): stage → STRATEGY, route to `brand-strategy`.
2. **Run 3** (after `BRAND_STRATEGY.md` locked): stage → VERBAL+VISUAL,
   route to `brand-verbal-identity` (verbal-first default, since objective
   didn't specify priority).
3. **Run 4**: `VERBAL_IDENTITY.md` exists, `APPROVED_VISUAL_DIRECTION.md`
   still missing → route to `brand-visual-direction`.
4. **Run 5**: visual direction approved → route to `brand-identity-system`.
5. **Run 6**: identity system complete, verbal set complete → route to
   `brand-book-builder`.
6. **Run 7**: `brand-book-builder` returns `status: COMPLETE` → orchestrator
   writes `COMPLETION_REPORT.md`, `status: COMPLETE`. Objective fulfilled —
   the orchestrator does NOT continue on into `creative-brief-generator` or
   `brand-content-system`, since the stated objective was only "a published,
   approved brand book."

Note what did NOT happen: no stage was re-run, no stage was skipped without
a stated reason in `BRAND_WORKFLOW_STATE.md`, and the orchestrator itself
never wrote strategy, voice, or visual content — every domain decision
appears only inside the routed skill's own output artifacts.
