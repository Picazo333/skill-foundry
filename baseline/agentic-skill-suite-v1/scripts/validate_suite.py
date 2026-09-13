#!/usr/bin/env python3
"""
Structural + integrity validator for the agentic skill suite.

Since these are prompt-defined skills (no runtime to execute them against),
"tests" take the practical form of: does every skill folder match
ARCHITECTURE.md's required contract, does every manifest.json validate
against shared/contracts/skill-manifest.schema.json, is every schemas/*.json
file a syntactically and semantically valid JSON Schema, do internal
cross-references actually resolve, does routing-graph.json actually match
what the manifests declare, is CHECKPOINT.md valid against its own contract,
does every SKILL.md carry the frontmatter its adapters/claude.md promises,
and does every declared output artifact have a template.

This validator has two hard dependencies -- `jsonschema` and `pyyaml`. If
either is missing, the script FAILS (exit 1) rather than silently skipping
the checks that depend on it. A validator that prints "all skills pass"
while a required check never ran is worse than no validator at all -- that
gap is exactly how the suite's own FINAL_REPORT.md came to assert an
unverified claim (see AUDIT_REPORT.md, finding P1-6).

Run from repo root:
    python3 scripts/validate_suite.py
"""
import json
import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
SKILLS_DIR = ROOT / "skills"

REQUIRED_TOP_FILES = ["SKILL.md", "README.md", "manifest.json"]
REQUIRED_SCHEMA_FILES = ["input.schema.json", "output.schema.json"]
REQUIRED_DIRS = ["schemas", "templates", "references", "examples", "evals", "adapters"]
REQUIRED_ADAPTERS = ["generic", "chatgpt", "codex", "claude", "gemini", "cursor"]
MANIFEST_REQUIRED_FIELDS = [
    "id", "name", "version", "category", "purpose",
    "triggers", "non_triggers", "outputs",
]
EVAL_REQUIRED_SECTIONS = [
    "## Scenario", "## Input", "## Expected behavior",
    "## Expected artifacts", "## Forbidden behavior", "## Pass criteria",
]
# Output-artifact directories a skill may declare in manifest.json `outputs`
# without a same-named file existing in templates/ -- these are directory
# outputs with a template file under a different, documented name.
OUTPUT_DIR_TEMPLATE_OVERRIDES = {
    "PROMPTS/": "PROMPT_TEMPLATE.md",
    "HANDOFF_PACKAGES/": "HANDOFF_PACKAGE_README.md",
}

# --- hard dependency check -------------------------------------------------

def require_dependencies():
    missing = []
    try:
        import jsonschema  # noqa: F401
    except ImportError:
        missing.append("jsonschema")
    try:
        import yaml  # noqa: F401
    except ImportError:
        missing.append("pyyaml")
    if missing:
        print(f"FAIL: required package(s) not installed: {', '.join(missing)}")
        print("      the manifest-schema, checkpoint-schema and frontmatter")
        print("      checks below cannot run without them. Install with:")
        print(f"      pip install {' '.join(missing)}")
        sys.exit(1)


def load_json(path):
    with open(path) as f:
        return json.load(f)


# --- per-skill structural checks (original) --------------------------------

def validate_manifest_shape(manifest, errors, skill_dir):
    for field in MANIFEST_REQUIRED_FIELDS:
        if field not in manifest:
            errors.append(f"{skill_dir.name}: manifest.json missing required field '{field}'")


def validate_skill_structure(skill_dir):
    errors = []
    warnings = []

    for f in REQUIRED_TOP_FILES:
        if not (skill_dir / f).exists():
            errors.append(f"{skill_dir.name}: missing {f}")

    for d in REQUIRED_DIRS:
        if not (skill_dir / d).is_dir():
            errors.append(f"{skill_dir.name}: missing directory {d}/")

    for sf in REQUIRED_SCHEMA_FILES:
        p = skill_dir / "schemas" / sf
        if not p.exists():
            errors.append(f"{skill_dir.name}: missing schemas/{sf}")
        else:
            try:
                load_json(p)
            except Exception as e:
                errors.append(f"{skill_dir.name}: schemas/{sf} invalid JSON: {e}")

    manifest_path = skill_dir / "manifest.json"
    if manifest_path.exists():
        try:
            manifest = load_json(manifest_path)
            validate_manifest_shape(manifest, errors, skill_dir)
        except Exception as e:
            errors.append(f"{skill_dir.name}: manifest.json invalid JSON: {e}")

    for a in REQUIRED_ADAPTERS:
        p = skill_dir / "adapters" / f"{a}.md"
        if not p.exists():
            errors.append(f"{skill_dir.name}: missing adapters/{a}.md")
        elif "TO BE GENERATED" in p.read_text():
            errors.append(f"{skill_dir.name}: adapters/{a}.md still a placeholder")

    if (skill_dir / "manifest.blueprint.json").exists():
        errors.append(f"{skill_dir.name}: stale manifest.blueprint.json still present")

    for jf in (skill_dir / "templates").glob("*.json") if (skill_dir / "templates").is_dir() else []:
        try:
            load_json(jf)
        except Exception as e:
            errors.append(f"{skill_dir.name}: templates/{jf.name} invalid JSON: {e}")

    return errors, warnings


# --- eval case structure ----------------------------------------------------

def validate_eval_cases(skill_dir):
    errors = []
    cases_dir = skill_dir / "evals" / "cases"
    eval_cases = list(cases_dir.glob("*.md")) if cases_dir.is_dir() else []
    if len(eval_cases) < 4:
        errors.append(f"{skill_dir.name}: only {len(eval_cases)} eval cases (need >=3 core + 1 edge = 4)")
    for c in eval_cases:
        txt = c.read_text()
        missing = [s for s in EVAL_REQUIRED_SECTIONS if s not in txt]
        if missing:
            errors.append(f"{skill_dir.name}: evals/cases/{c.name} missing section(s): {missing}")
    return errors


# --- meta-schema validation --------------------------------------------------

def validate_meta_schemas(skill_dirs):
    from jsonschema import Draft202012Validator

    errors = []
    schema_files = []
    for sd in skill_dirs:
        schema_files.extend(sorted((sd / "schemas").glob("*.json")) if (sd / "schemas").is_dir() else [])
    schema_files.extend(sorted((ROOT / "shared" / "contracts").glob("*.json")))

    for f in schema_files:
        try:
            s = load_json(f)
        except Exception as e:
            errors.append(f"{f.relative_to(ROOT)}: invalid JSON: {e}")
            continue
        if "$schema" not in s:
            errors.append(f"{f.relative_to(ROOT)}: missing '$schema' key")
        try:
            Draft202012Validator.check_schema(s)
        except Exception as e:
            errors.append(f"{f.relative_to(ROOT)}: not a valid JSON Schema: {str(e)[:200]}")
    return errors


# --- manifest.json vs skill-manifest.schema.json ----------------------------

def validate_manifests_against_schema(skill_dirs):
    from jsonschema import Draft202012Validator

    errors = []
    manifest_schema = load_json(ROOT / "shared" / "contracts" / "skill-manifest.schema.json")
    for sd in skill_dirs:
        mp = sd / "manifest.json"
        if not mp.exists():
            continue
        try:
            Draft202012Validator(manifest_schema).validate(load_json(mp))
        except Exception as e:
            errors.append(f"{sd.name}: manifest.json fails schema validation: {e}")
    return errors


# --- internal cross-reference resolution ------------------------------------

REF_PATTERN = re.compile(r"`([A-Za-z0-9_.\-]*/[A-Za-z0-9_./\-]+\.(?:md|json))`")


def validate_internal_references(skill_dirs):
    errors = []
    for sd in skill_dirs:
        for md in sd.rglob("*.md"):
            txt = md.read_text()
            for m in sorted(set(REF_PATTERN.findall(txt))):
                if m.startswith("<output>"):
                    continue  # declared output artifact, not a repo path
                candidates = [md.parent / m, sd / m, ROOT / m.lstrip("/")]
                if not any(c.exists() for c in candidates):
                    errors.append(
                        f"{md.relative_to(ROOT)}: broken reference to `{m}` "
                        f"(checked relative to file, skill root, and repo root)"
                    )
    return errors


# --- routing-graph.json vs manifests ----------------------------------------

def validate_routing_graph(skill_dirs):
    errors = []
    manifest_edges = set()
    for sd in skill_dirs:
        m = load_json(sd / "manifest.json")
        for h in m.get("handoffs_to", []):
            manifest_edges.add((m["id"], h))

    rg_path = ROOT / "routing-graph.json"
    if not rg_path.exists():
        return [f"routing-graph.json: missing"]
    rg = load_json(rg_path)
    rg_edges = {(e["from"], e["to"]) for e in rg.get("edges", [])}

    missing = manifest_edges - rg_edges
    extra = rg_edges - manifest_edges
    if missing:
        errors.append(f"routing-graph.json: missing {len(missing)} edge(s) present in manifests: {sorted(missing)[:5]}{'...' if len(missing) > 5 else ''}")
    if extra:
        errors.append(f"routing-graph.json: {len(extra)} edge(s) not backed by any manifest handoffs_to: {sorted(extra)[:5]}{'...' if len(extra) > 5 else ''}")

    # cycle check: fail only if a cycle exists made entirely of "forward" edges
    fwd = {(e["from"], e["to"]) for e in rg.get("edges", []) if e.get("type") == "forward"}
    adj = {}
    for f, t in fwd:
        adj.setdefault(f, []).append(t)

    def dfs(n, stack, seen):
        for x in adj.get(n, []):
            if x in stack:
                cyc = stack[stack.index(x):] + [x]
                errors.append(f"routing-graph.json: all-forward cycle: {' -> '.join(cyc)}")
            elif x not in seen:
                seen.add(x)
                dfs(x, stack + [x], seen)

    for n in list(adj):
        dfs(n, [n], {n})

    for e in rg.get("edges", []):
        if e.get("type") not in {"forward", "feedback", "conditional"}:
            errors.append(f"routing-graph.json: edge {e.get('from')} -> {e.get('to')} has invalid/missing type '{e.get('type')}'")

    return errors


# --- CHECKPOINT.md vs its schema --------------------------------------------

def validate_checkpoint():
    import yaml

    errors = []
    cp_path = ROOT / "CHECKPOINT.md"
    schema_path = ROOT / "shared" / "contracts" / "checkpoint.schema.json"
    if not cp_path.exists() or not schema_path.exists():
        return [f"CHECKPOINT.md or its schema is missing"]

    txt = cp_path.read_text()
    m = re.search(r"```yaml\n(.*?)\n```", txt, re.S)
    if not m:
        return ["CHECKPOINT.md: no ```yaml ... ``` block found"]
    try:
        data = yaml.safe_load(m.group(1))
    except Exception as e:
        return [f"CHECKPOINT.md: yaml block does not parse: {e}"]

    from jsonschema import Draft202012Validator
    schema = load_json(schema_path)
    try:
        Draft202012Validator(schema).validate(data)
    except Exception as e:
        errors.append(f"CHECKPOINT.md: fails checkpoint.schema.json: {e}")

    required10 = [
        "phase", "completed", "partially_completed", "files_created",
        "tests_passed", "tests_failed", "known_issues", "decisions_locked",
        "next_exact_action", "resume_command",
    ]
    missing = [f for f in required10 if f not in data]
    if missing:
        errors.append(f"CHECKPOINT.md: missing START_PROMPT.md Sec.4 field(s): {missing}")

    return errors


# --- SKILL.md frontmatter ----------------------------------------------------

def validate_frontmatter(skill_dirs):
    import yaml

    errors = []
    for sd in skill_dirs:
        skill_md = sd / "SKILL.md"
        manifest = load_json(sd / "manifest.json")
        txt = skill_md.read_text()
        if not txt.startswith("---\n"):
            errors.append(f"{sd.name}: SKILL.md does not start with YAML frontmatter")
            continue
        end = txt.find("\n---\n", 4)
        if end == -1:
            errors.append(f"{sd.name}: SKILL.md frontmatter block is not closed with '---'")
            continue
        try:
            fm = yaml.safe_load(txt[4:end])
        except Exception as e:
            errors.append(f"{sd.name}: SKILL.md frontmatter does not parse as YAML: {e}")
            continue
        if not isinstance(fm, dict) or "name" not in fm or "description" not in fm:
            errors.append(f"{sd.name}: SKILL.md frontmatter missing 'name' and/or 'description'")
            continue
        if fm["name"] != manifest["id"]:
            errors.append(f"{sd.name}: SKILL.md frontmatter name '{fm['name']}' != manifest.id '{manifest['id']}'")
        if len(fm["description"]) > 1024:
            errors.append(f"{sd.name}: SKILL.md frontmatter description exceeds 1024 chars ({len(fm['description'])})")
    return errors


# --- outputs[] vs templates/ coverage ----------------------------------------

def validate_template_coverage(skill_dirs):
    errors = []
    for sd in skill_dirs:
        manifest = load_json(sd / "manifest.json")
        tpl_names = {f.name for f in (sd / "templates").iterdir()} if (sd / "templates").is_dir() else set()
        for out in manifest.get("outputs", []):
            if out.endswith("/"):
                override = OUTPUT_DIR_TEMPLATE_OVERRIDES.get(out)
                if not override or override not in tpl_names:
                    errors.append(f"{sd.name}: directory output '{out}' has no documented template (expected '{override or '<override needed>'}' in templates/)")
                continue
            if out not in tpl_names:
                errors.append(f"{sd.name}: output '{out}' has no matching file in templates/")
    return errors


def main():
    require_dependencies()

    skill_dirs = sorted(p for p in SKILLS_DIR.iterdir() if p.is_dir())
    if len(skill_dirs) != 15:
        print(f"WARNING: expected 15 skill directories, found {len(skill_dirs)}")

    all_errors = []
    all_warnings = []

    for sd in skill_dirs:
        errors, warnings = validate_skill_structure(sd)
        all_errors.extend(errors)
        all_warnings.extend(warnings)
        all_errors.extend(validate_eval_cases(sd))

    all_errors.extend(validate_meta_schemas(skill_dirs))
    all_errors.extend(validate_manifests_against_schema(skill_dirs))
    all_errors.extend(validate_internal_references(skill_dirs))
    all_errors.extend(validate_routing_graph(skill_dirs))
    all_errors.extend(validate_checkpoint())
    all_errors.extend(validate_frontmatter(skill_dirs))
    all_errors.extend(validate_template_coverage(skill_dirs))

    print(f"Checked {len(skill_dirs)} skill directories.")
    if all_warnings:
        print(f"\n{len(all_warnings)} warning(s):")
        for w in all_warnings:
            print(f"  WARN  {w}")
    if all_errors:
        print(f"\n{len(all_errors)} error(s):")
        for e in all_errors:
            print(f"  FAIL  {e}")
        sys.exit(1)
    else:
        print("\nAll skills pass structural validation "
              "(folder contract, manifest+checkpoint schema validation, "
              "meta-schema validation, internal reference resolution, "
              "routing-graph/manifest consistency, forward-cycle check, "
              "SKILL.md frontmatter, output/template coverage, eval structure).")


if __name__ == "__main__":
    main()
