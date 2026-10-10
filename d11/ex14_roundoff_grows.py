"""The subtraction's error, alone, growing as the step shrinks."""
import numpy as np

from mpmath import cos, mp, mpf, sin

from nmkit.diff import central_diff

mp.dps = 50
x = 1.0
true_exact = float(cos(mpf(1)))
print(f"{'h':>8} {'total':>14} {'truncation':>14} {'the rest':>14}")
for k in range(4, 15, 2):
    h = 10.0 ** (-k)
    total = abs(central_diff(np.sin, x, h) - true_exact)
    hm = mpf(10) ** (-k)
    trunc = float(abs((sin(mpf(1) + hm) - sin(mpf(1) - hm)) / (2 * hm) - cos(mpf(1))))
    print(f"{h:>8.0e} {total:>14.3e} {trunc:>14.3e} {abs(total - trunc):>14.3e}")
print()
print("the step falls by 100 per row, so truncation "
      "falls by 10000 and the rest rises by 100")
