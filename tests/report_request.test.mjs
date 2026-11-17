// Run: node --test tests/report_request.test.mjs
// The savings report form endpoint. Resend is stubbed, so no email is sent.

import { test } from "node:test";
import assert from "node:assert/strict";

import handler, { parseRequest, requesterEmail } from "../site/api/report-request.js";

function mockRes() {
  const r = { statusCode: 200, headers: {}, body: undefined };
  r.setHeader = (k, v) => { r.headers[k.toLowerCase()] = v; };
  r.status = (c) => { r.statusCode = c; return r; };
  r.send = (b) => { r.body = b; return r; };
  r.parsed = () => JSON.parse(r.body);
  return r;
}
const good = { email: "Ops@Example.com ", where: "OpenRouter", bill: "$500 to $5,000", jobs: ["Monitoring", "Nope"] };

function stub(ok = true) {
  const calls = [];
  const f = async (url, init) => { calls.push({ url, body: JSON.parse(init.body) }); return { ok, status: ok ? 200 : 500 }; };
  return { f, calls };
}

test("parse cleans the email and drops unknown jobs", () => {
  const r = parseRequest(good);
  assert.equal(r.email, "ops@example.com");
  assert.deepEqual(r.jobs, ["Monitoring"]);
  assert.equal(r.bot, false);
});

test("parse rejects a bad email and an unknown choice", () => {
  assert.equal(parseRequest({ ...good, email: "nope" }).error, "bad_email");
  assert.equal(parseRequest({ ...good, bill: "$1" }).error, "bad_choice");
});

test("a small bill gets the honest note", () => {
  const t = requesterEmail(parseRequest({ ...good, bill: "Under $100" })).text;
  assert.match(t, /under \$100/);
  assert.doesNotMatch(requesterEmail(parseRequest(good)).text, /under \$100/);
});

test("no em dash in the email text", () => {
  assert.ok(!requesterEmail(parseRequest(good)).text.includes("—"));
});

test("posts two emails: founder first, then the requester", async () => {
  process.env.RESEND_API_KEY = "re_test";
  const { f, calls } = stub();
  const res = mockRes();
  await handler({ method: "POST", body: good }, res, { fetch: f });
  assert.equal(res.statusCode, 200);
  assert.equal(calls.length, 2);
  assert.deepEqual(calls[0].body.to, ["hello@bitdepth.dev"]);
  assert.equal(calls[0].body.reply_to, "ops@example.com");
  assert.deepEqual(calls[1].body.to, ["ops@example.com"]);
  assert.match(calls[1].body.text, /two files/);
});

test("honeypot gets a quiet 200 and no email", async () => {
  process.env.RESEND_API_KEY = "re_test";
  const { f, calls } = stub();
  const res = mockRes();
  await handler({ method: "POST", body: { ...good, website: "spam.example" } }, res, { fetch: f });
  assert.equal(res.statusCode, 200);
  assert.equal(calls.length, 0);
});

test("no key is a 503, GET is a 405, a send failure is a 502", async () => {
  delete process.env.RESEND_API_KEY;
  let res = mockRes();
  await handler({ method: "POST", body: good }, res);
  assert.equal(res.statusCode, 503);
  res = mockRes();
  await handler({ method: "GET" }, res);
  assert.equal(res.statusCode, 405);
  process.env.RESEND_API_KEY = "re_test";
  res = mockRes();
  await handler({ method: "POST", body: good }, res, { fetch: stub(false).f });
  assert.equal(res.statusCode, 502);
});
