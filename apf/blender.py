"""blender lane: headless batch. sandraschi MCP shape, kiln flow."""
# smart UV: angle 66, margin 0.02
# LOD decimate: 0.5 / 0.25 / 0.1
# bake: CYCLES DIFFUSE
# export: GLB Draco + FBX -Z/Y bake_anim
# cmd: blender --background --python batch.py -- ./in ./out
HEADLESS = "blender --background --python batch.py"
