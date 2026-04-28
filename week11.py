import time
from pathlib import Path

import numpy as np
import pandas as pd


class Week11:
    """Two-row table: method name and seconds elapsed (one run each)."""

    OUTPUT = Path(__file__).parent / "outputs" / "comparison.csv"
    SIZE = 10 ** 6

    def _time_old(self):
        start = time.time()
        np.random.rand(self.SIZE)
        return time.time() - start

    def _time_new(self):
        start = time.time()
        np.random.default_rng().random(self.SIZE)
        return time.time() - start

    def run(self):
        rows = [
            {"method": "np.random.rand", "seconds": self._time_old()},
            {"method": "default_rng().random", "seconds": self._time_new()},
        ]
        df = pd.DataFrame(rows)
        self.OUTPUT.parent.mkdir(exist_ok=True)
        df.to_csv(self.OUTPUT, index=False)
        print(df.to_string(index=False))
        print(f"Saved: {self.OUTPUT}")
        return df


if __name__ == "__main__":
    Week11().run()
