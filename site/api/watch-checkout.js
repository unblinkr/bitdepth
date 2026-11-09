// Watch checkout: the bitdepth.dev/watch picker posts the endpoints a buyer ticked.
// POST /api/watch/checkout  {"endpoints": ["<author/slug>:<tag>", ...], "test": "<code>"}
// Every endpoint is checked against the live public files before Stripe is called,
// so nobody can subscribe to a name we do not grade. Returns {"url": <Stripe Checkout>}.
//
// Env (Vercel): STRIPE_CHECKOUT_KEY (restricted: Checkout Sessions write),
// WATCH_PRICE_ID (the $5 per endpoint price). Optional: WATCH_TEST_PRICE_ID and
// WATCH_TEST_CODE, so the founder can buy at the internal test price with ?test=<code>.

import { getEndpoint, isModelId } from "./_lib/data.js";

const MIN = 3;
const MAX = 200;
const STRIPE = "https://api.stripe.com/v1/checkout/sessions";
const SITE = "https://bitdepth.dev";

function send(res, status, body) {
  res.setHeader("Content-Type", "application/json; charset=utf-8");
  res.setHeader("Cache-Control", "no-store");
  return res.status(status).send(JSON.stringify(body));
}

export function parseSpec(spec) {
  const s = String(spec || "").trim();
  const i = s.indexOf(":");
  if (i < 1) return null;
  const model = s.slice(0, i);
  const tag = s.slice(i + 1);
  if (!isModelId(model) || !/^[a-z0-9][a-z0-9._/-]*$/i.test(tag) || tag.includes("..")) return null;
  return { model, tag, spec: `${model}:${tag}` };
}

// Stripe metadata values hold 500 characters; spread the list over endpoints_0..n.
export function chunk(specs, size = 480) {
  const out = [];
  let cur = "";
  for (const s of specs) {
    const next = cur ? `${cur},${s}` : s;
    if (next.length > size && cur) {
      out.push(cur);
      cur = s;
    } else cur = next;
  }
  if (cur) out.push(cur);
  return out;
}

export default async function handler(req, res, deps = {}) {
  if (req.method !== "POST") return send(res, 405, { error: "method_not_allowed" });
  const key = (process.env.STRIPE_CHECKOUT_KEY || "").trim();
  if (!key) return send(res, 503, { error: "checkout_not_configured" });

  let body = req.body;
  if (typeof body === "string") {
    try { body = JSON.parse(body); } catch { body = {}; }
  }
  const raw = Array.isArray(body?.endpoints) ? body.endpoints : [];
  const parsed = [...new Map(raw.map(parseSpec).filter(Boolean).map((p) => [p.spec, p])).values()];
  if (parsed.length < MIN) return send(res, 400, { error: "too_few", min: MIN });
  if (parsed.length > MAX) return send(res, 400, { error: "too_many", max: MAX });

  const unknown = [];
  for (const p of parsed) {
    const { row } = await getEndpoint(p.model, p.tag).catch(() => ({ row: undefined }));
    if (row === undefined) return send(res, 502, { error: "upstream_unavailable" });
    if (!row) unknown.push(p.spec);
  }
  if (unknown.length) return send(res, 400, { error: "unknown_endpoints", unknown });

  const testCode = (process.env.WATCH_TEST_CODE || "").trim();
  const isTest = Boolean(testCode && body?.test && String(body.test) === testCode && process.env.WATCH_TEST_PRICE_ID);
  const price = (isTest ? process.env.WATCH_TEST_PRICE_ID : process.env.WATCH_PRICE_ID || "").trim();
  if (!price) return send(res, 503, { error: "price_not_configured" });

  const form = new URLSearchParams();
  form.set("mode", "subscription");
  form.set("line_items[0][price]", price);
  form.set("line_items[0][quantity]", String(parsed.length));
  form.set("success_url", `${SITE}/watch/thanks`);
  form.set("cancel_url", `${SITE}/watch`);
  form.set("metadata[bitdepth_watch]", "1");
  form.set("subscription_data[metadata][bitdepth_watch]", "1");
  if (isTest) form.set("metadata[test]", "1");
  chunk(parsed.map((p) => p.spec)).forEach((c, i) => {
    form.set(`metadata[endpoints_${i}]`, c);
    form.set(`subscription_data[metadata][endpoints_${i}]`, c);
  });

  const fetchFn = deps.fetch || fetch;
  const r = await fetchFn(STRIPE, {
    method: "POST",
    headers: { Authorization: `Bearer ${key}`, "Content-Type": "application/x-www-form-urlencoded" },
    body: form.toString(),
  }).catch(() => null);
  if (!r) return send(res, 502, { error: "stripe_unavailable" });
  const j = await r.json().catch(() => ({}));
  if (!r.ok || !j.url) return send(res, 502, { error: "stripe_error", detail: String(j?.error?.message || r.status).slice(0, 200) });
  return send(res, 200, { url: j.url, endpoints: parsed.length, test: isTest });
}
