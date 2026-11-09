// The route list: one model's endpoints to allow, in the shape OpenRouter's
// provider block takes. The nightly file is data/public/v1/routes/<model>.json,
// written by probe/emit.py route_doc. routeListFrom builds the same document
// from the model file, for the night before the routes file exists.

import { FOOTER, METHOD_URL, getModel, getRoutes } from "./data.js";

export const MIN_ROUTE_NIGHTS = 7;
export const blended = (e) => (e.price_in_per_m == null || e.price_out_per_m == null ? null : (3 * e.price_in_per_m + e.price_out_per_m) / 4);
export const routable = (e) => e.state === "within" && (e.nights ?? 0) >= MIN_ROUTE_NIGHTS;
export const USAGE = "Put openrouter.provider in the request body. Fallbacks stay on and move only among the allowed endpoints. An account-wide allowed providers list in OpenRouter settings also applies; if the two do not overlap, requests fail.";

const why = (e) => (e.state === "outside" ? "outside" : e.state === "stale" ? "stale" : `only ${e.nights ?? 0} nights; ${MIN_ROUTE_NIGHTS} needed`);

export function routeListFrom(doc) {
  // OpenRouter treats a slug as a prefix ("venice" matches every Venice endpoint), so an
  // allowed slug that would also match a left-out endpoint is left out too.
  const outTags = doc.endpoints.filter((e) => !routable(e)).map((e) => e.tag);
  const shadow = (e) => outTags.filter((x) => x.startsWith(`${e.tag}/`));
  const ok = doc.endpoints.filter((e) => routable(e) && shadow(e).length === 0)
    .sort((a, b) => (blended(a) ?? Infinity) - (blended(b) ?? Infinity) || a.tag.localeCompare(b.tag));
  const allow = ok.map((e) => e.tag);
  return {
    schema: "bitdepth.routelist.v1", model: doc.model, label: doc.label, as_of: doc.as_of,
    rule: `state within and ${MIN_ROUTE_NIGHTS}+ nights (the check_before_route rule); allowed endpoints ordered by blended price, cheapest first`,
    allow,
    allowed: ok.map((e) => ({ tag: e.tag, declared_quant: e.declared_quant, nights: e.nights, blended_price_per_m: blended(e) == null ? null : Number(blended(e).toFixed(4)) })),
    excluded: doc.endpoints.filter((e) => !allow.includes(e.tag)).sort((a, b) => a.tag.localeCompare(b.tag)).map((e) => ({ tag: e.tag, why: routable(e) ? `would also match ${shadow(e).join(", ")}` : why(e) })),
    openrouter: allow.length ? { provider: { only: allow, sort: "price", allow_fallbacks: true } } : null,
    usage: USAGE,
    method_url: METHOD_URL, footer: FOOTER,
  };
}

export async function getRouteList(model) {
  const r = await getRoutes(model);
  if (r) return r;
  const doc = await getModel(model);
  return doc ? routeListFrom(doc) : null;
}
