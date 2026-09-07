# BRIEF — pack spec (`brief.yaml`)

One file per pack. It is the order sheet. Code reads it, humans sign it.

## Shape

```yaml
id: "001-fantasy-props"          # slug (small letters, dash). Must be sole (no dup).
title: "Low-Poly Fantasy Props — Volume 1"
description: "30 props for stylized RPG. Modular (parts snap). Demo scenes in."

style:                            # heart of the brief. Locks the look.
  reference_image: "reference/hero.png"
  reference_description: "low-poly faceted shading, vibrant palette, Synty mood"
  generation_seed: 42             # seed = fixed random start. Same seed, same look.
  palette: ["#a04040", "#80c0ff", "#f0e090", "#604030", "#306020", "#c0c0c0"]
  polygon_count_band: [800, 2500] # poly = face count. Low = fast game.
  texel_density_px_per_unit: 512  # texel = texture dots per meter. 512 = crisp stylized.
  material_complexity: "low_poly_flat"
  shading: "faceted"              # faceted = flat hard faces. smooth = soft.
  uv_strategy: "smart_project"    # uv = flat skin map for paint. Smart = auto.

grid:                             # snap = parts click in place.
  preset: "synty_polygon"
  grid_unit_meters: 1.0
  snap_pivot_to: "base_center"    # pivot = grab point. Base = stands on floor.
  snap_rotation_to_axes: true
  normalize_scale: true

pieces:                           # the 30 pieces. Keep 30 for pack #1.
  - { id: "barrel_wooden", category: "container", prompt: "wooden barrel with iron rings" }
  # ... 29 more. id must be snake_case (small + _). No dup ids.

generation:                       # gen = AI birth routes. Cheap first.
  primary_routes: ["fal-trellis", "fal-triposr"]
  hero_routes: ["fal-hunyuan3d-21"]   # hero = cover stars. 4 max.
  fallback_routes: ["triposr-local", "trellis-hf", "hunyuan-mini-local"]
  max_retries_per_piece: 3
  estimated_cloud_cost_usd: 2.12
  pre_prompt_style_prefix: "Low-poly stylized fantasy prop, faceted shading, centered, base on Y=0."

hero_piece_ids: ["chest_iron", "sword_short", "lantern_oil", "anvil_iron"]

exports: [unity, unreal, godot, master_glb]
marketplaces: [fab, itchio, gumroad]  # unity store deferred to pack #2.

demo_scenes:                      # demo = small test rooms that sell the pack.
  - { name: "tavern_corner", description: "tables, chairs, lantern, bottles" }
  - { name: "blacksmith_yard", description: "anvil, axe, sword, shield, barrel" }
  - { name: "campsite", description: "logs, mushrooms, rocks, torch" }

pricing:
  launch_usd: 9.99
  normal_usd: 19.99
  launch_window_days: 14

ai_disclosure:                    # disclosure = tell the shop AI helped. Shops demand it.
  models_used: ["TRELLIS", "Hunyuan3D-mini"]
  human_review: "All 30 reviewed. Topology and UVs checked. Palette tuned by hand."
  commercial_use_verified: true
```

## Rules

- 30 pieces for pack #1. More later.
- 4 hero max. Heroes get the costly model.
- Palette holds 4-8 hex colors. All pieces must match it.
- Seed is fixed. Same seed each run.
- No "handmade" word in text. Shops ban it for AI packs.
