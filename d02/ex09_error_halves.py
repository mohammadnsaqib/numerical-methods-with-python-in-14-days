"""What halves is the BRACKET, and the distance to the root only has to stay under it.
"""
from mpmath import mp, findroot, mpf

from nmkit.roots import bisect

mp.dps = 40
true = float(findroot(lambda x: x ** 3 - 2 * x - 5, mpf(2)))  # the oracle, forty digits

a, b = 2.0, 3.0
fa = (lambda x: x ** 3 - 2 * x - 5)(a)
f = lambda x: x ** 3 - 2 * x - 5
print(f"{'step':>5} {'midpoint':>18} {'half-width':>12} {'true error':>12} "
      f"{'under it':>9}")
for k in range(1, 11):
    m = a + (b - a) / 2
    fm = f(m)
    half = (b - a) / 2
    err = abs(m - true)
    print(f"{k:>5} {m:>18.12f} {half:>12.3e} {err:>12.3e} {str(err <= half):>9}")
    if fa * fm < 0.0:
        b = m
    else:
        a, fa = m, fm
print("\nthe half-width halves exactly every step. The true error bounces below it.")
