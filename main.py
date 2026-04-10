import numpy as np
import time

start = time.time()
arr = np.random.rand(10 ** 6)
end = time.time()

print(f"Method: np.random.rand")
print(f"Array size: {len(arr)}")
print(f"Time: {end - start:.6f} seconds")
