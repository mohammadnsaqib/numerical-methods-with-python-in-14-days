"""Problem 13.40: the stability limit found by running, not by algebra."""
import numpy as np

from nmkit.ode import euler, heun, rk4, stability_region

LAM = -20.0


def blows_up(run, h):
    """True when the computed solution grows instead of decaying."""
    n = max(2, int(round(4.0 / h)))
    _, ys = run(lambda t, y: LAM * y, 0.0, 1.0, h, n)
    return not np.isfinite(float(ys[-1])) or abs(float(ys[-1])) > 1.0


print(f"the equation is y' = {LAM} y, whose solution decays to {np.exp(LAM * 4):.1e}")
print()
print(f"{'method':>10} {'measured limit':>16} {'from the polynomial':>21} {'gap':>10}")
for name, run in (("euler", euler), ("heun", heun), ("rk4", rk4)):
    lo, hi = 1e-6, 1.0
    for _ in range(60):
        mid = (lo + hi) / 2
        if blows_up(run, mid):
            hi = mid
        else:
            lo = mid
    zs = np.linspace(-4.0, -1e-7, 800000)
    z_max = float(np.min(zs[stability_region(name, zs) <= 1.0]))
    print(f"{name:>10} {lo:>16.8f} {z_max / LAM:>21.8f} {abs(lo - z_max / LAM):>10.1e}")
print()
print("a bisection on the step finds the same boundary the algebra gives")
