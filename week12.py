import json
import time
from datetime import datetime
from pathlib import Path

import numpy as np


class Week12:
    """Repeat 5 times for each method, store mean values with a version stamp."""

    OUTPUT = Path(__file__).parent / "outputs" / "results.json"
    SIZE = 10 ** 6
    REPEATS = 5
    VERSION = 1

    def _measure(self, fn):
        samples = []
        for _ in range(self.REPEATS):
            start = time.time()
            fn()
            samples.append(time.time() - start)
        return samples

    def run(self):
        old_samples = self._measure(lambda: np.random.rand(self.SIZE))
        new_samples = self._measure(lambda: np.random.default_rng().random(self.SIZE))

        payload = {
            "version": self.VERSION,
            "generated_at": datetime.utcnow().isoformat() + "Z",
            "size": self.SIZE,
            "repeats": self.REPEATS,
            "results": {
                "np.random.rand": {
                    "samples": old_samples,
                    "mean": float(np.mean(old_samples)),
                },
                "default_rng().random": {
                    "samples": new_samples,
                    "mean": float(np.mean(new_samples)),
                },
            },
        }

        self.OUTPUT.parent.mkdir(exist_ok=True)
        self.OUTPUT.write_text(json.dumps(payload, indent=2))

        for method, data in payload["results"].items():
            print(f"{method:<24} mean = {data['mean']:.6f} s")
        print(f"Saved: {self.OUTPUT} (version {self.VERSION})")
        return payload


if __name__ == "__main__":
    Week12().run()
