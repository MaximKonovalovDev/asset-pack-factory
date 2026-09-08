# COOK BOOK — auto 3D cook, zero clicks. Future AI read this first.

## THE workflow (checked, works). One file: work/cook.py
- `python work/cook.py start` — boot T4 forge-cook2 via colab-3.
- `python work/cook.py setup` — kernel pip: hy3dgen, trimesh, peft+transformers new. Background, poll import.
- `FORGE_COOK_TUNNEL=<live public url> python work/cook.py launch` — write worker to VM.
- `python work/cook.py run` — nohup background. `log` polls /tmp/cook.log. `stop` frees GPU.
- `python work/cook.py requeue` — stuck claims back to queued. `status` — quota.
- Worker loop: claim 2 -> image -> shape -> paint (sequential, del + empty_cache between, 12GB OOM else) -> deliver 32MB cap -> complete (gates) -> idle-out.
- Env law: kernel python IS /usr/bin/python3. Install ONLY via sys.executable -m pip. Fresh session beats dep war.
- Never 20 scripts again. One driver. VM log is truth, not MCP output slices.

## Pieces
- Queue: POST /v1/assets/generations (gateway :20128, token). Jobs sit in memory.
- Claim: POST /api/batch-factory/claim {workerId, limit 1-8}. Flips queued->claimed.
- Deliver: POST /api/batch-factory/deliver {batchId, jobId, fileBase64}. Cap 32MB. Writes staged.
- Complete: POST /api/batch-factory/complete {batchId, jobId}. Gates via acquire-first. Red blocks.
- Cook: work/real-cook.ipynb (private, holds token). Claims 2, renders Hunyuan (TripoSR fallback), delivers, completes, idle-out 10 min.
- Build it: python work/mkcook.py with FORGE_COOK_TUNNEL=live public url + FORGE_GATEWAY_TOKEN in env. Never print either.
- Tunnel: POST /api/tunnel/public starts cloudflared. URL dies on gateway restart -> rebuild notebook.
- Restart wipes queue (memory). Re-fire via apf/router.py generate().

## Lessons (blood)
- Farm templates were STUBS (idle loop, no render). Never trust, read code.
- :20129 aggregator died once; spawn detached python 8+512, probe /health.
- Vault has 70+ unit-test junk accounts. Do not touch. Kaggle key = kaggle-main.
- Kaggle MCP: quota/save calls refuse. Kernels push needs key server-side (door 2, open).
## Colab MCP truth (researched 2026-09-08)
- Official googlecolab/colab-mcp: browser-tab driving only. 1 tool visible. GPU = manual click. Dead end for auto.
- anluin/colab-mcp (in C:/tmp-acm): browserless runtimes, Windows OK. Needs ONE Google OAuth (cached forever). Tools: colab_health, start T4 session, run commands, stop. Serve is non-interactive.
- Machine ready: uv 0.11.32 + env built. Doctor says: auth missing. Human runs `uv run --directory C:/tmp-acm colab-mcp auth` once, then AI serves forever.
- After auth: wire as aggregator stdio remote, cook with zero clicks.
- deucebucket/colab-runtime-mcp: same family + long-job keepalive. Backup pick.
- Token in real-cook.ipynb. Private repo only. Rotate token if repo ever goes public.
- KAGGLE lane (live 2026-09-08): new KGAT_ token goes to ~/.kaggle/access_token (NOT kaggle.json). Kernel at maximkonovalovx/forge-cook-1, private, T4, internet. Source in C:/forge-scratch/kaggle-cook/ (NEVER git: holds gateway token). Push: kaggle kernels push -p DIR --accelerator NvidiaTeslaT4. Watch: kaggle kernels status SLUG. Pull: kaggle kernels output SLUG -p ./out.
- COLAB lane: colab-3 (anluin, browserless) for interactive; official needs tab. GPU grants dry at night; CPU proves account health.
- Model ids: shape+paint from 'tencent/Hunyuan3D-2' (lowercase full). 2mini id is wrong path.
- Colab env war: pip resolve hangs via MCP (500s). Use background installs + poll. Kernel env (/usr/local) != run_command python — install with sys.executable -m pip. Stale kernels hold old imports — fresh session wins.
- Stuck claims: dead workers leave claimed jobs. POST /api/batch-factory/requeue flips all non-done back to queued.
- No-popups wire: MCP SDK hides child windows only in Electron. Patched node_modules SDK esm+cjs stdio.js windowsHide:true (npm reinstall wipes it, re-apply). Services spawn headless flags 8+512+134217728 so children inherit no window.
