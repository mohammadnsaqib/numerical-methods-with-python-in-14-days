"""Stable at any step, and second order as well."""
import numpy as np

from nmkit.ode import euler_implicit, trapezoid_ode


def f(t, y):
    return -1000.0 * (y - np.cos(t)) - np.sin(t)


prev = None
print(f"{'h':>8} {'steps':>7} {'implicit Euler':>17} {'trapezoidal':>15} "
      f"{'trapezoidal ratio':>19}")
for n in (8, 15, 30, 60, 120):
    h = 3.0 / n
    _, i = euler_implicit(f, 0.0, 1.0, h, n)
    _, r = trapezoid_ode(f, 0.0, 1.0, h, n)
    ei = abs(float(i[-1]) - np.cos(3.0))
    er = abs(float(r[-1]) - np.cos(3.0))
    ratio = "" if prev is None else f"{prev / er:.4f}"
    print(f"{h:>8.3f} {n:>7} {ei:>17.3e} {er:>15.3e} {ratio:>19}")
    prev = er
print()
print("the implicit Euler column halves. The trapezoidal column quarters, so it is")
print("second order, and neither ever grows without bound.")
