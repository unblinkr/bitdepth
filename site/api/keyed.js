// Watch-key tools. GET /api/v1/changes and /api/v1/spread (vercel.json rewrites
// both here with ?tool=). A valid X-Bitdepth-Key (or ?key=) is required.
//
// changes: what moved between a night you name and the latest night, for one
//   model or all: endpoints added or removed, declared precision changed, output
//   price moved, grade state now, and exact match then and now.
// spread: for one model, the price range among endpoints that match the reference,
//   cheapest first, and the same within each declared precision.

import { checkKey } from "./_lib/keys.js";
import { FOOTER, METHOD_URL, getIndex, getModel, getRunEndpoints, isDate, isModelId } from "./_lib/data.js";

function send(res, status, body) {
  res.setHeader("Content-Type", "application/json; charset=utf-8");
  res.setHeader("Access-Control-Allow-Origin", "*");
  res.setHeader("Cache-Control", "no-store");
  return res.status(status).send(JSON.stringify(body));
}

const slugOf = (model) => model.split("/")[1];
const round = (n, d = 4) => (n == null ? null : Math.round(n * 10 ** d) / 10 ** d);
const perM = (p) => (p == null ? null : round(p * 1e6));

function listing(run, model) {
  const m = run?.models?.[slugOf(model)] || Object.values(run?.models || {}).find((x) => x.slug === model);
  const out = new Map();
  for (const e of m?.endpoints || []) out.set(e.tag, { quant: e.quantization ?? null, price_out_per_m: perM(e.price_out) });
  return out;
}

export async function changes(model, since) {
  const idx = await getIndex();
  const models = model ? [model] : (idx?.models || []).map((m) => m.model);
  const latest = idx?.as_of;
  const [then, now] = await Promise.all([getRunEndpoints(since), getRunEndpoints(latest)]);
  if (!then) return { status: 404, body: { error: "no_run_for_date", since, first_night: idx?.first_night } };
  const out = [];
  for (const mid of models) {
    const doc = await getModel(mid).catch(() => null);
    const a = listing(then, mid);
    const b = listing(now, mid);
    if (!a.size && !b.size) continue;
    const rows = new Map((doc?.endpoints || []).map((e) => [e.tag, e]));
    const items = [];
    for (const [tag, v] of b) {
      const r = rows.get(tag);
      const was = a.get(tag);
      const item = { tag, state_now: r?.state ?? null, exact_then: (r?.nightly_exact || []).find((n) => n.date === since)?.exact ?? null, exact_now: r?.exact ?? null };
      if (!was) items.push({ ...item, change: "added", quant: v.quant, price_out_per_m: v.price_out_per_m });
      else {
        const diffs = {};
        if (was.quant !== v.quant) diffs.declared_quant = { then: was.quant, now: v.quant };
        if (was.price_out_per_m != null && v.price_out_per_m != null && Math.abs(v.price_out_per_m - was.price_out_per_m) > 0.01 * was.price_out_per_m)
          diffs.price_out_per_m = { then: was.price_out_per_m, now: v.price_out_per_m };
        if (Object.keys(diffs).length) items.push({ ...item, change: "changed", ...diffs });
      }
    }
    for (const [tag, v] of a) if (!b.has(tag)) items.push({ tag, change: "removed", quant: v.quant, price_out_per_m: v.price_out_per_m });
    out.push({ model: mid, changes: items });
  }
  return { status: 200, body: { schema: "bitdepth.changes.v1", since, as_of: latest, models: out, method_url: METHOD_URL, footer: FOOTER } };
}

export async function spread(model) {
  const doc = await getModel(model);
  if (!doc) return { status: 404, body: { error: "not_found", model } };
  const priced = doc.endpoints.filter((e) => e.price_out_per_m != null);
  const within = priced.filter((e) => e.state === "within").sort((x, y) => x.price_out_per_m - y.price_out_per_m);
  const band = (list) => (list.length ? {
    count: list.length,
    cheapest: { tag: list[0].tag, price_out_per_m: list[0].price_out_per_m },
    priciest: { tag: list[list.length - 1].tag, price_out_per_m: list[list.length - 1].price_out_per_m },
    ratio: list[0].price_out_per_m > 0 ? round(list[list.length - 1].price_out_per_m / list[0].price_out_per_m, 2) : null,
  } : null);
  const byQuant = {};
  for (const e of within) (byQuant[e.declared_quant || "unknown"] ||= []).push(e);
  return { status: 200, body: {
    schema: "bitdepth.spread.v1",
    model,
    as_of: doc.as_of,
    rule: "endpoints whose state is within (match the reference), by output price per million tokens",
    matching_reference: band(within),
    by_declared_precision: Object.fromEntries(Object.entries(byQuant).map(([q, l]) => [q, band(l)])),
    all_priced: band([...priced].sort((x, y) => x.price_out_per_m - y.price_out_per_m)),
    endpoints: within.map((e) => ({ tag: e.tag, declared_quant: e.declared_quant, price_out_per_m: e.price_out_per_m, exact: e.exact })),
    method_url: METHOD_URL,
    footer: FOOTER,
  } };
}

export default async function handler(req, res, deps = {}) {
  if (req.method === "OPTIONS") {
    res.setHeader("Access-Control-Allow-Origin", "*");
    res.setHeader("Access-Control-Allow-Headers", "X-Bitdepth-Key, Content-Type");
    return res.status(204).end();
  }
  if (req.method !== "GET") return send(res, 405, { error: "method_not_allowed" });
  const k = await checkKey(req, deps.fetch);
  if (!k.ok) return send(res, k.status, { error: k.error, help: "Keys come with Bitdepth Watch: https://bitdepth.dev/watch" });

  const tool = String(req.query.tool || "");
  const model = req.query.model ? String(req.query.model) : "";
  if (model && !isModelId(model)) return send(res, 400, { error: "bad_model" });
  try {
    if (tool === "changes") {
      const since = String(req.query.since || "");
      if (!isDate(since)) return send(res, 400, { error: "bad_since", usage: "/api/v1/changes?since=2026-10-27&model=deepseek/deepseek-v4-pro" });
      const r = await changes(model, since);
      return send(res, r.status, r.body);
    }
    if (tool === "spread") {
      if (!model) return send(res, 400, { error: "model_required", usage: "/api/v1/spread?model=deepseek/deepseek-v4-pro" });
      const r = await spread(model);
      return send(res, r.status, r.body);
    }
  } catch {
    return send(res, 502, { error: "upstream_unavailable" });
  }
  return send(res, 404, { error: "unknown_tool" });
}
