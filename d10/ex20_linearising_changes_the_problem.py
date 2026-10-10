"""Fitting the logarithm minimises a different quantity, so the answer is a different
answer."""
import numpy as np
from scipy.optimize import curve_fit

from nmkit.lstsq import design_matrix, lstsq_qr

rng = np.random.default_rng(241)
xs = np.linspace(0.0, 3.0, 30)
# noise ADDED, not multiplied
ys = 2.5 * np.exp(0.8 * xs) + rng.normal(scale=0.6, size=30)

c = lstsq_qr(design_matrix(xs, 1), np.log(np.maximum(ys, 1e-9)))
lin = (float(np.exp(c[0])), float(c[1]))
direct, _ = curve_fit(lambda t, a, b: a * np.exp(b * t), xs, ys, p0=(1.0, 1.0))

def sse(a, b):
    return float(np.sum((ys - a * np.exp(b * xs)) ** 2))

print(f"true          : a 2.500000  b 0.800000")
print(f"via logarithms: a {lin[0]:.6f}  b {lin[1]:.6f}   sum of squares "
      f"{sse(*lin):.4f}")
print(f"fitted directly: a {direct[0]:.6f}  b {direct[1]:.6f}   sum of squares "
      f"{sse(*direct):.4f}")
