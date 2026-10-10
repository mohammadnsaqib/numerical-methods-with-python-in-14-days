"""A routine is trusted once an independent implementation agrees with it."""
import math

from scipy.optimize import brentq

from nmkit.roots import bisect, false_position

cases = [("cos", math.cos, 0.0, 3.0),
         ("exp(x)-3", lambda x: math.exp(x) - 3.0, 0.0, 2.0),
         ("x**3-2x-5", lambda x: x ** 3 - 2 * x - 5, 2.0, 3.0)]
print(f"{'case':<12}{'bisect':>20}{'false pos':>20}{'brentq':>20}{'max gap':>11}")
for name, f, a, b in cases:
    bi = bisect(f, a, b, tol=1e-15).root
    fp = false_position(f, a, b, tol=1e-15, max_iter=500).root
    bq = brentq(f, a, b, xtol=1e-15, rtol=8.9e-16)
    print(f"{name:<12}{bi:>20.15f}{fp:>20.15f}{bq:>20.15f}"
          f"{max(abs(bi - bq), abs(fp - bq)):>11.1e}")
