"""Problem 1.37: measure epsilon in two formats, and report each as a power of two."""
import math

import numpy as np

for name, dt in (("float32", np.float32), ("float64", np.float64)):
    one = dt(1.0)
    e = dt(1.0)
    while dt(one + e / dt(2.0)) != one:
        e = dt(e / dt(2.0))
    print(f"{name}: epsilon = {float(e):.8e}  =  2 ** {round(math.log2(float(e)))}")

print("numpy agrees:", float(np.finfo(np.float32).eps), float(np.finfo(np.float64).eps))
