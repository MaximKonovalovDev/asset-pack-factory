---
description: orchestrator — primary, holds plan
mode: primary
model: opencode-go/muse-spark-1.3-contributor
temperature: 0.2
steps: 500
permission:
  edit: allow
---

# orchestrator
Owns plan/, state/. One wave per run. Batch subs in parallel by dir.
