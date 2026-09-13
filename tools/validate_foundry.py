#!/usr/bin/env python3
import argparse, json, re, sys
from pathlib import Path

try:
    import yaml
    import jsonschema
except ImportError as e:
    print(f"FAIL: missing required dev dependency: {e.name}. Install requirements-dev.txt")
    sys.exit(1)

REQUIRED_CORE = [
    "FOUNDRY_CANON.md", "FOUNDRY_OPERATING_MODEL.md", "AGENTS.md",
    "COLLABORATION_PROTOCOL.md", "foundry/workflows/SF-WF-001_SKILL_GENESIS.md",
    "foundry/registry/SKILL_REGISTRY.yaml", "foundry/taxonomy/TAXONOMY.yaml",
    "foundry/ontology/ONTOLOGY.yaml", "foundry/state/CHECKPOINT.md",
    "foundry/contracts/candidate.schema.json", "foundry/contracts/skill-spec.schema.json",
    "catalog/_template/SKILL.md", "catalog/_template/manifest.json"
]
ALLOWED_DECISIONS = {"REUSE","EXTEND","MODE","DEPENDENT_SKILL","NEW_SKILL","NO_SKILL"}
ALLOWED_STATES = {"INTAKE","WORKFLOW_MAPPED","CAPABILITIES_MINED","OVERLAP_ANALYZED","RESEARCHING","RESEARCH_SKIPPED","PROPOSED","AWAITING_HUMAN_DECISION","APPROVED_FOR_BUILD","BUILDING","BUILD_COMPLETE","AUDITING","REWORK","PASS","READY_FOR_MERGE","PUBLISHED","CLOSED_REUSE","CLOSED_NO_SKILL","REJECTED","BLOCKED"}
SPEC_SECTIONS = ["## Identity","## Trigger","## Non-trigger","## Inputs","## Context policy","## Procedure","## Autonomy","## Outputs","## Quality gates","## Failure modes","## Stop conditions","## Dependencies","## handoffs_from","## handoffs_to","## Token/context strategy","## Portability","## Compatibility / migration impact","## Evals","## Explicit out-of-scope"]


def load_yaml(p):
    with p.open(encoding="utf-8") as f: return yaml.safe_load(f)

def load_json(p):
    with p.open(encoding="utf-8") as f: return json.load(f)

def frontmatter(text):
    if not text.startswith("---\n"):
        return None
    end=text.find("\n---\n",4)
    if end<0: return None
    return yaml.safe_load(text[4:end]) or {}

def validate(root: Path):
    errors=[]; warnings=[]
    for rel in REQUIRED_CORE:
        if not (root/rel).exists(): errors.append(f"missing required file: {rel}")

    # Parse all Foundry JSON/YAML.
    for p in (root/"foundry").rglob("*") if (root/"foundry").exists() else []:
        if not p.is_file(): continue
        try:
            if p.suffix==".json": load_json(p)
            elif p.suffix in {".yaml",".yml"}: load_yaml(p)
        except Exception as e: errors.append(f"parse error {p.relative_to(root)}: {e}")

    # Registry integrity.
    regp=root/"foundry/registry/SKILL_REGISTRY.yaml"
    if regp.exists():
        try:
            reg=load_yaml(regp) or {}; skills=reg.get("skills",[]) or []
            ids=[s.get("id") for s in skills]
            dup=sorted({x for x in ids if x and ids.count(x)>1})
            if dup: errors.append(f"duplicate registry ids: {', '.join(dup)}")
            rs=root/"foundry/contracts/registry-entry.schema.json"
            if rs.exists():
                schema=load_json(rs)
                for i,s in enumerate(skills):
                    try: jsonschema.validate(s,schema)
                    except Exception as e: errors.append(f"registry entry {i} invalid: {e.message}")
        except Exception as e: errors.append(f"registry validation failed: {e}")

    # Candidate queue legality.
    qp=root/"foundry/queue/CANDIDATES.yaml"
    if qp.exists():
        q=load_yaml(qp) or {}
        schema=load_json(root/"foundry/contracts/candidate.schema.json")
        for i,c in enumerate(q.get("candidates",[]) or []):
            try: jsonschema.validate(c,schema)
            except Exception as e: errors.append(f"candidate {i} invalid: {e.message}")
            if c.get("status") not in ALLOWED_STATES: errors.append(f"candidate {i} illegal state: {c.get('status')}")
            for d in c.get("decisions",[]) or []:
                if d.get("treatment") not in ALLOWED_DECISIONS: errors.append(f"candidate {i} illegal treatment: {d.get('treatment')}")

    # Approved spec frontmatter + sections.
    specs=root/"foundry/specs"
    if specs.exists():
        schema=load_json(root/"foundry/contracts/skill-spec.schema.json")
        for p in specs.glob("*.md"):
            text=p.read_text(encoding="utf-8"); fm=frontmatter(text)
            if not fm or fm.get("status")!="APPROVED_FOR_BUILD": continue
            try: jsonschema.validate(fm,schema)
            except Exception as e: errors.append(f"approved spec {p.name} frontmatter invalid: {e.message}")
            for sec in SPEC_SECTIONS:
                if sec not in text: errors.append(f"approved spec {p.name} missing section: {sec}")

    # Published catalog package minimum structural checks.
    cdir=root/"catalog/skills"
    if cdir.exists():
        for d in [x for x in cdir.iterdir() if x.is_dir()]:
            for rel in ["SKILL.md","manifest.json","evals"]:
                if not (d/rel).exists(): errors.append(f"catalog skill {d.name} missing {rel}")
            if (d/"manifest.json").exists():
                try:
                    m=load_json(d/"manifest.json")
                    if m.get("id")!=d.name: warnings.append(f"catalog folder/id differ: {d.name} vs {m.get('id')}")
                except Exception as e: errors.append(f"catalog skill {d.name} manifest invalid: {e}")
            cases=list((d/"evals/cases").glob("*.md")) if (d/"evals/cases").exists() else []
            if len(cases)<4: errors.append(f"catalog skill {d.name} requires >=4 eval cases, found {len(cases)}")

    # Template is a template, not a published skill.
    tp=root/"catalog/_template"
    if tp.exists():
        for rel in ["SKILL.md","manifest.json","evals/README.md","evals/cases/CASE.template.md","adapters/README.md"]:
            if not (tp/rel).exists(): errors.append(f"template missing {rel}")

    return errors,warnings

def main():
    ap=argparse.ArgumentParser(); ap.add_argument("--root",default=str(Path(__file__).resolve().parents[1])); args=ap.parse_args()
    root=Path(args.root).resolve(); errors,warnings=validate(root)
    for w in warnings: print("WARN:",w)
    if errors:
        for e in errors: print("FAIL:",e)
        print(f"Foundry validation FAILED with {len(errors)} error(s).")
        return 1
    print("Skill Foundry validation PASS.")
    return 0
if __name__=="__main__": raise SystemExit(main())
