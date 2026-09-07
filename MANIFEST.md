# MANIFEST — ship papers (`manifest.json` + `provenance.json`)

Two files per pack. Manifest says what you sell. Provenance proves it is yours.

## manifest.json

One per shop lane (fab, unity, itchio, gumroad). Zip dir + zip file share the name.

| Field | From | Note |
|---|---|---|
| pack_id | brief.id | e.g. `001-fantasy-props` |
| title | brief.title | shop headline |
| pieces | brief.pieces count | 30 for pack #1 |
| exports | brief.exports | unity, unreal, godot, master_glb |
| target | fab / unity / itchio / gumroad | one file per target |
| files_included | count at zip time | must be > 0 |
| size_bytes | sum at zip time | must be > 0 |
| pricing | brief.pricing | launch + normal + window days |
| ai_disclosure | brief.ai_disclosure | models + review line |
| bundle_path | zip path | what the seller uploads |
| description | per-target text | Unity text must name AI models (shop rule) |

Each bundle dir holds: `README.md`, `license.txt`, `ai_disclosure.txt`, `assets/<engine>/`, `previews/`, `<target>_description.md`.

## provenance.json (11 fields)

One line per work step. Saved to `receipts.ndjson`. Proves source if a shop asks.

| # | Field | Means |
|---|---|---|
| 1 | id | sole receipt id |
| 2 | pack_id | which pack |
| 3 | phase | step: brief_parsed, generation, retopo, uvunwrap, materials, style_review, lod, snap_grid, export, previews, manifest |
| 4 | piece_id | which piece, or null for pack-wide |
| 5 | tool | which tool ran (route or CLI name) |
| 6 | intent | what we tried, short |
| 7 | outcome | success / failed / skipped / pending |
| 8 | cost_usd | real spend for this step |
| 9 | error_code | short code, or null |
| 10 | ts | time (UTC) |
| 11 | metadata | small extra map (sha256, license, seed) |

Rules: SHA-256 (fingerprint code) per piece. License tag per piece. No ship if any step is `failed` with no fix note.
