"""Truncation error alone, with the subtraction's error kept out of the way."""
from mpmath import cos, mp, mpf, sin

from nmkit.diff import central_diff

# Fifty digits of working precision leaves the subtraction nothing to destroy, so what
# is left on this table is the formula's own error and nothing else.
mp.dps = 50
x = mpf(1)
true = cos(x)
print(f"{'h':>10} {'centred error':>18} {'ratio':>10}")
prev = None
for k in range(1, 9):
    h = mpf(2) ** (-k)
    e = abs((sin(x + h) - sin(x - h)) / (2 * h) - true)
    ratio = "" if prev is None else f"{float(prev / e):.4f}"
    print(f"{float(h):>10.6f} {float(e):>18.6e} {ratio:>10}")
    prev = e
print()
print("with no round-off in the way the ratio is 4 at every step, for ever")
