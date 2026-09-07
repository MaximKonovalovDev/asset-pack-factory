"""video lane: FFmpeg previews. No AE."""
# turntable: ffmpeg -framerate 30 -i frame_%04d.png -c:v libx264 -crf 18 -pix_fmt yuv420p -movflags +faststart turntable.mp4
# join: concat list.txt -c copy pack_preview.mp4
# store fix: scale 1920x1080 even, crf 20, +faststart. Fab <100MB. Unity <10MB.
