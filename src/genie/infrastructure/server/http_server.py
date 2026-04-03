import json
from http.server import BaseHTTPRequestHandler, ThreadingHTTPServer
from typing import Any

from genie.infrastructure.server.server_edge import LocalServerEdge, ServerPromptRequest


class LocalHttpServer:
    def __init__(self, edge: LocalServerEdge, host: str = "127.0.0.1", port: int = 8765) -> None:
        self._edge = edge
        self._host = host
        self._port = port
        self._server = ThreadingHTTPServer((host, port), self._build_handler())

    def _build_handler(self) -> type[BaseHTTPRequestHandler]:
        edge = self._edge

        class Handler(BaseHTTPRequestHandler):
            def _write_json(self, status_code: int, payload: dict[str, Any]) -> None:
                encoded = json.dumps(payload).encode("utf-8")
                self.send_response(status_code)
                self.send_header("Content-Type", "application/json")
                self.send_header("Content-Length", str(len(encoded)))
                self.end_headers()
                self.wfile.write(encoded)

            def do_GET(self) -> None:  # noqa: N802
                if self.path != "/health":
                    self._write_json(404, {"error": "not_found"})
                    return
                self._write_json(200, edge.health())

            def do_POST(self) -> None:  # noqa: N802
                if self.path != "/prompt":
                    self._write_json(404, {"error": "not_found"})
                    return
                content_length = self.headers.get("Content-Length")
                if content_length is None:
                    self._write_json(400, {"error": "missing_content_length"})
                    return
                try:
                    length = int(content_length)
                    raw = self.rfile.read(length)
                    body = json.loads(raw.decode("utf-8"))
                except (ValueError, json.JSONDecodeError):
                    self._write_json(400, {"error": "invalid_json"})
                    return

                prompt = body.get("prompt")
                if not isinstance(prompt, str) or not prompt.strip():
                    self._write_json(400, {"error": "invalid_prompt"})
                    return

                response = edge.handle_prompt_as_dict(ServerPromptRequest(prompt=prompt.strip()))
                self._write_json(200, response)

            def log_message(self, format: str, *args: Any) -> None:
                return

        return Handler

    @property
    def address(self) -> str:
        return f"http://{self._host}:{self._port}"

    def serve_forever(self) -> None:
        self._server.serve_forever()

    def shutdown(self) -> None:
        self._server.shutdown()
        self._server.server_close()
