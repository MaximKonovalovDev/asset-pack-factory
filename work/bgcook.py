import urllib.request, json

AGG = "http://127.0.0.1:20129/mcp/call"
SES = "forge-cook2"

WORKER = """
import base64, json, time, urllib.request, traceback

TUNNEL = "TUNNEL_HERE"
TOKEN = "TOKEN_HERE"
LOG = open("/tmp/cook.log", "a", buffering=1)

def log(*a):
    msg = " ".join(str(x) for x in a)
    LOG.write(msg + "\\n")

def api(path, body):
    req = urllib.request.Request(TUNNEL + path, data=json.dumps(body).encode(),
        headers={"Content-Type": "application/json", "x-gdr-cli-token": TOKEN})
    return json.load(urllib.request.urlopen(req, timeout=300))

def render(prompt, seed, out):
    from hy3dgen.shapegen import Hunyuan3DDiTFlowMatchingPipeline
    from hy3dgen.texgen import Hunyuan3DPaintPipeline
    from hy3dgen.text2image import HunyuanDiTPipeline
    log("loading models once")
    t2i = HunyuanDiTPipeline("Tencent-Hunyuan/HunyuanDiT-v1.2-Diffusers-Distilled")
    shape = Hunyuan3DDiTFlowMatchingPipeline.from_pretrained("tencent/Hunyuan3D-2")
    paint = Hunyuan3DPaintPipeline.from_pretrained("tencent/Hunyuan3D-2")
    log("models up")
    img = t2i(prompt).images[0]
    log("image done")
    mesh = shape(image=img)[0]
    log("shape done")
    mesh = paint(mesh, image=img)
    log("paint done")
    mesh.export(out)

while True:
    try:
        jobs = api("/api/batch-factory/claim", {"workerId": "cook-2", "limit": 2}).get("jobs", [])
    except Exception as e:
        log("claim failed", str(e)[:150])
        time.sleep(60)
        continue
    if not jobs:
        log("queue empty, COOK-EXIT")
        break
    for j in jobs:
        out = "/tmp/" + j["jobId"] + ".glb"
        try:
            log("start", j["jobId"], j["prompt"][:50])
            render(j["prompt"], j.get("seed", 42), out)
            raw = open(out, "rb").read()
            log("rendered", len(raw), "bytes")
            api("/api/batch-factory/deliver", {"batchId": j["batchId"], "jobId": j["jobId"],
                "fileBase64": base64.b64encode(raw).decode()})
            done = api("/api/batch-factory/complete", {"batchId": j["batchId"], "jobId": j["jobId"]})
            log("done", j["jobId"], done.get("code", done))
        except Exception:
            log("job failed", j["jobId"], traceback.format_exc()[-400:])
"""

def mcp(tool, args, timeout=300):
    d = json.dumps({"tool": tool, "arguments": args}).encode()
    r = urllib.request.Request(AGG, data=d, headers={"Content-Type": "application/json"})
    return json.load(urllib.request.urlopen(r, timeout=timeout + 60))

def show(out):
    for c in out.get("result", {}).get("content", []):
        t = c.get("text", "")
        t = t if isinstance(t, str) else json.dumps(t)
        try:
            j = json.loads(t)
            s = j.get("stdout", "")
            if s:
                print(s[-1500:])
                return
        except Exception:
            pass
        print(t[-300:])

if __name__ == "__main__":
    import os, sys
    mode = sys.argv[1]
    if mode == "launch":
        code = WORKER.replace("TUNNEL_HERE", os.environ["FORGE_COOK_TUNNEL"]).replace(
            "TOKEN_HERE", os.environ["FORGE_GATEWAY_TOKEN"])
        writer = "open('/tmp/w.py','w').write(" + repr(code) + ")\nprint('W-WROTE')\n"
        out = mcp("colab-3__colab_execute", {"session": SES, "code": writer, "timeout": 120}, 180)
        show(out)
    elif mode == "run":
        out = mcp("colab-3__colab_run_command", {"session": SES, "argv": [
            "bash", "-c", "rm -f /tmp/cook.log; nohup python3 /tmp/w.py > /tmp/nohup.log 2>&1 & echo BG-STARTED"]}, 120)
        show(out)
    elif mode == "log":
        out = mcp("colab-3__colab_run_command", {"session": SES, "argv": [
            "bash", "-c", "tail -n 25 /tmp/cook.log 2>/dev/null || echo NO-LOG-YET"]}, 120)
        show(out)
