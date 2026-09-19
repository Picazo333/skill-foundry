# R5 — Minimum Factory Ontology / Facets

Decision question: Which minimum Foundry-owned concepts materially improve Factory classification, dedup, routing and maintenance?

## Evidence
G3 intentionally deferred portfolio concepts until Factory existed. G5 now needs portfolio identity, item identity, ordered execution groups and traceable architecture exceptions.

## Decision
Add only these canonical Foundry domain entities:
- **Portfolio** — one bounded Factory intake/architecture/manufacturing program.
- **PortfolioItem** — one normalized capability/workflow observation under disposition.
- **Wave** — one dependency-safe execution group.
- **ArchitectureException** — a post-Plan-Lock finding that would change approved meaning/scope/topology.

Do not promote these to ontology entities yet:
- EffortProfile;
- RiskProfile;
- PlanLock;
- SourceFragment.

They remain typed contract/artifact concepts until repeated usage proves ontology value. Plan Lock is an explicit HumanDecision over a portfolio proposal.

## Minimum item facets
- item_type;
- family;
- disposition;
- effort;
- risk;
- dependencies;
- source_refs;
- lifecycle/status.

No deep domain hierarchy is introduced.

Confidence: high.

Revisit trigger: routing/dedup/maintenance requires a relation that cannot be expressed without hacks in two or more real portfolios.
