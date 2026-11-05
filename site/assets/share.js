// Share controls for the leaderboard, per-model and charts pages, and the model tabs.
// Copy link, Copy image, PNG and Share on X. A card with data-png shares that file;
// otherwise the target (an SVG chart or a table) is drawn onto a branded canvas.
(function () {
  var PINE = "#1E3B2F", CREAM = "#F4EEE2", GOLD = "#B8902A", INK = "#14291F", PANEL = "#FBF8F1", MUTED = "#4E5B53", LINE = "#D9CFB8";

  function flash(btn, txt) {
    var old = btn.textContent;
    btn.textContent = txt; btn.classList.add("ok");
    setTimeout(function () { btn.textContent = old; btn.classList.remove("ok"); }, 1500);
  }
  function permalink(box) {
    var u = box.getAttribute("data-url");
    return u ? u : location.href;
  }
  function wrap(ctx, text, maxW) {
    var words = text.split(/\s+/), lines = [], cur = "";
    for (var i = 0; i < words.length; i++) {
      var t = cur ? cur + " " + words[i] : words[i];
      if (ctx.measureText(t).width > maxW && cur) { lines.push(cur); cur = words[i]; } else { cur = t; }
    }
    if (cur) lines.push(cur);
    return lines;
  }
  function frame(title, cite, drawBody, bodyH) {
    var W = 1200, pad = 56;
    var c = document.createElement("canvas");
    var ctx = c.getContext("2d");
    ctx.font = "400 34px Georgia, serif";
    var tl = wrap(ctx, title, W - pad * 2);
    var H = pad + 26 + tl.length * 42 + 20 + bodyH + 70;
    c.width = W; c.height = H;
    ctx.fillStyle = PANEL; ctx.fillRect(0, 0, W, H);
    ctx.fillStyle = PINE; ctx.fillRect(0, 0, W, 8);
    ctx.fillStyle = GOLD; ctx.font = "700 16px Inter, system-ui, sans-serif";
    ctx.fillText("BITDEPTH", pad, pad);
    ctx.fillStyle = PINE; ctx.font = "400 34px Georgia, serif";
    var y = pad + 46;
    tl.forEach(function (l) { ctx.fillText(l, pad, y); y += 42; });
    y += 4;
    drawBody(ctx, pad, y, W - pad * 2);
    ctx.fillStyle = LINE; ctx.fillRect(pad, H - 52, W - pad * 2, 1);
    ctx.fillStyle = MUTED; ctx.font = "500 15px ui-monospace, Menlo, monospace";
    ctx.fillText(cite, pad, H - 24);
    return c;
  }
  function citeOf(box) {
    var card = box.closest(".card, .panel, .sec, .thought, .hero");
    var el = card && card.querySelector(".cite");
    return el ? el.textContent : "Cite: Bitdepth · bitdepth.dev";
  }
  function svgToImage(svg) {
    return new Promise(function (resolve, reject) {
      var clone = svg.cloneNode(true);
      var vb = (svg.getAttribute("viewBox") || "0 0 760 300").split(/\s+/);
      clone.setAttribute("width", vb[2]); clone.setAttribute("height", vb[3]);
      clone.setAttribute("xmlns", "http://www.w3.org/2000/svg");
      var xml = new XMLSerializer().serializeToString(clone);
      var img = new Image();
      img.onload = function () { resolve({ img: img, w: +vb[2], h: +vb[3] }); };
      img.onerror = reject;
      img.src = "data:image/svg+xml;charset=utf-8," + encodeURIComponent(xml);
    });
  }
  function tableRows(el) {
    var out = [];
    el.querySelectorAll("tbody tr").forEach(function (tr) {
      if (tr.classList.contains("div") || out.length >= 8) return;
      var td = tr.querySelectorAll("td");
      if (td.length < 10) return;
      out.push([td[0].textContent, td[1].textContent, td[2].textContent, td[3].textContent, td[8].textContent, td[9].textContent]);
    });
    return out;
  }
  function canvasFor(box) {
    var title = box.getAttribute("data-title") || document.title;
    var cite = citeOf(box);
    var png = box.getAttribute("data-png");
    var target = document.getElementById(box.getAttribute("data-target"));
    if (png && (!target || target.tagName.toLowerCase() !== "svg") && !(target && target.querySelector("table"))) {
      return fetch(png).then(function (r) { return r.blob(); });
    }
    var svg = target && (target.tagName.toLowerCase() === "svg" ? target : target.querySelector("svg"));
    if (svg) {
      return svgToImage(svg).then(function (o) {
        var bw = 1200 - 112, bh = Math.round(o.h * bw / o.w);
        return toBlob(frame(title, cite, function (ctx, x, y, w) { ctx.drawImage(o.img, x, y, w, bh); }, bh));
      });
    }
    var tbl = target && target.querySelector("table");
    if (tbl) {
      var rows = tableRows(target), rh = 40, bh = rh * (rows.length + 1) + 10;
      return Promise.resolve(toBlob(frame(title, cite, function (ctx, x, y, w) {
        ctx.fillStyle = INK; ctx.fillRect(x, y, w, bh);
        var cols = [x + 16, x + 60, x + 470, x + 600, x + 760, x + 920];
        ctx.font = "600 13px Inter, system-ui, sans-serif"; ctx.fillStyle = GOLD;
        ["#", "ENDPOINT", "DECLARED", "AGREEMENT", "QUALITY-ADJ.", "STATE"].forEach(function (h, i) { ctx.fillText(h, cols[i], y + 26); });
        rows.forEach(function (r, j) {
          var yy = y + rh * (j + 1) + 26;
          ctx.font = "500 16px Inter, system-ui, sans-serif"; ctx.fillStyle = CREAM;
          r.forEach(function (v, i) { ctx.fillStyle = i === 4 ? GOLD : CREAM; ctx.fillText(v.slice(0, i === 1 ? 40 : 24), cols[i], yy); });
        });
      }, bh)));
    }
    return Promise.reject(new Error("nothing to draw"));
  }
  function toBlob(c) {
    return new Promise(function (res) { c.toBlob(function (b) { res(b); }, "image/png"); });
  }
  function act(box, kind, btn) {
    if (kind === "link") {
      var url = permalink(box);
      (navigator.clipboard ? navigator.clipboard.writeText(url) : Promise.reject()).then(function () { flash(btn, "Copied"); }, function () { prompt("Copy this link", url); });
    } else if (kind === "x") {
      var t = box.getAttribute("data-tweet") || box.getAttribute("data-title") || "";
      var u = "https://twitter.com/intent/tweet?text=" + encodeURIComponent(t) + "&url=" + encodeURIComponent(permalink(box)) + "&via=bitdepthdev";
      window.open(u, "_blank", "noopener,noreferrer");
    } else if (kind === "png" || kind === "copyimg") {
      Promise.resolve(canvasFor(box)).then(function (blob) {
        if (kind === "png") {
          var a = document.createElement("a");
          a.href = URL.createObjectURL(blob);
          a.download = "bitdepth-" + (box.getAttribute("data-target") || "chart") + ".png";
          document.body.appendChild(a); a.click(); a.remove();
          setTimeout(function () { URL.revokeObjectURL(a.href); }, 4000);
          flash(btn, "Saved");
        } else if (navigator.clipboard && window.ClipboardItem) {
          navigator.clipboard.write([new ClipboardItem({ "image/png": blob })]).then(function () { flash(btn, "Copied"); }, function () { flash(btn, "Use PNG"); });
        } else { flash(btn, "Use PNG"); }
      }).catch(function () { flash(btn, "Try PNG"); });
    }
  }
  document.addEventListener("click", function (ev) {
    var btn = ev.target.closest(".share button");
    if (btn) { act(btn.closest(".share"), btn.getAttribute("data-act"), btn); return; }
    var tab = ev.target.closest(".tabs button");
    if (tab) {
      var id = tab.getAttribute("data-tab");
      tab.parentNode.querySelectorAll("button").forEach(function (b) { b.setAttribute("aria-selected", b === tab ? "true" : "false"); });
      document.querySelectorAll(".panel").forEach(function (p) { p.hidden = p.id !== id; });
      try { history.replaceState(null, "", "#" + id); } catch (e) {}
    }
  });
  var h = location.hash.slice(1);
  if (h && h.indexOf("t-") === 0) {
    var b = document.querySelector('.tabs button[data-tab="' + h + '"]');
    if (b) b.click();
  }
})();
