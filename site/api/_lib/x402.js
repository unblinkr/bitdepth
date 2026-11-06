// x402 v2 pay per call, ported from paddock.finance (src/lib/paddock/x402.ts)
// without dependencies: the CDP JWT is signed with node:crypto instead of jose.
//
// Flow per paid request: no payment header -> 402 with the challenge.
// Payment header -> local checks (amount, payTo, expiry) -> CDP /verify ->
// CDP /settle -> serve. Settling before serving means a replayed signature
// fails at settle (the EIP-3009 nonce is spent on chain), so no nonce store
// is needed here.
//
// Env: X402_PAYTO (Base wallet that receives USDC), CDP_API_KEY_ID,
// CDP_API_KEY_SECRET (same CDP key Paddock uses is fine).

import { createPrivateKey, randomBytes, sign } from "node:crypto";

export const X402_NETWORK = "eip155:8453";
export const USDC_BASE = "0x833589fCD6eDb6E08f4c7C32D4f71b54bdA02913";
const USDC_EIP712 = { name: "USD Coin", version: "2" };
const CDP = "api.cdp.coinbase.com/platform/v2/x402";
const TIMEOUT_MS = 8000;

export function payTo() {
  return (process.env.X402_PAYTO || "").trim();
}

export function requirements({ priceAtomic, resourceUrl, description }) {
  return {
    scheme: "exact",
    network: X402_NETWORK,
    amount: priceAtomic,
    maxAmountRequired: priceAtomic,
    asset: USDC_BASE,
    payTo: payTo(),
    resource: resourceUrl,
    description,
    mimeType: "application/json",
    maxTimeoutSeconds: 300,
    extra: { ...USDC_EIP712 },
  };
}

export function challenge(opts) {
  return {
    x402Version: 2,
    error: "Payment required",
    accepts: [requirements(opts)],
    resource: { url: opts.resourceUrl, description: opts.description, mimeType: "application/json" },
  };
}

export function challengeHeaders(ch, priceAtomic) {
  return {
    "Payment-Required": Buffer.from(JSON.stringify(ch)).toString("base64"),
    "X-Payment-Required": "true",
    "X-Payment-Amount": priceAtomic,
    "X-Payment-Asset": "USDC",
    "X-Payment-Network": X402_NETWORK,
  };
}

export function receiptFrom(headers) {
  return headers["payment-signature"] || headers["x-payment"] || headers["x-payment-receipt"] || null;
}

const b64url = (buf) => Buffer.from(buf).toString("base64url");

// Mirrors @coinbase/cdp-sdk generateJwt: claims { sub, iss: "cdp", uris: [..] },
// header { alg, kid, typ, nonce }, 120 s life. Ed25519 (64-byte base64) or EC PEM.
export function cdpJwt(keyId, keySecret, uri) {
  const secret = keySecret.replace(/\\n/g, "\n");
  const now = Math.floor(Date.now() / 1000);
  const raw = Buffer.from(secret, "base64");
  const ed = !secret.includes("BEGIN") && raw.length === 64;
  const header = { alg: ed ? "EdDSA" : "ES256", kid: keyId, typ: "JWT", nonce: randomBytes(16).toString("hex") };
  const claims = { sub: keyId, iss: "cdp", uris: [uri], iat: now, nbf: now, exp: now + 120 };
  const input = `${b64url(JSON.stringify(header))}.${b64url(JSON.stringify(claims))}`;
  let sig;
  if (ed) {
    const key = createPrivateKey({
      format: "jwk",
      key: { kty: "OKP", crv: "Ed25519", d: b64url(raw.subarray(0, 32)), x: b64url(raw.subarray(32)) },
    });
    sig = sign(null, Buffer.from(input), key);
  } else {
    sig = sign("sha256", Buffer.from(input), { key: createPrivateKey(secret), dsaEncoding: "ieee-p1363" });
  }
  return `${input}.${b64url(sig)}`;
}

async function cdp(op, paymentPayload, reqs, fetchFn = fetch) {
  const keyId = (process.env.CDP_API_KEY_ID || "").trim();
  const keySecret = (process.env.CDP_API_KEY_SECRET || "").trim();
  if (!keyId || !keySecret) return { ok: false, status: 503, reason: "facilitator_not_configured" };
  const ctrl = new AbortController();
  const timer = setTimeout(() => ctrl.abort(), TIMEOUT_MS);
  try {
    const resp = await fetchFn(`https://${CDP}/${op}`, {
      method: "POST",
      headers: {
        "Content-Type": "application/json",
        Authorization: `Bearer ${cdpJwt(keyId, keySecret, `POST ${CDP}/${op}`)}`,
      },
      body: JSON.stringify({ x402Version: 2, paymentPayload, paymentRequirements: reqs }),
      signal: ctrl.signal,
    });
    if (!resp.ok) return { ok: false, status: 503, reason: `facilitator_${op}_${resp.status}` };
    return { ok: true, body: await resp.json() };
  } catch (err) {
    return { ok: false, status: 503, reason: err?.name === "AbortError" ? `${op}_timeout` : `${op}_unavailable` };
  } finally {
    clearTimeout(timer);
  }
}

// Returns { ok: true, settlement } or { ok: false, status, reason }.
export async function verifyAndSettle(receipt, opts, fetchFn = fetch) {
  let payload;
  try {
    payload = JSON.parse(Buffer.from(String(receipt).trim(), "base64").toString("utf8"));
  } catch {
    return { ok: false, status: 400, reason: "malformed_receipt" };
  }
  const auth = payload?.payload?.authorization;
  if (!auth || typeof auth !== "object") return { ok: false, status: 400, reason: "malformed_receipt" };
  if (String(auth.value) !== opts.priceAtomic) return { ok: false, status: 402, reason: "amount_mismatch" };
  if (String(auth.to || "").toLowerCase() !== payTo().toLowerCase()) return { ok: false, status: 402, reason: "payto_mismatch" };
  const validBefore = parseInt(String(auth.validBefore), 10) * 1000;
  if (!Number.isFinite(validBefore) || Date.now() >= validBefore) return { ok: false, status: 402, reason: "receipt_expired" };

  const reqs = requirements(opts);
  const v = await cdp("verify", payload, reqs, fetchFn);
  if (!v.ok) return v;
  if (!v.body.isValid) return { ok: false, status: 402, reason: String(v.body.invalidReason || "invalid").toLowerCase() };

  const s = await cdp("settle", payload, reqs, fetchFn);
  if (!s.ok) return s;
  if (!s.body.success) return { ok: false, status: 402, reason: String(s.body.errorReason || "settlement_failed").toLowerCase() };
  return {
    ok: true,
    settlement: { success: true, transaction: s.body.transaction || "", network: s.body.network || X402_NETWORK, payer: s.body.payer || null },
  };
}

export function settlementHeaders(settlement) {
  const v = Buffer.from(JSON.stringify(settlement)).toString("base64");
  return { "PAYMENT-RESPONSE": v, "X-Payment-Response": v };
}
