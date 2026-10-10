"""One centred difference, every intermediate quantity printed."""
import numpy as np

x, h = 1.0, 0.1
a, b = np.sin(x - h), np.sin(x + h)
print(f"f(x - h) = sin(0.9)   = {a:.15f}")
print(f"f(x + h) = sin(1.1)   = {b:.15f}")
print(f"numerator             = {b - a:.15f}")
print(f"divided by 2h = 0.2   = {(b - a) / (2 * h):.15f}")
print(f"the exact derivative  = {np.cos(x):.15f}")
print(f"error                 = {abs((b - a) / (2 * h) - np.cos(x)):.15f}")
print()
print(f"the forward difference at the same step was off by "
      f"{abs((np.sin(x + h) - np.sin(x)) / h - np.cos(x)):.6f}")
