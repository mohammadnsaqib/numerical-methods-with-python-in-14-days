"""The day's methods against an independent solver, on three equations."""
import numpy as np
import scipy.integrate as si

from nmkit.ode import adaptive_rk, rk4

cases = [
    ("y' = y - t^2 + 1", lambda t, y: y - t ** 2 + 1.0, 0.5, 2.0,
     lambda t: t ** 2 + 2 * t + 1 - 0.5 * np.exp(t)),
    ("y' = -2ty", lambda t, y: -2 * t * y, 1.0, 1.5, lambda t: np.exp(-t ** 2)),
    ("y' = cos(t) - y", lambda t, y: np.cos(t) - y, 0.0, 4.0,
     lambda t: (np.sin(t) + np.cos(t) - np.exp(-t)) / 2),
]
print(f"{'equation':>18} {'RK4, 200 steps':>16} {'adaptive':>12} {'scipy RK45':>12}")
for label, f, y0, T, exact in cases:
    e1 = abs(float(rk4(f, 0.0, y0, T / 200, 200)[1][-1]) - exact(T))
    e2 = abs(float(adaptive_rk(f, 0.0, y0, T, tol=1e-10)[1][-1]) - exact(T))
    s = si.solve_ivp(f, (0.0, T), [y0], rtol=1e-10, atol=1e-12, dense_output=True)
    e3 = abs(float(s.y[0, -1]) - exact(T))
    print(f"{label:>18} {e1:>16.2e} {e2:>12.2e} {e3:>12.2e}")
print()
print("every column is an error against the solution in closed form")
