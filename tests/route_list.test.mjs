// Run: node --test tests/route_list.test.mjs
// Serves this checkout's data/ folder on a local port, so the route list is
// tested against the files emit.py writes, before they reach main.

import { test, before, after } from "node:test";
import assert from "node:assert/strict";
import { createServer } from "node:http";
import { readFile } from "node:fs/promises";
import { fileURLToPath } from "node:url";
import { join, normalize } from "node:path";

const DATA = fileURLToPath(new URL("../data/", import.meta.url));
let server, publicHandler, mcpHandler, routes;

before(async () => {
  server = createServer(async (req, res) => {
    const p = normalize(join(DATA, decodeURIComponent(req.url.split("?")[0])));
    if (!p.startsWith(DATA)) { res.statusCode = 404; return res.end(); }
    try { res.end(await readFile(p)); } catch { res.statusCode = 404; res.end(); }
  });
  await new Promise((r) => server.listen(0, "127.0.0.1", r));
  process.env.BITDEPTH_DATA_BASE = `http://127.0.0.1:${server.address().port}`;
  publicHandler = (await import("../site/api/public.js")).default;
  mcpHandler = (await import("../site/api/mcp.js")).default;
  routes = await import("../site/api/_lib/routes.js");
});
after(() => server.close());

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
const get = async (path) => { const res = mockRes(); await publicHandler(req({ query: { path } }), res); return res; };
const call = async (name, args) => {
  const res = mockRes();
  await mcpHandler(req({ method: "POST", body: { jsonrpc: "2.0", id: 1, method: "tools/call", params: { name, arguments: args } } }), res);
  return res.parsed().result;
};

test("routes: every model has a route list that agrees with check_before_route", async () => {
  const idx = (await get("index.json")).parsed();
  assert.ok(idx.models.length >= 3);
  for (const m of idx.models) {
    assert.equal(m.routes_path, `routes/${m.model}.json`);
    const res = await get(m.routes_path);
    assert.equal(res.statusCode, 200);
    assert.equal(res.headers["access-control-allow-origin"], "*");
    const r = res.parsed();
    assert.equal(r.schema, "bitdepth.routelist.v1");
    assert.equal(r.model, m.model);
    const doc = (await get(m.path)).parsed();
    assert.equal(r.allow.length + r.excluded.length, doc.endpoints.length);
    for (const e of r.excluded) assert.match(e.why, /^(outside|stale|only \d+ nights; 7 needed|would also match .+)$/);
    if (r.allow.length) assert.deepEqual(r.openrouter, { provider: { only: r.allow, sort: "price", allow_fallbacks: true } });
    else assert.equal(r.openrouter, null);
    // The file emit.py wrote and the JS fallback build the same list.
    assert.deepEqual(routes.routeListFrom(doc).allow, r.allow);
    for (const e of doc.endpoints) {
      const out = (await call("check_before_route", { model: m.model, endpoint: e.tag })).structuredContent;
      if (r.allow.includes(e.tag)) assert.equal(out.route, true, `${m.model} ${e.tag}`);
      else if (!/^would also match/.test(r.excluded.find((x) => x.tag === e.tag).why)) assert.notEqual(out.route, true, `${m.model} ${e.tag}`);
    }
  }
});

test("routes: traversal and unknown models 404", async () => {
  for (const p of ["routes/../index.json", "routes/x/../../or/openai/gpt-oss-120b.json", "routes/nope/nope.json", "routes/.json"]) {
    assert.equal((await get(p)).statusCode, 404, p);
  }
});

test("mcp: get_route_list returns the envelope", async () => {
  const out = await call("get_route_list", { model: "openai/gpt-oss-120b" });
  assert.equal(out.isError, false);
  const s = out.structuredContent;
  assert.ok(s.as_of && s.method_url && s.footer);
  assert.ok(Array.isArray(s.allow) && Array.isArray(s.excluded));
  assert.match(s.usage, /only among the allowed endpoints/);
  const bad = await call("get_route_list", { model: "nope/nope" });
  assert.equal(bad.isError, true);
});

test("routes: a slug that would also match a left-out endpoint is left out", () => {
  const row = (tag, state, nights = 9) => ({ tag, state, nights, declared_quant: "fp8", price_in_per_m: 1, price_out_per_m: 2 });
  const r = routes.routeListFrom({ model: "o/m", label: "m", as_of: "2026-11-09", endpoints: [
    row("venice", "within"), row("venice/fp4", "outside"), row("alibaba/fp8", "within"), row("alibaba/fp8/us", "within"), row("x/bf16", "within"),
  ] });
  assert.deepEqual(r.allow, ["alibaba/fp8", "alibaba/fp8/us", "x/bf16"]);
  assert.equal(r.excluded.find((e) => e.tag === "venice").why, "would also match venice/fp4");
});
