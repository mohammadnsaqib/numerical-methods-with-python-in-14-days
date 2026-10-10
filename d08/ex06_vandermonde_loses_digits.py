"""Measured at its own nodes the coefficient route looks perfect, which is Day 5's trap
exactly."""
import numpy as np

from nmkit.interp import lagrange_eval, vandermonde_fit

print(f"{'points':>7} {'miss at the nodes':>19} {'gap from Lagrange':>19} "
      f"{'largest coeff':>15}")
for n in (5, 10, 15, 20, 25, 30):
    xs = np.linspace(-1.0, 1.0, n)
    ys = np.exp(xs)
    c = vandermonde_fit(xs, ys)
    p = np.polynomial.Polynomial(c)
    t = np.linspace(-1.0, 1.0, 601)
    print(f"{n:>7} {np.max(np.abs(p(xs) - ys)):>19.3e} "
          f"{np.max(np.abs(p(t) - lagrange_eval(xs, ys, t))):>19.3e} "
          f"{np.max(np.abs(c)):>15.3e}")
print()
print("the first column stays at the format's "
      "floor while the second grows by more than")
print("six orders. A small residual at the nodes says nothing about the polynomial.")
