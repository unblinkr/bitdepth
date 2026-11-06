// Free public JSON. vercel.json rewrites /v1/<path> here as ?path=<path>.
// Serves only index.json, drift.json and or/<author>/<slug>.json.

import { getIndex, getDrift, getModel } from "./_lib/data.js";

export default async function handler(req, res) {
  res.setHeader("Access-Control-Allow-Origin", "*");
  res.setHeader("Content-Type", "application/json; charset=utf-8");
  if (req.method === "OPTIONS") return res.status(204).end();
  const path = String(req.query.path || "").replace(/^\/+/, "");
  try {
    let body = null;
    if (path === "index.json") body = await getIndex();
    else if (path === "drift.json") body = await getDrift();
    else {
      const m = path.match(/^or\/(.+)\.json$/);
      if (m) body = await getModel(m[1]);
    }
    if (!body) return res.status(404).send(JSON.stringify({ error: "not_found", path, index: "https://bitdepth.dev/v1/index.json" }));
    res.setHeader("Cache-Control", "public, max-age=21600");
    return res.status(200).send(JSON.stringify(body));
  } catch (err) {
    return res.status(502).send(JSON.stringify({ error: "upstream_unavailable", detail: String(err.message || err) }));
  }
}
