"""A check that needs no closed-form solution: a quantity the equations hold fixed."""
import numpy as np

from nmkit.ode import euler, heun, rk4


def f(t, y):
    """A pendulum at any angle, which has no elementary solution."""
    return np.array([y[1], -np.sin(y[0])])


def energy(ys):
    """Half the square of the rate, plus one minus the cosine of the angle."""
    return 0.5 * ys[:, 1] ** 2 + (1.0 - np.cos(ys[:, 0]))


print(f"{'method':>10} {'energy at t = 0':>17} {'at t = 50':>13} {'drift':>12}")
for name, m in (("Euler", euler), ("Heun", heun), ("RK4", rk4)):
    _, ys = m(f, 0.0, [2.0, 0.0], 0.005, 10000)
    e = energy(ys)
    print(f"{name:>10} {e[0]:>17.12f} {e[-1]:>13.9f} {e[-1] - e[0]:>12.3e}")
print()
print("the pendulum is released from 2 radians, far outside the small-angle regime.")
print("no formula describes it, and the energy still says which method to trust.")
