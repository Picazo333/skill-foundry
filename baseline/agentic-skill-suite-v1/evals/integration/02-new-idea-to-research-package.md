# Walkthrough 2 — New business idea → Research Architect → executor-ready package

## Starting state
A founder has a rough idea for a dental-practice operating system (matching
skill 02's own eval scenario). Canon is sparse — the idea exists but no
research has been architected.

## Sequence
1. **`canonical-context-builder`** run (`mode: STANDARD`) on whatever raw
   materials exist (notes, a chat, competitor mentions).
   - Output includes `OPEN_LOOPS.md` naming the market/competitive landscape
     as unknown — a material uncertainty.
   - `RUN_RESULT.handoff.next_skill: research-architect`.
2. **`research-architect`** run with `mode: AUTONOMOUS`,
   `source_artifacts: [PROJECT_CANON.md, OPEN_LOOPS.md]`.
   - Procedure runs the full invariant set (≥150 expansion + ≥50 polishing
     iterations, material-delta gate, Coverage Debt, contradiction/white-space
     ledgers, 10-pass QA) without pausing for "Siguiente/y" per the
     AUTONOMOUS mode contract.
   - Output: `PROJECT_RESEARCH_BRIEF.md`, `MASTER_RESEARCH_PROGRAM.md`,
     `DOMAIN_MAP.md`, `COVERAGE_DEBT.md`, `GAP_LEDGER.md`, `CHECKPOINT.md`,
     `EXECUTOR_START_PROMPT.md`. Per skill 02's hard stop condition, it stops
     here — it does not begin executing the research itself.
   - `RUN_RESULT.handoff.next_skill: canonical-context-builder` (to fold the
     research architecture back into project canon) — the actual research
     execution goes to a separate, future Research Executor per
     `docs/FUTURE_EXTENSIONS.md`, never merged into this skill.

## What must hold
- `research-architect` never begins deep research itself — `EXECUTOR_START_PROMPT.md`
  is a handoff document for a separate executor, not a research report.
- Iteration counts in `MASTER_RESEARCH_PROGRAM.md`/`CHECKPOINT.md` meet the
  200/150/50 invariants from `docs/RESEARCH_ARCHITECT_V2_INVARIANTS.md` —
  this is the one skill where the suite's build agent was told these numbers
  are non-negotiable, and this walkthrough is the check that they weren't
  quietly dropped in exchange for brevity.

## Failure signature
`EXECUTOR_START_PROMPT.md` containing actual research findings (rather than
an architecture/plan for finding them) means the skill merged with a
Research Executor role it must stay separate from.
