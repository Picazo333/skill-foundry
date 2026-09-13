# Foundation Gap Map: G0–G10 Lifecycle Coverage & Meta-Capability Analysis

Status: **CANONICAL FOUNDATION AUDIT**  
Authority: `FOUNDRY_CANON.md` §13, `FOUNDRY_OPERATING_MODEL.md` §3, `SF-WF-002_BOOTSTRAP_V5.md`  
Precedence: `REUSE → EXTEND → MODE → DEPENDENT_SKILL → NEW_SKILL → NO_SKILL`  
Rule: **Capability ≠ Skill**. Workflow stages are process nodes, not automatic meta-Skills.

---

## 1. Executive Summary

This document evaluates the 11 Skill Genesis lifecycle stages (G0–G10) against existing baseline capabilities, deterministic repository tooling, agentic execution roles, and human governance gates.

The goal is to determine the exact operational mechanism for each gate without artificially manufacturing a distinct "meta-Skill" for every process step.

---

## 2. Comprehensive G0–G10 Lifecycle Mapping

| Stage | Stage Name | Process Description | Existing Coverage / Mechanism | Gap / Missing Function | Architectural Decision |
|---|---|---|---|---|---|
| **G0** | **INTAKE** | Capture human raw workflow/need; separate facts, inference, unknowns. | Covered in part by `rapid-capture-triage` (raw capture) + `00_INTAKE.template.md`. | Intake specifically tailored to Skill Genesis schemas (distinguishing workflow signals from prompt requests). | `REUSE` + Template (`00_INTAKE.template.md`). Agent executes G0 using intake template. |
| **G1** | **WORKFLOW RECONSTRUCTION** | Reconstruct full process tree (triggers, steps, actors, tools, handoffs, stop conditions). | Process reasoning; follows `01_WORKFLOW_RECONSTRUCTION.template.md`. | Structured tag syntax enforcement (`[H]`, `[A]`, `[D]`, `[S]`, `[T]`, `[K]`, `[R]`). | `REUSE` + Process discipline. No new Skill needed; standard agent analytical execution. |
| **G2** | **CAPABILITY MINING** | Decompose reconstructed workflow into durable capabilities (reject microtasks). | Analytical capability mapping using `02_CAPABILITY_MAP.template.md`. | Ensuring agents enforce "Capability ≠ Skill" and avoid 1:1 node-to-skill translation. | `REUSE` + Template enforcement. Rule is codified in Canon & Operating Model. |
| **G3** | **REGISTRY & OVERLAP ANALYSIS** | Compare mined capabilities against `SKILL_REGISTRY.yaml` using strict decision precedence. | `foundry/registry/SKILL_REGISTRY.yaml` + `03_OVERLAP_ANALYSIS.template.md`. | Rigorous precedence enforcement (`REUSE → EXTEND → MODE → DEPENDENT_SKILL → NEW_SKILL → NO_SKILL`). | `REUSE` + Registry lookup. Agentic analytical comparison using structured template. |
| **G4** | **CONDITIONAL RESEARCH** | Targeted research on external standards, schemas, domain best practices when evidence changes architecture. | `research-architect` (for structuring research programs); web search / documentation tools for targeted lookup. | Distinguishing between skipped research (`RESEARCH_SKIPPED`) vs structured investigation. | `REUSE` (existing research tools / `research-architect` principles). Skip reason recorded when not needed. |
| **G5** | **ARCHITECTURE PROPOSAL** | Synthesize smallest coherent architecture bundle (or closure recommendation). | `05_SKILL_ARCHITECTURE_PROPOSAL.template.md`. | Consistently generating closure proposals for `REUSE`/`NO_SKILL` as well as buildable proposals. | `REUSE` + Template. Agent packages candidate bundle for G6. |
| **G6** | **HUMAN DECISION** | Mandatory human checkpoint for all G5 outcomes (approve, reject, correct, request research). | Sovereign Human Governance; recorded in `DECISION.md`. | Human prompt/response loop. | `NO_SKILL` (Human Governance Gate). Autonomous progression strictly forbidden prior to G6. |
| **G7** | **SURGICAL SPECIFICATION** | Implementation-ready spec with YAML frontmatter + 19 mandatory sections. | `foundry/contracts/skill-spec.schema.json` + `APPROVED_SKILL_SPEC.template.md`. | Frontmatter validation and completeness verification. | `REUSE` + Contract verification via `tools/validate_foundry.py`. |
| **G8** | **BUILD** | Implement `SKILL.md`, schemas, evals (>=4 cases), adapters, manifests. | Cursor/Builder execution role + `catalog/_template/` substrate. | Mechanical package validation before declaring `BUILD_COMPLETE`. | `REUSE` + Substrate templates + validator tools (`tools/validate_foundry.py`). |
| **G9** | **INDEPENDENT AUDIT** | Audit build against spec, baseline, drift, token efficiency, portability. | `product-auditor` / `brand-quality-auditor` principles + `AUDIT_REPORT.template.md`. | Automated and independent review report generation with PASS/REWORK verdict. | `REUSE` + Antigravity Auditor role using `AUDIT_REPORT.template.md`. |
| **G10** | **PUBLISH & CANON UPDATE** | Merge to main, update `SKILL_REGISTRY.yaml`, update taxonomy/ontology, update checkpoint. | Git merge + YAML registry update + `foundry/state/CHECKPOINT.md`. | Systematic registry entry schema compliance. | `REUSE` + Deterministic tooling / Antigravity canonical stewardship. |

---

## 3. Analysis of Potential Meta-Capabilities (Future Proposals)

During the foundation audit, two potential high-level meta-capabilities were examined to determine whether they warrant dedicated Skills or remain operational workflows:

### A. Genesis Workflow Assistant (`sf-genesis-assistant`) — PROPOSED
- **Nature**: An interactive agentic workflow guiding an operator through G0–G5 intake, capability mining, and overlap analysis.
- **Evaluation**: The current substrate of templates (`00_INTAKE.template.md` through `05_SKILL_ARCHITECTURE_PROPOSAL.template.md`) combined with the prompt instructions in `FOUNDRY_OPERATING_MODEL.md` and `SF-WF-001_SKILL_GENESIS.md` already provides complete operational guidance. Packaging this as a dedicated Skill in `catalog/skills/` is premature until high-volume intake proves that manual prompt execution degrades quality.
- **Status**: **PROPOSED** (pending human G6 decision; current recommendation is to operate via repository workflows).

### B. Foundry Pipeline Orchestrator (`sf-foundry-orchestrator`) — PROPOSED
- **Nature**: An autonomous state-machine orchestrator tracking candidate state transitions, handoffs between Antigravity (Architect/Auditor) and Cursor (Builder), and triggering validation tools.
- **Evaluation**: Per `FOUNDRY_CANON.md` §7, orchestrators should not be built prematurely before multiple active worker packages and candidate streams exist. Currently, the collaboration protocol (`COLLABORATION_PROTOCOL.md`) and Git branch model provide clean, resilient coordination.
- **Status**: **PROPOSED** (pending human G6 decision; current recommendation is to coordinate via `CHECKPOINT.md` and Git).

---

## 4. Architectural Conclusions

1. **Zero Unjustified Meta-Skills**: The deterministic substrate, templates, schemas, and validator tools in V5 completely fulfill the operational requirements of G0–G10.
2. **Strict Gate Discipline**: G6 is the sole human checkpoint; all other transitions are autonomous within strict schema and audit boundaries.
3. **Precedence Maintained**: No new skills are created for the Foundry itself during this bootstrap phase; all capabilities remain cleanly accounted for through existing tools and operational roles.
