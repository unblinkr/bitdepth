// Run: node --test tests/site_api.test.mjs
// Free routes and MCP read the live public files on main. x402 uses a
// stubbed facilitator, so no money moves.

import { test } from "node:test";
import assert from "node:assert/strict";
import { generateKeyPairSync, verify } from "node:crypto";

import publicHandler from "../site/api/public.js";
import mcpHandler from "../site/api/mcp.js";
import rowHandler, { PRICE_ATOMIC } from "../site/api/row.js";
import { cdpJwt } from "../site/api/_lib/x402.js";

function mockRes() {
  const r = { statusCode: 200, headers: {}, body: undefined };
  r.setHeader = (k, v) => { r.headers[k.toLowerCase()] = v; };
  r.status = (c) => { r.statusCode = c; return r; };
  r.send = (b) => { r.body = b; return r; };
  r.json = (b) => { r.body = JSON.stringify(b); return r; };
  r.end = () => r;
  r.parsed = () => JSON.parse(r.body);
  return r;
}
const req = (o) => ({ method: "GET", query: {}, headers: { host: "bitdepth.dev" }, ...o });
const rpc = async (method, params, id = 1) => {
  const res = mockRes();
  await mcpHandler(req({ method: "POST", body: { jsonrpc: "2.0", id, method, params } }), res);
  return res;
};

const PAYTO = "0x000000000000000000000000000000000000dEaD";

test("public: index, model, drift, and nothing else", async () => {
  let res = mockRes();
  await publicHandler(req({ query: { path: "index.json" } }), res);
  assert.equal(res.statusCode, 200);
  assert.equal(res.headers["access-control-allow-origin"], "*");
  const idx = res.parsed();
  assert.equal(idx.schema, "bitdepth.or.v1");
  assert.ok(idx.models.length >= 2);

  res = mockRes();
  await publicHandler(req({ query: { path: "or/deepseek/deepseek-v4-pro.json" } }), res);
  assert.equal(res.statusCode, 200);
  assert.ok(res.parsed().endpoints.length > 0);

  res = mockRes();
  await publicHandler(req({ query: { path: "drift.json" } }), res);
  assert.equal(res.statusCode, 200);

  for (const p of ["../runs/2026-11-03/run.json", "or/../../trend/latest.json", "or/nope/nope.json", "secrets.json"]) {
    res = mockRes();
    await publicHandler(req({ query: { path: p } }), res);
    assert.equal(res.statusCode, 404, p);
  }
});

test("mcp: initialize, tools/list, every tool, errors", async () => {
  let res = await rpc("initialize", { protocolVersion: "2025-06-18", capabilities: {}, clientInfo: { name: "t", version: "0" } });
  assert.equal(res.parsed().result.protocolVersion, "2025-06-18");
  assert.equal(res.parsed().result.serverInfo.name, "bitdepth");

  const note = mockRes();
  await mcpHandler(req({ method: "POST", body: { jsonrpc: "2.0", method: "notifications/initialized" } }), note);
  assert.equal(note.statusCode, 202);

  res = await rpc("tools/list");
  assert.deepEqual(res.parsed().result.tools.map((t) => t.name), ["list_models", "get_scorecard", "get_endpoint", "get_drift", "get_market_summary", "get_best_value_endpoint", "check_before_route", "check_declared", "get_changes"]);

  res = await rpc("tools/call", { name: "list_models", arguments: {} });
  const models = res.parsed().result.structuredContent.models;
  assert.ok(models.find((m) => m.model === "deepseek/deepseek-v4-pro"));

  res = await rpc("tools/call", { name: "get_scorecard", arguments: { model: "deepseek/deepseek-v4-pro" } });
  const sc = res.parsed().result.structuredContent;
  assert.equal(sc.footer, "Numbers against a stated reference. Not a claim about intent.");
  assert.ok(sc.method_url && sc.as_of);
  const key = sc.primary_columns[0];
  for (let i = 1; i < sc.endpoints.length; i++) assert.ok((sc.endpoints[i - 1][key] ?? -1) >= (sc.endpoints[i][key] ?? -1));

  const tag = sc.endpoints[0].tag;
  res = await rpc("tools/call", { name: "get_endpoint", arguments: { model: "deepseek/deepseek-v4-pro", endpoint: tag } });
  assert.equal(res.parsed().result.structuredContent.row.tag, tag);

  res = await rpc("tools/call", { name: "get_drift", arguments: {} });
  assert.ok(Array.isArray(res.parsed().result.structuredContent.items));

  res = await rpc("tools/call", { name: "get_market_summary", arguments: {} });
  const ms = res.parsed().result.structuredContent.models;
  assert.ok(ms.length >= 2 && ms.every((m) => m.endpoints === m.within + m.outside + m.no_data + m.stale));

  res = await rpc("tools/call", { name: "get_best_value_endpoint", arguments: { model: "deepseek/deepseek-v4-pro" } });
  const bv = res.parsed().result.structuredContent.endpoints;
  for (let i = 1; i < bv.length; i++) assert.ok(bv[i - 1].blended_price_per_m <= bv[i].blended_price_per_m);

  res = await rpc("tools/call", { name: "check_before_route", arguments: { model: "deepseek/deepseek-v4-pro", endpoint: tag } });
  const cr = res.parsed().result.structuredContent;
  assert.ok([true, false, "inconclusive"].includes(cr.route) && cr.reason);

  res = await rpc("tools/call", { name: "check_declared", arguments: { model: "deepseek/deepseek-v4-pro", endpoint: tag } });
  assert.equal(typeof res.parsed().result.structuredContent.declared_changed, "boolean");

  res = await rpc("tools/call", { name: "check_before_route", arguments: { model: "deepseek/deepseek-v4-pro", endpoint: "nope/x" } });
  assert.equal(res.parsed().result.isError, true);

  res = await rpc("tools/call", { name: "get_changes", arguments: {} });
  assert.ok(Array.isArray(res.parsed().result.structuredContent.changes));

  res = await rpc("tools/call", { name: "get_scorecard", arguments: { model: "nope/nope" } });
  assert.equal(res.parsed().result.isError, true);

  res = await rpc("tools/call", { name: "no_such_tool", arguments: {} });
  assert.equal(res.parsed().error.code, -32602);

  res = await rpc("bogus/method");
  assert.equal(res.parsed().error.code, -32601);

  const get = mockRes();
  await mcpHandler(req({ method: "GET" }), get);
  assert.equal(get.statusCode, 405);
});

test("row: 503 without payTo, 400, 404, then 402 challenge", async () => {
  delete process.env.X402_PAYTO;
  let res = mockRes();
  await rowHandler(req({ query: { model: "deepseek/deepseek-v4-pro", endpoint: "x" } }), res);
  assert.equal(res.statusCode, 503);

  process.env.X402_PAYTO = PAYTO;
  res = mockRes();
  await rowHandler(req({ query: {} }), res);
  assert.equal(res.statusCode, 400);

  res = mockRes();
  await rowHandler(req({ query: { model: "deepseek/deepseek-v4-pro", endpoint: "no/such" } }), res);
  assert.equal(res.statusCode, 404);

  const idx = mockRes();
  await publicHandler(req({ query: { path: "or/deepseek/deepseek-v4-pro.json" } }), idx);
  const tag = idx.parsed().endpoints[0].tag;

  res = mockRes();
  await rowHandler(req({ query: { model: "deepseek/deepseek-v4-pro", endpoint: tag } }), res);
  assert.equal(res.statusCode, 402);
  const ch = JSON.parse(Buffer.from(res.headers["payment-required"], "base64").toString());
  assert.equal(ch.x402Version, 2);
  assert.equal(ch.accepts[0].amount, "100000");
  assert.equal(ch.accepts[0].payTo, PAYTO);
  assert.equal(ch.accepts[0].network, "eip155:8453");
});

test("row: paid flow with stubbed facilitator serves the full row", async () => {
  process.env.X402_PAYTO = PAYTO;
  const { privateKey, publicKey } = generateKeyPairSync("ed25519");
  const jwk = privateKey.export({ format: "jwk" });
  process.env.CDP_API_KEY_ID = "test-key";
  process.env.CDP_API_KEY_SECRET = Buffer.concat([Buffer.from(jwk.d, "base64url"), Buffer.from(jwk.x, "base64url")]).toString("base64");

  // JWT signature checks out against the public key.
  const jwt = cdpJwt("test-key", process.env.CDP_API_KEY_SECRET, "POST api.cdp.coinbase.com/platform/v2/x402/verify");
  const [h, c, s] = jwt.split(".");
  assert.ok(verify(null, Buffer.from(`${h}.${c}`), publicKey, Buffer.from(s, "base64url")));
  assert.deepEqual(JSON.parse(Buffer.from(c, "base64url")).uris, ["POST api.cdp.coinbase.com/platform/v2/x402/verify"]);

  const idx = mockRes();
  await publicHandler(req({ query: { path: "or/deepseek/deepseek-v4-pro.json" } }), idx);
  const tag = idx.parsed().endpoints[0].tag;

  const pay = (value, to) => Buffer.from(JSON.stringify({
    x402Version: 2,
    payload: { signature: "0xsig", authorization: { from: "0xabc", to, value, validAfter: "0", validBefore: String(Math.floor(Date.now() / 1000) + 300), nonce: "0x01" } },
  })).toString("base64");

  const calls = [];
  const fetchStub = async (url, init) => {
    calls.push(url);
    assert.match(init.headers.Authorization, /^Bearer /);
    if (url.endsWith("/verify")) return new Response(JSON.stringify({ isValid: true, payer: "0xabc" }));
    return new Response(JSON.stringify({ success: true, transaction: "0xtx", network: "eip155:8453", payer: "0xabc" }));
  };

  let res = mockRes();
  await rowHandler(req({ query: { model: "deepseek/deepseek-v4-pro", endpoint: tag }, headers: { host: "bitdepth.dev", "payment-signature": pay("1", PAYTO) } }), res, { fetch: fetchStub });
  assert.equal(res.statusCode, 402);
  assert.equal(res.parsed().reason, "amount_mismatch");
  assert.equal(calls.length, 0);

  res = mockRes();
  await rowHandler(req({ query: { model: "deepseek/deepseek-v4-pro", endpoint: tag }, headers: { host: "bitdepth.dev", "payment-signature": pay(PRICE_ATOMIC, "0x1111111111111111111111111111111111111111") } }), res, { fetch: fetchStub });
  assert.equal(res.parsed().reason, "payto_mismatch");

  res = mockRes();
  await rowHandler(req({ query: { model: "deepseek/deepseek-v4-pro", endpoint: tag }, headers: { host: "bitdepth.dev", "payment-signature": pay(PRICE_ATOMIC, PAYTO) } }), res, { fetch: fetchStub });
  assert.equal(res.statusCode, 200);
  assert.deepEqual(calls.map((u) => u.split("/").pop()), ["verify", "settle"]);
  const body = res.parsed();
  assert.equal(body.schema, "bitdepth.or.row.v1");
  assert.equal(body.row.tag, tag);
  assert.ok(body.detail && body.detail.self_agreement, "trend detail joined");
  const settled = JSON.parse(Buffer.from(res.headers["payment-response"], "base64").toString());
  assert.equal(settled.transaction, "0xtx");

  // Facilitator says settle failed: no data served.
  const failStub = async (url) => url.endsWith("/verify")
    ? new Response(JSON.stringify({ isValid: true }))
    : new Response(JSON.stringify({ success: false, errorReason: "NONCE_ALREADY_USED" }));
  res = mockRes();
  await rowHandler(req({ query: { model: "deepseek/deepseek-v4-pro", endpoint: tag }, headers: { host: "bitdepth.dev", "payment-signature": pay(PRICE_ATOMIC, PAYTO) } }), res, { fetch: failStub });
  assert.equal(res.statusCode, 402);
  assert.equal(res.parsed().reason, "nonce_already_used");
  assert.equal(res.parsed().row, undefined);
});
