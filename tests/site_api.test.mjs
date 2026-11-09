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
import { mintKey, subFromKey } from "../site/api/_lib/keys.js";
import keyedHandler from "../site/api/keyed.js";
import watchCheckout, { chunk, parseSpec } from "../site/api/watch-checkout.js";

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
  assert.deepEqual(res.parsed().result.tools.map((t) => t.name), ["list_models", "get_scorecard", "get_endpoint", "get_drift", "get_market_summary", "get_best_value_endpoint", "check_before_route", "get_route_list", "check_declared", "get_changes"]);

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

test("row: 503 without payTo, bare probe 402, paid bare 400, 404, then 402 challenge", async () => {
  delete process.env.X402_PAYTO;
  let res = mockRes();
  await rowHandler(req({ query: { model: "deepseek/deepseek-v4-pro", endpoint: "x" } }), res);
  assert.equal(res.statusCode, 503);

  process.env.X402_PAYTO = PAYTO;
  res = mockRes();
  await rowHandler(req({ query: {} }), res);
  assert.equal(res.statusCode, 402, "a bare discovery probe gets the challenge, not a 400");
  assert.ok(res.headers["payment-required"]);
  assert.equal(res.parsed().accepts[0].amount, PRICE_ATOMIC);
  assert.ok(res.parsed().extensions.bazaar);

  res = mockRes();
  await rowHandler(req({ query: {}, headers: { host: "bitdepth.dev", "payment-signature": "x" } }), res);
  assert.equal(res.statusCode, 400, "a paid call without a query is refused before settlement");

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
  // Bazaar discovery: info and schema present, GET with both query params required.
  const bz = ch.extensions && ch.extensions.bazaar;
  assert.ok(bz && bz.info && bz.schema, "bazaar extension present");
  assert.equal(bz.info.input.type, "http");
  assert.equal(bz.info.input.method, "GET");
  assert.deepEqual(bz.schema.properties.input.properties.queryParams.required, ["model", "endpoint"]);
  assert.equal(bz.info.output.type, "json");
  assert.equal(ch.resource.serviceName, "Bitdepth");
  assert.match(ch.resource.iconUrl, /\.png$/);
  assert.ok(ch.accepts[0].description.length <= 500);
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
  const bodies = {};
  const fetchStub = async (url, init) => {
    calls.push(url);
    bodies[url.split("/").pop()] = JSON.parse(init.body);
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
  // Settle carries the Bazaar block and resource so the facilitator can index the route.
  assert.ok(bodies.settle.paymentPayload.extensions.bazaar, "bazaar sent at settle");
  assert.match(bodies.settle.paymentPayload.resource.url, /\/api\/v1\/row\?model=/);

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


test("watch checkout: validates endpoints against live data, then builds a subscription session", async () => {
  process.env.STRIPE_CHECKOUT_KEY = "rk_test";
  process.env.WATCH_PRICE_ID = "price_live";
  process.env.WATCH_TEST_PRICE_ID = "price_test";
  process.env.WATCH_TEST_CODE = "secretcode";
  const idx = mockRes();
  await publicHandler(req({ query: { path: "or/deepseek/deepseek-v4-pro.json" } }), idx);
  const tags = idx.parsed().endpoints.slice(0, 3).map((e) => `deepseek/deepseek-v4-pro:${e.tag}`);

  assert.equal(parseSpec("not-a-spec"), null);
  assert.deepEqual(chunk(["a", "b", "c"], 3), ["a,b", "c"]);

  let res = mockRes();
  await watchCheckout(req({ method: "POST", body: { endpoints: tags.slice(0, 2) } }), res);
  assert.equal(res.statusCode, 400);
  assert.equal(res.parsed().error, "too_few");

  res = mockRes();
  await watchCheckout(req({ method: "POST", body: { endpoints: [...tags.slice(0, 2), "deepseek/deepseek-v4-pro:nope/fp8"] } }), res);
  assert.equal(res.statusCode, 400);
  assert.deepEqual(res.parsed().unknown, ["deepseek/deepseek-v4-pro:nope/fp8"]);

  let sent;
  const stub = async (url, init) => { sent = new URLSearchParams(init.body); return new Response(JSON.stringify({ url: "https://checkout.stripe.com/c/pay/x" })); };
  res = mockRes();
  await watchCheckout(req({ method: "POST", body: { endpoints: tags } }), res, { fetch: stub });
  assert.equal(res.statusCode, 200);
  assert.equal(res.parsed().url, "https://checkout.stripe.com/c/pay/x");
  assert.equal(sent.get("mode"), "subscription");
  assert.equal(sent.get("line_items[0][price]"), "price_live");
  assert.equal(sent.get("line_items[0][quantity]"), "3");
  assert.equal(sent.get("metadata[bitdepth_watch]"), "1");
  assert.equal(sent.get("metadata[endpoints_0]"), tags.join(","));

  // Wrong test code pays full price; the right one uses the test price.
  await watchCheckout(req({ method: "POST", body: { endpoints: tags, test: "guess" } }), mockRes(), { fetch: stub });
  assert.equal(sent.get("line_items[0][price]"), "price_live");
  await watchCheckout(req({ method: "POST", body: { endpoints: tags, test: "secretcode" } }), mockRes(), { fetch: stub });
  assert.equal(sent.get("line_items[0][price]"), "price_test");
});


test("watch key: same key as the email, unlocks the row only while the subscription is active", async () => {
  process.env.WATCH_KEY_SECRET = "s3cret";
  process.env.STRIPE_CHECKOUT_KEY = "rk_test";
  process.env.X402_PAYTO = PAYTO;
  assert.equal(mintKey("sub_TEST123"), "bdw_c3ViX1RFU1QxMjM_986e5f11cc1358cb980d1c841178f452");
  assert.equal(subFromKey(mintKey("sub_TEST123")), "sub_TEST123");
  assert.equal(subFromKey(mintKey("sub_TEST123").slice(0, -1) + "0"), null);

  const idx = mockRes();
  await publicHandler(req({ query: { path: "or/deepseek/deepseek-v4-pro.json" } }), idx);
  const tag = idx.parsed().endpoints[0].tag;
  const q = { model: "deepseek/deepseek-v4-pro", endpoint: tag };
  const stripe = (status) => async () => new Response(JSON.stringify({ status }));

  let res = mockRes();
  await rowHandler(req({ query: q, headers: { host: "bitdepth.dev", "x-bitdepth-key": mintKey("sub_ACTIVE1") } }), res, { fetch: stripe("active") });
  assert.equal(res.statusCode, 200);
  assert.equal(res.headers["x-bitdepth-plan"], "watch");
  assert.equal(res.parsed().row.tag, tag);

  res = mockRes();
  await rowHandler(req({ query: q, headers: { host: "bitdepth.dev", "x-bitdepth-key": mintKey("sub_GONE1") } }), res, { fetch: stripe("canceled") });
  assert.equal(res.statusCode, 403);

  res = mockRes();
  await rowHandler(req({ query: q, headers: { host: "bitdepth.dev", "x-bitdepth-key": "bdw_bad" } }), res);
  assert.equal(res.statusCode, 401);
});


test("keyed tools: changes since a night and price spread need an active Watch key", async () => {
  process.env.WATCH_KEY_SECRET = "s3cret";
  process.env.STRIPE_CHECKOUT_KEY = "rk_test";
  const active = { fetch: async () => new Response(JSON.stringify({ status: "active" })) };
  const h = { host: "bitdepth.dev", "x-bitdepth-key": mintKey("sub_KEYED1") };

  let res = mockRes();
  await keyedHandler(req({ query: { tool: "spread", model: "deepseek/deepseek-v4-pro" } }), res);
  assert.equal(res.statusCode, 401);

  res = mockRes();
  await keyedHandler(req({ query: { tool: "spread", model: "deepseek/deepseek-v4-pro" }, headers: h }), res, active);
  assert.equal(res.statusCode, 200);
  const sp = res.parsed();
  assert.equal(sp.schema, "bitdepth.spread.v1");
  assert.ok(sp.matching_reference.count >= 1);
  assert.ok(sp.matching_reference.cheapest.price_out_per_m <= sp.matching_reference.priciest.price_out_per_m);

  res = mockRes();
  await keyedHandler(req({ query: { tool: "changes", since: "2026-10-27", model: "deepseek/deepseek-v4-pro" }, headers: h }), res, active);
  assert.equal(res.statusCode, 200);
  const ch = res.parsed();
  assert.equal(ch.schema, "bitdepth.changes.v1");
  assert.equal(ch.models[0].model, "deepseek/deepseek-v4-pro");
  assert.ok(Array.isArray(ch.models[0].changes));

  res = mockRes();
  await keyedHandler(req({ query: { tool: "changes", since: "yesterday" }, headers: h }), res, active);
  assert.equal(res.statusCode, 400);
});
