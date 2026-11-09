// scripts/x402-pay-test.ts
//
// Pays ONE x402 URL once, from the test wallet, so the CDP facilitator indexes the
// route in the Bazaar and the paid path is proven end to end.
// Brief: tasks/x402-pay-test/TASK.md
//
// Usage:
//   node tools/x402-pay/node_modules/.bin/tsx tools/x402-pay/x402-pay-test.ts check <url> <max_usdc>   pre-flight only, pays nothing
//   node tools/x402-pay/node_modules/.bin/tsx tools/x402-pay/x402-pay-test.ts pay   <url> <max_usdc>   pre-flight, then one payment
//
// The key is read from process.env only. It is never printed, written, or put in a
// URL or error message. Errors about it report its length only.
// The URL is marked "attempted" in the ledger BEFORE the paid call. Never retried.

import { existsSync, mkdirSync, readFileSync, writeFileSync } from "node:fs";
import { dirname, resolve } from "node:path";
import { wrapFetchWithPaymentFromConfig } from "@x402/fetch";
import { ExactEvmScheme } from "@x402/evm";
import { privateKeyToAccount } from "viem/accounts";
import { createPublicClient, formatUnits, http } from "viem";
import { base } from "viem/chains";

const WALLET = "0x7fb0Dc20F35435bA027dc267EF126f063353E159";
const RPC = "https://mainnet.base.org";
const USDC = "0x833589fCD6eDb6E08f4c7C32D4f71b54bdA02913";
const NETWORK = "eip155:8453";
const KEY_NAME = "PADDOCK_SELFPAY_KEY";
const LEDGER = resolve("tasks/x402-pay-test/results.json");
const ERC20 = [
  { name: "balanceOf", type: "function", stateMutability: "view", inputs: [{ name: "a", type: "address" }], outputs: [{ name: "", type: "uint256" }] },
] as const;

type State = "checked" | "attempted" | "settled" | "failed";
interface Rec {
  url: string;
  state: State;
  unpaid_status?: number;
  amount_atomic?: string;
  network?: string;
  asset?: string;
  payTo?: string;
  usdc_before?: string;
  usdc_after?: string;
  paid_status?: number;
  success?: boolean;
  transaction?: string;
  payer?: string;
  error?: string;
  at: string;
}
interface Ledger { wallet: string; runs: Rec[] }

function die(msg: string): never {
  console.error(`ERROR: ${msg}`);
  process.exit(1);
}
const load = (): Ledger => (existsSync(LEDGER) ? JSON.parse(readFileSync(LEDGER, "utf8")) : { wallet: WALLET, runs: [] });
function save(l: Ledger) {
  mkdirSync(dirname(LEDGER), { recursive: true });
  writeFileSync(LEDGER, JSON.stringify(l, null, 2) + "\n");
}

function key(): `0x${string}` {
  const raw = process.env[KEY_NAME];
  if (!raw) die(`${KEY_NAME} is not set`);
  const hex = raw.trim().replace(/^0x/i, "");
  if (!/^[0-9a-fA-F]{64}$/.test(hex)) die(`${KEY_NAME} is not a 32-byte hex key (${hex.length} chars after trim)`);
  return `0x${hex}`;
}

const pub = createPublicClient({ chain: base, transport: http(RPC) });
const balance = async () =>
  (await pub.readContract({ address: USDC, abi: ERC20, functionName: "balanceOf", args: [WALLET as `0x${string}`] })) as bigint;

async function main() {
  const [mode, url, maxArg] = process.argv.slice(2);
  if ((mode !== "check" && mode !== "pay") || !url || !maxArg) die("usage: x402-pay-test.ts check|pay <url> <max_usdc>");
  const max = parseFloat(maxArg);
  if (!Number.isFinite(max) || max <= 0) die(`max_usdc must be a positive number, got ${maxArg}`);

  // 1-2. Key and address.
  const account = privateKeyToAccount(key());
  if (account.address.toLowerCase() !== WALLET.toLowerCase()) die(`derived address ${account.address} is not the test wallet ${WALLET}`);

  // 3. Unpaid GET must be a parseable 402.
  const unpaid = await fetch(url);
  let body: { accepts?: { network?: string; asset?: string; amount?: string; maxAmountRequired?: string; payTo?: string }[] } = {};
  try { body = await unpaid.json(); } catch { /* checked below */ }
  if (unpaid.status !== 402 || !Array.isArray(body.accepts)) die(`expected HTTP 402 with accepts[], got HTTP ${unpaid.status}`);
  const acc = body.accepts.find((a) => a.network === NETWORK && (a.asset || "").toLowerCase() === USDC.toLowerCase());
  if (!acc) die(`no accept on ${NETWORK} in Base USDC`);
  const amount = BigInt(acc.amount ?? acc.maxAmountRequired ?? "0");
  if (amount <= 0n) die("402 amount is missing or zero");
  console.log(`402 ok: ${formatUnits(amount, 6)} USDC on ${acc.network} to ${acc.payTo}`);

  // 4. Cap.
  if (amount > BigInt(Math.round(max * 1e6))) die(`402 asks ${formatUnits(amount, 6)} USDC, above the cap of ${max}`);

  // 5. Balance.
  const before = await balance();
  console.log(`wallet USDC: ${formatUnits(before, 6)}`);
  if (before < amount) die("wallet USDC balance is below the amount");

  // 6. Ledger.
  const ledger = load();
  const prior = ledger.runs.find((r) => r.url === url && r.state !== "checked");
  const rec: Rec = prior ?? { url, state: "checked", at: "" };
  Object.assign(rec, {
    unpaid_status: unpaid.status,
    amount_atomic: amount.toString(),
    network: acc.network,
    asset: acc.asset,
    payTo: acc.payTo,
    usdc_before: formatUnits(before, 6),
    at: new Date().toISOString(),
  });
  if (!prior) {
    ledger.runs = ledger.runs.filter((r) => r.url !== url);
    ledger.runs.push(rec);
  }
  save(ledger);
  if (mode === "check") { console.log("check: pre-flight passed, nothing paid"); return; }

  // 7. Never pay twice.
  if (prior) die(`ledger already shows state "${prior.state}" for this URL; not paying again`);

  // 8. Attempted first, then pay.
  rec.state = "attempted";
  save(ledger);
  const payFetch = wrapFetchWithPaymentFromConfig(fetch, { schemes: [{ network: NETWORK, client: new ExactEvmScheme(account) }] });
  const paid = await payFetch(url);
  rec.paid_status = paid.status;

  // 9. Settlement header.
  const raw = paid.headers.get("PAYMENT-RESPONSE") || paid.headers.get("X-PAYMENT-RESPONSE");
  let settle: { success?: boolean; transaction?: string; payer?: string } = {};
  if (raw) { try { settle = JSON.parse(Buffer.from(raw, "base64").toString("utf8")); } catch { /* recorded as failed */ } }
  rec.success = settle.success;
  rec.transaction = settle.transaction;
  rec.payer = settle.payer;

  // 10. Settled or failed.
  const ok = paid.status === 200 && settle.success === true && /^0x[0-9a-fA-F]{64}$/.test(settle.transaction || "");
  if (!ok) {
    let text = "";
    try { text = (await paid.text()).slice(0, 400); } catch { /* ignore */ }
    rec.state = "failed";
    rec.error = `HTTP ${paid.status}; ${text}`;
    save(ledger);
    die(`payment not settled: HTTP ${paid.status}`);
  }
  rec.state = "settled";

  // 11. Balance after.
  rec.usdc_after = formatUnits(await balance(), 6);
  save(ledger);
  console.log(`settled: https://basescan.org/tx/${settle.transaction}`);
}

main().catch((e) => die(e instanceof Error ? e.message.replace(/0x[0-9a-fA-F]{64}/g, "[redacted]") : "unknown error"));
