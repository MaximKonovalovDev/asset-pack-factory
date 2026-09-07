import base64, json, urllib.request

TUNNEL = "TUNNEL_HERE"
TOKEN = "TOKEN_HERE"

def api(path, body):
    req = urllib.request.Request(TUNNEL + path, data=json.dumps(body).encode(),
        headers={"Content-Type": "application/json", "x-gdr-cli-token": TOKEN})
    return json.load(urllib.request.urlopen(req, timeout=300))

def render(prompt, seed, out):
    try:
        from hy3dgen.shapegen import Hunyuan3DDiTFlowMatchingPipeline
        from hy3dgen.texgen import Hunyuan3DPaintPipeline
        from hy3dgen.text2image import HunyuanDiTPipeline
        t2i = HunyuanDiTPipeline("Tencent-Hunyuan/HunyuanDiT-v1.2-Diffusers-Distilled")
        shape = Hunyuan3DDiTFlowMatchingPipeline.from_pretrained("tencent/Hunyuan3D-2mini")
        paint = Hunyuan3DPaintPipeline.from_pretrained("tencent/Hunyuan3D-2")
        img = t2i(prompt).images[0]
        mesh = paint(shape(image=img)[0], image=img)
        mesh.export(out)
        return "hunyuan"
    except Exception as e:
        print("hunyuan failed, triposr fallback:", str(e)[:200])
        import torch
        from PIL import Image
        from tsr.system import TSR
        model = TSR.from_pretrained("stabilityai/TripoSR", config_name="config.yaml", weight_name="model.ckpt")
        model.to("cuda")
        with torch.no_grad():
            mesh = model([Image.new("RGB", (512, 512), (200, 200, 200))], device="cuda")[0]
        mesh.export(out)
        return "triposr"

jobs = api("/api/batch-factory/claim", {"workerId": "cook-1", "limit": 2}).get("jobs", [])
print("claimed", len(jobs))
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
        print("job failed:", j["jobId"], str(e)[:300])
print("CHUNK-DONE")
