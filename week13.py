import json
from pathlib import Path

import matplotlib

matplotlib.use("Agg")
import matplotlib.pyplot as plt

from week12 import Week12


class Week13:
    """Bar chart of mean execution times (reads the versioned results.json)."""

    INPUT = Week12.OUTPUT
    OUTPUT = Path(__file__).parent / "outputs" / "comparison.png"

    def _load(self):
        if not self.INPUT.exists():
            Week12().run()
        return json.loads(self.INPUT.read_text())

    def run(self):
        payload = self._load()
        results = payload["results"]
        methods = list(results.keys())
        means = [results[m]["mean"] for m in methods]

        fig, ax = plt.subplots(figsize=(6, 4))
        ax.bar(methods, means, color=["#4C72B0", "#55A868"])
        ax.set_ylabel("Mean time, seconds")
        ax.set_title(
            f"NumPy RNG comparison (size={payload['size']}, "
            f"repeats={payload['repeats']}, v{payload['version']})"
        )
        for i, value in enumerate(means):
            ax.text(i, value, f"{value:.5f}", ha="center", va="bottom")
        fig.tight_layout()

        self.OUTPUT.parent.mkdir(exist_ok=True)
        fig.savefig(self.OUTPUT, dpi=120)
        plt.close(fig)
        print(f"Saved: {self.OUTPUT}")
        return self.OUTPUT


if __name__ == "__main__":
    Week13().run()
