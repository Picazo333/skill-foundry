#!/usr/bin/env python3
"""Derive a Foundry gate CompletionCertificate from structured claim evidence.

This tool never upgrades missing evidence to PASS and never lets an aggregate
score override a mandatory claim.
"""
from __future__ import annotations
import argparse, json
from pathlib import Path
import yaml

VERDICTS={"PASS","FAIL","UNASSESSED","BLOCKED"}

def derive(root: Path, gate: str, evidence_path: Path):
    claims_doc=yaml.safe_load((root/"foundry/evals/vnext/GATE_CLAIMS.yaml").read_text(encoding="utf-8"))
    required=list(claims_doc["gates"][gate]["mandatory_claims"])
    evidence=yaml.safe_load(evidence_path.read_text(encoding="utf-8")) or {}
    supplied=evidence.get("claims") or {}
    claims={}
    for claim in required:
        value=supplied.get(claim,"UNASSESSED")
        if value not in VERDICTS:
            raise ValueError(f"invalid verdict for {claim}: {value}")
        claims[claim]=value
    critical=int(evidence.get("open_critical_defects",0))
    if critical>0 or any(v=="FAIL" for v in claims.values()):
        verdict="FAIL"
    elif any(v=="BLOCKED" for v in claims.values()):
        verdict="BLOCKED"
    elif any(v=="UNASSESSED" for v in claims.values()):
        verdict="UNASSESSED"
    else:
        verdict="PASS"
    return {
      "certificate_version":1,
      "gate":gate,
      "candidate_id":evidence.get("candidate_id"),
      "skill_id":evidence.get("skill_id"),
      "claims":claims,
      "open_critical_defects":critical,
      "verdict":verdict,
      "evidence_refs":list(evidence.get("evidence_refs") or []),
      "generated_by":"tools/issue_completion_certificate.py",
      "notes":list(evidence.get("notes") or []),
    }

def main():
    ap=argparse.ArgumentParser()
    ap.add_argument("--root",default=str(Path(__file__).resolve().parents[1]))
    ap.add_argument("--gate",required=True,choices=[f"G{i}" for i in range(8)])
    ap.add_argument("--evidence",required=True)
    ap.add_argument("--output")
    args=ap.parse_args()
    root=Path(args.root).resolve()
    cert=derive(root,args.gate,Path(args.evidence).resolve())
    out=json.dumps(cert,indent=2)+"\n"
    if args.output:
        Path(args.output).write_text(out,encoding="utf-8")
    else:
        print(out,end="")
    return 0 if cert["verdict"]=="PASS" else 1

if __name__=="__main__":
    raise SystemExit(main())
