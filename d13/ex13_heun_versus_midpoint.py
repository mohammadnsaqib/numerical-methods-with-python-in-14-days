"""Two second-order methods of the same cost, and the equations that tell them apart."""
import numpy as np

from nmkit.ode import heun, midpoint_ode

cases = [
    ("y' = y", lambda t, y: y, 1.0, lambda t: np.exp(t), 1.0),
    ("y' = -y^2", lambda t, y: -y * y, 1.0, lambda t: 1.0 / (1.0 + t), 2.0),
    ("y' = t - y^2", lambda t, y: t - y * y, 0.0, None, 2.0),
]
print(f"{'equation':>15} {'steps':>7} {'Heun':>14} {'midpoint':>14} "
      f"{'which is better':>17}")
for label, f, y0, exact, T in cases:
    for n in (20, 80):
        a = float(heun(f, 0.0, y0, T / n, n)[1][-1])
        b = float(midpoint_ode(f, 0.0, y0, T / n, n)[1][-1])
        if exact is None:
            ref = float(heun(f, 0.0, y0, T / 200000, 200000)[1][-1])
        else:
            ref = exact(T)
        ea, eb = abs(a - ref), abs(b - ref)
        who = "Heun" if ea < eb else ("midpoint" if eb < ea else "neither")
        print(f"{label if n == 20 else '':>15} {n:>7} {ea:>14.3e} {eb:>14.3e} "
              f"{who:>17}")
print()
print("on the first equation the two are the same computation. On the others they")
print("are not, and neither is the better one everywhere.")
