"""Finding which piece a point falls in costs the logarithm of the count, not the count.
"""
import numpy as np

for n in (10, 100, 1000, 10000, 100000):
    print(f"{n:>7} knots: a linear scan looks at {n // 2:>6} on average, "
          f"a binary search at {int(np.ceil(np.log2(n))):>3}")
