#!/usr/bin/env python3
"""Deterministic validation for a Skill Foundry Factory portfolio."""
from __future__ import annotations
import argparse
from pathlib import Path
import yaml, jsonschema

BUILDABLE={"EXTEND","MODE","DEPENDENT_SKILL","NEW_SKILL"}

def load_yaml(path: Path):
    with path.open(encoding="utf-8") as f:
        return yaml.safe_load(f) or {}

def load_json(path: Path):
    import json
    return json.loads(path.read_text(encoding="utf-8"))

def validate_schema(doc, schema, label, errors):
    try:
        jsonschema.validate(doc, schema)
    except Exception as e:
        errors.append(f"{label} schema invalid: {getattr(e,'message',str(e))}")

def detect_cycle(item_ids, deps):
    visiting=set(); visited=set()
    def dfs(n):
        if n in visiting: return True
        if n in visited: return False
        visiting.add(n)
        for d in deps.get(n,[]):
            if d in item_ids and dfs(d): return True
        visiting.remove(n); visited.add(n); return False
    return any(dfs(n) for n in item_ids)

def validate(root: Path, portfolio: Path):
    errors=[]; warnings=[]
    required=[
      "00_RAW/SOURCES.yaml","01_SOURCE_LEDGER.yaml","02_ITEMS.yaml",
      "06_DEPENDENCY_GRAPH.yaml","07_PORTFOLIO_PROPOSAL.md",
      "08_PLAN.yaml","09_WAVES.yaml","10_STATUS.yaml","11_RISK_REGISTER.md"
    ]
    for rel in required:
        if not (portfolio/rel).exists(): errors.append(f"missing portfolio artifact: {rel}")
    if errors: return errors,warnings,{}

    raw=load_yaml(portfolio/"00_RAW/SOURCES.yaml")
    ledger=load_yaml(portfolio/"01_SOURCE_LEDGER.yaml")
    item_doc=load_yaml(portfolio/"02_ITEMS.yaml")
    plan=load_yaml(portfolio/"08_PLAN.yaml")
    waves=load_yaml(portfolio/"09_WAVES.yaml")
    graph=load_yaml(portfolio/"06_DEPENDENCY_GRAPH.yaml")

    schemas={
      "ledger":load_json(root/"foundry/contracts/factory-source-ledger.schema.json"),
      "item":load_json(root/"foundry/contracts/portfolio-item.schema.json"),
      "plan":load_json(root/"foundry/contracts/portfolio-plan.schema.json"),
      "waves":load_json(root/"foundry/contracts/factory-wave.schema.json"),
    }
    validate_schema(ledger,schemas["ledger"],"source ledger",errors)
    validate_schema(plan,schemas["plan"],"portfolio plan",errors)
    validate_schema(waves,schemas["waves"],"wave plan",errors)

    raw_sources=raw.get("sources") or []
    raw_ids=[x.get("source_id") for x in raw_sources]
    if len(raw_ids)!=len(set(raw_ids)): errors.append("duplicate raw source_id")
    ledger_sources=ledger.get("source_fragments") or []
    ledger_ids=[x.get("source_id") for x in ledger_sources]
    if len(ledger_ids)!=len(set(ledger_ids)): errors.append("duplicate ledger source_id")
    missing=set(raw_ids)-set(ledger_ids); extra=set(ledger_ids)-set(raw_ids)
    if missing: errors.append(f"source coverage missing: {sorted(missing)}")
    if extra: errors.append(f"ledger references unknown raw sources: {sorted(extra)}")

    items=item_doc.get("items") or []
    ids=[x.get("item_id") for x in items]
    if len(ids)!=len(set(ids)): errors.append("duplicate item_id")
    item_ids=set(ids)
    by_id={x.get("item_id"):x for x in items}
    for i,item in enumerate(items):
        validate_schema(item,schemas["item"],f"portfolio item {i}",errors)

    for src in ledger_sources:
        mapped=src.get("normalized_item_ids") or []
        for item_id in mapped:
            if item_id not in item_ids: errors.append(f"source {src.get('source_id')} maps to missing item {item_id}")
        disp=src.get("disposition")
        if disp=="NORMALIZED" and not mapped:
            errors.append(f"normalized source {src.get('source_id')} has no normalized item")
        if disp in {"IRRELEVANT_WITH_REASON","UNRESOLVED"} and not src.get("reason"):
            errors.append(f"source {src.get('source_id')} disposition {disp} requires reason")

    for item in items:
        for src in item.get("source_refs") or []:
            if src not in set(raw_ids): errors.append(f"item {item['item_id']} references unknown source {src}")
        for dep in item.get("dependencies") or []:
            if dep not in item_ids: errors.append(f"item {item['item_id']} depends on missing item {dep}")
        if item.get("disposition")=="MERGED" and item.get("merged_into") not in item_ids:
            errors.append(f"item {item['item_id']} merged_into missing item {item.get('merged_into')}")

    deps={i["item_id"]:list(i.get("dependencies") or []) for i in items}
    if detect_cycle(item_ids,deps): errors.append("dependency cycle detected")

    expected_edges={(d,i["item_id"]) for i in items for d in i.get("dependencies") or []}
    graph_edges={(e.get("dependency"),e.get("dependent")) for e in graph.get("edges") or []}
    if expected_edges!=graph_edges:
        errors.append(f"dependency graph mismatch expected={sorted(expected_edges)} actual={sorted(graph_edges)}")

    if plan.get("status")!="PLAN_LOCKED": errors.append("portfolio plan is not PLAN_LOCKED")
    locked=set(plan.get("locked_item_ids") or [])
    if locked!=item_ids:
        errors.append(f"Plan Lock coverage mismatch missing={sorted(item_ids-locked)} extra={sorted(locked-item_ids)}")

    wave_map={}; seen=set()
    for w in waves.get("waves") or []:
        if w.get("shared_canon_write") is not False:
            errors.append(f"wave {w.get('wave_id')} permits shared canon write")
        if w.get("publisher_serialized") is not True:
            errors.append(f"wave {w.get('wave_id')} lacks serialized publisher")
        seq=w.get("sequence")
        for item_id in w.get("item_ids") or []:
            if item_id not in item_ids: errors.append(f"wave {w.get('wave_id')} has unknown item {item_id}")
            if item_id in seen: errors.append(f"item {item_id} scheduled more than once")
            seen.add(item_id); wave_map[item_id]=seq

    buildable={i["item_id"] for i in items if i.get("disposition") in BUILDABLE}
    unscheduled=buildable-set(wave_map)
    if unscheduled: errors.append(f"buildable items missing from waves: {sorted(unscheduled)}")
    for item_id in buildable:
        if item_id not in wave_map:
            continue
        for dep in deps.get(item_id,[]):
            if dep in wave_map and wave_map[dep]>=wave_map[item_id]:
                errors.append(f"wave order invalid: {item_id} depends on {dep} at same/later sequence")

    exceptions_dir=portfolio/"exceptions"
    if exceptions_dir.exists():
        ex_schema=load_json(root/"foundry/contracts/architecture-exception.schema.json")
        for p in exceptions_dir.glob("*.yaml"):
            validate_schema(load_yaml(p),ex_schema,f"architecture exception {p.name}",errors)

    metrics={
      "raw_sources":len(raw_ids),
      "ledger_sources":len(ledger_ids),
      "source_coverage": 1.0 if raw_ids and not missing and not extra else (1.0 if not raw_ids and not ledger_ids else 0.0),
      "items":len(items),
      "buildable_items":len(buildable),
      "waves":len(waves.get("waves") or []),
    }
    return errors,warnings,metrics

def main():
    ap=argparse.ArgumentParser()
    ap.add_argument("--root",default=str(Path(__file__).resolve().parents[1]))
    ap.add_argument("--portfolio",required=True)
    args=ap.parse_args()
    root=Path(args.root).resolve(); portfolio=(root/args.portfolio).resolve() if not Path(args.portfolio).is_absolute() else Path(args.portfolio)
    errors,warnings,metrics=validate(root,portfolio)
    for w in warnings: print("WARN:",w)
    if errors:
        for e in errors: print("FAIL:",e)
        print(f"Factory validation FAILED with {len(errors)} error(s).")
        return 1
    print("Factory validation PASS.")
    print("Metrics:",metrics)
    return 0

if __name__=="__main__":
    raise SystemExit(main())
