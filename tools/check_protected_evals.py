#!/usr/bin/env python3
"""Verify protected VNext eval fixtures against recorded Git-blob SHA-1 values."""
from __future__ import annotations
import argparse, hashlib
from pathlib import Path
import yaml

def git_blob_sha1(data: bytes) -> str:
    return hashlib.sha1(b"blob "+str(len(data)).encode("ascii")+b"\0"+data).hexdigest()

def verify(root: Path, manifest: Path):
    doc=yaml.safe_load(manifest.read_text(encoding="utf-8")) or {}
    errors=[]
    for item in doc.get("files") or []:
        p=root/item["path"]
        if not p.exists():
            errors.append(f"missing protected eval: {item['path']}")
            continue
        actual=git_blob_sha1(p.read_bytes())
        expected=item["git_blob_sha1"]
        if actual!=expected:
            errors.append(f"protected eval changed: {item['path']} expected={expected} actual={actual}")
    return errors

def main():
    ap=argparse.ArgumentParser()
    ap.add_argument("--root",default=str(Path(__file__).resolve().parents[1]))
    ap.add_argument("--manifest",default="foundry/evals/vnext/holdouts/skill-foundry/PROTECTED_MANIFEST.yaml")
    args=ap.parse_args()
    root=Path(args.root).resolve()
    errors=verify(root,root/args.manifest)
    if errors:
        for e in errors: print("FAIL:",e)
        return 1
    print("Protected VNext eval integrity PASS.")
    return 0

if __name__=="__main__":
    raise SystemExit(main())
