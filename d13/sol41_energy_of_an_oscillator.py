"""Problem 13.41: an oscillator, where the error shows as a quantity that should not
move."""
import numpy as np

from nmkit.ode import euler, heun, midpoint_ode, rk4


def f(t, y):
    """A frictionless spring: position y[0], velocity y[1]."""
    return np.array([y[1], -y[0]])


def energy(ys):
    """Half the sum of the squares, which the true motion holds fixed for ever."""
    return 0.5 * (ys[:, 0] ** 2 + ys[:, 1] ** 2)


print(f"{'method':>10} {'energy at t = 0':>17} {'at t = 100':>13} {'drift':>12} "
      f"{'position error':>16}")
T, n = 100.0, 20000
for name, m in (("Euler", euler), ("Heun", heun), ("midpoint", midpoint_ode),
                ("RK4", rk4)):
    _, ys = m(f, 0.0, [1.0, 0.0], T / n, n)
    e = energy(ys)
    print(f"{name:>10} {e[0]:>17.10f} {e[-1]:>13.6f} {e[-1] / e[0] - 1:>12.3e} "
          f"{abs(ys[-1, 0] - np.cos(T)):>16.3e}")
print()
print("Heun and the midpoint rule agree to every digit, because the equation is linear")
print("and their two updates then coincide. Euler adds two thirds of the energy again")
print("over sixteen oscillations. RK4 holds it to eleven digits.")
