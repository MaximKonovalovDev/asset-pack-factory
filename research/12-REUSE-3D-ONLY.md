# 12 Reuse Plan - 3D ONLY (from your old works + org)

Date: 2026-09-07
Rule: 3D assets and packs only. No 2D leg. game-asset-factory 2D pixel stays frozen, we take only its manifest + verify idea.

## Found
- Org: flax-game-studio
- FAW = flax-game-studio/flax-asset-worker (was diklaaltman91-ux/faw). C# hub :8790 + Python assetboy CLI, 40+ cmds, recipe packs, 3-lane router, 19 providers.
- 3D base = flax-game-studio/asset-forge. AI pack pipeline. export unity/unreal/godot/master_glb, lod, manifest, materials, retopo, uv, previews, snap_grid, style, orchestrator brief/pipeline/state, showroom. Pack 001-fantasy-props with brief.yaml.
- Live 3D lane = forge. Router hunyuan3d-kaggle -> blender-colab. 7 gates. opencode orchestrator + subs.
- Market brain = diklaaltman91-ux/steam-mcp-suite. Steam intel + itch jams + marketing research.

## TAKE - copy these
From asset-forge (core, keep almost all):
- common/types, paths, settings, errors, logging + cli status/validate/build/doctor
- orchestrator/brief, pipeline (13 phases + receipts + cost), state
- export/api + unity (stable GUIDs) + unreal + godot + master_glb + _shared
- lod/api, manifest/api + templates (README + license + AI tag), materials/api + library (50 PBR)
- retopo/api + backends (QuadriFlow, InstantMeshes, Blender, QuadRemesher), uvunwrap/api
- previews/api (hero + turntable + cover), snap_grid/api (base_center + names), style/api + scorers, showroom/api
- tests: brief, export, manifest, materials, snap_grid, state, style, lod, smoke
- packs/001 brief.yaml shape: id, style palette 6 hex + poly 800-2500 + texel 512 + seed 42, grid 1m base_center, 30 pieces, gen fal-trellis/triposr + hero hunyuan $2.12, exports 4, markets fab/itch/gumroad, pricing 9.99/19.99, ai_disclosure
- docs/MARKET numbers: Fab 88%, Unity 70%, Gumroad ~90%, itch up to 100%. Synty $25-150. Top = modular kits + style fit + cross-engine.

From FAW (lanes + free stock):
- cli/app, __main__, pack (recipe YAML -> pack), import_cmd (FBX/GLB/OBJ to Flax), library (search/install)
- runners: polyhaven (CC0 PBR), quaternius (CC0 low-poly), kenney (CC0 stylized), ambientcg (CC0 mats), mixamo_download + mixamo_glb (rig + anim via Blender), colab_runner (Hunyuan/TRELLIS), comfyui_runner (local PBR), _http_retry
- library/paths, files, asset_metadata, packet_writer, intake_validator + provenance/schema + templates
- workflows/pack_pipeline, acquisition_router (direct/manual/generator), recipe_validator, catalog + providers/lanes, direct_url, bridge_registry
- data/quaternius_presets.yaml + colab_pipelines.yaml + recipes/sandbox/one_pack_smoke.yaml + primitive_tech/first_playable.yaml

From forge (live lane + agents + opencode):
- ROUTER-PLAN 3D lane: asset3d hunyuan3d-kaggle default, blender-colab backup, gateway :20128 only, 7 gates
- pipe-recipes provenance 11 fields: seed, prompt, promptFamily, lane, model, providerVersion, sha256, license, source, date, routerHealth + same seed = same hash
- .opencode/agent/orchestrator.md -> orchestrator, explore.md -> researcher, factory.md -> maker
- opencode.jsonc agent{} + plugin[] + mcp forge-gateway :20128 shape

From steam-mcp-suite (researcher brain):
- skills/steam-store-intelligence/SKILL.md + src/tools/store.ts + src/steam/analysis.ts + client.ts + types.ts
- src/tools/itch.ts + src/itch/jams.ts (jam themes = pack ideas) + src/tools/portal.ts + lib cache/rateLimit/retry/http

From demos (test beds only):
- web-arena (web host), spear-arena (three.js GLB break test), flax-arena-web-demo (Roman FPS demo), flax-mcp (main stack + showcases)

## DROP
- game-asset-factory code (2D only). Take manifest + verify idea only.
- FAW audio/video/2D runners: freesound, jamendo, stable_audio, pexels, pixabay, unsplash, iconify, scryfall, met, wikimedia, archive, inaturalist, openlibrary, rawg, local_image, gdrive merger. Plus C# hub Source/ + FAW.flaxplugin (too heavy v0).
- asset-forge mcp_client (old socket), kaggle ipynb, CLOUD_GPU/HARDWARE/COMPETITIVE/STEAL docs (stale), reference png.
- studio, StudioAI, surf-studio, paperlife, appeal-ghostwriter, antivirus, studio-ai, flax-nav, arena-game stub, prehistoric-survival empty.

## New repo (3D only)
Name: asset-pack-factory (new, clean). Not upgrade of 2D factory.
```
asset-pack-factory/
├── AGENTS.md (simple short, one task list, one writer per dir)
├── opencode.jsonc (orchestrator primary + researcher + maker + explore)
├── .opencode/agent/ (orchestrator.md, researcher.md, maker.md, explore.md)
├── .opencode/plugin/gates.mjs (manifest must match, no delete you did not create)
├── pipeline/ (from asset-forge src + FAW runners + forge gateway client)
├── packs/pack-a-sl-fall-5 + pack-b-fab-fall-65 + pack-c-roblox-hats-3
│   └── brief.yaml + manifest.json + provenance.json + previews + exports
├── research/ (move Desktop/forge-cash-packs 01-10 here, one file per site)
├── records/ + state/library.json
```

## Agents parallel (like here)
- orchestrator: owns plan, state, records. Small fix writes. Big -> batch subs. One dir per sub.
- researcher: owns research/. Steam + itch + SL + Fab numbers + 3 URLs each. Never touches packs/ at same time.
- maker: owns pipeline/ + packs/. Router -> clean -> LOD -> PBR -> verify -> ship. Logs library.json.
- Rule: researcher + maker together when dirs differ. Ship step alone (one writer).

## Next
1. Scaffold asset-pack-factory local with AGENTS + opencode + pipeline empty + research moved.
2. Wave 1: researcher refreshes SL + Fab Sept prices. Maker builds Pack A raw 5 via hunyuan.
3. Say GO and I scaffold.
