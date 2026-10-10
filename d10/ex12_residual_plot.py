"""The residuals say whether the model is right, and a single number cannot."""
import numpy as np

from nmkit.lstsq import design_matrix, lstsq_qr, polyval, r_squared

xs = np.linspace(1.0, 5.0, 20)
ys = 3.0 * np.exp(-0.4 * xs)
c = lstsq_qr(design_matrix(xs, 2), ys)
r = ys - polyval(c, xs)

print("r squared:", f"{r_squared(ys, polyval(c, xs)):.8f}")
signs = np.sign(r)
runs = 1 + int(np.sum(signs[1:] != signs[:-1]))
print("residual signs:", "".join("+" if s > 0 else "-" for s in signs))
print("runs of one sign:", runs, "-- random residuals would give about", xs.size // 2)
