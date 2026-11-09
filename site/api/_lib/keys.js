// Watch keys. A key is the Stripe subscription id, signed:
//   bdw_<base64url(sub_id)>_<first 32 hex of HMAC-SHA256(WATCH_KEY_SECRET, sub_id)>
// probe/watch.py mints the same key for the welcome email, so nothing is stored.
// A key works while its subscription is active in Stripe; cancelling ends it.
//
// Env (Vercel): WATCH_KEY_SECRET (same value as the GitHub secret),
// STRIPE_CHECKOUT_KEY (restricted key; needs Subscriptions: Read for this check).

import { createHmac, timingSafeEqual } from "node:crypto";

const TTL_MS = 10 * 60 * 1000;
const cache = new Map();

const sign = (secret, subId) => createHmac("sha256", secret).update(subId).digest("hex").slice(0, 32);

export function mintKey(subId, secret = process.env.WATCH_KEY_SECRET || "") {
  return `bdw_${Buffer.from(subId).toString("base64url")}_${sign(secret, subId)}`;
}

export function subFromKey(key, secret = process.env.WATCH_KEY_SECRET || "") {
  const m = /^bdw_([A-Za-z0-9_-]+)_([0-9a-f]{32})$/.exec(String(key || "").trim());
  if (!m || !secret) return null;
  const subId = Buffer.from(m[1], "base64url").toString("utf8");
  if (!/^sub_[A-Za-z0-9]+$/.test(subId)) return null;
  const want = Buffer.from(sign(secret, subId));
  const got = Buffer.from(m[2]);
  return want.length === got.length && timingSafeEqual(want, got) ? subId : null;
}

export function keyFrom(req) {
  const h = req.headers || {};
  return h["x-bitdepth-key"] || (req.query && req.query.key) || null;
}

// Returns {ok: true, subId} or {ok: false, status, error}.
export async function checkKey(req, fetchFn = fetch) {
  const key = keyFrom(req);
  if (!key) return { ok: false, status: 401, error: "key_required" };
  const subId = subFromKey(key);
  if (!subId) return { ok: false, status: 401, error: "invalid_key" };
  const hit = cache.get(subId);
  if (hit && Date.now() - hit.at < TTL_MS) return hit.value;
  const stripeKey = (process.env.STRIPE_CHECKOUT_KEY || "").trim();
  if (!stripeKey) return { ok: false, status: 503, error: "keys_not_configured" };
  const r = await fetchFn(`https://api.stripe.com/v1/subscriptions/${subId}`, {
    headers: { Authorization: `Bearer ${stripeKey}` },
  }).catch(() => null);
  if (!r) return { ok: false, status: 502, error: "stripe_unavailable" };
  if (r.status === 404) return remember(subId, { ok: false, status: 401, error: "subscription_not_found" });
  if (!r.ok) return { ok: false, status: 502, error: "stripe_error" };
  const sub = await r.json().catch(() => ({}));
  const active = sub.status === "active" || sub.status === "trialing" || sub.status === "past_due";
  return remember(subId, active ? { ok: true, subId } : { ok: false, status: 403, error: "subscription_inactive" });
}

function remember(subId, value) {
  cache.set(subId, { at: Date.now(), value });
  return value;
}
