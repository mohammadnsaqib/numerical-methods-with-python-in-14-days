"""One Simpson panel, every intermediate quantity printed."""
import numpy as np

a, b = 0.0, 1.0
m = (a + b) / 2
fa, fm, fb = np.exp(a), np.exp(m), np.exp(b)
print(f"f(a) = exp(0.0) = {fa:.15f}   weight 1")
print(f"f(m) = exp(0.5) = {fm:.15f}   weight 4")
print(f"f(b) = exp(1.0) = {fb:.15f}   weight 1")
print(f"weighted sum          = {fa + 4 * fm + fb:.15f}")
print(f"times width over six  = {(b - a) * (fa + 4 * fm + fb) / 6:.15f}")
print(f"the exact integral    = {np.e - 1:.15f}")
print(f"error                 = "
      f"{abs((b - a) * (fa + 4 * fm + fb) / 6 - (np.e - 1)):.9f}")
print(f"the trapezoidal rule was off by "
      f"{abs((b - a) * (fa + fb) / 2 - (np.e - 1)):.9f}")
