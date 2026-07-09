const $ = (sel) => document.querySelector(sel);

let currentSheetData = null;
let selectedDesignator = null;
let showAmbiguousParts = false;

async function api(path, options = {}) {
  const res = await fetch(path, {
    headers: { "Content-Type": "application/json" },
    ...options,
  });
  const data = await res.json().catch(() => ({}));
  if (!res.ok) throw new Error(data.error || res.statusText);
  return data;
}

function renderMarkdown(md) {
  return marked.parse(md || "");
}

async function loadFreshness() {
  const { freshness } = await api("/api/freshness");
  $("#freshness").textContent = freshness;
}

function renderSheets(sheets) {
  const ul = $("#sheet-list");
  ul.innerHTML = "";
  sheets.forEach((s) => {
    const li = document.createElement("li");
    const btn = document.createElement("button");
    btn.type = "button";
    btn.className = "sheet-btn";
    btn.dataset.sheet = s.bom_sheet;
    btn.innerHTML = `
      <span class="num">${s.bom_sheet}</span>${escapeHtml(s.design_name)}
      ${s.status ? `<span class="status">${escapeHtml(s.status)}</span>` : ""}
    `;
    btn.addEventListener("click", () => selectSheet(s.bom_sheet, btn));
    li.appendChild(btn);
    ul.appendChild(li);
  });
}

function setActiveNav(el) {
  document.querySelectorAll(".sheet-btn, .nav-link").forEach((n) => n.classList.remove("active"));
  if (el) el.classList.add("active");
}

function directionLabel(dir) {
  if (dir.includes("out") && dir.includes("in")) return "↔";
  if (dir.includes("out")) return "→ out";
  if (dir.includes("in")) return "← in";
  return "";
}

function renderPartsList(parts) {
  const list = $("#part-list");
  const ph = $("#parts-placeholder");
  list.innerHTML = "";
  const visible = showAmbiguousParts ? parts : parts.filter((p) => p.sheet_resolution === "exact");
  if (!visible.length) {
    ph.textContent = parts.length
      ? "No exact-sheet parts (toggle ambiguous below)."
      : "No BOM rows on this sheet.";
    ph.style.display = "block";
    return;
  }
  ph.style.display = "none";
  for (const p of visible) {
    const li = document.createElement("li");
    li.className = p.card ? "has-card" : "";
    if (p.sheet_resolution === "ambiguous") li.classList.add("ambiguous");
    li.dataset.designator = p.designator;
    li.innerHTML = `
      <span class="ref">${escapeHtml(p.designator)}</span>
      <span class="name">${escapeHtml(p.name)}</span>
      ${p.card ? '<span class="badge card">card</span>' : ""}
    `;
    li.addEventListener("click", () => selectPart(p.designator));
    list.appendChild(li);
  }
}

function renderContractsTable(contracts) {
  if (!contracts.length) {
    return `<p class="placeholder">No net-registry rows matched this sheet (substring match on driven_from / consumed_by — see cradle_sidecar/data/net-registry.md).</p>`;
  }
  let html = `<table class="contract-table"><thead><tr>
    <th></th><th>Net</th><th>Driven from</th><th>Consumed by</th><th>Status</th><th>Netlist</th>
  </tr></thead><tbody>`;
  for (const r of contracts) {
    const nl = r.in_netlist
      ? (r.single_member ? `${r.member_count} (single)` : `${r.member_count}`)
      : "missing";
    const cls = !r.in_netlist ? "missing" : r.single_member ? "single" : "";
    html += `<tr class="${cls}" data-net="${escapeAttr(r.net)}">
      <td class="dir">${directionLabel(r.direction)}</td>
      <td><code>${escapeHtml(r.net)}</code></td>
      <td>${escapeHtml(r.driven_from)}</td>
      <td>${escapeHtml(r.consumed_by)}</td>
      <td>${escapeHtml(r.status)}</td>
      <td>${escapeHtml(nl)}</td>
    </tr>`;
  }
  html += "</tbody></table>";
  return html;
}

function renderSheetMain(data) {
  const panel = $("#panel-main");
  let html = "";

  html += `<section class="block descriptor">
    <div class="markdown source-block">${renderMarkdown(data.sheet_descriptor_md)}</div>
  </section>`;

  html += `<details class="conventions">
    <summary>Project conventions <span class="source-tag">docs/schematic-status.md</span></summary>
    <div class="markdown">${renderMarkdown(data.schematic_preamble_md)}</div>
  </details>`;

  html += `<section class="block contracts">
    <h2 class="section-title">Cross-sheet contracts <span class="source-tag">net-registry.md</span></h2>
    <div class="markdown preamble">${renderMarkdown(data.registry_preamble_md)}</div>
    <p class="registry-summary">${data.registry_summary.present}/${data.registry_summary.total} nets in netlist · ${data.registry_summary.missing} missing · ${data.registry_summary.single_member} single-member</p>
    <p class="contract-legend"><code>→ out</code> this sheet drives · <code>← in</code> this sheet consumes · <code>↔</code> both</p>
    ${renderContractsTable(data.contracts)}
  </section>`;

  html += `<section class="block part-detail" id="part-detail-section">
    <p class="placeholder">Select a part in the list (left) for component card detail.</p>
  </section>`;

  panel.innerHTML = html;

  panel.querySelectorAll(".contract-table tbody tr").forEach((row) => {
    row.addEventListener("click", () => {
      const r = data.contracts.find((x) => x.net === row.dataset.net);
      if (!r) return;
      const detail = $("#part-detail-section");
      detail.innerHTML = `
        <h2 class="section-title">Contract: <code>${escapeHtml(r.net)}</code></h2>
        <table class="kv-table">
          <tr><th>Direction</th><td>${escapeHtml(directionLabel(r.direction))}</td></tr>
          <tr><th>Driven from</th><td>${escapeHtml(r.driven_from)}</td></tr>
          <tr><th>Consumed by</th><td>${escapeHtml(r.consumed_by)}</td></tr>
          <tr><th>Voltage domain</th><td>${escapeHtml(r.voltage_domain || "")}</td></tr>
          <tr><th>Pull/term</th><td>${escapeHtml(r.pull_term || "")}</td></tr>
          <tr><th>Protocol</th><td>${escapeHtml(r.protocol || "")}</td></tr>
          <tr><th>SoC pin</th><td>${escapeHtml(r.soc_pin)}</td></tr>
          <tr><th>Registry status</th><td>${escapeHtml(r.status)}</td></tr>
          <tr><th>Netlist</th><td>${r.in_netlist ? `${r.member_count} member(s)` : "not in export"}${r.single_member ? " — single-member only" : ""}</td></tr>
        </table>
        <p class="source-tag">Verbatim columns from cradle_sidecar/data/net-registry.md</p>
      `;
      selectedDesignator = null;
      document.querySelectorAll("#part-list li").forEach((li) => li.classList.remove("selected"));
    });
  });
}

async function selectSheet(sheetId, btnEl) {
  setActiveNav(btnEl);
  selectedDesignator = null;
  $("#panel-main").innerHTML = "<p class='placeholder'>Loading…</p>";
  $("#parts-placeholder").textContent = "Loading…";
  $("#parts-placeholder").style.display = "block";
  $("#part-list").innerHTML = "";

  const data = await api(`/api/sheet/${sheetId}`);
  currentSheetData = data;
  renderPartsList(data.parts);
  renderSheetMain(data);
}

async function selectPart(designator) {
  if (!currentSheetData) return;
  selectedDesignator = designator;
  document.querySelectorAll("#part-list li").forEach((li) => {
    li.classList.toggle("selected", li.dataset.designator === designator);
  });

  const part = currentSheetData.parts.find((p) => p.designator === designator);
  if (!part) return;

  const detail = $("#part-detail-section");
  let html = `<h2 class="section-title">${escapeHtml(part.designator)} — ${escapeHtml(part.name)}</h2>`;
  if (part.description) {
    html += `<p class="bom-desc">${escapeHtml(part.description)}</p>`;
  }

  if (part.datasheets?.length) {
    html += `<div class="file-links"><strong>Datasheets</strong><br>`;
    for (const d of part.datasheets) {
      if (d.kind === "pdf") {
        html += `<button type="button" class="btn small open-file" data-path="${escapeAttr(d.path)}">${escapeHtml(d.name)}</button> `;
      }
    }
    html += `</div>`;
  }

  if (part.card) {
    const card = await api(`/api/card/${encodeURIComponent(part.card.file)}`);
    html += `<p class="source-tag">cradle_sidecar/data/components/${escapeHtml(part.card.file)}</p>`;
    html += `<div class="markdown">${renderMarkdown(card.markdown)}</div>`;
  } else {
    html += `<p class="placeholder">No component card. Template: <code>cradle_sidecar/data/components/_TEMPLATE.md</code></p>`;
  }

  detail.innerHTML = html;
  detail.querySelectorAll(".open-file").forEach((btn) => {
    btn.addEventListener("click", () => openFile(btn.dataset.path));
  });
}

async function showRegistry(navBtn) {
  setActiveNav(navBtn);
  currentSheetData = null;
  selectedDesignator = null;
  $("#parts-placeholder").textContent = "Full registry view";
  $("#parts-placeholder").style.display = "block";
  $("#part-list").innerHTML = "";

  const data = await api("/api/registry");
  const s = data.summary;
  const panel = $("#panel-main");
  let html = `<h2>Net registry</h2>
    <p class="source-tag">cradle_sidecar/data/net-registry.md</p>
    <p class="registry-summary">${s.present}/${s.total} in netlist · ${s.missing} missing · ${s.single_member} single-member</p>
    <table class="contract-table full-registry"><thead><tr>
      <th>Net</th><th>Driven from</th><th>Consumed by</th><th>SoC pin</th><th>Status</th><th>Netlist</th>
    </tr></thead><tbody>`;

  for (const r of data.rows) {
    const nl = r.in_netlist ? String(r.member_count) : "missing";
    const cls = !r.in_netlist ? "missing" : r.single_member ? "single" : "";
    html += `<tr class="${cls}">
      <td><code>${escapeHtml(r.net)}</code></td>
      <td>${escapeHtml(r.driven_from)}</td>
      <td>${escapeHtml(r.consumed_by)}</td>
      <td>${escapeHtml(r.soc_pin)}</td>
      <td>${escapeHtml(r.status)}</td>
      <td>${escapeHtml(nl)}</td>
    </tr>`;
  }
  html += "</tbody></table>";
  panel.innerHTML = html;
}

async function openFile(path) {
  await api("/api/open", { method: "POST", body: JSON.stringify({ path }) });
}

async function runRefresh() {
  const btn = $("#refresh-btn");
  btn.disabled = true;
  btn.textContent = "Running…";
  const dlg = $("#refresh-dialog");
  const out = $("#refresh-output");
  out.textContent = "Running project_refresh.py…";
  dlg.showModal();
  try {
    const result = await api("/api/refresh", { method: "POST", body: "{}" });
    out.textContent = (result.stdout || "") + (result.stderr ? "\n--- stderr ---\n" + result.stderr : "");
    if (result.exit_code !== 0) out.textContent += `\n\nExit code: ${result.exit_code}`;
    await loadFreshness();
    const overview = await api("/api/overview");
    renderSheets(overview.sheets);
    if (currentSheetData) {
      const btn = document.querySelector(`.sheet-btn[data-sheet="${currentSheetData.bom_sheet}"]`);
      await selectSheet(currentSheetData.bom_sheet, btn);
      if (selectedDesignator) await selectPart(selectedDesignator);
    }
  } catch (e) {
    out.textContent = "Error: " + e.message;
  } finally {
    btn.disabled = false;
    btn.textContent = "Run project refresh";
  }
}

function escapeHtml(s) {
  return String(s).replace(/&/g, "&amp;").replace(/</g, "&lt;").replace(/>/g, "&gt;");
}

function escapeAttr(s) {
  return escapeHtml(s).replace(/"/g, "&quot;");
}

async function init() {
  $("#refresh-btn").addEventListener("click", runRefresh);
  $("#nav-registry").addEventListener("click", (e) => showRegistry(e.target));
  $("#toggle-ambiguous").addEventListener("click", () => {
    showAmbiguousParts = !showAmbiguousParts;
    $("#toggle-ambiguous").textContent = showAmbiguousParts ? "− hide ambiguous" : "+ ambiguous BOM rows";
    if (currentSheetData) renderPartsList(currentSheetData.parts);
  });

  const overview = await api("/api/overview");
  await loadFreshness();
  renderSheets(overview.sheets);
}

init().catch((e) => {
  $("#panel-main").innerHTML = `<p style="color:#f08080">Failed to load: ${escapeHtml(e.message)}</p>`;
});
