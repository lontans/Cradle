const $ = (sel) => document.querySelector(sel);

let currentSheetData = null;
let selectedDesignator = null;
let showAmbiguousParts = false;
let currentCardsList = null;
let editorState = null; // { filename, isNew, onSaved }
let currentPdfPage = 1;
let currentView = "home"; // "home" | "sheet" | "registry" | "cards" -- lets runRefresh() know what to re-render

const ORIGIN_CLASS = {
  "Datasheet-derived": "origin-datasheet",
  "Manually authored": "origin-manual",
  "Mixed": "origin-mixed",
};

function originBadge(origin) {
  if (!origin) return `<span class="badge origin-unknown">no card origin</span>`;
  const cls = ORIGIN_CLASS[origin] || "origin-unknown";
  return `<span class="badge ${cls}">${escapeHtml(origin)}</span>`;
}

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

const PROVENANCE_RE = /\[(VERIFIED|UNVERIFIED|MANUAL)\b[^\]]*\]/g;
const PROVENANCE_CLASS = { VERIFIED: "prov-verified", UNVERIFIED: "prov-unverified", MANUAL: "prov-manual" };

// Runs after any card/sheet markdown is dropped into the DOM: colors the
// Status column in vendor pin tables (Decided/Open/Not addressed) and wraps
// [VERIFIED]/[UNVERIFIED]/[MANUAL] provenance tags in a colored span. Both
// operate on the live DOM, not the markdown source, so they can't corrupt
// table/code parsing the way a regex over raw markdown could.
function enhanceRenderedMarkdown(container) {
  container.querySelectorAll("table").forEach((table) => {
    const headerCells = [...table.querySelectorAll("thead th")];
    const statusIdx = headerCells.findIndex((th) => th.textContent.trim().toLowerCase() === "status");
    if (statusIdx === -1) return;
    table.querySelectorAll("tbody tr").forEach((tr) => {
      const cell = tr.children[statusIdx];
      if (!cell) return;
      const text = cell.textContent.trim();
      if (/^Decided/.test(text)) cell.classList.add("status-decided");
      else if (/^Open/.test(text)) cell.classList.add("status-open");
      else if (/^Not addressed/i.test(text)) cell.classList.add("status-not-addressed");
    });
  });

  const walker = document.createTreeWalker(container, NodeFilter.SHOW_TEXT, null);
  const targets = [];
  let node;
  while ((node = walker.nextNode())) {
    if (PROVENANCE_RE.test(node.nodeValue)) targets.push(node);
    PROVENANCE_RE.lastIndex = 0;
  }
  for (const textNode of targets) {
    const frag = document.createDocumentFragment();
    let lastIndex = 0;
    let m;
    PROVENANCE_RE.lastIndex = 0;
    while ((m = PROVENANCE_RE.exec(textNode.nodeValue))) {
      if (m.index > lastIndex) frag.appendChild(document.createTextNode(textNode.nodeValue.slice(lastIndex, m.index)));
      const span = document.createElement("span");
      span.className = "prov-tag " + (PROVENANCE_CLASS[m[1]] || "");
      span.textContent = m[0];
      frag.appendChild(span);
      lastIndex = PROVENANCE_RE.lastIndex;
    }
    if (lastIndex < textNode.nodeValue.length) frag.appendChild(document.createTextNode(textNode.nodeValue.slice(lastIndex)));
    textNode.parentNode.replaceChild(frag, textNode);
  }
}

// Resolves a relative markdown link (e.g. "decisions-log.md", "../CHANGELOG.md")
// against the repo-root-relative directory of the file it was rendered from
// -- plain string join + "." / ".." handling, no URL object (these aren't
// real page URLs, so letting the browser resolve href against the sidecar's
// own location is exactly what was going nowhere before).
function resolveRelativePath(baseDir, href) {
  const parts = `${baseDir}/${href}`.split("/");
  const stack = [];
  for (const part of parts) {
    if (part === "" || part === ".") continue;
    if (part === "..") stack.pop();
    else stack.push(part);
  }
  return stack.join("/");
}

// Markdown links in these docs/cards point at other repo files
// (`[decisions-log.md](decisions-log.md)`), not real URLs -- clicking one
// used to hand the href straight to the browser, which tried to navigate
// the sidecar itself to a path with no matching route and silently did
// nothing. Intercept instead: resolve against the source file's own
// directory and open it with the OS's default app via the same /api/open
// path the datasheet buttons already use. External (http/https/mailto)
// links are left alone and just open in a new tab.
function wireMarkdownLinks(container, baseDir) {
  if (!container) return;
  container.querySelectorAll("a[href]").forEach((a) => {
    const href = a.getAttribute("href");
    if (!href || /^([a-z][a-z0-9+.-]*:)?\/\//i.test(href) || href.startsWith("mailto:")) {
      a.target = "_blank";
      a.rel = "noopener";
      return;
    }
    const resolved = resolveRelativePath(baseDir, href.split("#")[0]);
    a.title = `Open ${resolved}`;
    a.addEventListener("click", (e) => {
      e.preventDefault();
      openFile(resolved).catch((err) => console.warn(`Could not open ${resolved}:`, err.message));
    });
  });
}

const PAGE_IN_TAG_RE = /\bp\.\s*(\d+)/i;

function setPdfPage(n) {
  const frame = document.getElementById("pdf-frame");
  if (!frame || !n) return;
  currentPdfPage = n;
  frame.src = `${frame.dataset.baseSrc}#page=${n}`;
  const pageInput = document.getElementById("pdf-page-input");
  if (pageInput) pageInput.value = n;
  const notePage = document.getElementById("note-page");
  if (notePage && !notePage.dataset.userEdited) notePage.value = n;
}

// The signature interaction: a [VERIFIED — ... p.12] tag rendered by
// enhanceRenderedMarkdown becomes clickable when a PDF pane is on screen,
// jumping the embedded viewer straight to that page -- the citation *is*
// the navigation, instead of a separate "open PDF, scroll to page 12" step.
function wireProvenancePageLinks(container) {
  if (!document.getElementById("pdf-frame")) return;
  container.querySelectorAll(".prov-tag").forEach((span) => {
    const m = PAGE_IN_TAG_RE.exec(span.textContent);
    if (!m) return;
    span.classList.add("prov-tag-linked");
    span.title = `Jump to page ${m[1]} in the datasheet`;
    span.addEventListener("click", () => setPdfPage(parseInt(m[1], 10)));
  });
}

function noteComposerHTML(datasheetName) {
  const sourcePlaceholder = datasheetName ? `${datasheetName} p.N` : "source citation";
  return `
    <div class="note-composer">
      <div class="note-composer-head">
        <span>Add a note</span>
        <select id="note-tag" class="note-tag-select">
          <option value="MANUAL">My own knowledge</option>
          <option value="VERIFIED">Verified — read directly off the datasheet</option>
          <option value="UNVERIFIED">Unverified — web search / secondary source</option>
        </select>
      </div>
      <textarea id="note-text" class="note-textarea" placeholder="What did you find?" rows="2"></textarea>
      <div class="note-composer-row" id="note-source-row" hidden>
        <input type="text" id="note-source" class="note-source-input" placeholder="${escapeAttr(sourcePlaceholder)}">
      </div>
      <div class="note-composer-actions">
        <label class="note-page-label">page <input type="number" id="note-page" min="1" value="${datasheetName ? 1 : ""}"></label>
        <span id="note-error" class="editor-error"></span>
        <button type="button" id="note-save-btn" class="btn small primary">Add note</button>
      </div>
    </div>`;
}

// Shared by selectPart() and openCardFromList() -- both entry points to
// "look at one card" render the same PDF-pane + markdown + note-composer
// shape, so the shape (and its wiring) lives once, not twice.
function cardPaneHTML({ file, title, origin, markdown, datasheetName }) {
  const hasPdf = !!datasheetName;
  const pdfUrl = hasPdf ? `/datasheets/${encodeURIComponent(datasheetName)}` : null;
  currentPdfPage = 1;
  return `
    <div class="card-pane ${hasPdf ? "with-pdf" : ""}">
      ${hasPdf ? `
      <div class="pdf-pane">
        <div class="pdf-pane-head">
          <span class="pdf-pane-title" title="${escapeAttr(datasheetName)}">${escapeHtml(datasheetName)}</span>
          <label class="pdf-page-jump">p. <input type="number" min="1" id="pdf-page-input" value="1"></label>
        </div>
        <iframe class="pdf-frame" id="pdf-frame" data-base-src="${escapeAttr(pdfUrl)}" src="${escapeAttr(pdfUrl)}#page=1" title="${escapeAttr(datasheetName)}"></iframe>
      </div>` : `<p class="placeholder pdf-pane-missing">No PDF datasheet declared in this card's <code>**Datasheet:**</code> header — nothing to embed here.</p>`}
      <div class="card-pane-content">
        <h2 class="section-title">${escapeHtml(title)}</h2>
        <p class="source-tag">cradle_sidecar/data/components/${escapeHtml(file)} ${originBadge(origin)}
          <button type="button" class="btn small edit-card-btn" data-file="${escapeAttr(file)}">Edit</button></p>
        <div class="markdown card-markdown">${renderMarkdown(markdown)}</div>
        ${noteComposerHTML(datasheetName)}
      </div>
    </div>
  `;
}

function wireCardPane(container, { file, onSaved }) {
  enhanceRenderedMarkdown(container);
  wireProvenancePageLinks(container);
  wireMarkdownLinks(container.querySelector(".card-markdown"), "cradle_sidecar/data/components");

  const pageInput = container.querySelector("#pdf-page-input");
  if (pageInput) pageInput.addEventListener("change", () => setPdfPage(parseInt(pageInput.value, 10) || 1));

  const notePageInput = container.querySelector("#note-page");
  if (notePageInput) notePageInput.addEventListener("input", () => { notePageInput.dataset.userEdited = "1"; });

  const tagSelect = container.querySelector("#note-tag");
  const sourceRow = container.querySelector("#note-source-row");
  if (tagSelect) {
    tagSelect.addEventListener("change", () => { sourceRow.hidden = tagSelect.value === "MANUAL"; });
  }

  const editBtn = container.querySelector(".edit-card-btn");
  if (editBtn) {
    editBtn.addEventListener("click", async () => {
      const existing = await api(`/api/card/${encodeURIComponent(editBtn.dataset.file)}`);
      openCardEditor({ filename: editBtn.dataset.file, isNew: false, markdown: existing.markdown, onSaved });
    });
  }

  const saveBtn = container.querySelector("#note-save-btn");
  if (saveBtn) {
    saveBtn.addEventListener("click", async () => {
      const errorEl = container.querySelector("#note-error");
      errorEl.textContent = "";
      const text = container.querySelector("#note-text").value.trim();
      const tag = tagSelect.value;
      const source = container.querySelector("#note-source").value.trim();
      const page = container.querySelector("#note-page").value;
      if (!text) { errorEl.textContent = "Note text is required."; return; }
      if (tag !== "MANUAL" && !source) { errorEl.textContent = "Source citation is required for Verified/Unverified."; return; }
      try {
        await api(`/api/card/${encodeURIComponent(file)}/note`, {
          method: "POST",
          body: JSON.stringify({ text, tag, source: source || undefined, page: page ? parseInt(page, 10) : undefined }),
        });
        if (onSaved) await onSaved();
      } catch (e) {
        errorEl.textContent = `Save failed: ${e.message}`;
      }
    });
  }
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

  if (data.vision_md) {
    html += `<section class="block vision">
      <h2 class="section-title">Project vision <span class="source-tag">docs/architecture.md</span></h2>
      <div class="markdown">${renderMarkdown(data.vision_md)}</div>
    </section>`;
  }

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
  enhanceRenderedMarkdown(panel);
  wireMarkdownLinks(panel.querySelector(".block.vision .markdown"), "docs");
  wireMarkdownLinks(panel.querySelector(".block.descriptor .markdown"), "docs");
  wireMarkdownLinks(panel.querySelector(".conventions .markdown"), "docs");
  wireMarkdownLinks(panel.querySelector(".contracts .preamble"), "cradle_sidecar/data");

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
      enhanceRenderedMarkdown(detail);
      selectedDesignator = null;
      document.querySelectorAll("#part-list li").forEach((li) => li.classList.remove("selected"));
    });
  });
}

async function selectSheet(sheetId, btnEl) {
  currentView = "sheet";
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
  let html = "";
  if (!part.card) html += `<h2 class="section-title">${escapeHtml(part.designator)} — ${escapeHtml(part.name)}</h2>`;
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

  let cardHtml = "";
  let card = null;
  if (part.card) {
    card = await api(`/api/card/${encodeURIComponent(part.card.file)}`);
    cardHtml = cardPaneHTML({
      file: part.card.file,
      title: `${part.designator} — ${part.name}`,
      origin: part.card.origin,
      markdown: card.markdown,
      datasheetName: card.datasheet,
    });
  } else {
    cardHtml = `<p class="placeholder">No component card yet. If a datasheet exists, ask your agent to draft one
      first (it reads the PDF directly plus a web search, and leaves genuine gaps as blanks) — then come back
      here to review. Only start blank if there's truly nothing to draft from.
      <br><button type="button" class="btn small" id="create-card-for-part">+ Start card for ${escapeHtml(part.designator)}</button></p>`;
  }
  html += cardHtml;

  detail.innerHTML = html;
  detail.querySelectorAll(".open-file").forEach((btn) => {
    btn.addEventListener("click", () => openFile(btn.dataset.path));
  });
  if (card) wireCardPane(detail, { file: part.card.file, onSaved: () => selectPart(designator) });
  const createBtn = detail.querySelector("#create-card-for-part");
  if (createBtn) {
    createBtn.addEventListener("click", async () => {
      const tmpl = await api("/api/card_template");
      const prefill = tmpl.markdown
        .replace("<PART_NUMBER> — <short description>", `${part.name || "PART_NUMBER"} — <short description>`)
        .replace("<U?>", part.designator);
      openCardEditor({
        filename: `${(part.name || "NEWPART").toUpperCase().replace(/[^A-Z0-9_-]/g, "_")}.md`,
        isNew: true,
        markdown: prefill,
        onSaved: () => selectPart(designator),
      });
    });
  }
}

async function showRegistry(navBtn) {
  currentView = "registry";
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
  enhanceRenderedMarkdown(panel);
}

async function showCardsView(navBtn) {
  currentView = "cards";
  setActiveNav(navBtn);
  currentSheetData = null;
  selectedDesignator = null;
  $("#parts-placeholder").textContent = "All component cards";
  $("#parts-placeholder").style.display = "block";
  $("#part-list").innerHTML = "";

  const { cards } = await api("/api/cards");
  currentCardsList = cards;
  renderCardsMain(cards);
}

function renderCardsMain(cards, filterText = "") {
  const panel = $("#panel-main");
  const filtered = filterText
    ? cards.filter((c) => `${c.file} ${c.title} ${c.designator}`.toLowerCase().includes(filterText.toLowerCase()))
    : cards;

  let html = `<div class="cards-toolbar">
    <input type="text" id="cards-search" class="cards-search" placeholder="Filter by name, file, or designator…" value="${escapeAttr(filterText)}">
    <button type="button" id="new-card-btn" class="btn primary small">+ New card</button>
  </div>
  <p class="cards-toolbar-hint">If a datasheet exists, prefer asking your agent to draft the card first (reads the PDF directly + web search, leaves real gaps as blanks) — use <strong>+ New card</strong> mainly to review that draft or to start truly from scratch.</p>`;

  if (!filtered.length) {
    html += `<p class="placeholder">${cards.length ? "No cards match." : "No component cards yet."}</p>`;
  } else {
    html += `<ul class="cards-list">`;
    for (const c of filtered) {
      html += `<li class="cards-list-item" data-file="${escapeAttr(c.file)}">
        <div class="cards-list-main">
          <span class="ref">${escapeHtml(c.designator || "—")}</span>
          <span class="name">${escapeHtml(c.title)}</span>
        </div>
        <div class="cards-list-meta">
          ${originBadge(c.origin)}
          ${!c.designator_in_bom ? `<span class="badge badge-warn" title="Designator not found in the current BOM export">designator not in BOM</span>` : ""}
        </div>
      </li>`;
    }
    html += `</ul>`;
  }

  html += `<div class="block" id="cards-detail"></div>`;
  panel.innerHTML = html;

  $("#new-card-btn").addEventListener("click", async () => {
    const tmpl = await api("/api/card_template");
    openCardEditor({ filename: "", isNew: true, markdown: tmpl.markdown, onSaved: () => showCardsView(document.querySelector("#nav-cards")) });
  });
  $("#cards-search").addEventListener("input", (e) => renderCardsMain(cards, e.target.value));
  panel.querySelectorAll(".cards-list-item").forEach((li) => {
    li.addEventListener("click", () => openCardFromList(li.dataset.file));
  });
}

async function openCardFromList(filename) {
  const detail = $("#cards-detail");
  detail.innerHTML = "<p class='placeholder'>Loading…</p>";
  const card = await api(`/api/card/${encodeURIComponent(filename)}`);
  const meta = (currentCardsList || []).find((c) => c.file === filename) || {};
  detail.innerHTML = cardPaneHTML({
    file: filename,
    title: meta.title || filename,
    origin: meta.origin,
    markdown: card.markdown,
    datasheetName: card.datasheet,
  });
  wireCardPane(detail, { file: filename, onSaved: () => openCardFromList(filename) });
}

function openCardEditor({ filename, isNew, markdown, onSaved }) {
  editorState = { filename, isNew, onSaved };
  $("#editor-title").textContent = isNew ? "New component card" : `Edit ${filename}`;
  const filenameInput = $("#editor-filename");
  filenameInput.value = filename;
  filenameInput.disabled = !isNew;
  $("#editor-textarea").value = markdown || "";
  $("#editor-error").textContent = "";
  $("#editor-lint-summary").textContent = "";
  $("#editor-lint-results").innerHTML = "";
  $("#card-editor-dialog").showModal();
  runEditorLint(); // surface remaining blanks/issues immediately, not just on request
}

const PLACEHOLDER_RE_JS = /<[A-Za-z][^<>\n]{0,60}>/g;

function jumpToNextPlaceholder() {
  const ta = $("#editor-textarea");
  const text = ta.value;
  PLACEHOLDER_RE_JS.lastIndex = ta.selectionEnd || 0;
  let m = PLACEHOLDER_RE_JS.exec(text);
  if (!m) {
    PLACEHOLDER_RE_JS.lastIndex = 0;
    m = PLACEHOLDER_RE_JS.exec(text);
  }
  if (!m) {
    $("#editor-lint-summary").textContent = "No placeholders left.";
    $("#editor-lint-summary").className = "lint-summary lint-clean";
    return;
  }
  ta.focus();
  ta.setSelectionRange(m.index, m.index + m[0].length);
  const linesBefore = text.slice(0, m.index).split("\n").length;
  const lineHeight = parseFloat(getComputedStyle(ta).lineHeight) || 18;
  ta.scrollTop = Math.max(0, (linesBefore - 3) * lineHeight);
}

function closeCardEditor() {
  $("#card-editor-dialog").close();
  editorState = null;
}

function insertManualTag() {
  const ta = $("#editor-textarea");
  const date = new Date().toISOString().slice(0, 10);
  const tag = `[MANUAL — user, ${date}]`;
  const start = ta.selectionStart ?? ta.value.length;
  const end = ta.selectionEnd ?? ta.value.length;
  ta.value = ta.value.slice(0, start) + tag + ta.value.slice(end);
  ta.focus();
  ta.selectionStart = ta.selectionEnd = start + tag.length;
}

async function runEditorLint() {
  const { findings } = await api("/api/lint", { method: "POST", body: JSON.stringify({ markdown: $("#editor-textarea").value }) });
  const summary = $("#editor-lint-summary");
  const results = $("#editor-lint-results");
  summary.textContent = findings.length ? `${findings.length} finding(s)` : "Clean";
  summary.className = "lint-summary " + (findings.length ? "lint-issues" : "lint-clean");
  results.innerHTML = findings
    .map((f) => `<li class="lint-finding"><span class="badge">${escapeHtml(f.kind)}</span> ${f.line ? `line ${f.line}: ` : ""}${escapeHtml(f.message)}</li>`)
    .join("");
}

async function saveEditorCard() {
  if (!editorState) return;
  const errorEl = $("#editor-error");
  errorEl.textContent = "";
  let filename = editorState.isNew ? $("#editor-filename").value.trim() : editorState.filename;
  if (editorState.isNew && !filename.endsWith(".md")) filename += ".md";
  if (!filename || filename === ".md") {
    errorEl.textContent = "File name required.";
    return;
  }
  try {
    const result = await api(`/api/card/${encodeURIComponent(filename)}`, {
      method: "POST",
      body: JSON.stringify({ markdown: $("#editor-textarea").value, overwrite: !editorState.isNew }),
    });
    const onSaved = editorState.onSaved;
    closeCardEditor();
    await loadFreshness();
    if (onSaved) await onSaved();
  } catch (e) {
    errorEl.textContent = e.message.includes("already exists")
      ? "A card with that file name already exists — pick another name or open it to edit."
      : `Save failed: ${e.message}`;
  }
}

async function openFile(path) {
  await api("/api/open", { method: "POST", body: JSON.stringify({ path }) });
}

const USAGE_STORAGE_KEY = "sidecar_total_usage_seconds";
let usageBaseline = 0;
let usageSessionStart = null;

function formatDuration(totalSeconds) {
  const h = Math.floor(totalSeconds / 3600);
  const m = Math.floor((totalSeconds % 3600) / 60);
  const s = totalSeconds % 60;
  if (h > 0) return `${h}h ${m}m ${s}s`;
  if (m > 0) return `${m}m ${s}s`;
  return `${s}s`;
}

// Recomputes and paints the usage numbers from the fixed session-start
// timestamp -- safe to call as often as we like (every tick, and once
// immediately whenever Home is redisplayed) since it never resets the
// clock itself, only reads it.
function updateUsageDisplay() {
  if (usageSessionStart === null) return;
  const sessionElapsed = Math.floor((Date.now() - usageSessionStart) / 1000);
  localStorage.setItem(USAGE_STORAGE_KEY, String(usageBaseline + sessionElapsed));
  const sessionEl = $("#usage-session");
  const totalEl = $("#usage-total");
  if (sessionEl) sessionEl.textContent = formatDuration(sessionElapsed);
  if (totalEl) totalEl.textContent = formatDuration(usageBaseline + sessionElapsed);
}

// Called exactly once, from init() -- the session clock has to start at
// actual page load and never reset after that. Previously this ran again
// every time showHome() rendered, which reset sessionStart to "now" on
// every visit to Home, so "this session" only ever showed the time since
// the *last* time you looked at Home, not since the page was opened. The
// ongoing interval keeps persisting to localStorage regardless of which
// view is on screen; only the DOM update in updateUsageDisplay() is
// conditional on Home actually being open.
function startUsageTimer() {
  usageBaseline = parseInt(localStorage.getItem(USAGE_STORAGE_KEY) || "0", 10);
  usageSessionStart = Date.now();
  updateUsageDisplay();
  setInterval(updateUsageDisplay, 1000);
}

function statTile(value, label, opts = {}) {
  const cls = opts.extraClass || "";
  const idAttr = opts.id ? ` id="${escapeAttr(opts.id)}"` : "";
  return `<div class="stat-tile"><span class="stat-value ${cls}"${idAttr}>${escapeHtml(String(value))}</span><span class="stat-label">${escapeHtml(label)}</span></div>`;
}

async function showHome() {
  currentView = "home";
  setActiveNav(null);
  currentSheetData = null;
  selectedDesignator = null;
  $("#parts-placeholder").textContent = "Home";
  $("#parts-placeholder").style.display = "block";
  $("#part-list").innerHTML = "";

  const panel = $("#panel-main");
  panel.innerHTML = "<p class='placeholder'>Loading…</p>";

  const stats = await api("/api/home");
  const ps = stats.pin_status;
  const totalPins = ps.Decided + ps.Open + ps["Not addressed"] + ps.other;
  const decidedPct = totalPins ? Math.round((ps.Decided / totalPins) * 100) : 0;
  const rs = stats.registry_summary;

  panel.innerHTML = `
    <section class="block home-hero">
      <h2 class="section-title">Welcome back</h2>
      <p class="placeholder">
        Live, deterministic snapshot of the Cradle co-design state — every number below is
        recomputed from the same BOM/netlist/card files <code>project_refresh.py</code> reads,
        not cached or randomized. Click a sheet on the left, or
        <span class="source-tag">Component cards</span> in the nav, to dig in.
      </p>
      <p class="source-tag">${escapeHtml(stats.freshness)}</p>
    </section>

    <section class="block home-usage">
      <h2 class="section-title">Sidecar usage</h2>
      <div class="stat-row">
        ${statTile("0s", "this session", { extraClass: "usage-value", id: "usage-session" })}
        ${statTile("0s", "all-time, this browser", { extraClass: "usage-value", id: "usage-total" })}
      </div>
    </section>

    <section class="block home-stats">
      <h2 class="section-title">Project stats</h2>
      <div class="stat-row">
        ${statTile(stats.bom_designators, "BOM designators")}
        ${statTile(stats.netlist_components, "components in netlist")}
        ${statTile(stats.net_count, "nets")}
        ${statTile(stats.sheet_count, "sheets")}
        ${statTile(stats.card_count, "component cards")}
        ${statTile(stats.datasheet_count, "datasheets on file")}
      </div>
    </section>

    <section class="block home-progress">
      <h2 class="section-title">Wiring progress <span class="source-tag">pin Status, across all cards</span></h2>
      <div class="stat-row">
        ${statTile(ps.Decided, "Decided", { extraClass: "status-decided" })}
        ${statTile(ps.Open, "Open", { extraClass: "status-open" })}
        ${statTile(ps["Not addressed"], "Not addressed", { extraClass: "status-not-addressed" })}
      </div>
      <p class="registry-summary">${totalPins ? `${decidedPct}% of ${totalPins} documented pin row(s) Decided` : "No pin rows documented yet."}</p>
    </section>

    <section class="block home-registry">
      <h2 class="section-title">Net registry <span class="source-tag">net-registry.md</span></h2>
      <p class="registry-summary">${rs.present}/${rs.total} in netlist · ${rs.missing} missing · ${rs.single_member} single-member</p>
    </section>
  `;

  updateUsageDisplay();
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
    if (currentView === "sheet" && currentSheetData) {
      const btn = document.querySelector(`.sheet-btn[data-sheet="${currentSheetData.bom_sheet}"]`);
      await selectSheet(currentSheetData.bom_sheet, btn);
      if (selectedDesignator) await selectPart(selectedDesignator);
    } else if (currentView === "home") {
      await showHome();
    } else if (currentView === "registry") {
      await showRegistry(document.querySelector("#nav-registry"));
    } else if (currentView === "cards") {
      await showCardsView(document.querySelector("#nav-cards"));
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
  startUsageTimer();
  $("#refresh-btn").addEventListener("click", runRefresh);
  $("#brand-home").addEventListener("click", () => showHome());
  $("#nav-registry").addEventListener("click", (e) => showRegistry(e.target));
  $("#nav-cards").addEventListener("click", (e) => showCardsView(e.target));
  $("#jump-blank-btn").addEventListener("click", jumpToNextPlaceholder);
  $("#insert-manual-tag").addEventListener("click", insertManualTag);
  $("#editor-lint-btn").addEventListener("click", runEditorLint);
  $("#editor-save-btn").addEventListener("click", saveEditorCard);
  $("#editor-cancel-btn").addEventListener("click", closeCardEditor);
  $("#toggle-ambiguous").addEventListener("click", () => {
    showAmbiguousParts = !showAmbiguousParts;
    $("#toggle-ambiguous").textContent = showAmbiguousParts ? "− hide ambiguous" : "+ ambiguous BOM rows";
    if (currentSheetData) renderPartsList(currentSheetData.parts);
  });

  const overview = await api("/api/overview");
  await loadFreshness();
  renderSheets(overview.sheets);
  await showHome();
}

init().catch((e) => {
  $("#panel-main").innerHTML = `<p style="color:#f08080">Failed to load: ${escapeHtml(e.message)}</p>`;
});
