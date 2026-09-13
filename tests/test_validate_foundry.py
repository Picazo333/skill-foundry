import json, shutil, tempfile, unittest
from pathlib import Path
import yaml

ROOT=Path(__file__).resolve().parents[1]
import importlib.util
spec=importlib.util.spec_from_file_location("vf", ROOT/"tools/validate_foundry.py")
vf=importlib.util.module_from_spec(spec); spec.loader.exec_module(vf)

SPEC_BODY="\n\n".join(vf.SPEC_SECTIONS)+"\n"
SKILL_BODY="---\nname: ok-skill\ndescription: durable test skill\n---\n# Ok Skill\n\n"+"\n\n".join(vf.SKILL_QUALITY_SECTIONS)+"\n"
EVAL_BODY="\n\n".join(vf.EVAL_REQUIRED_SECTIONS)+"\n"
MANIFEST={
    "id":"ok-skill","name":"Ok Skill","version":"1.0.0","category":"test",
    "purpose":"durable test skill","triggers":["t"],"non_triggers":["n"],"outputs":["OUT.md"]
}

class FoundryValidatorTests(unittest.TestCase):
    def clone(self):
        td=Path(tempfile.mkdtemp()); dst=td/"repo"
        shutil.copytree(ROOT,dst,ignore=shutil.ignore_patterns(".git","__pycache__","baseline"))
        reg=yaml.safe_load((ROOT/"foundry/registry/SKILL_REGISTRY.yaml").read_text(encoding="utf-8")) or {}
        for s in reg.get("skills") or []:
            rel=s.get("canonical_path")
            if rel: (dst/rel).mkdir(parents=True, exist_ok=True)
        self.addCleanup(lambda: shutil.rmtree(td,ignore_errors=True)); return dst

    def errors(self, root):
        try:
            e,w=vf.validate(root)
        except Exception as exc:
            self.fail(f"validator crashed instead of returning targeted errors: {exc}")
        return e

    def add_catalog_skill(self, root, skill_id="ok-skill", skill_md=None, manifest=None, eval_text=None, n_cases=4):
        d=root/"catalog/skills"/skill_id; d.mkdir(parents=True, exist_ok=True)
        (d/"SKILL.md").write_text(skill_md or SKILL_BODY.replace("ok-skill", skill_id), encoding="utf-8")
        m=dict(manifest or MANIFEST); m["id"]=skill_id
        (d/"manifest.json").write_text(json.dumps(m), encoding="utf-8")
        cases=d/"evals/cases"; cases.mkdir(parents=True, exist_ok=True)
        for i in range(n_cases):
            (cases/f"{i+1:02}.md").write_text(eval_text if eval_text is not None else EVAL_BODY, encoding="utf-8")
        return d

    def test_valid_repo_passes(self):
        r=self.clone(); e=self.errors(r); self.assertEqual([],e)

    def test_invalid_candidate_fails(self):
        r=self.clone(); p=r/"foundry/queue/CANDIDATES.yaml"
        q=yaml.safe_load(p.read_text(encoding="utf-8"))
        q["candidates"]=[{"id":"x","title":"x","status":"BOGUS","decisions":[{"capability":"x","treatment":"WRONG"}]}]
        p.write_text(yaml.safe_dump(q,sort_keys=False), encoding="utf-8")
        e=self.errors(r)
        self.assertTrue(any("candidate 0 invalid" in x for x in e), e)
        self.assertTrue(any("illegal state: BOGUS" in x for x in e), e)
        self.assertTrue(any("illegal treatment: WRONG" in x for x in e), e)

    def test_malformed_approved_spec_fails(self):
        r=self.clone(); p=r/"foundry/specs/bad.md"
        p.write_text("---\nstatus: APPROVED_FOR_BUILD\ncandidate_id: c\nskill_id: bad\nchange_kind: NEW_SKILL\n---\n# Bad\n", encoding="utf-8")
        e=self.errors(r)
        missing=[x for x in e if "approved spec bad.md missing section:" in x]
        self.assertTrue(missing, e)
        self.assertTrue(any("missing section: ## Autonomy" in x for x in e), e)
        self.assertFalse(any("skipped" in x and "skill-spec.schema.json" in x for x in e), e)

    def test_malformed_skill_package_fails(self):
        r=self.clone(); d=r/"catalog/skills/bad-skill"; d.mkdir(parents=True); (d/"SKILL.md").write_text("# bad", encoding="utf-8")
        e=self.errors(r)
        self.assertTrue(any("catalog skill bad-skill missing manifest.json" in x for x in e), e)
        self.assertTrue(any("catalog skill bad-skill missing evals" in x for x in e), e)
        self.assertTrue(any("catalog skill bad-skill missing section: ## Autonomy" in x for x in e), e)

    def test_extend_spec_requires_target_skill_id(self):
        r=self.clone(); p=r/"foundry/specs/ext.md"
        p.write_text("---\nstatus: APPROVED_FOR_BUILD\ncandidate_id: c\nskill_id: ext\nchange_kind: EXTEND\n---\n"+SPEC_BODY, encoding="utf-8")
        e=self.errors(r)
        self.assertTrue(any("approved spec ext.md frontmatter invalid" in x for x in e), e)

    def test_catalog_eval_cases_require_sections(self):
        r=self.clone(); self.add_catalog_skill(r, eval_text="# empty\n")
        e=self.errors(r)
        self.assertTrue(any("catalog skill ok-skill evals/cases/" in x and "missing section(s):" in x for x in e), e)

    def test_template_missing_autonomy_fails(self):
        r=self.clone(); p=r/"catalog/_template/SKILL.md"
        p.write_text(p.read_text(encoding="utf-8").replace("## Autonomy\n","## NotAutonomy\n"), encoding="utf-8")
        e=self.errors(r)
        self.assertTrue(any("template missing section: ## Autonomy" in x for x in e), e)

    def test_missing_registry_schema_is_reported_not_skipped_silently(self):
        r=self.clone(); (r/"foundry/contracts/registry-entry.schema.json").unlink()
        e=self.errors(r)
        self.assertTrue(any("registry-entry.schema.json" in x for x in e), e)
        self.assertTrue(any("skipped" in x for x in e), e)

    def test_missing_candidate_schema_does_not_crash(self):
        r=self.clone(); (r/"foundry/contracts/candidate.schema.json").unlink()
        e=self.errors(r)
        self.assertTrue(any("candidate.schema.json" in x for x in e), e)

    def test_missing_canonical_path_fails(self):
        r=self.clone(); p=r/"foundry/registry/SKILL_REGISTRY.yaml"
        reg=yaml.safe_load(p.read_text(encoding="utf-8"))
        reg["skills"][0]["canonical_path"]="baseline/missing-skill"
        p.write_text(yaml.safe_dump(reg,sort_keys=False), encoding="utf-8")
        e=self.errors(r)
        self.assertTrue(any("canonical_path missing: baseline/missing-skill" in x for x in e), e)

if __name__=="__main__": unittest.main()
