"""Problem 14.39: the capstone fin at four thicknesses, and where the profile turns."""
import numpy as np

from d14._fin import L, TA, U0, UL, C2
from nmkit.bvp import shoot
from nmkit.quad import simpson_n

print(f"{'C1':>8} {'slope at x = 0':>17} {'coolest point':>15} {'at x =':>9} "
      f"{'heat lost':>13}")
for c1 in (25.0, 100.0, 400.0, 1600.0):
    def rhs(x, y, c1=c1):
        return np.array([y[1], c1 * (y[0] - TA) + C2 * (y[0] ** 4 - TA ** 4)])

    # The slope at the hot end grows like the square root of C1, so a fixed pair of
    # guesses works for one thickness and sends the next one to infinity. Scaling them
    # is not a convenience: without it the run overflows at C1 = 1600.
    g = (U0 - TA) * np.sqrt(c1)
    ts, ys, slope, miss, _ = shoot(rhs, 0.0, L, U0, UL, -1.2 * g, -0.6 * g, n=800)
    u = ys[:, 0]
    k = int(np.argmin(u))
    q = simpson_n(lambda v: c1 * (np.interp(v, ts, u) - TA)
                  + C2 * (np.interp(v, ts, u) ** 4 - TA ** 4), 0.0, L, 800)
    print(f"{c1:>8.0f} {slope:>17.4f} {u[k]:>15.6f} {ts[k]:>9.4f} {q:>13.4f}")
print()
print("at the two smallest losses the fin is coolest at its cold end. Past that the")
print("middle drops below BOTH ends, and the "
      "dip moves towards the hot end as C1 grows,")
print("because that is where the loss is largest.")
