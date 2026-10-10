"""The library routine, and the halving that names the method's order."""
import numpy as np

from nmkit.ode import euler


def f(t, y):
    return y - t ** 2 + 1.0


def exact(t):
    return t ** 2 + 2 * t + 1 - 0.5 * np.exp(t)


prev = None
print(f"{'steps':>7} {'h':>10} {'y(2)':>14} {'error':>12} {'error ratio':>13}")
for n in (10, 20, 40, 80, 160, 320, 640):
    _, ys = euler(f, 0.0, 0.5, 2.0 / n, n)
    e = abs(float(ys[-1]) - exact(2.0))
    ratio = "" if prev is None else f"{prev / e:.4f}"
    print(f"{n:>7} {2.0 / n:>10.6f} {float(ys[-1]):>14.8f} {e:>12.3e} {ratio:>13}")
    prev = e
print(f"{'exact':>7} {'':>10} {exact(2.0):>14.8f}")
