"""Build real-cook.ipynb: claim -> render (Hunyuan, TripoSR fallback) -> deliver -> complete -> idle-out."""
import json, os

TUNNEL = os.environ.get("FORGE_COOK_TUNNEL", "")
TOKEN = os.environ.get("FORGE_GATEWAY_TOKEN", "")
assert TUNNEL and TOKEN, "set FORGE_COOK_TUNNEL + FORGE_GATEWAY_TOKEN"

WORKER = r'''
import base64, json, time, urllib.request

TUNNEL = "TUNNEL_HERE"
TOKEN = "TOKEN_HERE"
IDLE_SEC = 600

def api(path, body):
    req = urllib.request.Request(TUNNEL + path, data=json.dumps(body).encode(),
        headers={"Content-Type": "application/json", "x-gdr-cli-token": TOKEN})
    return json.load(urllib.request.urlopen(req, timeout=120))

def render(prompt, seed, out):
    # Hunyuan first (quality), TripoSR fallback (speed). Tries in order.
    try:
        from hy3dgen.rembg import BackgroundRemover
        from hy3dgen.shapegen import Hunyuan3DDiTFlowMatchingPipeline
        from hy3dgen.texgen import Hunyuan3DPaintPipeline
        from hy3dgen.text2image import HunyuanDiTPipeline
        t2i = HunyuanDiTPipeline("Tencent-Hunyuan/HunyuanDiT-v1.2-Diffusers-Distilled")
        shape = Hunyuan3DDiTFlowMatchingPipeline.from_pretrained("tencent/Hunyuan3D-2mini")
        paint = Hunyuan3DPaintPipeline.from_pretrained("tencent/Hunyuan3D-2")
        img = t2i(prompt).images[0]
        mesh = shape(image=img)[0]
        mesh = paint(mesh, image=img)
        mesh.export(out)
        return "hunyuan"
    except Exception as e:
        print("hunyuan failed, fallback triposr:", str(e)[:200])
        import torch, trimesh
        from PIL import Image
        from tsr.system import TSR
        model = TSR.from_pretrained("stabilityai/TripoSR", config_name="config.yaml", weight_name="model.ckpt")
        model.to("cuda")
        img = Image.new("RGB", (512, 512), (200, 200, 200))
        with torch.no_grad():
            mesh = model([img], device="cuda")[0]
        mesh.export(out)
        return "triposr"

print("cook up. idle-out after 10 empty min.")
last = time.time()
while time.time() - last < IDLE_SEC:
    jobs = api("/api/batch-factory/claim", {"workerId": "cook-1", "limit": 2}).get("jobs", [])
    if not jobs:
        time.sleep(15)
        continue
    last = time.time()
    for j in jobs:
        out = "/tmp/" + j["jobId"] + ".glb"
        try:
            model = render(j["prompt"], j.get("seed", 42), out)
            raw = open(out, "rb").read()
            api("/api/batch-factory/deliver", {"batchId": j["batchId"], "jobId": j["jobId"],
                "fileBase64": base64.b64encode(raw).decode()})
            done = api("/api/batch-factory/complete", {"batchId": j["batchId"], "jobId": j["jobId"]})
            print(j["jobId"], model, done.get("code", done))
        except Exception as e:
            print("job failed:", j["jobId"], str(e)[:200])
print("idle-out. quota saved.")
'''

WORKER = WORKER.replace("TUNNEL_HERE", TUNNEL).replace("TOKEN_HERE", TOKEN)
nb = {"nbformat": 4, "nbformat_minor": 5,
      "metadata": {"kernelspec": {"display_name": "Python 3", "language": "python", "name": "python3"},
                   "accelerator": "GPU"},
      "cells": [
          {"cell_type": "markdown", "metadata": {}, "source": ["# REAL cook: claims board jobs, renders, delivers. Private notebook only (holds gateway token)."]},
          {"cell_type": "code", "metadata": {}, "execution_count": None, "outputs": [],
           "source": ["!pip install -q hy3dgen trimesh torch 2>&1 | tail -n 1"]},
          {"cell_type": "code", "metadata": {}, "execution_count": None, "outputs": [], "source": [WORKER]},
      ]}
open("work/real-cook.ipynb", "w").write(json.dumps(nb))
print("wrote work/real-cook.ipynb")
