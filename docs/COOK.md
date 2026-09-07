# COOK BOOK — auto 3D cook, zero clicks. Future AI read this first.

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
- No-popups wire: MCP SDK hides child windows only in Electron. Patched node_modules SDK esm+cjs stdio.js windowsHide:true (npm reinstall wipes it, re-apply). Services spawn headless flags 8+512+134217728 so children inherit no window.
