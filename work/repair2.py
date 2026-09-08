import urllib.request, json

URL = "http://127.0.0.1:7875/repair"

JOBS = [
    ("C:/asset-pack-factory/work/kout/66a58f18-5299-4007-997a-bc6965412ce0.glb",
     "C:/asset-pack-factory/work/pack-a-sl-fall-5/pumpkin1-30k.glb", 30000),
    ("C:/asset-pack-factory/work/kout/67479fa3-2ce8-47f6-a950-e876342f112f.glb",
     "C:/asset-pack-factory/work/pack-a-sl-fall-5/pumpkin2-30k.glb", 30000),
]

for inp, out, faces in JOBS:
    body = json.dumps({"inputPath": inp, "outputPath": out, "target_faces": faces,
                       "remove_dup": True, "remove_degenerate": True,
                       "fill_holes": True, "fix_normals": True}).encode()
    r = urllib.request.Request(URL, data=body, headers={"Content-Type": "application/json"})
    print(inp[-20:], json.load(urllib.request.urlopen(r, timeout=600)))
print("REPAIRED-2")
