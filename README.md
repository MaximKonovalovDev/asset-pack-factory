# Asset Pack Factory — brief to shippable 3D + SFX + VFX packs

Pipeline that turns a `brief.yaml` into verified, export-ready packs for Unity, Unreal, Godot, Flax, Second Life, Roblox, Minecraft, and FiveM — plus generated SFX/VFX and store-ready previews.

```
brief.yaml -> generate -> fix -> PBR -> LOD -> verify -> export -> ship
```

## Quickstart

```bash
pip install -r requirements.txt
python -m apf packs3d packs/pack-a-sl-fall-5/brief.yaml
python -m apf verify3d work/pack-a-sl-fall-5
python -m apf ship work/pack-a-sl-fall-5 --site sl-market
```

## Layout

```
apf/        # generator, fixer, PBR, LOD, verifier, packer, CLI, state
exports/    # per-engine export profiles
ship/       # one lane per storefront
sfx/ vfx/ packs/ previews/ research/ records/
.opencode/  # 10 lane agents + project config
```

## What it proves

- Repeatable asset ops: every run keeps provenance, manifests, and verification receipts.
- Multi-engine exports from one source brief.
- Agent-assisted workflow (10 lane agents) with gates before ship.

## Built from

- `asset-forge` (brief/pipeline/state, LOD, manifest, previews)
- `flax-asset-worker` (pack CLI, free runners, provenance)
- Private forge gateway (3D lane, quality gates)
- `steam-mcp-suite` (store/jam research input)

Full attribution in `CREDITS.md`. All bundled code is MIT-compatible or original.

## Roadmap

More export profiles, preview renders per pack, automated store listing drafts.

## Author

Maxim Konovalov — Haifa · game assets + AI pipelines. Live pack demos on call.
