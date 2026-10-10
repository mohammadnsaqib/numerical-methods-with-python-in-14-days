"""The day's routines against an independent one, with a 40-digit value as the standard.
"""
import numpy as np
import scipy.integrate as si
from mpmath import cos as mpcos, exp as mpexp, mp, mpf, quad as mpquad, sqrt as mpsqrt

from nmkit.quad import adaptive_simpson, gauss_legendre, romberg, simpson_n

mp.dps = 40
cases = [("exp(-t^2)", lambda v: np.exp(-v * v), lambda v: mpexp(-v * v), 0.0, 2.0),
         ("cos(t)/(1+t)", lambda v: np.cos(v) / (1 + v), lambda v: mpcos(v) / (1 + v),
         0.0, 3.0),
         ("sqrt(1+t^3)", lambda v: np.sqrt(1 + v ** 3), lambda v: mpsqrt(1 + v ** 3),
         0.0, 1.5)]

print(f"{'integrand':>14} {'Simpson 64':>12} {'Romberg':>11} {'Gauss 10':>11} "
      f"{'adaptive':>11} {'scipy':>11}")
for name, f, g, a, b in cases:
    exact = float(mpquad(g, [mpf(a), mpf(b)]))
    row = [abs(simpson_n(f, a, b, 64) - exact),
           abs(romberg(f, a, b, levels=6)[5, 5] - exact),
           abs(gauss_legendre(f, a, b, 10) - exact),
           abs(adaptive_simpson(f, a, b, tol=1e-12)[0] - exact),
           abs(si.quad(f, a, b)[0] - exact)]
    print(f"{name:>14} " + " ".join(f"{v:>11.2e}" for v in row))
print()
print("every column is an error against a value computed at forty digits")
