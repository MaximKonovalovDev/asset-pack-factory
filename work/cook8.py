import urllib.request, json, sys

AGG = "http://127.0.0.1:20129/mcp/call"

def call(tool, args, timeout=600):
    d = json.dumps({"tool": tool, "arguments": args}).encode()
    r = urllib.request.Request(AGG, data=d, headers={"Content-Type": "application/json"})
    out = json.load(urllib.request.urlopen(r, timeout=timeout))
    txt = json.dumps(out)
    print(tool, "ok=" + str(out.get("ok")), txt[120:320].replace("\n", " "))
    return out

def exe(code, timeout=600):
    return call("colab-3__colab_execute", {"session": "forge-cook2", "code": code, "timeout": timeout}, timeout + 120)

if __name__ == "__main__":
    step = sys.argv[1]
    if step == "start":
        call("colab-3__colab_start", {"session": "forge-cook", "gpu": "T4"})
    elif step == "install":
        exe("import subprocess, sys\nsubprocess.run([sys.executable, '-m', 'pip', 'install', '-q', 'hy3dgen', 'trimesh', 'boto3'], check=False)\nprint('deps-done')", 2400)
    elif step == "cook":
        import os
        code = open("C:/asset-pack-factory/work/cookloop.py").read()
        code = code.replace("TUNNEL_HERE", os.environ["FORGE_COOK_TUNNEL"]).replace("TOKEN_HERE", os.environ["FORGE_GATEWAY_TOKEN"])
        exe(code, 3000)
    elif step == "stop":
        call("colab-3__colab_stop", {"session": "forge-cook"})
