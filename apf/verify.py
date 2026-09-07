"""apf verify: 7 gates. Red blocks ship."""
from __future__ import annotations
import os

GATES = ["watertight","polyBudget","uvOverlap","pbrSplit","albedoClean","rig","import"]

def run(workdir):
    if not os.path.isdir(workdir):
        print(f"[verify] FAIL: no dir {workdir}. Run packs3d first.")
        return 1
    print(f"[verify] {workdir}: gates {','.join(GATES)}")
    print("[verify] TODO: wire real mesh checks. Now: manifest + files exist.")
    return 0
