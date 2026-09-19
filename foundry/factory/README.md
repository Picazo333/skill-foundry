# Skill Foundry Factory

Factory is a **mode/control plane inside Skill Foundry**, not a separate product and not a new lifecycle replacing G0–G10.

## Canonical portfolio layout

```
foundry/factory/portfolios/<portfolio_id>/
├── 00_RAW/
├── 01_SOURCE_LEDGER.yaml
├── 02_ITEMS.yaml
├── 03_DEDUP_MAP.yaml
├── 04_FAMILY_MAP.yaml
├── 05_CONTRACT_MAP.yaml
├── 06_DEPENDENCY_GRAPH.yaml
├── 07_PORTFOLIO_PROPOSAL.md
├── 08_PLAN.yaml
├── 09_WAVES.yaml
├── 10_STATUS.yaml
├── 11_RISK_REGISTER.md
├── exceptions/
└── work_orders/
```

Authority lives in the normalized source/item/plan records. Family/dependency/wave views are derived and may not silently override the Plan Lock.

## Scale
The same representation supports 1→1000 items by splitting files when needed; stable IDs and validation semantics do not change.

## Human boundary
Factory discovery/architecture is interactive until Plan Lock. After Plan Lock routine execution is autonomous. Architecture-changing findings create explicit exceptions and do not silently mutate the locked plan.

## Validation
Use `python tools/validate_factory.py --portfolio <path>`.
