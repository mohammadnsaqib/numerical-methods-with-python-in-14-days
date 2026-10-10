"""Every extra degree fits the data better, which is not the same as being better."""
import numpy as np

from nmkit.lstsq import design_matrix, lstsq_qr, polyval, r_squared

rng = np.random.default_rng(211)
xs = np.linspace(0.0, 4.0, 25)
truth = 2.0 - 1.5 * xs + 0.4 * xs ** 2
ys = truth + rng.normal(scale=0.3, size=xs.size)

print(f"{'degree':>7} {'r squared':>12} {'error against the truth':>25}")
for d in (1, 2, 3, 6, 12, 20):
    c = lstsq_qr(design_matrix(xs, d), ys)
    print(f"{d:>7} {r_squared(ys, polyval(c, xs)):>12.8f} "
          f"{np.max(np.abs(polyval(c, xs) - truth)):>25.6f}")
