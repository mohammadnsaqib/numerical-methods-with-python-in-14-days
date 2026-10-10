"""Problem 11.37: the two errors separated, and the crossing point found."""
import numpy as np
from mpmath import cos, mp, mpf, sin

from nmkit.diff import central_diff

mp.dps = 50
x = 1.0
true = float(cos(mpf(1)))
hs = 10.0 ** np.arange(-1.0, -14.01, -0.25)

rows = []
for h in hs:
    total = abs(central_diff(np.sin, x, h) - true)
    hm = mpf(h)
    trunc = float(abs((sin(mpf(1) + hm) - sin(mpf(1) - hm)) / (2 * hm) - cos(mpf(1))))
    rows.append((h, total, trunc, abs(total - trunc)))

cross = next(r for r in rows if r[3] > r[2])
print(f"{'h':>10} {'total':>12} {'truncation':>12} {'the rest':>12}")
for h, total, trunc, rest in rows[::6]:
    print(f"{h:>10.2e} {total:>12.3e} {trunc:>12.3e} {rest:>12.3e}")
print()
print(f"the two are equal near h = {cross[0]:.3e}")
print(f"the smallest error of all is {min(r[1] for r in rows):.3e}")
