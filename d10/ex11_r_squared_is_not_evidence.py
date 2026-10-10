"""A high r squared says the curve is near the points and nothing about whether the
model is right."""
import numpy as np

from nmkit.lstsq import design_matrix, lstsq_qr, polyval, r_squared

xs = np.linspace(1.0, 5.0, 20)
ys = 3.0 * np.exp(-0.4 * xs)                          # a decay, not a polynomial

for d in (1, 2, 3):
    c = lstsq_qr(design_matrix(xs, d), ys)
    print(f"polynomial of degree {d}: r squared {r_squared(ys, polyval(c, xs)):.8f}, "
          f"value at x = 8 is {polyval(c, 8.0):+.4f}")
print("the true value "
      "at x = 8 is", f"{3.0 * np.exp(-0.4 * 8.0):.4f}, and it cannot be negative.")
