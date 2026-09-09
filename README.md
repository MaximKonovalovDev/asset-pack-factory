# Asset Pack Factory

Slim 3D + SFX + VFX factory: a `brief.yaml` in, verified shippable packs out.

Built for Flax engine asset work, beside `flax-asset-worker` (https://github.com/MaximKonovalovDev/flax-asset-worker).

## Why

Selling a 3D pack means the same checklist every time: generate meshes, clean
them, PBR texture, LOD, verify, export per engine, write the store listings.
This repo keeps that checklist as code, so every pack ships with provenance
and receipts instead of loose files.

## What it does

- `brief.yaml` -> generate -> fix -> PBR -> LOD -> verify -> export -> ship.
- 8 export profiles: Unity, Unreal, Godot, Flax, Second Life, Roblox, Minecraft, FiveM.
- 9 storefront lanes (Fab, Unity, Second Life market, Roblox, itch.io,
  vault/Patreon/Ko-fi, stock, Minecraft, UEFN) with fee, upload, and
  AI-disclosure notes per site.
- Heavy 3D generation runs through a gateway (Hunyuan/Trellis); the repo holds
  briefs, state, and receipts, not GPU code.
- 10 lane agents under `.opencode/` assist the run; verify gates block ship on red.

## Quick start

```bash
pip install -r requirements.txt
python -m apf packs3d packs/pack-a-sl-fall-5/brief.yaml
python -m apf verify3d work/pack-a-sl-fall-5
python -m apf ship work/pack-a-sl-fall-5 --site sl-market
```

All four commands were run clean on 2026-09-09 (Python 3.13, Pillow + PyYAML).

## Demo + proof numbers

Measured 2026-09-09, in this checkout:

- `packs3d` on `pack-a-sl-fall-5`: brief ok, 5 pieces -> `work/pack-a-sl-fall-5`.
- `verify3d`: 7 gates (watertight, polyBudget, uvOverlap, pbrSplit, albedoClean,
  rig, import). Honest limit: mesh checks are still TODO stubs that pass on
  manifest + file presence.
- `ship --site sl-market`: verify green, then writes `dist/manifest.json`.
- `packs/` holds 3 briefs: pack-a-sl-fall-5, pack-b-fab-fall-65,
  pack-d-castle-kit-30. There is no `pack-e-roman-legion-40` in this checkout.
- `out/` holds 9 storefront listing templates + `manifest.json`. The per-site
  fee/upload/AI-tag research is real; per-pack values are placeholders
  ("Pack title", "pack-id", "Short blurb").
- `work/pack-a-sl-fall-5` ships real gateway output: a 35 MB raw `.glb`, two
  ~540 KB 30k LOD `.glb` files, and `raw_jobs.json` provenance.

## Project structure

```
apf/        # CLI + pipeline: gen, fix, pbr, lod, verify, pack, router, state
packs/      # 3 pack briefs (yaml): SL fall, Fab fall, castle kit
work/       # per-pack workdirs: meshes, jobs, dist manifests
out/        # 9 storefront listing templates + manifest.json
exports/    # 8 per-engine export profiles
ship/       # storefront ship lane (ship.ps1)
docs/       # brief, lanes, manifest, cook, Flax notes
.opencode/  # 10 lane agents + project config
```

## License

MIT — see `LICENSE` (Maxim Konovalov). Attribution in `CREDITS.md`.

## Author

Maxim Konovalov — Haifa. Game assets + AI pipelines.
