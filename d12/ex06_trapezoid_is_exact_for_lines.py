"""The rule reproduces a straight line and nothing above it."""
import numpy as np
import sympy as sp

from nmkit.quad import trapezoid

t = sp.Symbol("t")
print(f"{'integrand':>12} {'one panel':>18} {'exact':>18} {'error':>12}")
for expr in (sp.Integer(3), 2 * t + 1, t ** 2, t ** 3):
    f = sp.lambdify(t, expr, "numpy")
    exact = float(sp.integrate(expr, (t, 0, 2)))
    est = trapezoid(lambda v: float(f(v)), 0.0, 2.0)
    print(f"{str(expr):>12} {est:>18.12f} {exact:>18.12f} {abs(est - exact):>12.3e}")
print()
print("a constant and a straight line are reproduced. "
      "Degree 2 is where it starts to be wrong.")
