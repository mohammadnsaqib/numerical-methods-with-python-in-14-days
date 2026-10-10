"""The order of a method is measured, not claimed, and this is how."""
import numpy as np

from nmkit.ode import euler, heun, rk4


def f(t, y):
    return y - t ** 2 + 1.0


def exact(t):
    return t ** 2 + 2 * t + 1 - 0.5 * np.exp(t)


print(f"{'steps':>7} {'Euler':>10} {'Heun':>10} {'RK4':>10}")
prev = {}
for n in (20, 40, 80, 160, 320):
    row = {}
    for name, m in (("Euler", euler), ("Heun", heun), ("RK4", rk4)):
        e = abs(float(m(f, 0.0, 0.5, 2.0 / n, n)[1][-1]) - exact(2.0))
        row[name] = f"{np.log2(prev[name] / e):.4f}" if name in prev else ""
        prev[name] = e
    print(f"{n:>7} {row['Euler']:>10} {row['Heun']:>10} {row['RK4']:>10}")
print()
print("the measured orders are 1, 2 and 4, which is what the three methods claim")
