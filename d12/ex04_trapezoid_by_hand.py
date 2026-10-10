"""One trapezoidal panel, every intermediate quantity printed."""
import numpy as np

a, b = 0.0, 1.0
fa, fb = np.exp(a), np.exp(b)
print(f"f(a) = exp(0) = {fa:.15f}")
print(f"f(b) = exp(1) = {fb:.15f}")
print(f"their average = {(fa + fb) / 2:.15f}")
print(f"times the width {b - a} = {(b - a) * (fa + fb) / 2:.15f}")
print(f"the exact integral      = {np.e - 1:.15f}")
print(f"error                   = {abs((b - a) * (fa + fb) / 2 - (np.e - 1)):.15f}")
