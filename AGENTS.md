# Skill Foundry — Repository Instructions V5

Read in this order before Foundry work:
1. `FOUNDRY_CANON.md`
2. `FOUNDRY_OPERATING_MODEL.md`
3. `COLLABORATION_PROTOCOL.md`
4. current task prompt/handoff
5. current candidate + compact registry/taxonomy/ontology
6. only relevant V1 baseline pieces

## Scope lock
This repository exists only to discover, classify, specify, build, validate, audit and package reusable agentic Skills. Do not import unrelated project/personal context. Examples or vertical names inside the original canon/baseline are illustrative/test evidence, not current-cycle facts.

## Baseline lock
`baseline/agentic-skill-suite-v1/` is an exact implemented precedent of 15 Skills. Do not modify it unless an explicit migration is approved.

## Operating lifecycle
`FOUNDRY_OPERATING_MODEL.md` + `foundry/workflows/SF-WF-001_SKILL_GENESIS.md` are the canonical executable process. Do not replace them with a different abstract framework during ordinary work.

## Decision precedence
`REUSE → EXTEND → MODE → DEPENDENT_SKILL → NEW_SKILL → NO_SKILL`.
A workflow node is not automatically a Skill. A new Skill is not the default output.

## Human gate
G6 is mandatory for every architecture/closure proposal. Do not self-approve buildable architecture or silently close REUSE/NO_SKILL before the human decision.

## Skill package architecture
`SKILL.md` is the universal core. Platform behavior belongs in thin adapters. Reuse shared contracts before inventing new ones.

## Git
- `main` stable canon.
- Cursor `agent/cursor`.
- Antigravity `agent/antigravity`.
- Sync latest `origin/main` before each work unit.
- Never force-push.
- Push meaningful completed work.

## Context efficiency
Prefer current candidate artifacts, registry entries, manifests, diffs and checkpoints over full-history reloads. Do not duplicate canonical policy into every artifact.
