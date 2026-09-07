# LANES — engines + sites

## Engine lanes (files in -> caps -> LOD)
- unity: FBX in. Props 200-800 tris. Hero 10-50k. Photo 512-1024 prop, 1024-2048 hero. LOD Group LOD0/1/2 at 60/30/10.
- unreal/fab: FBX/GLB in. Nanite = millions ok, keep fallback. Non-Nanite 3-4 LODs. Fab takes GLB + PBR.
- godot 4: GLB best. Principled only. 1 unit = 1 m. LOD0 in file, Godot makes rest.
- flax: FBX best + packet.json. Up to 6 LODs LOD0-5. Merge same-mat meshes.
- secondlife: DAE 1.4.1 only. Max 8 mats. Photo 1024 max. 4 LODs HIGH/MED/LOW/LOWEST + PHYS. Good LI 1-5.
- roblox: FBX/GLB max 50 MB. Rigid = 1 mesh, max 4000 tris, watertight. Photo 1024. No manual LOD.
- minecraft: .mcpack zip. Blockbench JSON. Blocky 30px max. Photo 16x. No LODs, use culling JSON.
- fivem: FBX -> Sollumz -> ydr/yft/ytyp/ytd. Props few k-20k. DDS + mips. LOD hi/med/low/vlow in ytyp.

## Site lanes (fee -> price sweet -> AI tag -> ship)
- fab: keep 88%. $14.99-19.99 sweet. Tag CreatedWithAI. Portal web. 3-10 day check.
- unity: keep 70%. $10-30 sweet, floor $4.99. AI note field. Portal. 2-4 wk check (often 50-60 days).
- sl-market: fee 10%. L$199 sweet (~$0.80). Mod/Copy + low LI. Write AI use in text. Instant list.
- roblox: 80 Robux upload + 1500 hat advance. Sweet 75-150. AI allowed if owned. Auto+human check, mins-hours.
- itch: fee you pick 0-100% (base 10%) + pay fee. $3-10 small. AI Disclosure must. `butler push`. Instant.
- patreon/kofi: Patreon 10% new + pay fee. Ko-fi 0% tips, 5% fans. $5 entry. Tag ai-assisted. Instant.
- stock (cgtrader/etsy): CG 60-85% keep. Etsy ~10% + list $0.20. $10-30 single. CG flag AI. Etsy note AI. TurboSquid = NO AI, skip for AI packs.
- minecraft partner: keep 70%. $2.99-7.99. Must own IP. Weeks-months to join.
- uefn: pool 40% by play (~$67 per 1M mins). Items keep 100% to Jan 2027. AI chat form. Days check.

## Gen lanes (arxiv ids)
- gen: 2501.12202 Hunyuan3D 2.0 hero, 2412.01506 TRELLIS bulk, 2403.02151 TripoSR fast draft.
- clean: 2408.00653 SF3D de-light + UV base, 2404.07191 InstantMesh watertight base.
- pbr: StableMaterials text-to-maps (basecolor/normal/rough/metal).
- retopo: MeshAnything dense-to-quad low.
- uv: 2509.20710 ArtUV clean islands.
- sfx: 2407.14358 Stable Audio Open 44.1k WAV, -14 LUFS long, -1 dB short.
- vfx: CogVideoX 2408.06072 text-to-video -> 8x8 flipbook PNG 2048 (256 per cell), hero cap 2000 particles.
