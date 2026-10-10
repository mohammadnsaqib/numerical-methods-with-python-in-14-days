"""Problem 10.38: choose the degree by fitting half the data and judging on the other
half."""
import numpy as np

from nmkit.lstsq import design_matrix, lstsq_qr, polyval

rng = np.random.default_rng(20251)
xs = np.linspace(0.0, 6.0, 40)
truth = 1.0 + 0.5 * xs - 0.3 * xs ** 2 + 0.04 * xs ** 3
ys = truth + rng.normal(scale=0.4, size=xs.size)

fit, test = xs[0::2], xs[1::2]
yfit, ytest = ys[0::2], ys[1::2]

print(f"{'degree':>7} {'error on the fit':>18} {'error on the rest':>19}")
best, best_d = np.inf, 0
for d in range(1, 13):
    c = lstsq_qr(design_matrix(fit, d), yfit)
    e_fit = np.sqrt(np.mean((polyval(c, fit) - yfit) ** 2))
    e_test = np.sqrt(np.mean((polyval(c, test) - ytest) ** 2))
    if e_test < best:
        best, best_d = e_test, d
    print(f"{d:>7} {e_fit:>18.5f} {e_test:>19.5f}")
print(f"\nthe held-back data prefers degree {best_d}, and the truth is degree 3")
