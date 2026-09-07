"""apf pack: manifest.json + provenance.json + listings."""
from __future__ import annotations
import json, os

def run(workdir, site):
    os.makedirs(os.path.join(workdir, "dist"), exist_ok=True)
    mf = {"pack": os.path.basename(workdir), "site": site, "license": "see LICENSE", "ai": "Made with AI gen + human clean"}
    with open(os.path.join(workdir, "dist", "manifest.json"), "w", encoding="utf-8") as fh:
        json.dump(mf, fh, indent=2)
    print(f"[pack] {workdir} -> dist/manifest.json for {site}")
    return 0
