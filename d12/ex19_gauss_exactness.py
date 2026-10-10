"""n points integrate degree 2n-1 exactly, and degree 2n not at all."""
import sympy as sp

from nmkit.quad import gauss_legendre

t = sp.Symbol("t")
print(f"{'n':>3} {'points':>8} {'exact up to degree':>20} {'error at 2n-1':>15} "
      f"{'error at 2n':>13}")
for n in (2, 3, 4, 5):
    errs = []
    for d in (2 * n - 1, 2 * n):
        expr = t ** d
        f = sp.lambdify(t, expr, "numpy")
        exact = float(sp.integrate(expr, (t, 0, 1)))
        errs.append(abs(gauss_legendre(lambda v: float(f(v)), 0.0, 1.0, n) - exact))
    print(f"{n:>3} {n:>8} {2 * n - 1:>20} {errs[0]:>15.3e} {errs[1]:>13.3e}")
print()
print("a rule on a fixed grid with n points reaches "
      "degree n-1. Freeing the points doubles it.")
