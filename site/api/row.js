// Pay per call: one endpoint's full row with trend detail.
// GET /api/v1/row?model=<author/slug>&endpoint=<tag>
// 0.10 USDC over x402 on Base. No account, no key.

import { getEndpoint, getFullRow, isModelId } from "./_lib/data.js";
import { challenge, challengeHeaders, payTo, receiptFrom, settlementHeaders, verifyAndSettle } from "./_lib/x402.js";

export const PRICE_ATOMIC = "100000"; // 0.10 USDC (6 decimals)
const DESCRIPTION = "Bitdepth: one inference endpoint's full nightly row (per-night exact, per-family self-agreement with pair counts, self-check nights) against the published reference.";

function send(res, status, body, headers = {}) {
  for (const [k, v] of Object.entries(headers)) res.setHeader(k, v);
  res.setHeader("Content-Type", "application/json; charset=utf-8");
  return res.status(status).send(JSON.stringify(body));
}

export default async function handler(req, res, deps = {}) {
  res.setHeader("Access-Control-Allow-Origin", "*");
  res.setHeader("Access-Control-Expose-Headers", "Payment-Required, PAYMENT-RESPONSE, X-Payment-Response");
  if (req.method === "OPTIONS") {
    res.setHeader("Access-Control-Allow-Headers", "PAYMENT-SIGNATURE, X-PAYMENT, Content-Type");
    return res.status(204).end();
  }
  if (req.method !== "GET" && req.method !== "HEAD") return send(res, 405, { error: "method_not_allowed" });

  const model = String(req.query.model || "");
  const tag = String(req.query.endpoint || "");
  if (!isModelId(model) || !tag) {
    return send(res, 400, { error: "bad_request", usage: "/api/v1/row?model=deepseek/deepseek-v4-pro&endpoint=<tag from /v1/or/<model>.json>" });
  }
  if (!payTo()) return send(res, 503, { error: "payments_not_configured", detail: "X402_PAYTO is not set." });

  const { row } = await getEndpoint(model, tag).catch(() => ({ row: undefined }));
  if (row === undefined) return send(res, 502, { error: "upstream_unavailable" });
  if (!row) return send(res, 404, { error: "not_found", model, endpoint: tag });

  const host = req.headers["x-forwarded-host"] || req.headers.host || "bitdepth.dev";
  const resourceUrl = `https://${host}/api/v1/row?model=${encodeURIComponent(model)}&endpoint=${encodeURIComponent(tag)}`;
  const opts = { priceAtomic: PRICE_ATOMIC, resourceUrl, description: DESCRIPTION };
  const ch = challenge(opts);

  const receipt = receiptFrom(req.headers);
  if (!receipt) return send(res, 402, ch, challengeHeaders(ch, PRICE_ATOMIC));

  // Build the row before taking money, so a data fetch can never fail after settlement.
  const full = await getFullRow(model, tag).catch(() => null);
  if (!full) return send(res, 502, { error: "upstream_unavailable" });

  const result = await verifyAndSettle(receipt, opts, deps.fetch);
  if (!result.ok) {
    const status = result.status;
    return send(res, status, { ...ch, status: "payment_failed", reason: result.reason }, status === 402 ? challengeHeaders(ch, PRICE_ATOMIC) : {});
  }
  return send(res, 200, full, { ...settlementHeaders(result.settlement), "Cache-Control": "no-store" });
}
