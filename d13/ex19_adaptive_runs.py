"""An equation that is quiet, then busy, then quiet again."""
import numpy as np

from nmkit.ode import adaptive_rk, rk4


def f(t, y):
    """A decay driven by a pulse a tenth of a unit wide, centred at t = 3."""
    return -y + 10.0 * np.exp(-100.0 * (t - 3.0) ** 2)


ts, ys, ok, bad = adaptive_rk(f, 0.0, 1.0, 6.0, tol=1e-9)
print(f"steps accepted : {ok}")
print(f"steps rejected : {bad}")
print(f"shortest step  : {np.min(np.diff(ts)):.6f}")
print(f"longest step   : {np.max(np.diff(ts)):.6f}")
print(f"ratio          : {np.max(np.diff(ts)) / np.min(np.diff(ts)):.1f}")
print()
print(f"{'region':>16} {'width':>8} {'steps taken':>13} {'steps per unit':>16}")
for lo, hi, name in ((0.0, 2.7, "before the pulse"), (2.7, 3.3, "the pulse"),
                     (3.3, 6.0, "after it")):
    inside = int(np.sum((ts[:-1] >= lo) & (ts[:-1] < hi)))
    print(f"{name:>16} {hi - lo:>8.1f} {inside:>13} {inside / (hi - lo):>16.1f}")
print()
print("the pulse occupies a tenth of the interval and takes six times the step density")
