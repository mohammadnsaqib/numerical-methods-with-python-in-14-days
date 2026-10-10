"""Both routines checked against independent implementations of the same two ideas."""
import numpy as np
from scipy.interpolate import CubicSpline, PchipInterpolator

from nmkit.spline import cubic_spline, hermite_eval, pchip_slopes, spline_eval

rng = np.random.default_rng(191)
print(f"{'knots':>7} {'natural spline':>17} {'shape-preserving':>19}")
for n in (5, 8, 12, 20):
    xs = np.sort(rng.uniform(0, 10, n))
    ys = rng.uniform(-2, 2, n)
    t = np.linspace(xs[0], xs[-1], 400)
    g1 = np.max(np.abs(spline_eval(xs, ys, cubic_spline(xs, ys), t)
                       - CubicSpline(xs, ys, bc_type="natural")(t)))
    g2 = np.max(np.abs(hermite_eval(xs, ys, pchip_slopes(xs, ys), t)
                       - PchipInterpolator(xs, ys)(t)))
    print(f"{n:>7} {g1:>17.3e} {g2:>19.3e}")
