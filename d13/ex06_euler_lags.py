"""The error is not scatter. It points the same way at every step."""
import numpy as np

from nmkit.ode import euler


def f(t, y):
    return y - t ** 2 + 1.0


def exact(t):
    return t ** 2 + 2 * t + 1 - 0.5 * np.exp(t)


ts, ys = euler(f, 0.0, 0.5, 0.2, 10)
print(f"{'t':>5} {'Euler':>12} {'exact':>12} {'error':>12} {'sign':>6}")
for t, y in zip(ts, ys):
    e = y - exact(t)
    print(f"{t:>5.1f} {y:>12.8f} {exact(t):>12.8f} {e:>12.8f} "
          f"{'+' if e > 0 else ('-' if e < 0 else '0'):>6}")
print()
print("every sign after the first is the same. The solution curves upwards, and a")
print("straight step from the start of each interval falls below it.")
