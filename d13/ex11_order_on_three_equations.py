"""An order belongs to the method, so it should not change with the equation."""
import numpy as np

from nmkit.ode import euler, heun, rk4

cases = [
    ("y' = y", lambda t, y: y, 1.0, lambda t: np.exp(t), 1.0),
    ("y' = -2ty", lambda t, y: -2 * t * y, 1.0, lambda t: np.exp(-t ** 2), 1.5),
    ("y' = cos(t) - y", lambda t, y: np.cos(t) - y, 0.0,
     lambda t: (np.sin(t) + np.cos(t) - np.exp(-t)) / 2, 2.0),
]
print(f"{'equation':>18} {'Euler':>10} {'Heun':>10} {'RK4':>10}")
for label, f, y0, exact, T in cases:
    row = []
    for m in (euler, heun, rk4):
        e = [abs(float(m(f, 0.0, y0, T / n, n)[1][-1]) - exact(T)) for n in (80, 160)]
        row.append(np.log2(e[0] / e[1]))
    print(f"{label:>18} " + " ".join(f"{v:>10.4f}" for v in row))
