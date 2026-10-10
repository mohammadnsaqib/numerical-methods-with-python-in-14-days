"""When the slope does not depend on y, Runge-Kutta IS composite Simpson."""
import numpy as np

from nmkit.ode import rk4
from nmkit.quad import simpson_n

# An equation of the form y' = g(t) is an integral wearing different clothes: its
# solution is the integral of g. Both routines are given the same problem and the same
# panel count.
cases = [("g(t) = exp(t)", np.exp, 0.0, 1.0),
         ("g(t) = sin(t)", np.sin, 0.0, np.pi),
         ("g(t) = 1/(1+t^2)", lambda v: 1.0 / (1.0 + v * v), 0.0, 4.0)]

print(f"{'integrand':>18} {'steps':>7} {'Runge-Kutta':>20} {'Simpson':>20} {'gap':>10}")
for label, g, a, b in cases:
    for n in (4, 16):
        _, ys = rk4(lambda t, y: g(t), a, 0.0, (b - a) / n, n)
        r = float(ys[-1])
        s = simpson_n(g, a, b, 2 * n)
        print(f"{label if n == 4 else '':>18} {n:>7} {r:>20.15f} {s:>20.15f} "
              f"{abs(r - s):>10.1e}")
print()
print("one Runge-Kutta step evaluates at the two ends and twice at the middle, which")
print("is one Simpson panel. n steps are 2n Simpson panels, and the answers agree.")
