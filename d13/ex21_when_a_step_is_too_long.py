"""A decaying solution, and a method whose answer grows without bound."""
import numpy as np

from nmkit.ode import euler

LAM = -15.0


def f(t, y):
    """y' = -15 y, whose solution decays by a factor of e every fifteenth of a unit."""
    return LAM * y


print(f"the exact solution at t = 2 is {np.exp(LAM * 2.0):.3e}, which is almost zero")
print(f"Euler is stable while |1 + h lambda| <= 1, so while h <= {2.0 / abs(LAM):.6f}")
print()
print(f"{'h':>10} {'h times lambda':>16} {'growth factor':>15} {'y(2)':>16}")
for h in (0.05, 0.10, 0.1333, 0.14, 0.20, 0.30):
    n = int(round(2.0 / h))
    _, ys = euler(f, 0.0, 1.0, h, n)
    print(f"{h:>10.4f} {h * LAM:>16.4f} {abs(1 + h * LAM):>15.6f} "
          f"{float(ys[-1]):>16.3e}")
print()
print("nothing about accuracy changed at h = 0.14. The answer stopped decaying and")
print("started doubling, which is not a poor answer but a different kind of failure.")
