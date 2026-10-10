"""The right weight is one over the square of the uncertainty, and the reason is
measurable."""
import numpy as np

from nmkit.lstsq import design_matrix, weighted

rng = np.random.default_rng(251)
xs = np.linspace(0.0, 10.0, 12)
sigma = np.array([0.05] * 6 + [1.0] * 6)
A = design_matrix(xs, 1)

def spread(w):
    out = []
    for _ in range(3000):
        ys = 1.0 + 0.5 * xs + rng.normal(scale=sigma)
        out.append(weighted(A, ys, w)[1])
    return float(np.std(out))

print("slope's spread over 3000 simulated data sets")
print("  every point equal     :", f"{spread(np.ones(12)):.6f}")
print("  weight 1/sigma        :", f"{spread(1.0 / sigma):.6f}")
print("  weight 1/sigma squared:", f"{spread(1.0 / sigma ** 2):.6f}")
