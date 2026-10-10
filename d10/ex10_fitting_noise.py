"""With as many parameters as points the fit is perfect and means nothing."""
import numpy as np

from nmkit.lstsq import design_matrix, lstsq_qr, polyval, r_squared

rng = np.random.default_rng(223)
xs = np.linspace(0.0, 1.0, 8)
ys = rng.normal(size=8)                              # pure noise, no signal at all

for d in (1, 3, 7):
    c = lstsq_qr(design_matrix(xs, d), ys)
    print(f"degree {d}: r squared {r_squared(ys, polyval(c, xs)):.10f}")
print("\nthe data was noise. A perfect fit to it describes nothing.")
