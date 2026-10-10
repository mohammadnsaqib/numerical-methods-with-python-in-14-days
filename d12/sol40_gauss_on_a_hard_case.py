"""Problem 12.40: where Gauss stops winning, and what the three cases have in common."""
import numpy as np
from mpmath import exp as mpexp, mp, mpf, quad as mpquad

from nmkit.quad import gauss_legendre, simpson_n

mp.dps = 40
cases = [
    ("exp(t), smooth",
     np.exp,
     float(mpquad(mpexp, [mpf(0), mpf(1)]))),
    ("|t - 0.5|, a corner",
     lambda v: abs(v - 0.5),
     0.25),
    ("a peak of width 0.01",
     lambda v: 1.0 / (1.0 + 1e4 * (v - 0.5) ** 2),
     float(mpquad(lambda u: 1 / (1 + mpf(10) ** 4 * (u - mpf("0.5")) ** 2),
                  [mpf(0), mpf("0.5"), mpf(1)]))),
]

print(f"{'integrand':>22} {'calls':>7} {'Simpson':>12} {'Gauss':>12}")
for name, f, exact in cases:
    for n in (16, 64):
        es = abs(simpson_n(f, 0.0, 1.0, n) - exact)
        eg = abs(gauss_legendre(f, 0.0, 1.0, n + 1) - exact)
        print(f"{name if n == 16 else '':>22} {n + 1:>7} {es:>12.3e} {eg:>12.3e}")
print()
print("Gauss assumes the integrand is close to one polynomial of high degree.")
print("A corner and a narrow peak both break that assumption, and Day 8 said why.")
