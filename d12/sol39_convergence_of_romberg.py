"""Problem 12.39: the order of each Romberg column, measured rather than claimed."""
import numpy as np

from nmkit.quad import romberg

exact = 2.0
T = romberg(np.sin, 0.0, np.pi, levels=8)
print(f"{'column':>8} {'order it should have':>22} {'measured order':>16}")
for j in range(4):
    rows = [i for i in range(j, 8) if abs(T[i, j] - exact) > 1e-13]
    if len(rows) < 3:
        print(f"{j:>8} {2 * j + 2:>22} {'at the floor':>16}")
        continue
    a, b = abs(T[rows[-2], j] - exact), abs(T[rows[-1], j] - exact)
    print(f"{j:>8} {2 * j + 2:>22} {np.log2(a / b):>16.4f}")
print()
print("each column removes one more error term, so each gains two orders")
