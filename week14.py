import json

import uvicorn
from fastapi import FastAPI
from fastapi.responses import FileResponse

from week12 import Week12
from week13 import Week13


class Week14:
    """FastAPI GET endpoint serving averaged times from the same versioned file."""

    def __init__(self):
        self.app = FastAPI(title="project35 — Variant 35")
        self._register_routes()

    def _ensure_results(self):
        if not Week12.OUTPUT.exists():
            Week12().run()
        return json.loads(Week12.OUTPUT.read_text())

    def _register_routes(self):
        @self.app.get("/")
        def index():
            return {"endpoints": ["/timings", "/chart.png"], "variant": 35}

        @self.app.get("/timings")
        def timings():
            payload = self._ensure_results()
            return {
                "version": payload["version"],
                "generated_at": payload["generated_at"],
                "size": payload["size"],
                "repeats": payload["repeats"],
                "averages": {
                    method: data["mean"]
                    for method, data in payload["results"].items()
                },
            }

        @self.app.get("/chart.png")
        def chart():
            if not Week13.OUTPUT.exists():
                Week13().run()
            return FileResponse(Week13.OUTPUT, media_type="image/png")

    def run(self, host="127.0.0.1", port=8000):
        print(f"Serving on http://{host}:{port}/timings")
        uvicorn.run(self.app, host=host, port=port)


if __name__ == "__main__":
    Week14().run()
