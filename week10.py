import numpy as np
import time


class Week10:
    def run(self):
        start = time.time()
        arr = np.random.default_rng().random(10**6)
        end = time.time()
        self.time_new = end - start
        print(f"Method: default_rng().random")
        print(f"Time: {self.time_new:.6f} seconds")


if __name__ == '__main__':
    Week10().run()
