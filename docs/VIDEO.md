# VIDEO — pack previews + AI video

## Skip After Effects MCP
- Real but weak. Fan hubs only (Dakkshin, HeroicSwan, Fansist 24 tools, davidcasan 70+). Needs AE open. No headless. One crash kills queue.
- No AE lane in new repo. Agent writes .jsx only if buyer pays custom job.

## Use FFmpeg lane (core)
- Turntable: `ffmpeg -framerate 30 -i frame_%04d.png -c:v libx264 -crf 18 -pix_fmt yuv420p -movflags +faststart turntable.mp4`
- Join hero + turntable via list.txt concat -c copy.
- Store fix: scale 1920x1080 even, crf 20, +faststart. Fab <100MB. Unity <10MB. Sketchfab <50MB H264.
- Render PNG frames first (Blender Cycles or UE5 Movie Queue, 300 frames, 30fps, 10s, 360 deg, no blur). Never render mp4 direct.

## Resolve only for batch
- samuelgursky/davinci-resolve-mcp (1240 stars, 34 easy / 341 full tools). Needs Studio $295 + open Resolve + Python 3.10-12.
- Use when 10+ packs. One script loops render queue. Else FFmpeg alone wins.

## AI video (CogVideoX) = mood only
- Open, 5B needs 5-26GB. 10s 1360x768 16fps. 45-180s per clip on A100.
- Good for smoke/fire idea plates. Bad for hero: soft, warps hands, no alpha, no 360. Buyers want true shape. Never use for pack hero.
