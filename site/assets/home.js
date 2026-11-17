// Savings report form on the home page. Posts to /api/report-request and shows the result in place.
(function () {
  var form = document.getElementById("report-form");
  if (!form) return;
  var status = document.getElementById("report-status");
  var button = form.querySelector("button[type=submit]");

  function say(text, isError) {
    status.textContent = text;
    status.className = "fnote" + (isError ? " err" : "");
  }

  form.addEventListener("submit", function (ev) {
    ev.preventDefault();
    var email = form.email.value.trim();
    if (!/^[^\s@]+@[^\s@]+\.[^\s@]+$/.test(email)) {
      say("Please enter a work email.", true);
      form.email.focus();
      return;
    }
    var jobs = Array.prototype.slice.call(form.querySelectorAll("input[name=jobs]:checked")).map(function (c) { return c.value; });
    var body = { email: email, where: form.where.value, bill: form.bill.value, jobs: jobs, website: form.website.value };
    button.disabled = true;
    say("Sending...", false);
    fetch("/api/report-request", { method: "POST", headers: { "Content-Type": "application/json" }, body: JSON.stringify(body) })
      .then(function (r) { return r.json().then(function (j) { return { ok: r.ok, j: j }; }); })
      .then(function (res) {
        if (!res.ok) throw new Error(res.j && res.j.error || "failed");
        form.classList.add("done");
        Array.prototype.forEach.call(form.elements, function (el) { el.disabled = true; });
        say("Done. Check your inbox for what to send. Nothing there in ten minutes? Write to hello@bitdepth.dev.", false);
      })
      .catch(function () {
        button.disabled = false;
        say("That did not go through. Try again, or write to hello@bitdepth.dev.", true);
      });
  });
})();
