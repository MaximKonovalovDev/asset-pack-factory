# asset-pack-factory — slim 3D + SFX + VFX pack factory

You direct, pipe produces. Sell on Fab / Unity / SL / Roblox / itch / Patreon.

```
brief.yaml -> gen -> fix -> pbr -> lod -> verify -> export -> ship
```

## Layout (slim, 24 files max)
```
apf/ (gen, fix, pbr, lod, verify, pack, cli, state)
exports/ (unity, unreal, godot, flax, secondlife, roblox, minecraft, fivem)
ship/ (one lane file per site)
sfx/ vfx/ packs/ previews/ research/ records/ state/
.opencode/agent/ (10 agents) + opencode.jsonc
```

## Quick start
```bash
pip install -r requirements.txt
python -m apf packs3d packs/pack-a-sl-fall-5/brief.yaml
python -m apf verify3d work/pack-a-sl-fall-5
python -m apf ship work/pack-a-sl-fall-5 --site sl-market
```

## Took from
- asset-forge: orchestrator brief/pipeline/state, export, lod, manifest, mats, retopo, uv, previews, snap, style.
- FAW: pack CLI, free runners (polyhaven, quaternius, kenney, ambientcg, mixamo, colab, comfyui), provenance, router.
- forge: gateway :20128 3D lane, 7 gates, provenance 11 fields, opencode agents.
- steam-mcp-suite: researcher Steam + itch jam brain.
See STEAL.md for credit.
