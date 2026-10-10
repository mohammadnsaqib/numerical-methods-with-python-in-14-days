"""Where the power goes: the two errors on one table."""
import numpy as np

from nmkit.ode import euler


def f(t, y):
    return y - t ** 2 + 1.0


def exact(t):
    return t ** 2 + 2 * t + 1 - 0.5 * np.exp(t)


print(f"{'h':>10} {'steps':>7} {'local error':>14} {'steps x local':>15} "
      f"{'error at t = 2':>16} {'ratio':>8}")
for k in range(1, 7):
    h = 0.2 * 2.0 ** (-k)
    n = int(round(2.0 / h))
    start = exact(1.0)
    local = abs(start + h * f(1.0, start) - exact(1.0 + h))
    _, ys = euler(f, 0.0, 0.5, h, n)
    whole = abs(float(ys[-1]) - exact(2.0))
    print(f"{h:>10.6f} {n:>7} {local:>14.3e} {n * local:>15.3e} {whole:>16.3e} "
          f"{whole / (n * local):>8.4f}")
print()
print("the last column barely moves. The count of steps times one step's error tracks")
print("the whole error, up to a constant the method does not control.")
