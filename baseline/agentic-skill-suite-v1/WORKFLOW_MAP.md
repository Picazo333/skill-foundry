# WORKFLOW MAP

## General intake
```text
RAW INPUT / VOICE NOTES / FILES
        ↓
Rapid Capture & Triage
        ↓
Canonical Context Builder
        ↓
 major uncertainty? ──yes──> Research Architect ──> Research Executor (external)
        │ no
        ├──> Product Auditor (for product/app work)
        └──> Brand Discovery (for brand work)
```

`AI Resource Router` can be invoked at any execution boundary to choose the best available model/tool and generate a dispatch prompt.

## Brand workflow
```text
Rapid Capture
    ↓
Canonical Context
    ↓
Brand Discovery
    ↓
Brand Strategy
   ↙          ↘
Verbal       Visual Direction
Identity          ↓
   └──────→ Brand Identity System
                    ↓
              Brand Book Builder
                 ↙       ↘
      Creative Brief   Content System
                 ↘       ↙
              Brand Quality Auditor
```

`Brand Skill Orchestrator` routes this workflow, skips completed stages, and only asks for truly blocking missing inputs.

## Existing product/app
```text
Canonical Context
      ↓
Product Auditor & Implementation Architect
      ↓
IMPLEMENTATION PLAN
      ↓
AI Resource Router
      ↓
Execution Agent (external)
      ↓
Product Auditor — QA mode
      ↓
Canonical Context Builder — update canon
```

## Research-heavy business
```text
Rapid Capture → Canonical Context → Research Architect (autonomous architecture rounds)
→ Research Package → Research Executor (external) → Canon update
```
