"""The same method run to a fixed time, where the errors have had somewhere to
accumulate."""
import numpy as np

from nmkit.ode import euler


def f(t, y):
    return y - t ** 2 + 1.0


def exact(t):
    return t ** 2 + 2 * t + 1 - 0.5 * np.exp(t)


prev = None
print(f"{'h':>10} {'steps':>7} {'error at t = 2':>17} {'ratio':>8}")
for k in range(1, 7):
    h = 0.2 * 2.0 ** (-k)
    n = int(round(2.0 / h))
    _, ys = euler(f, 0.0, 0.5, h, n)
    e = abs(float(ys[-1]) - exact(2.0))
    ratio = "" if prev is None else f"{prev / e:.4f}"
    print(f"{h:>10.6f} {n:>7} {e:>17.3e} {ratio:>8}")
    prev = e
print()
print("the ratio is 2, not 4. One power of h was spent on having more steps to take.")
