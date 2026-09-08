import base64, json, os, urllib.request

GW = "http://127.0.0.1:20128"
TOK = os.environ.get("FORGE_GATEWAY_TOKEN", "")

def post(path, body, timeout=600):
    r = urllib.request.Request(GW + path, data=json.dumps(body).encode(),
                               headers={"Content-Type": "application/json",
                                        "x-gdr-cli-token": TOK})
    return json.load(urllib.request.urlopen(r, timeout=timeout))

FILES = {
    "small round pumpkin with stem, game prop":
        "work/kout/66a58f18-5299-4007-997a-bc6965412ce0.glb",
    "tall ribbed pumpkin, game prop":
        "work/kout/67479fa3-2ce8-47f6-a950-e876342f112f.glb",
}

for prompt, path in FILES.items():
    b = post("/v1/assets/generations", {"prompt": prompt, "model": "hunyuan3d-kaggle",
                                        "kind": "asset", "seed": 42})
    batch, job = b["batchId"], b["jobId"]
    claimed = post("/api/batch-factory/claim", {"workerId": "local-1", "limit": 8})["jobs"]
    mine = [j for j in claimed if j["jobId"] == job][0]
    raw = open(path, "rb").read()
    print(prompt[:30], len(raw), "bytes")
    print(post("/api/batch-factory/deliver",
               {"batchId": batch, "jobId": job,
                "fileBase64": base64.b64encode(raw).decode()}).get("staged"))
    done = post("/api/batch-factory/complete", {"batchId": batch, "jobId": job})
    print("complete:", done.get("ok"), done.get("code"))
print("LANDED-2")
