// Free savings report request: the form on bitdepth.dev posts here.
// POST /api/report-request  {"email", "where", "bill", "jobs": [...], "website": ""}
// Sends two emails through Resend: the request to the founder, and the requester's
// instructions (what two files to send back). Nothing is stored here; the founder's
// copy is the record. "website" is a honeypot: a filled one gets a quiet 200 and no email.
//
// Env (Vercel): RESEND_API_KEY. Optional: REPORT_NOTIFY_TO (default hello@bitdepth.dev).

const RESEND = "https://api.resend.com/emails";
const FROM = "Mancy at Bitdepth <hello@bitdepth.dev>";
const REPLY_TO = "hello@bitdepth.dev";

export const WHERE = ["OpenRouter", "Anthropic API", "OpenAI API", "Google Gemini API", "Hermes Agent or OpenClaw", "More than one"];
export const BILL = ["Under $100", "$100 to $500", "$500 to $5,000", "Over $5,000"];
export const JOBS = ["Status checks", "Monitoring", "Tagging or sorting", "Pulling out data", "Summaries", "Something else"];

const EMAIL_RE = /^[^\s@<>"',;]{1,64}@[^\s@<>"',;]{1,190}\.[a-z]{2,24}$/i;

function send(res, status, body) {
  res.setHeader("Content-Type", "application/json; charset=utf-8");
  res.setHeader("Cache-Control", "no-store");
  return res.status(status).send(JSON.stringify(body));
}

export function parseRequest(body) {
  const b = body && typeof body === "object" ? body : {};
  const email = String(b.email || "").trim().toLowerCase();
  if (!EMAIL_RE.test(email) || email.length > 254) return { error: "bad_email" };
  const where = WHERE.includes(b.where) ? b.where : null;
  const bill = BILL.includes(b.bill) ? b.bill : null;
  if (!where || !bill) return { error: "bad_choice" };
  const jobs = Array.isArray(b.jobs) ? [...new Set(b.jobs.filter((j) => JOBS.includes(j)))] : [];
  return { email, where, bill, jobs, bot: Boolean(String(b.website || "").trim()) };
}

export function requesterEmail(r) {
  const small = r.bill === "Under $100";
  const lines = [
    "Hi,",
    "",
    "Thanks for asking for a Bitdepth savings report.",
  ];
  if (small) {
    lines.push("", "You said your model bill is under $100 a month, so the saving may only be a few dollars. I'm happy to run it anyway.");
  }
  lines.push(
    "",
    "Reply to this email with two files:",
    "",
    "1. A 30-day usage export from " + (r.where === "More than one" || r.where === "Hermes Agent or OpenClaw" ? "each provider you pay" : r.where) + ". A CSV from the usage or billing page is fine. It should show the model, tokens and cost by day.",
    "",
    "2. 20 recent runs of your three most frequent jobs. For each run: the instructions, the input, and the answer your model gave. A CSV, a JSONL file or pasted examples all work. Remove names, emails and anything private first.",
    "",
    "Optional: one line per job on what a wrong answer looks like.",
    "",
    "What happens next: I run each job on cheaper open models and compare the answers with yours. You get a private link showing what passed, what failed and what you'd save each month. It takes about a week. I delete your files once the report is sent.",
    "",
    "Questions? Just reply.",
    "",
    "Mancy Thurston",
    "Bitdepth.dev",
    "",
    "Autumn Sun LLC, 30 N Gould St, Ste R, Sheridan, WY 82801",
  );
  return { subject: "Your Bitdepth savings report: two files to send", text: lines.join("\n") };
}

export function founderEmail(r) {
  return {
    subject: `New free report request from ${r.email}`,
    text: [
      "Someone asked for a free savings report on bitdepth.dev.",
      "",
      "What they told us:",
      `- Email: ${r.email}`,
      `- Their AI calls go to: ${r.where}`,
      `- Their model bill a month: ${r.bill}`,
      `- Jobs that repeat: ${r.jobs.length ? r.jobs.join(", ") : "none ticked"}`,
      "",
      "What happens next:",
      "1. They were just emailed, asking them to reply with two files: a 30-day usage export and 20 recent runs of their three biggest jobs.",
      "2. Their reply will land in this inbox.",
      "3. When it does, start a Claude session, attach the two files and say \"make the savings report\".",
      "",
      "Nothing to do until they reply. Reply to this email to write to them directly.",
    ].join("\n"),
  };
}

async function resend(fetchFn, key, payload) {
  const r = await fetchFn(RESEND, {
    method: "POST",
    headers: { Authorization: `Bearer ${key}`, "Content-Type": "application/json" },
    body: JSON.stringify(payload),
  });
  if (!r.ok) throw new Error(`resend_${r.status}`);
}

export default async function handler(req, res, deps = {}) {
  if (req.method !== "POST") return send(res, 405, { error: "method_not_allowed" });
  const key = (process.env.RESEND_API_KEY || "").trim();
  if (!key) return send(res, 503, { error: "not_configured" });
  let body = req.body;
  if (typeof body === "string") {
    try { body = JSON.parse(body); } catch { body = {}; }
  }
  const r = parseRequest(body);
  if (r.error) return send(res, 400, { error: r.error });
  if (r.bot) return send(res, 200, { ok: true });

  const fetchFn = deps.fetch || fetch;
  const notify = (process.env.REPORT_NOTIFY_TO || "hello@bitdepth.dev").trim();
  const mine = requesterEmail(r);
  const theirs = founderEmail(r);
  try {
    await resend(fetchFn, key, { from: FROM, to: [notify], reply_to: r.email, subject: theirs.subject, text: theirs.text });
    await resend(fetchFn, key, { from: FROM, to: [r.email], reply_to: REPLY_TO, subject: mine.subject, text: mine.text });
  } catch {
    return send(res, 502, { error: "send_failed" });
  }
  return send(res, 200, { ok: true });
}
