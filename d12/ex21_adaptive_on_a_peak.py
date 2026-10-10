"""An integrand that is flat almost everywhere and steep in one thousandth of the
interval."""
import numpy as np
from mpmath import mp, mpf, quad as mpquad

from nmkit.quad import adaptive_simpson, simpson_n


def peak(t):
    """A spike of width about 0.001, centred at 0.3."""
    return 1.0 / (1.0 + 1e6 * (t - 0.3) ** 2)


mp.dps = 40
exact = float(mpquad(lambda v: 1 / (1 + mpf(10) ** 6 * (v - mpf("0.3")) ** 2),
              [0, mpf("0.3"), 1]))
print(f"the exact value is {exact:.15f}")
print()
print(f"{'rule':>22} {'calls':>7} {'error':>13}")
for n in (100, 1000, 10000, 100000):
    print(f"{'uniform, ' + str(n) + ' panels':>22} {n + 1:>7} "
          f"{abs(simpson_n(peak, 0.0, 1.0, n) - exact):>13.3e}")
print()
for tol in (1e-8, 1e-10, 1e-13):
    value, calls = adaptive_simpson(peak, 0.0, 1.0, tol=tol)
    print(f"{'adaptive, '
             'tol ' + f'{tol:.0e}':>22} {calls:>7} {abs(value - exact):>13.3e}")
print()
print("at about a thousand calls the uniform rule is wrong in the fifth digit and the")
print("adaptive one in the eleventh. The peak is one thousandth of the interval wide.")
