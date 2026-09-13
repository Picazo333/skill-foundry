import copy, importlib.util, json, shutil, tempfile, unittest
from pathlib import Path
import yaml

ROOT=Path(__file__).resolve().parents[1]
spec=importlib.util.spec_from_file_location("vf", ROOT/"tools/validate_foundry.py")
vf=importlib.util.module_from_spec(spec); spec.loader.exec_module(vf)

class FoundryValidatorTests(unittest.TestCase):
    def clone(self):
        td=Path(tempfile.mkdtemp()); dst=td/"repo"; shutil.copytree(ROOT,dst,ignore=shutil.ignore_patterns('.git','__pycache__'))
        self.addCleanup(lambda: shutil.rmtree(td,ignore_errors=True)); return dst
    def test_valid_repo_passes(self):
        r=self.clone(); e,_=vf.validate(r); self.assertEqual([],e)
    def test_invalid_candidate_fails(self):
        r=self.clone(); p=r/"foundry/queue/CANDIDATES.yaml"
        q=yaml.safe_load(p.read_text()); q["candidates"]=[{"id":"x","title":"x","status":"BOGUS","decisions":[{"capability":"x","treatment":"WRONG"}]}]
        p.write_text(yaml.safe_dump(q,sort_keys=False)); e,_=vf.validate(r); self.assertTrue(any("candidate" in x for x in e))
    def test_malformed_approved_spec_fails(self):
        r=self.clone(); p=r/"foundry/specs/bad.md"; p.write_text("---\nstatus: APPROVED_FOR_BUILD\ncandidate_id: c\nskill_id: bad\nchange_kind: NEW_SKILL\n---\n# Bad\n")
        e,_=vf.validate(r); self.assertTrue(any("approved spec bad.md missing section" in x for x in e))
    def test_malformed_skill_package_fails(self):
        r=self.clone(); d=r/"catalog/skills/bad-skill"; d.mkdir(parents=True); (d/"SKILL.md").write_text("# bad")
        e,_=vf.validate(r); self.assertTrue(any("catalog skill bad-skill" in x for x in e))

if __name__=="__main__": unittest.main()
