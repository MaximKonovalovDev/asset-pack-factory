# FLAX — project + MCP access for new repo

## Answer: yes, new repo gets Flax access. But thin, not full.
- New repo has NO Flax project inside. Keeps slim.
- It talks to forge scratch project: `C:/forge-scratch/scratch-game`.
- It uses forge sidecar server: `C:/forge/sidecars/flax-live-mcp/server.mjs`.
- Config in opencode.jsonc: `flax-live` MCP, OFF by default. Turn ON only for import test + anim check + preview render.

## When ON
- Import test: drop FBX/GLB into scratch Content, check no red errors.
- Anim check: load bvh/fbx clip, retarget 22->65 guard must pass.
- Preview: screenshot viewport for store cover.
- Same 16 verbs as forge. Editor down = honest refuse, never fake.

## When OFF (normal)
- Build packs with gateway + Blender only. No editor needed.
- Ship never needs Flax. Stores take FBX/GLB/DAE direct.

## Rule
- Clips born in forge. Packs tested in scratch. Stores fed from new repo.
- Never copy scratch Content into new repo. Test files stay scratch.
