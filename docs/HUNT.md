# HUNT — 40 picks, 5 corners. Flax first.

Rule: Flax eats FBX/GLB. Every pick must end as FBX/GLB into scratch Content. Test there, sell after.

## MIGRATE (take whole)
- meshy-dev/game-asset-pipeline (MIT) — batch text->3D loop. Closest to us.
- elithril/blender-kiln (MIT) — brief -> Blender -> GLB batch.
- OndrejNepozitek/Edgar-DotNet (MIT, C#) — snap-grid dungeons. Easy Flax port. Pair with KayKit meshes.
- BuildingBlock paper (SIGGRAPH 25) — box -> rule -> mesh. Copy in C#.
- zeux/meshoptimizer (MIT) — gltfpack LOD + pack. Embed in import.
- Veradictus/FlaxMCP (MIT-ish) — 87 tools C# bridge. Drop to editor.
- tbarracha/Blender-To-Flax (no license, ask) — split anims to FBX for Flax.
- MuddyTerrain/unreal-ci-cd-for-fab (MIT) — zip + upload. Copy for Flax+Fab.
- Korext/ai-attestation (Apache) — AI license YAML + CI gate.

## REUSE (use as-is)
- TRELLIS (MIT) — detail gen. GLB out.
- TripoSR (MIT) — 0.5s draft. OBJ -> GLB fix.
- SF3D — 0.5s GLB direct. Low GPU.
- OnePersonLabs/asset-mcp — router part only.
- KayKit Dungeon (CC0) — 200+ parts, 2m grid, Flax ready.
- Quaternius MegaKit (CC0) — 270+ parts, 1-2m grid, Flax ready.
- StableMaterials — 5 PBR maps. Flax eats all.
- ArmorPaint — outside painter. Export maps to Flax.
- QuadriFlow/InstantMeshes — retopo CLI on import.
- glTF-Transform — clean + squeeze before Flax.
- FlaxEngine + Samples + Arizona (MIT frame) — import, anim graph, demo scenes.
- Pirouette3D — browser turntable video for store.
- pfxr / make-sfx — retro SFX WAV packs.
- V1xel/mixamo-mcp — auto Mixamo downloads. Flax eats FBX.

## STEAL (idea only)
- Hunyuan 7-step studio — too heavy. Take pattern.
- LL3M agents write Blender code — take agent shape. Too slow whole.
- Infinigen + Indoors + CityX + Tome — take layout logic. Bake to FBX. Heavy polys.
- Material Maker — take node idea. Add Flax export.
- MeshAnything — take auto-clean idea. Run offline.
- ArtUV — take seam idea. Use Smart UV now.
- UnityBuildUploader — take one-build-many-ships config.
- HumanRig paper — same Mixamo bones = anims just work.
- GaussianMarker paper — hidden watermark for stolen packs.

## Flax-first via all? YES.
- Gen anywhere. End as FBX/GLB. Drop in scratch Content. Import. Snap. Anim graph. Shot. Then export per engine + ship per site.
