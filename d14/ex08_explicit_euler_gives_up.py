"""The fast part is gone from the solution and still fixes the step."""
import numpy as np

from nmkit.ode import euler


def f(t, y):
    """y' = -1000 y + 999 exp(-t)."""
    return -1000.0 * y + 999.0 * np.exp(-t)


def exact(t):
    return np.exp(-1000 * t) + np.exp(-t)


print(f"the stability limit for Euler is h = 2/1000 = {2 / 1000:.6f}")
print()
# The step counts are chosen so that n * h lands exactly on 3.0. A step that overshoots
# would report the error of a different endpoint, which is a defect in the measurement
# rather than in the method.
print(f"{'h':>10} {'steps to t = 3':>16} {'y(3)':>18} {'error':>12}")
for n in (1200, 1500, 1600, 3000):
    h = 3.0 / n
    _, ys = euler(f, 0.0, 2.0, h, n)
    v = float(ys[-1])
    print(f"{h:>10.4f} {n:>16} {v:>18.6e} {abs(v - exact(3.0)):>12.3e}")
print()
print(f"the exact value at t = 3 is {exact(3.0):.9f}. Past t = 0.01 the solution is a")
print("plain decaying exponential that ten spline knots would fit. Sixteen hundred")
print("steps are needed anyway, and it was stability that asked for them.")
