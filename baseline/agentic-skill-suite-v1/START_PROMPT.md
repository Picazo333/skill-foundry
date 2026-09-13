# START PROMPT — CLAUDE SONNET
## Build the Agentic Skill Suite autonomously

You are the implementation agent for this repository.

Your mission is to transform this blueprint into a production-quality, self-contained **15-skill agentic suite**.

Do not treat this as brainstorming. Build the complete repository.

---

# 1. READ FIRST

Before writing implementation:

1. Read `README.md`.
2. Read `MASTER_PLAN.md`.
3. Read `ARCHITECTURE.md`.
4. Read `WORKFLOW_MAP.md`.
5. Read `PORTABILITY.md`.
6. Read `TOKEN_EFFICIENCY.md`.
7. Read `QUALITY_GATES.md`.
8. Read every `skills/*/SPEC.md`.
9. Inspect `shared/` templates, policies and schemas.

Then create `EXECUTION_PLAN.md` containing only:
- build order;
- dependencies;
- wave boundaries;
- checkpoint points;
- QA sequence;
- packaging sequence.

## Autonomy rule

Once `EXECUTION_PLAN.md` exists, **do not ask the user to approve it**. Continue automatically.

Do not stop to ask:
- “Should I continue?”
- “Would you like me to build the next skill?”
- “Do you approve this structure?”
- questions already answered by this repo.

Stop only if a genuine hard blocker prevents further progress and cannot be solved from the available repository/files/tools.

When several valid choices exist, choose the one that best:
1. preserves portability;
2. minimizes duplication;
3. improves reliability;
4. reduces token/context cost;
5. remains easy to audit.

---

# 2. CANONICAL IMPLEMENTATION

Every skill gets **one canonical core**.

Do not create five independent versions.

Final folder:

```text
skills/<skill>/
  SKILL.md
  README.md
  manifest.json
  schemas/
  templates/
  references/
  examples/
  evals/
  adapters/
```

Required adapters:
- generic;
- chatgpt;
- codex;
- claude;
- gemini;
- cursor.

Adapters are thin wrappers. They may not silently change purpose, procedure, outputs, quality gates or stop conditions.

If a platform lacks a formal skill primitive, produce a portable instruction adapter instead of inventing unsupported behavior.

---

# 3. BUILD ORDER

Use this sequence unless a dependency analysis proves a superior one.

## Wave 0 — Foundation
Build shared schemas, manifest contract, adapter contract, checkpoint contract, eval contract and canonical template. Validate architecture with one representative skill.

## Wave 1 — Cross-functional primitives
1. Canonical Context Builder
2. Rapid Capture & Triage
3. Research Architect
4. Product Auditor & Implementation Architect
5. AI Resource Router

## Wave 2 — Brand foundations
6. Brand Discovery
7. Brand Strategy
8. Brand Verbal Identity
9. Brand Visual Direction

## Wave 3 — Brand production
10. Brand Identity System
11. Brand Book Builder
12. Creative Brief Generator
13. Brand Content System
14. Brand Quality Auditor

## Wave 4 — Orchestration
15. Brand Skill Orchestrator

Build the Orchestrator last so it routes real contracts, not imagined ones.

## Wave 5 — Integration
- cross-skill tests;
- handoff validation;
- adapters;
- exports;
- documentation;
- final QA;
- ZIP.

---

# 4. CHECKPOINTS — MANDATORY

Maintain `CHECKPOINT.md`.

Update:
- after Wave 0;
- after every 2–3 completed skills;
- after every Wave;
- immediately before packaging.

Use:

```yaml
phase:
completed:
partially_completed:
files_created:
tests_passed:
tests_failed:
known_issues:
decisions_locked:
next_exact_action:
resume_command:
```

Keep it concise and recovery-oriented.

When resuming:
1. read checkpoint;
2. verify claimed files exist;
3. run smallest relevant smoke test;
4. continue from `next_exact_action`;
5. do not rebuild completed skills unless an integration failure requires it.

---

# 5. TOKEN / CONTEXT OPTIMIZATION

Apply the policies in `TOKEN_EFFICIENCY.md` aggressively.

Mandatory:
- centralize common instructions;
- progressive context loading;
- structured artifact handoffs;
- delta updates;
- explicit stop conditions;
- narrow retries;
- compact logs;
- batch mechanical adapter/eval generation only after the pattern is validated;
- no duplicate platform implementations.

Do not expose chain-of-thought. Record only decisions, deltas, failures and next action.

---

# 6. QUALITY STANDARD

A skill is not complete because its folder exists.

It must have:
1. clear trigger;
2. clear non-trigger;
3. minimum inputs;
4. optional inputs;
5. executable procedure;
6. explicit output schema;
7. handoffs;
8. stop conditions;
9. failure modes;
10. minimum 3 meaningful evals + 1 edge/failure case;
11. portable adapters;
12. integration validation where applicable.

Avoid generic “AI best practices”. Reflect the actual workflows in each `SPEC.md`.

---

# 7. RESEARCH ARCHITECT — SPECIAL CONTRACT

Preserve the methodology of Research Plan Architect v2:
- minimum **200 valid iterations**;
- minimum **150 scope-expansion**;
- minimum **50 domain-polishing/consolidation**;
- material-delta/novelty test;
- key-area weighting;
- Coverage Debt;
- contradictions;
- white-space protocol;
- domain interconnection;
- evidence requirements;
- 10 quality passes.

Add an **AUTONOMOUS architecture mode**:
1. create the complete architecture plan;
2. checkpoint;
3. execute architecture rounds automatically without asking for “Siguiente” / “y”;
4. checkpoint after logical blocks;
5. stop before deep research;
6. output an executor-ready research package.

Do not merge Research Architect with Research Executor.

---

# 8. PORTABILITY

All canonical skills must be platform-agnostic.

Generate exports/adapters for:
- ChatGPT;
- Codex;
- Claude;
- Gemini;
- Cursor;
- Generic.

A platform switch must be possible using canonical artifacts + checkpoint + adapter. No chat memory may be required for correctness.

---

# 9. EVALS & INTEGRATION TESTS

Each skill:
- minimum 3 scenarios;
- minimum 1 edge/failure case;
- expected artifact properties;
- forbidden behavior;
- pass/fail criteria.

Suite integration must test at least:

1. chaotic voice note → Rapid Capture → Canonical Context;
2. new business idea → Research Architect → executor-ready package;
3. existing app → Product Auditor → implementation handoff;
4. new brand → Discovery → Strategy → Verbal + Visual → Identity → Brand Book → QA;
5. existing brand → Content System → Creative Brief → QA;
6. multi-tool workload → AI Resource Router;
7. Brand Orchestrator resumes a partially completed brand without restarting finished stages.

---

# 10. FINAL PACKAGE

At the end:
1. run evals/integration checks;
2. create `FINAL_REPORT.md`;
3. create `suite.manifest.json`;
4. generate exports;
5. move useful checkpoints/QA into `docs/`;
6. remove disposable scratch files;
7. package:

`dist/AGENTIC_SKILL_SUITE_V1.zip`

Also create:
`dist/AGENTIC_SKILL_SUITE_V1_SHA256.txt`

The ZIP must contain all 15 finished skills, shared contracts, adapters, examples, evals, docs, workflow map, manifest and final report.

---

# 11. FINAL RESPONSE

Do not paste every file into chat.

Return only:
- completion status;
- number of skills completed;
- eval summary;
- unresolved issues;
- final ZIP path;
- final report path.

Begin now: read this repo, write `EXECUTION_PLAN.md`, then continue autonomously.
