#!/usr/bin/env python3
import argparse, json, sys
from pathlib import Path

try:
    import yaml
    import jsonschema
    from jsonschema import Draft202012Validator
except ImportError as e:
    print(f"FAIL: missing required dev dependency: {e.name}. Install requirements-dev.txt")
    sys.exit(1)

REQUIRED_CORE = [
    "FOUNDRY_CANON.md", "FOUNDRY_OPERATING_MODEL.md", "AGENTS.md",
    "COLLABORATION_PROTOCOL.md", "foundry/workflows/SF-WF-001_SKILL_GENESIS.md",
    "foundry/registry/SKILL_REGISTRY.yaml", "foundry/taxonomy/TAXONOMY.yaml",
    "foundry/ontology/ONTOLOGY.yaml", "foundry/state/CHECKPOINT.md",
    "foundry/contracts/candidate.schema.json", "foundry/contracts/skill-spec.schema.json",
    "foundry/contracts/registry-entry.schema.json", "foundry/contracts/skill-manifest.schema.json",
    "catalog/_template/SKILL.md", "catalog/_template/manifest.json"
]
ALLOWED_DECISIONS = {"REUSE","EXTEND","MODE","DEPENDENT_SKILL","NEW_SKILL","NO_SKILL"}
ALLOWED_STATES = {"INTAKE","WORKFLOW_MAPPED","CAPABILITIES_MINED","OVERLAP_ANALYZED","RESEARCHING","RESEARCH_SKIPPED","PROPOSED","AWAITING_HUMAN_DECISION","APPROVED_FOR_BUILD","BUILDING","BUILD_COMPLETE","AUDITING","REWORK","PASS","READY_FOR_MERGE","PUBLISHED","CLOSED_REUSE","CLOSED_NO_SKILL","REJECTED","BLOCKED"}
SPEC_SECTIONS = ["## Identity","## Trigger","## Non-trigger","## Inputs","## Context policy","## Procedure","## Autonomy","## Outputs","## Quality gates","## Failure modes","## Stop conditions","## Dependencies","## handoffs_from","## handoffs_to","## Token/context strategy","## Portability","## Compatibility / migration impact","## Evals","## Explicit out-of-scope"]
SKILL_QUALITY_SECTIONS = [
    "## Identity","## Trigger","## Non-trigger","## Inputs","## Context policy",
    "## Procedure","## Autonomy","## Outputs","## Quality gates","## Failure modes",
    "## Stop conditions","## Handoffs","## Evals"
]
EVAL_REQUIRED_SECTIONS = [
    "## Scenario","## Input","## Expected behavior",
    "## Expected artifacts","## Forbidden behavior","## Pass criteria"
]
TEMPLATE_REQUIRED = [
    "SKILL.md","manifest.json","evals/README.md","evals/cases/CASE.template.md","adapters/README.md"
]


def load_yaml(p):
    with p.open(encoding="utf-8") as f: return yaml.safe_load(f)

def load_json(p):
    with p.open(encoding="utf-8") as f: return json.load(f)

def normalize_newlines(text):
    return text.replace("\r\n","\n").replace("\r","\n")

def err_msg(exc):
    return getattr(exc, "message", None) or str(exc)

def frontmatter(text):
    text = normalize_newlines(text)
    if not text.startswith("---\n"):
        return None
    end=text.find("\n---\n",4)
    if end<0: return None
    return yaml.safe_load(text[4:end]) or {}

def read_text(p):
    return normalize_newlines(p.read_text(encoding="utf-8"))

def load_optional_json(root, rel, errors):
    p=root/rel
    if not p.exists():
        return None
    try:
        return load_json(p)
    except Exception as e:
        errors.append(f"parse error {rel}: {e}")
        return None

def missing_sections(text, sections):
    text = normalize_newlines(text)
    return [sec for sec in sections if sec not in text]


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

    contracts_dir=root/"foundry/contracts"
    if contracts_dir.exists():
        for p in sorted(contracts_dir.glob("*.json")):
            try:
                Draft202012Validator.check_schema(load_json(p))
            except Exception as e:
                errors.append(f"contract {p.name} is not a valid JSON Schema: {err_msg(e)}")

    # Registry integrity. Do not silently skip schema validation.
    regp=root/"foundry/registry/SKILL_REGISTRY.yaml"
    registry_rel="foundry/contracts/registry-entry.schema.json"
    registry_schema=load_optional_json(root, registry_rel, errors)
    if registry_schema is None and not (root/registry_rel).exists():
        errors.append(f"registry schema validation skipped because {registry_rel} is missing")
    if regp.exists():
        try:
            reg=load_yaml(regp) or {}; skills=reg.get("skills",[]) or []
            ids=[s.get("id") for s in skills]
            dup=sorted({x for x in ids if x and ids.count(x)>1})
            if dup: errors.append(f"duplicate registry ids: {', '.join(dup)}")
            for i,s in enumerate(skills):
                if registry_schema is not None:
                    try: jsonschema.validate(s,registry_schema)
                    except Exception as e: errors.append(f"registry entry {i} invalid: {err_msg(e)}")
                cp=s.get("canonical_path")
                if cp and not (root/cp).exists():
                    errors.append(f"registry entry {s.get('id') or i} canonical_path missing: {cp}")
        except Exception as e: errors.append(f"registry validation failed: {e}")

    # Candidate queue legality.
    qp=root/"foundry/queue/CANDIDATES.yaml"
    if qp.exists():
        try:
            q=load_yaml(qp) or {}
        except Exception as e:
            errors.append(f"parse error foundry/queue/CANDIDATES.yaml: {e}")
            q=None
        candidate_rel="foundry/contracts/candidate.schema.json"
        candidate_schema=load_optional_json(root, candidate_rel, errors)
        if candidate_schema is None and not (root/candidate_rel).exists():
            errors.append(f"candidate schema validation skipped because {candidate_rel} is missing")
        if q is not None:
            for i,c in enumerate(q.get("candidates",[]) or []):
                if candidate_schema is not None:
                    try: jsonschema.validate(c,candidate_schema)
                    except Exception as e: errors.append(f"candidate {i} invalid: {err_msg(e)}")
                if c.get("status") not in ALLOWED_STATES: errors.append(f"candidate {i} illegal state: {c.get('status')}")
                for d in c.get("decisions",[]) or []:
                    if d.get("treatment") not in ALLOWED_DECISIONS: errors.append(f"candidate {i} illegal treatment: {d.get('treatment')}")

    # Approved spec frontmatter + sections.
    specs=root/"foundry/specs"
    spec_rel="foundry/contracts/skill-spec.schema.json"
    spec_schema=load_optional_json(root, spec_rel, errors)
    if specs.exists():
        approved=[p for p in specs.glob("*.md") if p.name.lower()!="readme.md"]
        if approved and spec_schema is None and not (root/spec_rel).exists():
            errors.append(f"approved spec schema validation skipped because {spec_rel} is missing")
        for p in approved:
            text=read_text(p); fm=frontmatter(text)
            if not fm or fm.get("status")!="APPROVED_FOR_BUILD": continue
            if spec_schema is not None:
                try: jsonschema.validate(fm,spec_schema)
                except Exception as e: errors.append(f"approved spec {p.name} frontmatter invalid: {err_msg(e)}")
            for sec in missing_sections(text, SPEC_SECTIONS):
                errors.append(f"approved spec {p.name} missing section: {sec}")

    # Published catalog package minimum structural checks.
    manifest_rel="foundry/contracts/skill-manifest.schema.json"
    manifest_schema=load_optional_json(root, manifest_rel, errors)
    catalog_dir=root/"catalog/skills"
    if catalog_dir.exists():
        for d in [x for x in catalog_dir.iterdir() if x.is_dir()]:
            for rel in ["SKILL.md","manifest.json","evals"]:
                if not (d/rel).exists(): errors.append(f"catalog skill {d.name} missing {rel}")
            if (d/"SKILL.md").exists():
                for sec in missing_sections(read_text(d/"SKILL.md"), SKILL_QUALITY_SECTIONS):
                    errors.append(f"catalog skill {d.name} missing section: {sec}")
            if (d/"manifest.json").exists():
                try:
                    m=load_json(d/"manifest.json")
                    if m.get("id")!=d.name: warnings.append(f"catalog folder/id differ: {d.name} vs {m.get('id')}")
                    if manifest_schema is not None:
                        try: jsonschema.validate(m,manifest_schema)
                        except Exception as e: errors.append(f"catalog skill {d.name} manifest invalid: {err_msg(e)}")
                    elif not (root/manifest_rel).exists():
                        errors.append(f"catalog manifest schema validation skipped because {manifest_rel} is missing")
                except Exception as e: errors.append(f"catalog skill {d.name} manifest invalid: {e}")
            if (d/"evals").exists():
                cases_dir=d/"evals/cases"
                cases=list(cases_dir.glob("*.md")) if cases_dir.exists() else []
                if len(cases)<4: errors.append(f"catalog skill {d.name} requires >=4 eval cases, found {len(cases)}")
                for c in cases:
                    missing=missing_sections(read_text(c), EVAL_REQUIRED_SECTIONS)
                    if missing:
                        errors.append(f"catalog skill {d.name} evals/cases/{c.name} missing section(s): {missing}")

    # Template is a template, not a published skill.
    tp=root/"catalog/_template"
    if tp.exists():
        for rel in TEMPLATE_REQUIRED:
            if not (tp/rel).exists(): errors.append(f"template missing {rel}")
        skill_md=tp/"SKILL.md"
        if skill_md.exists():
            for sec in missing_sections(read_text(skill_md), SKILL_QUALITY_SECTIONS):
                errors.append(f"template missing section: {sec}")
        case_tpl=tp/"evals/cases/CASE.template.md"
        if case_tpl.exists():
            missing=missing_sections(read_text(case_tpl), EVAL_REQUIRED_SECTIONS)
            if missing:
                errors.append(f"template eval case missing section(s): {missing}")

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
