# V1 Capability Coverage Analysis

Status: **CANONICAL BASELINE AUDIT**  
Authority: `FOUNDRY_CANON.md` §2, `FOUNDRY_OPERATING_MODEL.md` §3 (G3), `SF-WF-002_BOOTSTRAP_V5.md`  
Scope: Deep inspection of all 15 baseline skills in `baseline/agentic-skill-suite-v1/`.

---

## 1. Executive Summary

The V1 baseline suite represents an implemented, verified precedent of 15 modular, composable agentic skills. It partitions capabilities into two primary families:
1. **Cross-functional Operating Skills (01–05)**: Core architectural, context management, triage, and dispatch capabilities.
2. **Brand & Creative Operating Skills (06–15)**: End-to-end brand development, strategy, verbal/visual identity, design systems, content architecture, quality auditing, and orchestration.

Every skill follows the canonical core pattern (`SKILL.md` + schemas + evals + thin platform adapters), enforces explicit non-triggers, defines strict stop conditions, and operates with clear handoff interfaces.

---

## 2. Cross-Functional Operating Skills (01–05)

### 01. Canonical Context Builder (`canonical-context-builder`)
- **Order & Family**: 1 | `cross-functional`
- **Purpose & Core Boundary**: Reconstruct and maintain the single canonical truth of a project from fragmented conversations, files, renames, decisions, and prior outputs.
- **Key Inputs**: Fragmented chat logs, project files, decision fragments, previous unversioned notes.
- **Key Outputs**: `PROJECT_CANON.md`, `DECISION_REGISTER.md`, `OPEN_LOOPS.md`, `DEPRECATED_REGISTER.md`, `NEXT_START_PROMPT.md`.
- **Actual Handoffs**:
  - `handoffs_to`: `research-architect`, `product-auditor`, `brand-discovery`, `brand-skill-orchestrator`, `rapid-capture-triage`.
  - `handoffs_from`: `rapid-capture-triage`, `research-architect`, `product-auditor`, `brand-discovery`, `brand-skill-orchestrator`.
- **Dependencies**: None (foundational anchor).
- **Genesis Coverage**: Serves as the primary truth-crystallization engine across multi-stage workflows; provides context stabilization before downstream reasoning.
- **Explicit Non-Coverage**:
  - Generic summarization with no canonical-state requirement.
  - Primary research outside supplied sources.
  - Inventing missing facts or filling gaps with unverified guesses.
  - Producing downstream execution or implementation plans.

### 02. Research Architect (`research-architect`)
- **Order & Family**: 2 | `cross-functional`
- **Purpose & Core Boundary**: Transform a raw idea/problem into an exhaustive, decision-oriented research architecture (weighted, interconnected domain map and iteration program) *before* deep research; explicitly stops before executing the deep research itself.
- **Key Inputs**: Problem statement, target domains, business/product hypotheses, high-level objectives.
- **Key Outputs**: `PROJECT_RESEARCH_BRIEF.md`, `MASTER_RESEARCH_PROGRAM.md`, `DOMAIN_MAP.md`, `COVERAGE_DEBT.md`, `GAP_LEDGER.md`, `CHECKPOINT.md`, `EXECUTOR_START_PROMPT.md`.
- **Actual Handoffs**:
  - `handoffs_to`: `canonical-context-builder`, `ai-resource-router`.
  - `handoffs_from`: `canonical-context-builder`, `ai-resource-router`, `brand-discovery`, `brand-skill-orchestrator`.
- **Dependencies**: None.
- **Genesis Coverage**: Solves the scoping and question-design phase for exploratory or uncertain domains (G4 research structuring).
- **Explicit Non-Coverage**:
  - Deep research execution (live web crawling, paper downloading, data extraction).
  - Single factual lookups or narrow comparisons.
  - Simple technical fixes.
  - Rebuilding project canon from scratch.

### 03. Product Auditor & Implementation Architect (`product-auditor`)
- **Order & Family**: 3 | `cross-functional`
- **Purpose & Core Boundary**: Inspect an existing app, repository, or product workflow, verify issues/opportunities against concrete evidence, and produce an implementation plan precise enough for execution without writing code during audit mode.
- **Key Inputs**: Codebase files, UX recordings/walkthroughs, issue backlogs, architecture diagrams.
- **Key Outputs**: `PRODUCT_AUDIT.md`, `IMPLEMENTATION_PLAN.md`, `REGRESSION_MATRIX.md`, `QA_CONTRACT.md`, `HANDOFF_PROMPT.md`.
- **Actual Handoffs**:
  - `handoffs_to`: `ai-resource-router`, `canonical-context-builder`.
  - `handoffs_from`: `canonical-context-builder`, `rapid-capture-triage`, `ai-resource-router`, `brand-quality-auditor`.
- **Dependencies**: None.
- **Genesis Coverage**: Models the inspection-before-action paradigm; enforces separation between evaluation/architecture and execution.
- **Explicit Non-Coverage**:
  - Writing or editing production source code directly.
  - Generic feature ideation without inspecting the current state.
  - Replacing approved design/brand direction without audit evidence.
  - Building project canon from zero.

### 04. Rapid Capture & Triage (`rapid-capture-triage`)
- **Order & Family**: 4 | `cross-functional`
- **Purpose & Core Boundary**: Convert fast, chaotic voice-note/text captures into structured project/process/task/idea updates while preserving ambiguity and minimizing formatting overhead.
- **Key Inputs**: Raw unstructured voice dictations, brain dumps, loose notes.
- **Key Outputs**: `CAPTURE_PREVIEW.md`, `STRUCTURED_DELTA.json`, `AMBIGUITIES.md`, `APPLY_INSTRUCTIONS.md`.
- **Actual Handoffs**:
  - `handoffs_to`: `canonical-context-builder`, `product-auditor`, `ai-resource-router`.
  - `handoffs_from`: `canonical-context-builder`.
- **Dependencies**: None.
- **Genesis Coverage**: Handles raw human intake (G0 pre-processing); translates stream-of-consciousness input into structured candidate signals.
- **Explicit Non-Coverage**:
  - Long-term canonical synthesis across historical archives.
  - Executing captured action items.
  - Hallucinating unstated priorities, owners, or deadlines.
  - Product quality auditing.

### 05. AI Resource Router (`ai-resource-router`)
- **Order & Family**: 5 | `cross-functional`
- **Purpose & Core Boundary**: Route tasks to the optimal AI model, platform, or tool based on capability fit, quota availability, context limits, reset urgency, and cost constraints; generates tailored dispatch prompts.
- **Key Inputs**: Task backlog, available AI subscriptions/quotas, platform capabilities, token constraints.
- **Key Outputs**: `ROUTING_PLAN.md`, `DISPATCH_QUEUE.json`, `PROMPTS/` (dispatch prompts), `CAPACITY_RISK.md`.
- **Actual Handoffs**:
  - `handoffs_to`: `research-architect`, `product-auditor`, `brand-skill-orchestrator`.
  - `handoffs_from`: `canonical-context-builder`, `research-architect`, `product-auditor`, `rapid-capture-triage`, `brand-content-system`, `brand-skill-orchestrator`.
- **Dependencies**: None.
- **Genesis Coverage**: Provides deterministic/heuristic workload dispatch across disparate AI models and environments.
- **Explicit Non-Coverage**:
  - Abstract benchmarking without concrete routing targets.
  - Performing the actual domain work of dispatched tasks.
  - Multi-stage project orchestration or workflow state machine management.

---

## 3. Brand & Creative Operating Skills (06–15)

### 06. Brand Discovery (`brand-discovery`)
- **Order & Family**: 6 | `brand-creative`
- **Purpose & Core Boundary**: Convert raw founder interviews, customer notes, market signals, and business context into a structured, canonical brand discovery brief.
- **Key Inputs**: Stakeholder interviews, market notes, raw founder vision.
- **Key Outputs**: `BRAND_DISCOVERY_BRIEF.md`, `STAKEHOLDER_MATRIX.md`, `AUDIENCE_RAW_SIGNALS.md`, `DISCOVERY_SYNTHESIS.md`.
- **Actual Handoffs**:
  - `handoffs_to`: `brand-strategy`, `canonical-context-builder`, `research-architect`.
  - `handoffs_from`: `canonical-context-builder`, `brand-skill-orchestrator`.
- **Dependencies**: None.
- **Genesis Coverage**: Upstream domain intake for brand positioning workflows.
- **Explicit Non-Coverage**: Finalizing brand strategy, inventing brand names/visuals, writing finished copy.

### 07. Brand Strategy (`brand-strategy`)
- **Order & Family**: 7 | `brand-creative`
- **Purpose & Core Boundary**: Define positioning, market category, target personas, value proposition, brand pillars, and core differentiation based on discovery evidence.
- **Key Inputs**: `BRAND_DISCOVERY_BRIEF.md`, market evidence.
- **Key Outputs**: `BRAND_STRATEGY.md`, `POSITIONING_STATEMENT.md`, `VALUE_PROPOSITION.md`, `AUDIENCE_PERSONAS.md`.
- **Actual Handoffs**:
  - `handoffs_to`: `brand-verbal-identity`, `brand-visual-direction`, `brand-skill-orchestrator`.
  - `handoffs_from`: `brand-discovery`, `brand-skill-orchestrator`.
- **Dependencies**: `brand-discovery`.
- **Genesis Coverage**: Strategic reasoning and positioning core for brand assets.
- **Explicit Non-Coverage**: Writing marketing copy, visual asset creation, design system tokens.

### 08. Brand Verbal Identity (`brand-verbal-identity`)
- **Order & Family**: 8 | `brand-creative`
- **Purpose & Core Boundary**: Operationalize voice attributes, tone matrices, messaging pillars, tagline options, and terminology rules (dos/don'ts).
- **Key Inputs**: `BRAND_STRATEGY.md`.
- **Key Outputs**: `VERBAL_IDENTITY.md`, `TONE_MATRIX.md`, `MESSAGING_FRAMEWORK.md`, `VOCABULARY_RULES.md`.
- **Actual Handoffs**:
  - `handoffs_to`: `brand-book-builder`, `creative-brief-generator`, `brand-content-system`, `brand-quality-auditor`.
  - `handoffs_from`: `brand-strategy`, `brand-book-builder` (feedback loop), `brand-skill-orchestrator`.
- **Dependencies**: `brand-strategy`.
- **Genesis Coverage**: Codifies verbal language standards and voice constraints.
- **Explicit Non-Coverage**: Writing full blog posts/campaigns, visual design, strategy modification.

### 09. Brand Visual Direction (`brand-visual-direction`)
- **Order & Family**: 9 | `brand-creative`
- **Purpose & Core Boundary**: Explore, structure, and compare creative territories, aesthetic moodboards, visual metaphors, and visual anti-patterns to lock an approved visual direction.
- **Key Inputs**: `BRAND_STRATEGY.md`.
- **Key Outputs**: `VISUAL_TERRITORIES.md`, `APPROVED_VISUAL_DIRECTION.md`, `VISUAL_ANTI_PATTERNS.md`, `GENERATION_LANGUAGE.md`.
- **Actual Handoffs**:
  - `handoffs_to`: `brand-identity-system`, `creative-brief-generator`, `brand-quality-auditor`.
  - `handoffs_from`: `brand-strategy`, `brand-skill-orchestrator`.
- **Dependencies**: `brand-strategy`.
- **Genesis Coverage**: Creative territory exploration and visual constraint definition.
- **Explicit Non-Coverage**: Exact token/pixel engineering, logo vector files, verbal copy generation.

### 10. Brand Identity System (`brand-identity-system`)
- **Order & Family**: 10 | `brand-creative`
- **Purpose & Core Boundary**: Turn an approved visual direction into an operational identity system: logo usage rules, color tokens (hex/rgb/contrast), type scale, grid/spacing, iconography/imagery guidelines.
- **Key Inputs**: `APPROVED_VISUAL_DIRECTION.md`, `BRAND_STRATEGY.md`.
- **Key Outputs**: `IDENTITY_SYSTEM.md`, `DESIGN_TOKENS.json`, `APPLICATION_RULES.md`.
- **Actual Handoffs**:
  - `handoffs_to`: `brand-book-builder`, `creative-brief-generator`, `brand-quality-auditor`.
  - `handoffs_from`: `brand-visual-direction`, `brand-book-builder` (feedback loop), `brand-skill-orchestrator`.
- **Dependencies**: `brand-visual-direction`.
- **Genesis Coverage**: Systematic design tokenization and rule codification.
- **Explicit Non-Coverage**: Subjective moodboarding, brand narrative synthesis, campaign asset production.

### 11. Brand Book Builder (`brand-book-builder`)
- **Order & Family**: 11 | `brand-creative`
- **Purpose & Core Boundary**: Compile validated verbal and visual identity canon into a single, cohesive, client-ready brand manual without reopening upstream strategic decisions or hallucinating missing rules.
- **Key Inputs**: `VERBAL_IDENTITY.md`, `IDENTITY_SYSTEM.md`, `BRAND_STRATEGY.md`.
- **Key Outputs**: `BRAND_BOOK.md`, `BRAND_BOOK_OUTLINE.md`, `BRAND_BOOK_ASSET_CHECKLIST.md`.
- **Actual Handoffs**:
  - `handoffs_to`: `creative-brief-generator`, `brand-content-system`, `brand-quality-auditor`, `brand-verbal-identity`, `brand-identity-system`.
  - `handoffs_from`: `brand-verbal-identity`, `brand-identity-system`, `brand-quality-auditor` (feedback), `brand-skill-orchestrator`.
- **Dependencies**: `brand-verbal-identity`, `brand-identity-system`.
- **Genesis Coverage**: Document compilation and canon packaging.
- **Explicit Non-Coverage**: Inventing rules to fill gaps; creative ideation; production asset creation.

### 12. Creative Brief Generator (`creative-brief-generator`)
- **Order & Family**: 12 | `brand-creative`
- **Purpose & Core Boundary**: Translate brand canon plus a specific business objective into an execution-ready brief for web, campaigns, social, video, or packaging.
- **Key Inputs**: `BRAND_BOOK.md` (or strategy + verbal identity), specific campaign objective.
- **Key Outputs**: `CREATIVE_BRIEF.md`, `ASSET_REQUIREMENTS.md`, `PRODUCTION_HANDOFF.md`.
- **Actual Handoffs**:
  - `handoffs_to`: `brand-quality-auditor`, `brand-content-system`.
  - `handoffs_from`: `brand-book-builder`, `brand-verbal-identity`, `brand-visual-direction`, `brand-identity-system`, `brand-content-system`, `brand-quality-auditor` (feedback), `brand-skill-orchestrator`.
- **Dependencies**: `brand-book-builder` (or verbal/visual canon).
- **Genesis Coverage**: Objective-to-brief translation and downstream specification.
- **Explicit Non-Coverage**: Strategy definition, direct asset production/copywriting, quality auditing.

### 13. Brand Content System (`brand-content-system`)
- **Order & Family**: 13 | `brand-creative`
- **Purpose & Core Boundary**: Turn approved brand canon into a repeatable content operating system: content pillars, format rules, cadence schedules, and reusable templates for ongoing production.
- **Key Inputs**: `BRAND_STRATEGY.md`, `VERBAL_IDENTITY.md`, `BRAND_BOOK.md`.
- **Key Outputs**: `CONTENT_SYSTEM.md`, `CONTENT_PILLARS.md`, `FORMAT_LIBRARY.md`, `CONTENT_PIPELINE.md`, `MEASUREMENT_MODEL.md`.
- **Actual Handoffs**:
  - `handoffs_to`: `creative-brief-generator`, `brand-quality-auditor`, `ai-resource-router`.
  - `handoffs_from`: `brand-book-builder`, `brand-verbal-identity`, `creative-brief-generator`, `brand-skill-orchestrator`.
- **Dependencies**: `brand-strategy`, `brand-verbal-identity`, `brand-book-builder`.
- **Genesis Coverage**: Recurring content workflow systematization.
- **Explicit Non-Coverage**: One-off social posts, brand strategy re-definition, QA auditing.

### 14. Brand Quality Auditor (`brand-quality-auditor`)
- **Order & Family**: 14 | `brand-creative`
- **Purpose & Core Boundary**: Audit a delivered creative/content asset against explicit brand canon (strategy, voice, visual identity) to detect drift, regression, and AI-slop, producing a traceable PASS/FIX/POLISH/DEFER verdict.
- **Key Inputs**: Delivered creative asset, reference brand canon (`BRAND_BOOK.md`, `VERBAL_IDENTITY.md`, etc.).
- **Key Outputs**: `BRAND_QA_REPORT.md`, `FIX_LIST.md`, `DRIFT_REGISTER.md`.
- **Actual Handoffs**:
  - `handoffs_to`: `brand-book-builder`, `creative-brief-generator`, `product-auditor`.
  - `handoffs_from`: `brand-verbal-identity`, `brand-visual-direction`, `brand-identity-system`, `brand-book-builder`, `creative-brief-generator`, `brand-content-system`, `brand-skill-orchestrator`.
- **Dependencies**: None.
- **Genesis Coverage**: Domain-specific quality gate and compliance audit.
- **Explicit Non-Coverage**: Creating brand canon, subjective critique without canon criteria, product software QA (routes to `product-auditor`).

### 15. Brand Skill Orchestrator (`brand-skill-orchestrator`)
- **Order & Family**: 15 | `brand-creative` / `orchestration`
- **Purpose & Core Boundary**: Coordinate and route multi-stage brand projects across worker skills (06–14) and cross-functional skills (01, 02, 05); maintain workflow state, resume partial projects without restarting finished stages, and manage handoff packages.
- **Key Inputs**: Project state, existing brand artifacts, target objective.
- **Key Outputs**: `BRAND_WORKFLOW_STATE.md`, `NEXT_SKILL_RUN.json`, `HANDOFF_PACKAGES/`, `COMPLETION_REPORT.md`.
- **Actual Handoffs**:
  - `handoffs_to`: Skills 01, 02, 05, 06, 07, 08, 09, 10, 11, 12, 13, 14.
  - `handoffs_from`: Skills 01, 05, 07.
- **Dependencies**: References skills 01–14 as workers.
- **Genesis Coverage**: Orchestrates a mature domain cluster after worker boundaries are established.
- **Explicit Non-Coverage**: Performing deep worker tasks internally; forcing unnecessary linear runs; replacing human gate decisions.

---

## 4. Synthesis & Architectural Takeaways

1. **Strict Separation of Concerns**: Workers do domain work; auditors evaluate against explicit contracts without modifying source; orchestrators route state without performing worker tasks.
2. **Context Efficiency by Design**: Skills load only immediate dependencies and schemas rather than full historical conversation logs.
3. **Traceability**: Every output artifact has a defined schema and clear recipient downstream.
4. **Baseline Invariant**: This 15-skill suite is locked as architectural precedent and must remain unmodified.
