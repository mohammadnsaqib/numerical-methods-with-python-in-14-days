"""Stable is not the same as damped, and the difference shows at a very long step."""
import numpy as np

from nmkit.ode import euler_implicit, stability_region, trapezoid_ode


def f(t, y):
    """y' = -1000 y, whose solution is gone by t = 0.01."""
    return -1000.0 * y


print(f"{'h times lambda':>16} {'implicit Euler':>16} {'trapezoidal':>14}")
for z in (-2.0, -10.0, -100.0, -1000.0, -100000.0):
    print(f"{z:>16.1f} {float(stability_region('implicit_euler', z)):>16.9f} "
          f"{float(stability_region('trapezoid', z)):>14.9f}")
print()
print("both stay at or below one, so both are stable at every step. Only one of them")
print("goes to zero.")
print()
print(f"{'h':>8} {'implicit Euler y(1)':>22} {'trapezoidal y(1)':>20}")
for h in (0.1, 0.5, 1.0):
    n = int(round(1.0 / h))
    _, i = euler_implicit(f, 0.0, 1.0, h, n)
    _, r = trapezoid_ode(f, 0.0, 1.0, h, n)
    print(f"{h:>8.2f} {float(i[-1]):>22.6e} {float(r[-1]):>20.6e}")
print()
print("the true value is 0. At h = 1 the trapezoidal answer is still the size it")
print("started, with its sign flipped at every step. It is stable and it is useless.")
