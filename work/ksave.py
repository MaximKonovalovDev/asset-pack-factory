import urllib.request, json

AGG = "http://127.0.0.1:20129/mcp/call"

def call(tool, args):
    d = json.dumps({"tool": tool, "arguments": args}).encode()
    r = urllib.request.Request(AGG, data=d, headers={"Content-Type": "application/json"})
    return urllib.request.urlopen(r, timeout=180).read().decode(errors="replace")

if __name__ == "__main__":
    import sys
    req = {
        "newTitle": "forge-probe", "hasNewTitle": True,
        "text": "print('hello-forge')", "hasText": True,
        "language": "python", "hasLanguage": True,
        "isPrivate": True, "hasIsPrivate": True,
        "enableGpu": False, "hasEnableGpu": True,
        "enableInternet": False, "hasEnableInternet": True,
    }
    print(call("kaggle__save_notebook", {"request": req})[:800])
