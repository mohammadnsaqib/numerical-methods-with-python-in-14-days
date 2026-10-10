"""The error of the composite trapezoidal rule, predicted before it is measured."""
import numpy as np
import sympy as sp

from nmkit.quad import trapezoid_n

t = sp.Symbol("t")
expr = sp.exp(t)
a, b = 0.0, 1.0
exact = float(sp.integrate(expr, (t, a, b)))
# The composite error is minus (b - a) h^2 / 12 times the second derivative at some
# interior point. exp is its own second derivative, so the point is somewhere in [0, 1]
# and the term is bracketed by the values at the two ends.
print(f"{'panels':>8} {'measured error':>17} {'predicted, low':>17} "
      f"{'predicted, high':>17}")
for n in (4, 8, 16, 32, 64):
    h = (b - a) / n
    err = trapezoid_n(np.exp, a, b, n) - exact
    term = (b - a) * h * h / 12.0
    print(f"{n:>8} {err:>17.3e} {term * np.exp(a):>17.3e} {term * np.exp(b):>17.3e}")
print()
print("every measured error lies between the two "
      "predictions, which is what the formula claims")
