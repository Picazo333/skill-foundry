# Reference: stage detection rules

Given an inventory of which artifacts exist (from `references/routed-skill-contracts.md`'s
outputs column) and their approval states, determine current stage and the
single next routing decision.

| Condition | Stage | Route to |
|---|---|---|
| `BRAND_DISCOVERY_BRIEF.md` missing, and objective needs it | DISCOVERY | `brand-discovery` |
| `BRAND_DISCOVERY_BRIEF.md` exists with material blocking `DISCOVERY_GAPS.md` | DISCOVERY (incomplete) | `research-architect` if the gap is market/category/customer uncertainty, else back to `brand-discovery` |
| `BRAND_DISCOVERY_BRIEF.md` exists, `BRAND_STRATEGY.md` missing | STRATEGY | `brand-strategy` |
| `BRAND_STRATEGY.md` exists (locked positioning), `VERBAL_IDENTITY.md` missing | VERBAL | `brand-verbal-identity` |
| `BRAND_STRATEGY.md` exists (locked positioning), `APPROVED_VISUAL_DIRECTION.md` missing | VISUAL | `brand-visual-direction` |
| both of the above missing | VERBAL+VISUAL (parallel) | both, as two independent `NEXT_SKILL_RUN.json` candidates — orchestrator still recommends one per run, per RUN_RESULT's single `next_skill`, defaulting to whichever the objective prioritizes or verbal-first if unspecified |
| `APPROVED_VISUAL_DIRECTION.md` exists, `IDENTITY_SYSTEM.md` missing/stale | IDENTITY SYSTEM | `brand-identity-system` |
| verbal set + identity-system set both complete, `BRAND_BOOK.md` missing | BRAND BOOK | `brand-book-builder` |
| `brand-book-builder` returned `PARTIAL` with a named coherence gap | BRAND BOOK (blocked) | whichever upstream skill(s) `brand-book-builder` named |
| canon sufficient for the requested deliverable, one-off request | PRODUCTION (brief) | `creative-brief-generator` |
| canon sufficient for the requested deliverable, recurring/systemic request | PRODUCTION (system) | `brand-content-system` |
| a production artifact was just delivered and this is a meaningful gate (milestone, external presentation, end of engagement) | QA | `brand-quality-auditor` |
| canon for the artifact's relevant dimensions is missing/unapproved | — | do not route to `brand-quality-auditor` yet; route to whichever skill owns the missing canon layer instead |
| execution environment/model allocation materially matters for the chosen next skill's run | (orthogonal) | `ai-resource-router`, then the chosen skill |
| objective fulfilled | DONE | none — write `COMPLETION_REPORT.md` |

## Conflict detection
Before applying the table above, scan the inventory for:
- **Duplicate artifacts** — two versions of the same required output with no
  clear authoritative one (no later date, no explicit approval). This is a
  `BLOCKED` condition, not routable — surface it, name both versions, ask
  which is authoritative.
- **Stale downstream artifacts** — a downstream artifact (e.g.
  `IDENTITY_SYSTEM.md`) that predates a newer upstream artifact it depends
  on (e.g. a revised `APPROVED_VISUAL_DIRECTION.md`). Route back to refresh
  the downstream artifact before proceeding further.
