# FLOW-100X — merged smart workflow (6GB + Colab + Kaggle)

Rule: draft 100 free. Hero 10 only. Bake local. Ship last.

## Spend truth
- Kaggle 30h/week = 1800 min. Left 257. Used ~1543 (~128 jobs at ~12 min each). Daily-3d chain + tests ate it. Reset Monday.
- Colab-1 720 + Colab-2 720 = untouched. Use Colab first now.
- Local: RTX 3050 6GB, 5.5GB free. Good for draft + bake + render. Bad for big gen.

## DRAFT — local RTX, free
- Tool: fast image (LCM 10x) -> TripoSR 0.5s / SF3D 0.5s + UV.
- VRAM 4-5GB. 20-40s each. 100 drafts ~60 min. $0.
- Out: low GLB ~20k tris. No PBR. Throw 90% away.

## HERO — cloud, only best 10
- First: Hunyuan Turbo on Colab-1 T4. 2-4 min each. 10 heroes ~40 min. Keep Colab-2 full as backup.
- Backup: Kaggle lane only if Colab busy. 1 hero ~25 min. Keep Kaggle over 200.
- Night: Hunyuan2GP fp16 local (5.5GB fit). 8-12 min each. Sleep when cloud free.
- Hard shapes: TRELLIS only when draft mesh broken. Skip else.
- FlashVDM 32x for turn views. LCM 10x steps cut.

## BAKE — local RTX (quality lives here)
- Tool: Blender Cycles OptiX ON + PBR bake (color/normal/rough).
- 2k maps. 5-10 min each. Preview 1080p 30-60s at 128 samples.
- Clean UV, no overlap, watertight. This makes Fab look real. Never bake in draft.

## SHIP — last
- gltfpack -80% size + LODs x3 + 7 gates. 30s each. Never before bake.

## RTX for render? Yes.
- Gen: small (draft + bake). Render: big (Cycles previews, turntables, store video). RTX OptiX cuts render 3-5x.
- Math: old 50 min/hand -> new ~30s mean. ~100x combined, never one model.
