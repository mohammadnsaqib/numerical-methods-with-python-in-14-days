"""The honest comparison is error against work, not error against panel count."""
import numpy as np

from nmkit.quad import simpson_n, trapezoid_n

exact = np.e - 1.0
print(f"{'calls':>7} {'trapezoidal':>15} {'Simpson':>15} {'how many times':>16}")
for n in (4, 8, 16, 32, 64, 128):
    et = abs(trapezoid_n(np.exp, 0.0, 1.0, n) - exact)
    es = abs(simpson_n(np.exp, 0.0, 1.0, n) - exact)
    print(f"{n + 1:>7} {et:>15.3e} {es:>15.3e} {et / es:>16.1f}")
print()
print("both columns use the same points. Only the weights differ.")
