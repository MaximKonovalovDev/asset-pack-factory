"""apf cli: packs3d, verify3d, ship. Slim."""
from __future__ import annotations
import argparse, os, sys
from .state import load_brief
from .verify import run as verify_run
from .pack import run as pack_run

def cmd_packs3d(a):
    b = load_brief(a.brief)
    out = os.path.join("work", b["id"])
    os.makedirs(out, exist_ok=True)
    print(f"[packs3d] {b['id']}: brief ok, {len(b.get('pieces', []))} pieces -> {out}")
    print("[packs3d] next: gen via gateway hunyuan/trellis, then fix/pbr/lod")
    return 0

def main(argv=None):
    ap = argparse.ArgumentParser(prog="apf")
    sub = ap.add_subparsers(dest="cmd", required=True)
    p = sub.add_parser("packs3d"); p.add_argument("brief")
    p = sub.add_parser("verify3d"); p.add_argument("workdir")
    p = sub.add_parser("ship"); p.add_argument("workdir"); p.add_argument("--site", required=True)
    a = ap.parse_args(argv)
    if a.cmd == "packs3d": return cmd_packs3d(a)
    if a.cmd == "verify3d": return verify_run(a.workdir)
    if a.cmd == "ship":
        rc = verify_run(a.workdir)
        if rc != 0: print("[ship] BLOCKED: verify red"); return rc
        return pack_run(a.workdir, a.site)
    return 2

if __name__ == "__main__":
    sys.exit(main())
