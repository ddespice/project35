import json

from flask import Flask, jsonify, send_file

from week12 import Week12
from week13 import Week13


class Week14:
    """Flask GET endpoint serving averaged times from the same versioned file."""

    def __init__(self):
        self.app = Flask(__name__)
        self._register_routes()

    def _ensure_results(self):
        if not Week12.OUTPUT.exists():
            Week12().run()
        return json.loads(Week12.OUTPUT.read_text())

    def _register_routes(self):
        @self.app.get("/timings")
        def timings():
            payload = self._ensure_results()
            return jsonify(
                {
                    "version": payload["version"],
                    "generated_at": payload["generated_at"],
                    "size": payload["size"],
                    "repeats": payload["repeats"],
                    "averages": {
                        method: data["mean"]
                        for method, data in payload["results"].items()
                    },
                }
            )

        @self.app.get("/chart.png")
        def chart():
            if not Week13.OUTPUT.exists():
                Week13().run()
            return send_file(Week13.OUTPUT, mimetype="image/png")

        @self.app.get("/")
        def index():
            return jsonify(
                {
                    "endpoints": ["/timings", "/chart.png"],
                    "variant": 35,
                }
            )

    def run(self, host="127.0.0.1", port=5000):
        print(f"Serving on http://{host}:{port}/timings")
        self.app.run(host=host, port=port)


if __name__ == "__main__":
    Week14().run()
