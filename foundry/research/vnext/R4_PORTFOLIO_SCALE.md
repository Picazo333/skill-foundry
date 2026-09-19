# R4 — Portfolio Scale

Decision question: How should Factory represent 1→1000 inputs while preserving source accounting and avoiding premature graph infrastructure?

## Evidence
- Existing Foundry already benefits from durable Git artifacts and deterministic validation.
- Noema RC0 requires evidence before canon, durable coordination in artifacts, and complexity that pays rent.
- Anthropic recommends parallelization only when subtasks are independent and complexity is justified; predictable workflows remain preferable for well-defined paths.
- G4 proved one candidate lifecycle without a persistent runtime or graph database.

## Alternatives
1. Graph database / workflow runtime now.
2. One large portfolio YAML.
3. Git-native normalized ledgers + typed derived views.

## Decision
Choose **Git-native normalized ledgers + derived views**.

Canonical portfolio data:
- immutable raw/source fragments;
- stable normalized item IDs;
- explicit source→item mappings;
- explicit dispositions;
- typed dependency edges;
- explicit Plan Lock reference.

Derived views:
- family map;
- dependency DAG;
- wave plan;
- dashboard/status.

No graph DB is introduced. Derived views may be regenerated and never silently become authority.

## Scale rule
A portfolio may split raw/source/item records across files when size makes one file unwieldy, but IDs and schemas remain stable. Validation operates over the whole portfolio directory.

## Acceptance implication
Factory must prove:
- 100% source coverage;
- unique stable IDs;
- no dangling/duplicate dependency edges;
- every terminal item has a justified disposition;
- derived graphs are reproducible from canonical records.

Confidence: high.

Revisit trigger: repeated performance/maintenance problems at real portfolio scale that cannot be solved by indexed files or simple tooling.
