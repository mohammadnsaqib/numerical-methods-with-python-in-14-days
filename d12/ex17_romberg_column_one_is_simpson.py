"""The first extrapolated column is not LIKE Simpson's rule. It is Simpson's rule."""
import numpy as np

from nmkit.quad import romberg, simpson_n

T = romberg(np.exp, 0.0, 1.0, levels=5)
print(f"{'panels':>8} {'Romberg column 1':>22} {'composite Simpson':>22} {'gap':>10}")
for i in range(1, 5):
    n = 2 ** i
    s = simpson_n(np.exp, 0.0, 1.0, n)
    print(f"{n:>8} {T[i, 1]:>22.16f} {s:>22.16f} {abs(T[i, 1] - s):>10.1e}")
print()
print("combining two trapezoidal estimates to cancel the h squared term produces")
print("exactly the weights 1, 4, 2, 4, 1 -- so the two are the same computation.")
