"""Error against evaluations, which is the only comparison that settles anything."""
import numpy as np

from nmkit.ode import euler, heun


def f(t, y):
    return y - t ** 2 + 1.0


def exact(t):
    return t ** 2 + 2 * t + 1 - 0.5 * np.exp(t)


print(f"{'calls':>7} {'Euler steps':>12} {'Euler error':>14} {'Heun steps':>12} "
      f"{'Heun error':>14}")
for calls in (40, 80, 160, 320, 640):
    ee = abs(float(euler(f, 0.0, 0.5, 2.0 / calls, calls)[1][-1]) - exact(2.0))
    m = calls // 2
    eh = abs(float(heun(f, 0.0, 0.5, 2.0 / m, m)[1][-1]) - exact(2.0))
    print(f"{calls:>7} {calls:>12} {ee:>14.3e} {m:>12} {eh:>14.3e}")
print()
print("Heun takes half as many steps for the same evaluations and is still far ahead")
