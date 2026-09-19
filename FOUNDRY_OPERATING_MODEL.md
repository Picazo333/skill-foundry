# SKILL FOUNDRY — OPERATING MODEL V1.1

Status: **CANONICAL OPERATIONAL TRANSLATION**  
Authority: `FOUNDRY_CANON.md` remains the constitutional source. This file makes it executable and must not contradict it.

## 1. Purpose
Skill Foundry converts recurrent real-world workflows into the smallest coherent set of reusable agentic capabilities. Success can be REUSE, EXTEND, MODE, DEPENDENT_SKILL, NEW_SKILL, or NO_SKILL. Creating a new Skill is never the default objective.

## 2. Canonical unit of work
Every cycle has one stable `candidate_id`, created once at intake and reused across all artifacts.

Recommended format: `sf-cand-YYYYMMDD-<short-slug>`.

Candidate artifacts live under:
`foundry/candidates/<candidate_id>/`

Required bundle as the cycle advances:
- `00_INTAKE.md`
- `01_WORKFLOW_RECONSTRUCTION.md`
- `02_CAPABILITY_MAP.md`
- `03_OVERLAP_ANALYSIS.md`
- `04_RESEARCH_PLAN.md` and `04_RESEARCH_FINDINGS.md` only when research is actually needed
- `05_SKILL_ARCHITECTURE_PROPOSAL.md`
- `DECISION.md`

Approved build specs live under `foundry/specs/`; builds under `catalog/skills/`; audits under `foundry/reviews/`.

## 3. Skill Genesis lifecycle

### G0 — INTAKE
Capture the human's actual recurring activity/need before designing Skills. Separate explicit facts, labeled inference, and architecture-blocking unknowns.

**Output:** `00_INTAKE.md`  
**Gate:** enough real process signal exists to reconstruct a workflow. If indispensable information is missing, status `BLOCKED` with one exact question/next action.

### G1 — WORKFLOW RECONSTRUCTION
Reconstruct the real process/tree. For each stage identify trigger, inputs, actions, decisions, actors, tools, knowledge/context, persistent artifacts, handoffs, approvals, failure paths and stop condition.

Use tags where useful:
- `[H]` human judgment/approval
- `[A]` agentic reasoning
- `[D]` deterministic/mechanical
- `[S]` existing/proposed Skill
- `[T]` tool/platform
- `[K]` durable knowledge/context
- `[R]` persistent record/artifact

**Output:** `01_WORKFLOW_RECONSTRUCTION.md`  
**Gate:** another agent can understand the process without the original conversation.

### G2 — CAPABILITY MINING
Decompose the workflow into durable capabilities **without equating workflow nodes with Skills**. Classify recurrence, depth, actor type, scope, reuse potential, inputs/outputs and dependencies. Explicitly reject/absorb microtasks.

**Output:** `02_CAPABILITY_MAP.md`.

### G3 — REGISTRY & OVERLAP ANALYSIS
Compare every mined capability against `foundry/registry/SKILL_REGISTRY.yaml` and only the relevant baseline Skills.

Mandatory decision precedence:
1. `REUSE`
2. `EXTEND`
3. `MODE`
4. `DEPENDENT_SKILL`
5. `NEW_SKILL`
6. `NO_SKILL`

Every decision requires evidence and boundary reasoning.

**Output:** `03_OVERLAP_ANALYSIS.md`.

### G4 — CONDITIONAL RESEARCH
Research only when external evidence could materially improve methodology, standards/contracts, architecture, domain practices, platform behavior, eval design or portability.

When needed: define questions → collect/inspect evidence using available research capability/tools → distinguish sourced findings from inference → record architectural implications.

**Outputs:** `04_RESEARCH_PLAN.md`, `04_RESEARCH_FINDINGS.md`.  
**Skip:** record `RESEARCH_SKIPPED` and why.

### G5 — SKILL ARCHITECTURE PROPOSAL
Produce the **smallest coherent architecture** covering the workflow: reuse, extensions/modes, genuinely new Skills, deterministic utilities, human-only judgments, families, dependencies, handoff graph, shared contracts, tier and orchestrator assessment.

Even when the recommended outcome is only `REUSE` or `NO_SKILL`, produce a concise proposal/closure recommendation so the human can verify the decision.

**Output:** `05_SKILL_ARCHITECTURE_PROPOSAL.md`.

### G6 — HUMAN DECISION
Mandatory human architecture checkpoint for **all** G5 outcomes. The human may approve, reject, correct, merge/split, change priority or request research.

**Output:** `DECISION.md` recording exactly what is authoritative.

No buildable item may become `APPROVED_FOR_BUILD` before this gate.

If the approved outcome contains only `REUSE`/`NO_SKILL`, skip G7–G9 and close at G10 without fabricating a Skill.

### G7 — SURGICAL SPECIFICATION
For every approved buildable item (`EXTEND`, `MODE`, `DEPENDENT_SKILL`, `NEW_SKILL`), create an implementation-ready spec with YAML frontmatter plus full specification.

Required frontmatter:
- `status: APPROVED_FOR_BUILD`
- `candidate_id`
- `skill_id`
- `change_kind`
- `target_skill_id` when modifying/depending on an existing Skill

Required body: identity, trigger/non-trigger, inputs, context policy, procedure, autonomy, checkpoints when needed, outputs, contracts, quality gates, failure modes, stop conditions, dependencies, handoffs, token/context strategy, portability, at least 3 normal evals + 1 edge/failure eval, integration evals when needed, explicit out-of-scope, backward-compatibility/migration impact when extending or adding a mode.

**Output:** `foundry/specs/<skill_id>.md`.

### G8 — BUILD
Cursor/Builder implements exactly the approved spec.

Canonical package principle:
`SKILL.md` = universal source of truth + thin platform adapters only where needed.

Build requirements:
- reuse proven shared contracts before inventing new ones;
- minimum sufficient package, not boilerplate for ceremony;
- create required evals;
- validate mechanically where possible;
- repair failures autonomously;
- produce builder handoff.

Status becomes `BUILD_COMPLETE` only when required artifacts/evals exist and validation passes.

### G9 — INDEPENDENT AUDIT
Antigravity/Auditor compares the build against approved spec, baseline architecture, overlap decision, portability, context/token efficiency, handoffs, eval quality, regressions and scope creep.

Verdict is exactly:
- `PASS`, or
- `REWORK` with concrete defects and acceptance criteria.

Audit may not silently redesign the approved Skill.

### G10 — PUBLISH & CANON UPDATE
After human-approved `REUSE`/`NO_SKILL`, close the candidate and checkpoint without build.

After implementation `PASS`:
1. merge the passed implementation to `main`;
2. update Skill Registry;
3. update taxonomy/ontology only when a genuinely new concept is needed;
4. update routing/handoff data where catalog graph changed;
5. add/adjust integration evals where materially needed;
6. record version/provenance;
7. update Foundry checkpoint;
8. mark candidate/Skill `PUBLISHED` or closed outcome.

A published capability becomes baseline evidence for all future overlap analysis.

## 4. Lifecycle states
Allowed canonical states:
`INTAKE`, `WORKFLOW_MAPPED`, `CAPABILITIES_MINED`, `OVERLAP_ANALYZED`, `RESEARCHING`, `RESEARCH_SKIPPED`, `PROPOSED`, `AWAITING_HUMAN_DECISION`, `APPROVED_FOR_BUILD`, `BUILDING`, `BUILD_COMPLETE`, `AUDITING`, `REWORK`, `PASS`, `READY_FOR_MERGE`, `PUBLISHED`, `CLOSED_REUSE`, `CLOSED_NO_SKILL`, `REJECTED`, `BLOCKED`.

State movement must follow G0–G10; skipping a stage requires recording the applicable skip reason.

## 5. Stop conditions
A cycle stops only as:
- **PUBLISHED** — justified build passed audit and canon is updated;
- **CLOSED_REUSE** — human confirmed existing capability covers the need;
- **CLOSED_NO_SKILL** — human confirmed a Skill is not justified;
- **REJECTED** — human rejected the proposal;
- **BLOCKED** — indispensable input/decision is absent and exact next action is recorded.

## 6. Context discipline
Repository-level cold-start and static context routing are governed by `AGENTS.md` + `noema.project.yaml`. This operating model remains the **Foundry process authority**; Noema does not own or redefine taxonomy, ontology, registry, lifecycle, Skill contracts or eval semantics.

After the selected Noema mode loads its required stable files, Foundry work loads dynamically:
1. the current task/handoff;
2. only the current candidate artifacts;
3. compact Skill Registry when overlap/routing is relevant;
4. relevant existing Skill manifest/`SKILL.md` only;
5. deeper baseline evidence only when necessary.

Do not load the whole suite by default. Baseline examples are evidence/test fixtures, not current project facts. Unrelated personal/project context must not enter a Foundry cycle unless the human explicitly supplies it as that cycle's input.

Noema conformance is a repository-governance gate. It never substitutes for Foundry's own contracts, evals, G6 approval, G9 audit or publish gates.


## 7. Portfolio Factory mode
Portfolio-scale input is governed by `foundry/workflows/SF-WF-003_PORTFOLIO_FACTORY.md`.

Factory does not replace G0–G10. It:
1. preserves and normalizes many source items;
2. performs cross-item/catalog overlap and portfolio architecture;
3. obtains explicit Portfolio Review / Plan Lock;
4. schedules dependency-safe work units;
5. invokes ordinary Foundry build/audit semantics for buildable items;
6. serializes canonical publication;
7. re-runs overlap against the updated catalog between waves.

No real portfolio build may start before Plan Lock. Post-lock architecture-changing findings must become explicit ArchitectureExceptions instead of silent plan mutation.
