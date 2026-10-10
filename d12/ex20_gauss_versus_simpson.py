"""The same count of evaluations, spent two ways."""
import numpy as np

from nmkit.quad import gauss_legendre, simpson_n

cases = [("exp(t) on [0, 1]", np.exp, 0.0, 1.0, np.e - 1.0),
         ("sin(t) on [0, pi]", np.sin, 0.0, np.pi, 2.0),
         ("sqrt(t) on [0, 1]", np.sqrt, 0.0, 1.0, 2.0 / 3.0)]

print(f"{'integrand':>20} {'calls':>7} {'Simpson':>13} {'Gauss':>13}")
for name, f, a, b, exact in cases:
    for n in (4, 8):
        es = abs(simpson_n(f, a, b, n) - exact)
        eg = abs(gauss_legendre(f, a, b, n + 1) - exact)
        print(f"{name if n == 4 else '':>20} {n + 1:>7} {es:>13.3e} {eg:>13.3e}")
print()
print("Gauss wins by decades on the smooth rows and by a factor of about twenty on the")
print("square root, whose derivative is unbounded at zero.")
