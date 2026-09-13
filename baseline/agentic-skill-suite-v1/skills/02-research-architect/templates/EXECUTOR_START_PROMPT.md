# EXECUTOR START PROMPT — <project name>

You are beginning **research execution** on <project name>. This package was
produced by `research-architect` and is self-sufficient — do not ask for
background, and do not re-derive the architecture. Read these artifacts
first:

- `PROJECT_RESEARCH_BRIEF.md` — master decision question, facts, hypotheses,
  constraints.
- `DOMAIN_MAP.md` — the weighted, interconnected domain structure.
- `MASTER_RESEARCH_PROGRAM.md` — every question to research, with its
  domain, material-delta justification, and decision link. Execute against
  this list; do not invent new top-level domains without checking
  `GAP_LEDGER.md`'s white-space ledger first.
- `COVERAGE_DEBT.md` — domains that were still under-explored architecturally;
  weight execution effort accordingly.
- `GAP_LEDGER.md` — contradictions to watch for/help resolve with evidence,
  white-space to prioritize, and primary-evidence triggers requiring
  interviews/surveys/direct measurement rather than secondary sources.

## Immediate objective
<first N questions/domains to execute, in priority order per DOMAIN_MAP.md weighting>

## Constraints carried forward
<from PROJECT_RESEARCH_BRIEF.md CONSTRAINTS>

## Explicit boundary
This prompt starts **execution** (live research, sourced findings, answering
the questions in `MASTER_RESEARCH_PROGRAM.md`). `research-architect` itself
never performs this step — if you are `research-architect`, you must not
continue past producing this file.
