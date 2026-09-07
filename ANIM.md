# ANIM — where anim lives

## Flax here = clip maker
- Makes: text -> bvh/npy/glb via :7863. Retarget 22 -> 65 bones. Montages (startup/active/recovery). State machines (idle/walk/guard/air + 6 strikes).
- Rules: 20 -> 60 fps bake offline once. Guard never skip. Gateway :20128 only. bvh stays donor, never in git.
- Cannot make: skin weights. Hand keys. Custom nodes need editor.

## Blender in new repo = pack maker
- Put Blender lane in new repo. Yes.
- Use sandraschi/blender-mcp (MIT, 41 tools, headless --background). Factory core. Batch mesh, export glb/fbx/obj/usd/vrm, decimate, batch render. No GUI needed.
- Use ahujasid/blender-mcp (MIT, 26k stars, port 9876) for art test only. One asset at a time. Needs open Blender.
- Use elithril/blender-kiln flow (MIT): BRIEF > SOURCE > CLEANUP > TEXTURE > OPTIMIZE > EXPORT. Batch YAML. Keep .blend always.
- Headless cmds: smart_project UV (angle 66, margin 0.02). Decimate 0.5/0.25/0.1 for LOD1/2/3. Cycles DIFFUSE bake. Export GLB Draco + FBX -Z/Y bake_anim.
- Skin lives here. Mixamo flow: Blender apply transforms -> Mixamo T-pose markers -> FBX skin 30fps -> Blender bone fix + NLA bake -> Flax FBX import.

## Rule
- Clips born here (forge). Packs born there (asset-pack-factory).
- New repo pulls clips via gateway, never direct :78xx.
