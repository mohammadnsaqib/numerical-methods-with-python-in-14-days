"""Problem 2.40: every real root of a polynomial, checked against an independent solver.
"""
import numpy as np

from nmkit.roots import bracket_scan, bisect

coeffs = [1.0, -6.0, 11.0, -6.0]          # x**3 - 6x**2 + 11x - 6

def f(x):
    return np.polyval(coeffs, x)

mine = [bisect(f, a, b, tol=1e-14).root for a, b in bracket_scan(f, -1.0, 5.0, n=300)]
theirs = sorted(r.real for r in np.roots(coeffs) if abs(r.imag) < 1e-12)

print("bisection :", [f"{r:.12f}" for r in mine])
print("np.roots  :", [f"{r:.12f}" for r in theirs])
print("largest gap:", f"{max(abs(a - b) for a, b in zip(mine, theirs)):.3e}")
