#!/usr/bin/env python3
"""
Cradle sidecar v0 — localhost co-design companion.

Mostly read-only views of cradle_sidecar/data/, plus a few write-capable
actions: POST /api/refresh runs project_refresh.py (same as the agent
workflow), and POST /api/card/<name> creates or updates a component card
(the manual-card-authoring path — for parts whose datasheet is missing,
scrambled, or otherwise unusable for automated extraction). POST /api/lint
runs the same structural check as tools/card_lint.py against draft text.

Does NOT run datasheet_index or invoke AI. Those stay in the agent/CLI
path. Open http://127.0.0.1:8765/ while working in Altium.

Usage (from repo root):
    python cradle_sidecar/app/server.py
"""

import json
import mimetypes
import os
import subprocess
import sys
from http.server import BaseHTTPRequestHandler, ThreadingHTTPServer
from pathlib import Path
from urllib.parse import parse_qs, unquote, urlparse

APP_DIR = Path(__file__).resolve().parent
REPO_ROOT = APP_DIR.parent.parent
TOOLS_DIR = APP_DIR.parent / "tools"
STATIC_DIR = APP_DIR / "static"

sys.path.insert(0, str(TOOLS_DIR))
import data_api  # noqa: E402
from paths import SIDECAR_DEFAULT_PORT  # noqa: E402


def run_project_refresh():
    script = REPO_ROOT / "cradle_sidecar" / "tools" / "project_refresh.py"
    proc = subprocess.run(
        [sys.executable, str(script)],
        cwd=str(REPO_ROOT),
        capture_output=True,
        text=True,
        timeout=120,
    )
    return {
        "exit_code": proc.returncode,
        "stdout": proc.stdout,
        "stderr": proc.stderr,
    }


def json_response(handler, status, payload):
    body = json.dumps(payload, indent=2).encode("utf-8")
    handler.send_response(status)
    handler.send_header("Content-Type", "application/json; charset=utf-8")
    handler.send_header("Content-Length", str(len(body)))
    handler.end_headers()
    handler.wfile.write(body)


class SidecarHandler(BaseHTTPRequestHandler):
    def log_message(self, fmt, *args):
        pass

    def do_GET(self):
        parsed = urlparse(self.path)
        path = parsed.path

        if path in ("/", "/index.html"):
            return self._serve_static("index.html", "text/html; charset=utf-8")
        if path.startswith("/static/"):
            rel = path[len("/static/") :]
            return self._serve_static(rel)

        if path == "/api/overview":
            return json_response(self, 200, {
                "freshness": data_api.freshness(),
                "sheets": data_api.list_sheets(),
                "cards": data_api.list_cards(),
            })
        if path == "/api/sheets":
            return json_response(self, 200, data_api.list_sheets())
        if path.startswith("/api/sheet/"):
            sheet_id = path.split("/")[-1]
            if not sheet_id.isdigit():
                return json_response(self, 400, {"error": "invalid sheet id"})
            return json_response(self, 200, data_api.sheet_detail(sheet_id))
        if path.startswith("/api/card/"):
            name = path.split("/api/card/", 1)[1]
            if ".." in name or "/" in name:
                return json_response(self, 400, {"error": "invalid card name"})
            content = data_api.read_card(name)
            if content is None:
                return json_response(self, 404, {"error": "card not found"})
            return json_response(self, 200, {
                "file": name,
                "markdown": content,
                "datasheet": data_api.extract_datasheet_name(content),
            })
        if path == "/api/registry":
            return json_response(self, 200, data_api.registry_with_checks())
        if path == "/api/freshness":
            return json_response(self, 200, {"freshness": data_api.freshness()})
        if path == "/api/cards":
            return json_response(self, 200, {"cards": data_api.list_cards()})
        if path == "/api/card_template":
            return json_response(self, 200, {"markdown": data_api.read_template()})
        if path == "/api/home":
            return json_response(self, 200, data_api.homepage_stats())
        if path.startswith("/datasheets/"):
            name = path[len("/datasheets/") :]
            asset = data_api.read_datasheet(unquote(name))
            if asset is None:
                return self.send_error(404)
            self.send_response(200)
            self.send_header("Content-Type", asset["mime"])
            self.send_header("Content-Length", str(len(asset["bytes"])))
            self.end_headers()
            return self.wfile.write(asset["bytes"])

        self.send_error(404)

    def do_POST(self):
        parsed = urlparse(self.path)
        length = int(self.headers.get("Content-Length", 0))
        raw = self.rfile.read(length).decode("utf-8") if length else "{}"
        try:
            body = json.loads(raw) if raw.strip() else {}
        except json.JSONDecodeError:
            body = {}

        if parsed.path == "/api/refresh":
            result = run_project_refresh()
            result["freshness"] = data_api.freshness()
            return json_response(self, 200, result)

        if parsed.path.startswith("/api/card/") and parsed.path.endswith("/note"):
            name = parsed.path[len("/api/card/") : -len("/note")]
            result = data_api.add_card_note(
                name, body.get("text", ""), body.get("tag", ""), body.get("source"), body.get("page"),
            )
            status = 200 if result.get("ok") else (404 if result.get("error") == "card does not exist" else 400)
            return json_response(self, status, result)

        if parsed.path.startswith("/api/card/"):
            name = parsed.path.split("/api/card/", 1)[1]
            markdown = body.get("markdown", "")
            overwrite = bool(body.get("overwrite", False))
            if not name or ".." in name or "/" in name:
                return json_response(self, 400, {"error": "invalid card name"})
            result = data_api.write_card(name, markdown, overwrite)
            status = 200 if result.get("ok") else (409 if result.get("error") == "card already exists" else 400)
            return json_response(self, status, result)

        if parsed.path == "/api/lint":
            findings = data_api.lint_card_text(body.get("markdown", ""))
            return json_response(self, 200, {"findings": findings})

        if parsed.path == "/api/open":
            rel = body.get("path", "")
            if not data_api.is_safe_open_path(REPO_ROOT, rel):
                return json_response(self, 400, {"error": "path not allowed"})
            full = (REPO_ROOT / rel).resolve()
            try:
                if sys.platform == "win32":
                    os.startfile(full)  # noqa: S606
                elif sys.platform == "darwin":
                    subprocess.run(["open", str(full)], check=False)
                else:
                    subprocess.run(["xdg-open", str(full)], check=False)
            except OSError as e:
                return json_response(self, 500, {"error": str(e)})
            return json_response(self, 200, {"opened": rel})

        json_response(self, 404, {"error": "not found"})

    def _serve_static(self, rel_path, content_type=None):
        safe = Path(rel_path)
        if ".." in safe.parts:
            self.send_error(403)
            return
        full = STATIC_DIR / safe
        if not full.is_file():
            self.send_error(404)
            return
        data = full.read_bytes()
        if content_type is None:
            content_type = mimetypes.guess_type(str(full))[0] or "application/octet-stream"
        self.send_response(200)
        self.send_header("Content-Type", content_type)
        self.send_header("Content-Length", str(len(data)))
        self.end_headers()
        self.wfile.write(data)


def main():
    port = int(os.environ.get("CRADLE_SIDECAR_PORT", SIDECAR_DEFAULT_PORT))
    os.chdir(REPO_ROOT)
    server = ThreadingHTTPServer(("127.0.0.1", port), SidecarHandler)
    print(f"Cradle sidecar v0 — http://127.0.0.1:{port}/")
    print("Read-only co-design views. Refresh button runs project_refresh.py only.")
    print("Press Ctrl+C to stop.")
    try:
        server.serve_forever()
    except KeyboardInterrupt:
        print("\nStopped.")
        server.server_close()


if __name__ == "__main__":
    main()
