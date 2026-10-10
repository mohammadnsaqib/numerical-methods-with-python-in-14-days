"""Straight pieces meet at an angle, so the slope jumps at every knot."""
import numpy as np

xs = np.array([0.0, 1.0, 2.0, 3.0])
ys = np.array([0.0, 1.0, 0.0, 2.0])
slopes = np.diff(ys) / np.diff(xs)

print("slopes of the three pieces:", slopes)
for i in range(1, 3):
    print(f"at knot {i} (x = {xs[i]}): slope jumps from {slopes[i-1]:+.1f} "
          f"to {slopes[i]:+.1f}")
print("\nthe interpolant is continuous and its slope is not.")
