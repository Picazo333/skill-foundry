import json, tempfile, unittest
from pathlib import Path
import importlib.util, yaml

ROOT=Path(__file__).resolve().parents[1]

def load_module(name,path):
    spec=importlib.util.spec_from_file_location(name,path)
    mod=importlib.util.module_from_spec(spec); spec.loader.exec_module(mod); return mod

cert=load_module("cert",ROOT/"tools/issue_completion_certificate.py")
integrity=load_module("integrity",ROOT/"tools/check_protected_evals.py")

class VNextEvidenceTests(unittest.TestCase):
    def test_missing_claim_is_unassessed_not_pass(self):
        with tempfile.TemporaryDirectory() as td:
            p=Path(td)/"e.yaml"
            p.write_text(yaml.safe_dump({"claims":{}}),encoding="utf-8")
            c=cert.derive(ROOT,"G4",p)
            self.assertEqual("UNASSESSED",c["verdict"])
            self.assertTrue(all(v=="UNASSESSED" for v in c["claims"].values()))

    def test_failure_dominates_other_passes(self):
        with tempfile.TemporaryDirectory() as td:
            p=Path(td)/"e.yaml"
            req=yaml.safe_load((ROOT/"foundry/evals/vnext/GATE_CLAIMS.yaml").read_text(encoding="utf-8"))["gates"]["G4"]["mandatory_claims"]
            claims={x:"PASS" for x in req}; claims[req[0]]="FAIL"
            p.write_text(yaml.safe_dump({"claims":claims}),encoding="utf-8")
            c=cert.derive(ROOT,"G4",p)
            self.assertEqual("FAIL",c["verdict"])

    def test_all_mandatory_pass_yields_pass(self):
        with tempfile.TemporaryDirectory() as td:
            p=Path(td)/"e.yaml"
            req=yaml.safe_load((ROOT/"foundry/evals/vnext/GATE_CLAIMS.yaml").read_text(encoding="utf-8"))["gates"]["G4"]["mandatory_claims"]
            p.write_text(yaml.safe_dump({"claims":{x:"PASS" for x in req},"open_critical_defects":0}),encoding="utf-8")
            c=cert.derive(ROOT,"G4",p)
            self.assertEqual("PASS",c["verdict"])

    def test_committed_g4_certificate_matches_derivation(self):
        evidence=ROOT/"foundry/evidence/vnext/G4/G4_EVIDENCE.yaml"
        committed=json.loads((ROOT/"foundry/evidence/vnext/G4/G4_COMPLETION_CERTIFICATE.json").read_text(encoding="utf-8"))
        self.assertEqual(committed,cert.derive(ROOT,"G4",evidence))

    def test_committed_g5_certificate_matches_derivation(self):
        evidence=ROOT/"foundry/evidence/vnext/G5/G5_EVIDENCE.yaml"
        committed=json.loads((ROOT/"foundry/evidence/vnext/G5/G5_COMPLETION_CERTIFICATE.json").read_text(encoding="utf-8"))
        self.assertEqual(committed,cert.derive(ROOT,"G5",evidence))

    def test_git_blob_sha_matches_known_value(self):
        self.assertEqual("a9993e364706816aba3e25717850c26c9cd0d89d",__import__("hashlib").sha1(b"abc").hexdigest())
        # Git blob identity intentionally differs from raw SHA-1.
        self.assertEqual("f2ba8f84ab5c1bce84a7b441cb1959cfc7093b7f",integrity.git_blob_sha1(b"abc"))

if __name__=="__main__":
    unittest.main()
