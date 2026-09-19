import copy, shutil, tempfile, unittest
from pathlib import Path
import importlib.util, yaml

ROOT=Path(__file__).resolve().parents[1]
spec=importlib.util.spec_from_file_location("factory", ROOT/"tools/validate_factory.py")
factory=importlib.util.module_from_spec(spec); spec.loader.exec_module(factory)

FIXTURE=ROOT/"foundry/factory/portfolios/g5-smoke"

class FactoryValidatorTests(unittest.TestCase):
    def clone_fixture(self):
        td=Path(tempfile.mkdtemp())
        dst=td/"g5-smoke"
        shutil.copytree(FIXTURE,dst)
        self.addCleanup(lambda: shutil.rmtree(td,ignore_errors=True))
        return dst

    def validate(self,p):
        return factory.validate(ROOT,p)[0]

    def test_valid_smoke_passes(self):
        self.assertEqual([],self.validate(FIXTURE))

    def test_missing_source_ledger_entry_fails(self):
        p=self.clone_fixture(); f=p/"01_SOURCE_LEDGER.yaml"
        d=yaml.safe_load(f.read_text(encoding="utf-8")); d["source_fragments"]=d["source_fragments"][:-1]
        f.write_text(yaml.safe_dump(d,sort_keys=False),encoding="utf-8")
        e=self.validate(p); self.assertTrue(any("source coverage missing" in x for x in e),e)

    def test_duplicate_item_id_fails(self):
        p=self.clone_fixture(); f=p/"02_ITEMS.yaml"
        d=yaml.safe_load(f.read_text(encoding="utf-8")); d["items"][1]["item_id"]=d["items"][0]["item_id"]
        f.write_text(yaml.safe_dump(d,sort_keys=False),encoding="utf-8")
        e=self.validate(p); self.assertTrue(any("duplicate item_id" in x for x in e),e)

    def test_dependency_cycle_fails(self):
        p=self.clone_fixture(); f=p/"02_ITEMS.yaml"
        d=yaml.safe_load(f.read_text(encoding="utf-8"))
        next(x for x in d["items"] if x["item_id"]=="i1")["dependencies"]=["i8"]
        f.write_text(yaml.safe_dump(d,sort_keys=False),encoding="utf-8")
        g=p/"06_DEPENDENCY_GRAPH.yaml"; gd=yaml.safe_load(g.read_text(encoding="utf-8")); gd["edges"].append({"dependency":"i8","dependent":"i1"})
        g.write_text(yaml.safe_dump(gd,sort_keys=False),encoding="utf-8")
        e=self.validate(p); self.assertTrue(any("dependency cycle detected" in x for x in e),e)

    def test_buildable_unscheduled_fails(self):
        p=self.clone_fixture(); f=p/"09_WAVES.yaml"
        d=yaml.safe_load(f.read_text(encoding="utf-8")); d["waves"]=d["waves"][:1]
        f.write_text(yaml.safe_dump(d,sort_keys=False),encoding="utf-8")
        e=self.validate(p); self.assertTrue(any("buildable items missing from waves" in x for x in e),e)

    def test_same_wave_dependency_fails(self):
        p=self.clone_fixture(); f=p/"09_WAVES.yaml"
        d=yaml.safe_load(f.read_text(encoding="utf-8"))
        d["waves"]=[{"wave_id":"w1","sequence":1,"item_ids":["i6","i8"],"max_parallel_builders":2,"shared_canon_write":False,"publisher_serialized":True}]
        f.write_text(yaml.safe_dump(d,sort_keys=False),encoding="utf-8")
        e=self.validate(p); self.assertTrue(any("wave order invalid" in x for x in e),e)

    def test_plan_lock_coverage_mismatch_fails(self):
        p=self.clone_fixture(); f=p/"08_PLAN.yaml"
        d=yaml.safe_load(f.read_text(encoding="utf-8")); d["locked_item_ids"]=d["locked_item_ids"][:-1]
        f.write_text(yaml.safe_dump(d,sort_keys=False),encoding="utf-8")
        e=self.validate(p); self.assertTrue(any("Plan Lock coverage mismatch" in x for x in e),e)

    def test_disposition_lifecycle_mismatch_fails(self):
        p=self.clone_fixture(); f=p/"02_ITEMS.yaml"
        d=yaml.safe_load(f.read_text(encoding="utf-8"))
        next(x for x in d["items"] if x["item_id"]=="i1")["lifecycle"]="PUBLISHED"
        f.write_text(yaml.safe_dump(d,sort_keys=False),encoding="utf-8")
        e=self.validate(p); self.assertTrue(any("inconsistent with disposition REUSE" in x for x in e),e)

    def test_non_buildable_item_in_wave_fails(self):
        p=self.clone_fixture(); f=p/"09_WAVES.yaml"
        d=yaml.safe_load(f.read_text(encoding="utf-8")); d["waves"][0]["item_ids"].append("i1")
        f.write_text(yaml.safe_dump(d,sort_keys=False),encoding="utf-8")
        e=self.validate(p); self.assertTrue(any("schedules non-buildable item i1" in x for x in e),e)

    def test_blocked_exception_item_cannot_be_scheduled(self):
        p=self.clone_fixture(); f=p/"09_WAVES.yaml"
        d=yaml.safe_load(f.read_text(encoding="utf-8")); d["waves"][0]["item_ids"].append("i4")
        f.write_text(yaml.safe_dump(d,sort_keys=False),encoding="utf-8")
        e=self.validate(p); self.assertTrue(any("blocked architecture-exception item scheduled: i4" in x for x in e),e)

    def test_parallelism_above_policy_fails(self):
        p=self.clone_fixture(); f=p/"09_WAVES.yaml"
        d=yaml.safe_load(f.read_text(encoding="utf-8")); d["waves"][0]["max_parallel_builders"]=3
        f.write_text(yaml.safe_dump(d,sort_keys=False),encoding="utf-8")
        e=self.validate(p); self.assertTrue(any("exceeds Factory parallel builder limit" in x for x in e),e)

    def test_shared_canon_write_fails_schema(self):
        p=self.clone_fixture(); f=p/"09_WAVES.yaml"
        d=yaml.safe_load(f.read_text(encoding="utf-8")); d["waves"][0]["shared_canon_write"]=True
        f.write_text(yaml.safe_dump(d,sort_keys=False),encoding="utf-8")
        e=self.validate(p)
        self.assertTrue(any("wave plan schema invalid" in x or "permits shared canon write" in x for x in e),e)

if __name__=="__main__":
    unittest.main()
