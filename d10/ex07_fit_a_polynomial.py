"""A polynomial fit is the same machinery with more columns."""
import numpy as np

from nmkit.lstsq import design_matrix, lstsq_qr, polyval, r_squared

rng = np.random.default_rng(211)
xs = np.linspace(0.0, 4.0, 25)
truth = 2.0 - 1.5 * xs + 0.4 * xs ** 2
ys = truth + rng.normal(scale=0.3, size=xs.size)

c = lstsq_qr(design_matrix(xs, 2), ys)
print("fitted coefficients:", np.array2string(c, precision=6))
print("the true ones      : [ 2.      -1.5      0.4    ]")
print("r squared          :", f"{r_squared(ys, polyval(c, xs)):.6f}")
