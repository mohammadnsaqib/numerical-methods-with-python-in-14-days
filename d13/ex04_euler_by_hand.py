"""Five Euler steps, every quantity printed, against the solution in closed form."""
import numpy as np


def f(t, y):
    """y' = y - t^2 + 1."""
    return y - t ** 2 + 1.0


def exact(t):
    """The closed-form solution with y(0) = 0.5."""
    return t ** 2 + 2 * t + 1 - 0.5 * np.exp(t)


t, y, h = 0.0, 0.5, 0.2
print(f"{'step':>5} {'t':>6} {'y':>12} {'slope':>12} {'y + h*slope':>14} {'exact':>12}")
for k in range(5):
    s = f(t, y)
    print(f"{k:>5} {t:>6.1f} {y:>12.8f} {s:>12.8f} {y + h * s:>14.8f} "
          f"{exact(t + h):>12.8f}")
    y = y + h * s
    t = t + h
print()
print(f"after five steps t = {t:.1f}, y = {y:.8f}, exact = {exact(t):.8f}")
print(f"error = {abs(y - exact(t)):.8f}")
