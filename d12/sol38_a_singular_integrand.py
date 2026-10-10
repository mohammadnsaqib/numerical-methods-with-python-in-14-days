"""Problem 12.38: an integrand that is infinite at an endpoint, met three ways."""
import numpy as np
from mpmath import mp, mpf, quad as mpquad, sqrt as mpsqrt

from nmkit.quad import gauss_legendre, simpson_n

mp.dps = 40
exact = float(mpquad(lambda v: 1 / mpsqrt(v), [mpf(0), mpf(1)]))
print(f"the integral of 1/sqrt(t) on [0, 1] is finite: {exact:.15f}")
print("the INTEGRAND is not. It grows without bound as t approaches zero.")
print()

# Route one: any rule with a node at the endpoint evaluates there and gets infinity
# back.
with np.errstate(divide="ignore", invalid="ignore"):
    s = simpson_n(lambda v: 1.0 / np.sqrt(v), 0.0, 1.0, 64)
print(f"composite Simpson, whose first node IS the endpoint: {s}")
print()

# Route two: Gauss puts no node at an endpoint, so it returns a number. The number is
# poor, and it improves slowly, because the integrand is not near any polynomial.
print(f"{'points':>8} {'Gauss':>14} {'error':>12} {'ratio':>8}")
prev = None
for n in (10, 40, 160, 640):
    g = gauss_legendre(lambda v: 1.0 / np.sqrt(v), 0.0, 1.0, n)
    e = abs(g - exact)
    ratio = "" if prev is None else f"{prev / e:.3f}"
    print(f"{n:>8} {g:>14.9f} {e:>12.3e} {ratio:>8}")
    prev = e
print()

# Route three: substitute t = u squared. Then dt = 2u du and the integrand becomes 2
# exactly.
sub = gauss_legendre(lambda u: 2.0, 0.0, 1.0, 2)
print(f"with t = u squared the integrand becomes the constant 2: {sub:.15f}")
print(f"error {abs(sub - exact):.3e}, from two evaluations rather than six hundred and "
      f"forty")
