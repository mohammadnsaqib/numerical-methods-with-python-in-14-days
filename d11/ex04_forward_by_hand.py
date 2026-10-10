"""One forward difference, every intermediate quantity printed."""
import numpy as np

x, h = 1.0, 0.1
a, b = np.sin(x), np.sin(x + h)
print(f"f(x)     = sin(1.0)   = {a:.15f}")
print(f"f(x + h) = sin(1.1)   = {b:.15f}")
print(f"numerator             = {b - a:.15f}")
print(f"divided by h = 0.1    = {(b - a) / h:.15f}")
print(f"the exact derivative  = {np.cos(x):.15f}")
print(f"error                 = {abs((b - a) / h - np.cos(x)):.15f}")
