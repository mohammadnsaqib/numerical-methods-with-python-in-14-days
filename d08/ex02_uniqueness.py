"""Two polynomials of degree below n through the same n points must be the same
polynomial."""
import numpy as np

from nmkit.interp import lagrange_eval, vandermonde_fit

rng = np.random.default_rng(157)
xs = np.sort(rng.uniform(-2, 2, 6))
ys = rng.uniform(-3, 3, 6)

c = vandermonde_fit(xs, ys)
t = np.linspace(-2, 2, 9)
by_coeffs = np.polynomial.Polynomial(c)(t)
by_lagrange = lagrange_eval(xs, ys, t)
print("largest gap between "
      "the two routes:", f"{np.max(np.abs(by_coeffs - by_lagrange)):.3e}")
print("both pass through every node      :",
      np.allclose(lagrange_eval(xs, ys, xs), ys))
