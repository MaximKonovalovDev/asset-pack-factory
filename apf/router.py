"""router: forge 3D lane client. Gateway :20128 only, never direct :78xx."""
from __future__ import annotations
import json, urllib.request

GATEWAY = "http://127.0.0.1:20128"
DEFAULT_MODEL = "hunyuan3d-kaggle"
FALLBACK_MODEL = "blender-colab"

def generate(prompt, model=DEFAULT_MODEL, seed=170129):
    body = json.dumps({"prompt": prompt, "model": model, "kind": "asset", "seed": seed}).encode()
    req = urllib.request.Request(GATEWAY + "/v1/assets/generations", data=body, headers={"Content-Type": "application/json"})
    try:
        with urllib.request.urlopen(req, timeout=120) as r:
            return json.load(r)
    except Exception as ex:
        return {"ok": False, "error": str(ex), "fallback": FALLBACK_MODEL}
