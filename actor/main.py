"""Bitdepth endpoint probe, Apify actor entry point.

Input (see .actor/input_schema.json): a graded model and a target, either an
OpenRouter endpoint tag or a custom OpenAI-compatible base URL. Output: one
dataset item and the OUTPUT record, schema bitdepth.probe.v1.

Pricing: one pay-per-event charge, event `endpoint-probe`, made only after the
run completes with at least half the prompts answered. Bad input, an
unreachable endpoint or a budget stop is not charged.
"""

from __future__ import annotations

import asyncio
import os
import tempfile
from pathlib import Path

from apify import Actor

from actor.probe_one import (
    ProbeInputError, custom_completer, custom_target, load_reference, openrouter_target, run_probe,
)
from probe import openrouter

EVENT = "endpoint-probe"


async def main() -> None:
    async with Actor:
        inp = await Actor.get_input() or {}
        model = str(inp.get("model") or "").strip()
        kind = str(inp.get("target") or "openrouter").strip()
        try:
            ref = await asyncio.to_thread(load_reference, model)
            if kind == "openrouter":
                if not os.environ.get("OPENROUTER_API_KEY", "").strip():
                    raise ProbeInputError("This actor is not configured for OpenRouter probes yet. Try again later.")
                tag = str(inp.get("openrouter_endpoint") or "").strip()
                if not tag:
                    raise ProbeInputError("openrouter_endpoint is required, e.g. deepinfra/fp8")
                target = await asyncio.to_thread(openrouter_target, model, tag)
                completer = openrouter.complete
            elif kind == "custom":
                base_url = str(inp.get("base_url") or "").strip()
                target = await asyncio.to_thread(custom_target, base_url, str(inp.get("model_name") or "").strip(),
                                                 inp.get("declared_quant"))
                completer = custom_completer(base_url, str(inp.get("api_key") or ""), str(inp.get("model_name")).strip())
            else:
                raise ProbeInputError("target must be 'openrouter' or 'custom'")
        except ProbeInputError as exc:
            await Actor.fail(status_message=str(exc))
            return

        Actor.log.info(f"Probing {target['tag']} on {model}: {len(ref['reference'])} prompts against the {ref['night']} reference")
        await Actor.set_status_message(f"Probing {target['tag']}")
        with tempfile.TemporaryDirectory() as tmp:
            result = await asyncio.to_thread(run_probe, ref, target, completer, Path(tmp), kind)

        if result["chargeable"]:
            await Actor.push_data(result, charged_event_name=EVENT)
        else:
            await Actor.push_data(result)
        await Actor.set_value("OUTPUT", result)

        r = result["result"]
        msg = (f"{target['tag']}: exact {r['exact_pct']}%, string {r['string']}%, "
               f"{r['ok']}/{r['rows']} answered; reference night {ref['night']}")
        if not result["chargeable"]:
            msg += ". Not charged: fewer than half the prompts were answered."
        await Actor.exit(status_message=msg)


if __name__ == "__main__":
    asyncio.run(main())
