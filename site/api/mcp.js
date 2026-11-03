// Free MCP server, streamable HTTP, stateless. vercel.json rewrites
// /api/mcp/mcp and /mcp here. Each POST carries one JSON-RPC message (or a
// batch) and gets a JSON response; no sessions, no SSE stream, which the
// streamable HTTP transport allows. No key.

import { FOOTER, METHOD_URL, getDrift, getEndpoint, getIndex, getModel } from "./_lib/data.js";

const PROTOCOL_VERSIONS = ["2025-06-18", "2025-03-26", "2024-11-05"];
const SERVER = { name: "bitdepth", title: "Bitdepth", version: "0.1.0" };
const INSTRUCTIONS =
  "Bitdepth grades every OpenRouter endpoint serving the same open-weight model, nightly, against a published reference, " +
  "and shows each beside its price. Start with list_models, then get_scorecard. Every number is against the stated reference; " +
  "state 'outside' means the endpoint agrees with itself more than with the reference. Method: " + METHOD_URL;

const str = (description) => ({ type: "string", description });
const TOOLS = [
  {
    name: "list_models",
    title: "List graded models",
    description: "Models Bitdepth grades nightly, with as_of date and endpoint count.",
    inputSchema: { type: "object", properties: {}, additionalProperties: false },
    annotations: { readOnlyHint: true, openWorldHint: false },
  },
  {
    name: "get_scorecard",
    title: "Scorecard for one model",
    description: "Every endpoint serving the model: declared quant, nights, primary columns, price in and out per million tokens, and state (within, outside, no_data, stale). Sorted by the model's first primary column, best first.",
    inputSchema: { type: "object", properties: { model: str("Model id, e.g. deepseek/deepseek-v4-pro") }, required: ["model"], additionalProperties: false },
    annotations: { readOnlyHint: true, openWorldHint: false },
  },
  {
    name: "get_endpoint",
    title: "One endpoint's row",
    description: "One endpoint's row for a model, including the per-night exact series. Use the tag from get_scorecard, e.g. deepinfra/fp8.",
    inputSchema: { type: "object", properties: { model: str("Model id"), endpoint: str("Endpoint tag from get_scorecard") }, required: ["model", "endpoint"], additionalProperties: false },
    annotations: { readOnlyHint: true, openWorldHint: false },
  },
  {
    name: "get_drift",
    title: "Endpoints that moved",
    description: "Endpoint and model pairs whose score moved beyond the noise threshold between the first and last nights of the window. An empty list means nothing moved.",
    inputSchema: { type: "object", properties: {}, additionalProperties: false },
    annotations: { readOnlyHint: true, openWorldHint: false },
  },
];

const envelope = (doc, extra) => ({ as_of: doc?.as_of ?? null, method_url: METHOD_URL, ...extra, footer: FOOTER });

function summarizeRow(e, primary) {
  const out = { tag: e.tag, provider: e.provider_slug, declared_quant: e.declared_quant, nights: e.nights };
  for (const c of primary) out[c] = e[c];
  if (!primary.includes("exact")) out.exact = e.exact;
  return { ...out, price_in_per_m: e.price_in_per_m, price_out_per_m: e.price_out_per_m, state: e.state };
}

async function callTool(name, args = {}) {
  if (name === "list_models") {
    const idx = await getIndex();
    return envelope(idx, {
      models: (idx?.models ?? []).map(({ model, label, as_of, endpoint_count }) => ({ model, label, as_of, endpoint_count })),
      first_night: idx?.first_night ?? null,
    });
  }
  if (name === "get_scorecard") {
    const doc = await getModel(String(args.model || ""));
    if (!doc) throw toolError(`Unknown model '${args.model}'. Call list_models.`);
    const primary = doc.primary_columns || ["exact"];
    const key = primary[0];
    const rows = doc.endpoints.map((e) => summarizeRow(e, primary)).sort((a, b) => (b[key] ?? -1) - (a[key] ?? -1));
    return envelope(doc, {
      model: doc.model, nights: doc.nights, reference_rule: doc.reference_rule, primary_columns: primary,
      state_rule: doc.state_rule, noise_floor: doc.noise_floor, endpoints: rows,
    });
  }
  if (name === "get_endpoint") {
    const { doc, row } = await getEndpoint(String(args.model || ""), String(args.endpoint || ""));
    if (!doc) throw toolError(`Unknown model '${args.model}'. Call list_models.`);
    if (!row) throw toolError(`No endpoint '${args.endpoint}' for ${doc.model}. Tags: ${doc.endpoints.map((e) => e.tag).join(", ")}`);
    return envelope(doc, {
      model: doc.model, reference_rule: doc.reference_rule, primary_columns: doc.primary_columns, row,
      full_row: "Per-family self-agreement and self-check nights: GET https://bitdepth.dev/api/v1/row (0.10 USDC over x402).",
    });
  }
  if (name === "get_drift") {
    const d = await getDrift();
    return envelope(d, { items: d?.items ?? [] });
  }
  throw rpcError(-32602, `Unknown tool: ${name}`);
}

const toolError = (message) => Object.assign(new Error(message), { tool: true });
const rpcError = (code, message) => Object.assign(new Error(message), { code });

async function handleMessage(msg) {
  const { id, method, params } = msg || {};
  const isNotification = id === undefined || id === null;
  const reply = (result) => ({ jsonrpc: "2.0", id, result });
  const fail = (code, message) => ({ jsonrpc: "2.0", id: id ?? null, error: { code, message } });

  if (!msg || msg.jsonrpc !== "2.0" || typeof method !== "string") return isNotification ? null : fail(-32600, "Invalid Request");
  if (method.startsWith("notifications/")) return null;

  try {
    switch (method) {
      case "initialize": {
        const asked = params?.protocolVersion;
        return reply({
          protocolVersion: PROTOCOL_VERSIONS.includes(asked) ? asked : PROTOCOL_VERSIONS[0],
          capabilities: { tools: { listChanged: false } },
          serverInfo: SERVER,
          instructions: INSTRUCTIONS,
        });
      }
      case "ping":
        return reply({});
      case "tools/list":
        return reply({ tools: TOOLS });
      case "tools/call": {
        try {
          const data = await callTool(params?.name, params?.arguments);
          return reply({ content: [{ type: "text", text: JSON.stringify(data, null, 1) }], structuredContent: data, isError: false });
        } catch (err) {
          if (err.code) throw err;
          return reply({ content: [{ type: "text", text: err.tool ? err.message : `Upstream error: ${err.message}` }], isError: true });
        }
      }
      case "resources/list":
        return reply({ resources: [] });
      case "prompts/list":
        return reply({ prompts: [] });
      default:
        return isNotification ? null : fail(-32601, `Method not found: ${method}`);
    }
  } catch (err) {
    return fail(err.code || -32603, err.message || "Internal error");
  }
}

export default async function handler(req, res) {
  res.setHeader("Access-Control-Allow-Origin", "*");
  res.setHeader("Access-Control-Allow-Headers", "Content-Type, Accept, Mcp-Session-Id, Mcp-Protocol-Version, Authorization");
  res.setHeader("Access-Control-Allow-Methods", "GET, POST, DELETE, OPTIONS");
  if (req.method === "OPTIONS") return res.status(204).end();
  if (req.method === "GET") {
    // No server-initiated stream in this stateless server.
    res.setHeader("Allow", "POST, OPTIONS");
    return res.status(405).json({ jsonrpc: "2.0", id: null, error: { code: -32000, message: "Use POST. This server is stateless and opens no SSE stream." } });
  }
  if (req.method === "DELETE") return res.status(200).end();
  if (req.method !== "POST") return res.status(405).end();

  let body = req.body;
  if (typeof body === "string") {
    try { body = JSON.parse(body); } catch { return res.status(400).json({ jsonrpc: "2.0", id: null, error: { code: -32700, message: "Parse error" } }); }
  }
  const batch = Array.isArray(body);
  const replies = (await Promise.all((batch ? body : [body]).map(handleMessage))).filter(Boolean);
  if (replies.length === 0) return res.status(202).end();
  res.setHeader("Content-Type", "application/json");
  return res.status(200).send(JSON.stringify(batch ? replies : replies[0]));
}

export { TOOLS, handleMessage };
