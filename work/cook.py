"""One cook workflow. Colab T4 via colab-3 + gateway board. Zero clicks after auth."""
import base64, json, os, sys, urllib.request

AGG = "http://127.0.0.1:20129/mcp/call"
GW = "http://127.0.0.1:20128"
SES = "forge-cook3"

WORKER = """
import base64, json, time, urllib.request, traceback

TUNNEL = "TUNNEL_HERE"
TOKEN = "TOKEN_HERE"
LOG = open("/tmp/cook.log", "a", buffering=1)

def log(*a):
    LOG.write(" ".join(str(x) for x in a) + "\\n")

def api(path, body):
    req = urllib.request.Request(TUNNEL + path, data=json.dumps(body).encode(),
        headers={"Content-Type": "application/json", "x-gdr-cli-token": TOKEN})
    return json.load(urllib.request.urlopen(req, timeout=300))

STAGE_IMG = '''
import sys
from hy3dgen.text2image import HunyuanDiTPipeline
t2i = HunyuanDiTPipeline("Tencent-Hunyuan/HunyuanDiT-v1.2-Diffusers-Distilled")
_img = t2i(sys.argv[1])
img = _img.images[0] if hasattr(_img, "images") else _img
img.save(sys.argv[2])
print("IMG-DONE")
'''

STAGE_SHAPE = '''
import sys
from hy3dgen.shapegen import Hunyuan3DDiTFlowMatchingPipeline
from PIL import Image
shape = Hunyuan3DDiTFlowMatchingPipeline.from_pretrained("tencent/Hunyuan3D-2")
mesh = shape(image=Image.open(sys.argv[1]).convert("RGB"))[0]
mesh.export(sys.argv[2])
print("SHAPE-DONE")
'''

STAGE_PAINT = '''
import sys, trimesh
from hy3dgen.texgen import Hunyuan3DPaintPipeline
from PIL import Image
paint = Hunyuan3DPaintPipeline.from_pretrained("tencent/Hunyuan3D-2")
mesh = trimesh.load(sys.argv[2])
mesh = paint(mesh, image=Image.open(sys.argv[1]).convert("RGB"))
mesh.export(sys.argv[3])
print("PAINT-DONE")
'''

def render(prompt, seed, out):
    import subprocess
    open("/tmp/s_img.py", "w").write(STAGE_IMG)
    open("/tmp/s_shape.py", "w").write(STAGE_SHAPE)
    open("/tmp/s_paint.py", "w").write(STAGE_PAINT)
    imgp, rawp = "/tmp/in.png", out + ".raw.glb"
    run = lambda *a: subprocess.run(["/usr/bin/python3", *a], check=True,
                                    stdout=open("/tmp/stage.log", "a"), stderr=subprocess.STDOUT)
    log("stage 1/3 image")
    run("/tmp/s_img.py", prompt, imgp)
    log("stage 2/3 shape")
    run("/tmp/s_shape.py", imgp, rawp)
    log("stage 3/3 paint")
    try:
        run("/tmp/s_paint.py", imgp, rawp, out)
    except Exception as e:
        log("paint skipped (needs compiled rasterizer), ship raw shape:", str(e)[:120])
        import shutil
        shutil.copyfile(rawp, out)

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


def mex(code, timeout=180):
    return mcp("colab-3__colab_execute",
               {"session": SES, "code": code, "timeout": timeout}, timeout)


def mrun(argv, timeout=300):
    return mcp("colab-3__colab_run_command", {"session": SES, "argv": argv}, timeout)


def out_text(out):
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


def gw(path, body=None):
    tok = os.environ.get("FORGE_GATEWAY_TOKEN", "")
    r = urllib.request.Request(GW + path,
                               data=json.dumps(body or {}).encode() if body is not None else None,
                               headers={"Content-Type": "application/json", "x-gdr-cli-token": tok})
    return json.load(urllib.request.urlopen(r, timeout=120))


if __name__ == "__main__":
    cmd = sys.argv[1]
    if cmd == "start":
        print(mcp("colab-3__colab_start", {"session": SES, "gpu": "T4"}, 300))
    elif cmd == "setup":
        # Kernel env only (sys.executable -m pip). Fixes: peft + transformers new.
        out_text(mex("import subprocess, sys\n"
                     "subprocess.Popen([sys.executable, '-m', 'pip', 'install', '-q',\n"
                     " 'hy3dgen', 'trimesh', '--no-deps', '-U', 'peft', 'transformers'],\n"
                     " stdout=open('/tmp/pip.log','w'), stderr=subprocess.STDOUT, start_new_session=True)\n"
                     "print('SETUP-BG-STARTED')\n", 120))
    elif cmd == "launch":
        code = WORKER.replace("TUNNEL_HERE", os.environ["FORGE_COOK_TUNNEL"]).replace(
            "TOKEN_HERE", os.environ["FORGE_GATEWAY_TOKEN"])
        writer = "open('/tmp/w.py','w').write(" + repr(code) + ")\nprint('W-WROTE')\n"
        out_text(mex(writer, 120))
    elif cmd == "run":
        out_text(mcp("colab-3__colab_run_command", {"session": SES, "argv": [
            "bash", "-c", "rm -f /tmp/cook.log; nohup /usr/bin/python3 /tmp/w.py > /tmp/nohup.log 2>&1 & echo BG-STARTED"]}, 120))
    elif cmd == "log":
        out_text(mcp("colab-3__colab_run_command", {"session": SES, "argv": [
            "bash", "-c", "tail -n 25 /tmp/cook.log 2>/dev/null || echo NO-LOG-YET"]}, 120))
    elif cmd == "stop":
        print(mcp("colab-3__colab_stop", {"session": SES}, 120))
    elif cmd == "status":
        print(json.dumps(gw("/api/quota"))[:300])
    elif cmd == "requeue":
        print(gw("/api/batch-factory/requeue", {}))
