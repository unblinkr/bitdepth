#!/usr/bin/env bash
# Publish the leaderboard with real grades. Run once, after Mancy approves the fourteen-night read.
#   1. moves the hand-written home page to /compare
#   2. writes the leaderboard as the home page, /m/<model>, /charts, share cards, badges, /data/v1
#   3. removes the placeholder preview at /lab
#   4. creates site/.live so the nightly run rebuilds the pages from then on
# It does not commit or push; review the diff, then commit and push main to deploy.
set -euo pipefail
cd "$(dirname "$0")/.."
python -m probe.emit
python -m probe.site --live
rm -rf site/lab
touch site/.live
python3 - <<'PY'
import json
p = "site/vercel.json"
d = json.load(open(p))
d["headers"] = [h for h in d.get("headers", []) if not h["source"].startswith("/lab")]
d.setdefault("redirects", []).append({"source": "/lab/:path*", "destination": "/:path*", "permanent": False})
json.dump(d, open(p, "w"), indent=2)
open(p, "a").write("\n")
PY
git status --short site | head -40
echo "Review, then: git add site && git commit -m 'Publish the leaderboard' && git push origin main"
