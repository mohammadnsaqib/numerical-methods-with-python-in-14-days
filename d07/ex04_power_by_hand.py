"""Multiplying repeatedly amplifies the largest stretch until nothing else is left."""
import numpy as np

A = np.array([[3.0, 1.0], [1.0, 3.0]])
x = np.array([1.0, 0.0])
print(f"{'step':>5} {'direction':>28} {'Rayleigh quotient':>19}")
for k in range(1, 8):
    x = A @ x
    x = x / np.sqrt(x @ x)
    print(f"{k:>5} {np.array2string(x, precision=10):>28} {x @ (A @ x):>19.12f}")
print("\nthe true largest eigenvalue is 4.")
