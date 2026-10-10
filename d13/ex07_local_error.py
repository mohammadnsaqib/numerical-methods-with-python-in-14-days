"""One step, started from the exact answer, so nothing has accumulated."""
import numpy as np


def f(t, y):
    return y - t ** 2 + 1.0


def exact(t):
    return t ** 2 + 2 * t + 1 - 0.5 * np.exp(t)


t0 = 1.0
prev = None
print(f"{'h':>10} {'one Euler step':>18} {'exact':>18} {'local error':>13} "
      f"{'ratio':>8}")
for k in range(1, 7):
    h = 0.2 * 2.0 ** (-k)
    start = exact(t0)
    step = start + h * f(t0, start)
    e = abs(step - exact(t0 + h))
    ratio = "" if prev is None else f"{prev / e:.4f}"
    print(f"{h:>10.6f} {step:>18.12f} {exact(t0 + h):>18.12f} {e:>13.3e} {ratio:>8}")
    prev = e
print()
print("the ratio is 4. One step's error is proportional to h squared.")
