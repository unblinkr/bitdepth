// Reads the probe repo's public files. The nightly workflow commits
// data/public/v1/ and data/trend/latest.json to main; this module fetches
// them from raw GitHub and caches them in memory for ten minutes per warm
// function instance. No other source of numbers exists for the API.

const RAW = process.env.BITDEPTH_DATA_BASE ||
  "https://raw.githubusercontent.com/unblinkr/bitdepth/main/data";
const TTL_MS = 10 * 60 * 1000;
const cache = new Map();

export const FOOTER = "Numbers against a stated reference. Not a claim about intent.";
export const METHOD_URL = "https://bitdepth.dev/method";

async function getJson(path) {
  const hit = cache.get(path);
  if (hit && Date.now() - hit.at < TTL_MS) return hit.value;
  const resp = await fetch(`${RAW}/${path}`, { headers: { "User-Agent": "bitdepth-site" } });
  if (resp.status === 404) return null;
  if (!resp.ok) throw new Error(`upstream ${resp.status} for ${path}`);
  const value = await resp.json();
  cache.set(path, { at: Date.now(), value });
  return value;
}

// Only these three shapes are ever served. Anything else is a 404, so the
// /v1 proxy can never be pointed at another file in the repo.
const MODEL_RE = /^[a-z0-9][a-z0-9._-]*\/[a-z0-9][a-z0-9._-]*$/i;

export function isModelId(model) {
  return typeof model === "string" && MODEL_RE.test(model) && !model.includes("..");
}

export const getIndex = () => getJson("public/v1/index.json");
export const getDrift = () => getJson("public/v1/drift.json");
export const getTrend = () => getJson("trend/latest.json");
export const getChanges = () => getJson("public/v1/changes.json");

const DATE_RE = /^\d{4}-\d{2}-\d{2}$/;
export const isDate = (d) => typeof d === "string" && DATE_RE.test(d);
// One night's listing as the router showed it: tags, declared quantization, prices.
export const getRunEndpoints = (date) => (isDate(date) ? getJson(`runs/${date}/endpoints.json`) : Promise.resolve(null));

export async function getModel(model) {
  if (!isModelId(model)) return null;
  const index = await getIndex();
  const listed = index?.models?.find((m) => m.model === model);
  if (!listed) return null;
  return getJson(`public/v1/${listed.path}`);
}

// Route list per model. Older index files have no routes_path; the route
// list is derived from the same path pattern so the API works the night it ships.
export async function getRoutes(model) {
  if (!isModelId(model)) return null;
  const index = await getIndex();
  const listed = index?.models?.find((m) => m.model === model);
  if (!listed) return null;
  return getJson(`public/v1/${listed.routes_path || `routes/${model}.json`}`);
}

export async function getEndpoint(model, tag) {
  const doc = await getModel(model);
  if (!doc) return { doc: null, row: null };
  const row = doc.endpoints.find((e) => e.tag === tag) || null;
  return { doc, row };
}

// The paid row: the free row plus the trend detail the public file leaves
// out (min and max, per-family self-agreement with pair counts, self-check
// nights). Same numbers the packet uses, no new grade.
export async function getFullRow(model, tag) {
  const { doc, row } = await getEndpoint(model, tag);
  if (!row) return null;
  const trend = await getTrend();
  const slug = model.split("/")[1];
  const tm = trend?.models?.find((m) => m.slug === model || m.slug === slug || m.label === doc.label);
  const te = tm?.endpoints?.find((e) => e.tag === tag) || null;
  return {
    schema: "bitdepth.or.row.v1",
    model,
    as_of: doc.as_of,
    reference_rule: doc.reference_rule,
    primary_columns: doc.primary_columns,
    state_rule: doc.state_rule,
    noise_floor: doc.noise_floor,
    row,
    detail: te ? {
      exact_by_night: te.exact_by_night ?? null,
      exact_mean: te.exact_mean ?? null,
      exact_min: te.exact_min ?? null,
      exact_max: te.exact_max ?? null,
      movement_overlap: te.movement_overlap ?? null,
      self_agreement: te.self ?? null,
      selfcheck: te.selfcheck ?? null,
    } : null,
    method_url: METHOD_URL,
    footer: FOOTER,
  };
}
