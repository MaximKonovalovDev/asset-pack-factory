# 11 New Repo Plan - Asset Pack Factory v2

Date: 2026-09-07
Note: no repo named FAW found. I used forge as FAW (Flax AI factory) + game-asset-factory (2D pixel).

## What you have now
- forge (private, live Sep 7): Flax game factory. 16 verbs. Router service. 3D lane hunyuan3d-kaggle -> blender-colab. 7 asset gates. opencode setup with orchestrator + 19 subs + 3 plugins + 4 skills. Parallel by lane.
- game-asset-factory (private, Aug 18): 2D only. 16x16 pixel art. Pure Python + Pillow. Deterministic seeds. CLI: packs, tiles, ai-pass OFF, verify. 3 packs with manifest.json + preview.png + itch-listing.txt. MIT. GAP says: no 3D, no audio, no rig, no engine exports.

## New repo: do NOT overwrite game-asset-factory
- Keep game-asset-factory as 2D leg. It sells on itch $5-29.
- Make new repo: asset-pack-factory (name pick: asset-pack-factory).
- Why new: old GAP bans 3D. Side cash needs 3D (SL, Fab, Unity, Roblox). New repo = 3D + 2D side by side.

## Reuse list (copy, do not fork blind)
From game-asset-factory, reuse:
- packs/<pack>/manifest.json (seed, license, file bytes) -> keep same shape, add tris, LODs, PBR maps, rights.
- packs/<pack>/itch-listing.txt (3-line blurb) -> keep, add per-site listings: fab-listing.txt, sl-listing.txt, roblox-listing.txt.
- pipeline/cli.py packs + verify -> keep pattern: packs3d, verify3d, ship.
- pipeline/ai_pass.py HUMAN_GATE (no spend without human OK) -> keep for 3D router spend.
From forge, reuse:
- docs/ROUTER-PLAN.md 3D lane: hunyuan3d-kaggle default, blender-colab backup, 7 gates (watertight, poly budget, UV overlap, PBR split, albedo clean, rig, import).
- gateway :20128 only, never direct :78xx. Same seed+prompt+lane = same hash.
- state/library.json reuse catalog (id, path, source, owner).
- opencode setup: opencode.jsonc + .opencode/agent/ + .opencode/plugin/ + AGENTS.md simple-short rule.

## New repo layout
```
asset-pack-factory/
├── AGENTS.md              # simple short English, one task list, one writer per dir
├── opencode.jsonc         # orchestrator primary + 3 subs (see below)
├── .opencode/agent/       # orchestrator.md, researcher.md, maker.md, explore.md
├── .opencode/plugin/      # gates.mjs (no delete you did not create, manifest must match)
├── .opencode/skills/      # pack-ship (ships SL/Fab/Unity/Roblox checks)
├── pipeline3d/            # cli.py: packs3d, clean, lods, pbr, verify3d, ship
├── packs/                 # pack-a-sl-fall-5, pack-b-fab-fall-65, pack-c-roblox-hats-3
│   └── <pack>/manifest.json + preview.png + *-listing.txt + provenance.json
├── research/              # one file per site, from Desktop/forge-cash-packs 01-09
├── records/               # decisions by slug-name, no numbers in comments
└── state/library.json     # reuse catalog
```

## Research each site -> plan for it (one file each in research/)
- SL: LI 1-5/prop, DAE + 4 LODs + physics, Mod/Copy, PBR, L$199. Full-perm rule: must add value, next perms no-copy or no-transfer.
- Fab: 100-1500 tris/prop, FBX/GLB, PBR, LODs, demo scene, tag Created with AI, $15.99 for 65.
- Unity: same + URP/HDRP, LOD Group, 2-4 week review, $15.99 same pack.
- Roblox: 4000 tris max, 1 mesh, no holes, 1024, 75-95 Robux, AI ok if owned.
- itch: $3-10 small, 10% fee + $0.30+2.9%, Halloween sale 13k items.
- Patreon/Ko-fi: $5 entry, vault after season.
- Minecraft/UEFN/FiveM/Horizon: phase 2, not pack 1.

## Agents: 3 only (parallel like here)
- orchestrator (primary): owns plan, state/, records/, docs/. Writes small. Big work -> batch subs. One dir per sub. Never writes files a running sub touches.
- researcher (subagent, no write to packs/): owns research/. Web only. Returns numbers + 3 URLs per site. Never plans, never judges. Like explore but may write research/ only.
- maker (subagent): owns pipeline3d/ + packs/. Router -> clean -> LOD -> PBR -> verify -> ship. Logs every asset in state/library.json. Never touches research/ while researcher runs.
- Dispatch rule: researcher + maker run together when dirs differ. Same files, one writer. Pilot-like lock for ship step (one ship at a time).

## opencode.jsonc minimal (copy from forge, trim to 3)
- default_agent orchestrator, instructions AGENTS.md
- mcp: forge-gateway remote :20128 (3D lane), no local forge/flax-live (this repo has no engine)
- agent: orchestrator primary, researcher subagent, maker subagent, explore subagent
- plugin: gates.mjs only (manifest size check + no-delete rule)

## Next steps
1. Confirm name: asset-pack-factory (new) vs game-asset-factory-v2 (upgrade). I vote new.
2. I scaffold repo local, copy AGENTS + opencode + pipeline verify pattern, no packs yet.
3. Move Desktop/forge-cash-packs 01-10 into research/.
4. First wave: researcher refreshes SL + Fab prices, maker builds Pack A raw 5.
