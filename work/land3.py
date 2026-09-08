import base64, json, os, urllib.request

GW = "http://127.0.0.1:20128"
TOK = os.environ.get("FORGE_GATEWAY_TOKEN", "")

def post(path, body, timeout=600):
    r = urllib.request.Request(GW + path, data=json.dumps(body).encode(),
                               headers={"Content-Type": "application/json",
                                        "x-gdr-cli-token": TOK})
    return json.load(urllib.request.urlopen(r, timeout=timeout))

b = post("/v1/assets/generations", {"prompt": "autumn leaf wreath round, game decor",
                                    "model": "hunyuan3d-kaggle", "kind": "asset", "seed": 42})
batch, job = b["batchId"], b["jobId"]
claimed = post("/api/batch-factory/claim", {"workerId": "local-1", "limit": 8})["jobs"]
assert any(j["jobId"] == job for j in claimed), "claim missed"
raw = open("work/kout3/6d27fb98-60b8-480c-a294-e799e805f9d4.glb", "rb").read()
print(len(raw), "bytes")
print(post("/api/batch-factory/deliver",
           {"batchId": batch, "jobId": job,
            "fileBase64": base64.b64encode(raw).decode()}).get("staged"))
done = post("/api/batch-factory/complete", {"batchId": batch, "jobId": job})
print("complete:", done.get("ok"), done.get("code"))
print("LANDED-WREATH")
