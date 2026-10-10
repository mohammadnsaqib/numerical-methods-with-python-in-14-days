"""Two points of exactness are free, and the third is not."""
import sympy as sp

from nmkit.quad import simpson, trapezoid

t = sp.Symbol("t")
print(f"{'degree':>7} {'trapezoidal':>14} {'Simpson':>14}")
for d in range(6):
    expr = t ** d
    f = sp.lambdify(t, expr, "numpy")
    exact = float(sp.integrate(expr, (t, 0, 2)))
    et = abs(trapezoid(lambda v: float(f(v)), 0.0, 2.0) - exact)
    es = abs(simpson(lambda v: float(f(v)), 0.0, 2.0) - exact)
    print(f"{d:>7} {et:>14.3e} {es:>14.3e}")
print()
print("Simpson fits a parabola and is exact for cubics as well, by symmetry.")
print("Degree 4 is where it stops.")
