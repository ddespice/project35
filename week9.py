import numpy as np
import time


class Week9:
    def run(self):
        start = time.time()
        arr = np.random.rand(10**6)
        end = time.time()
        self.time_old = end - start
        print(f"Method: np.random.rand")
        print(f"Time: {self.time_old:.6f} seconds")


if __name__ == '__main__':
    Week9().run()
