"""Second order means each error is about the square of the one before it, and that is
checkable."""
from mpmath import mp, findroot, mpf

from nmkit.roots import newton

mp.dps = 40
true = float(findroot(lambda x: x ** 3 - 2 * x - 5, mpf(2)))
r = newton(lambda x: x ** 3 - 2 * x - 5, lambda x: 3 * x * x - 2, 3.0, tol=1e-16,
           max_iter=8)

print(f"{'step':>5} {'error':>12} {'previous error squared':>24}")
prev = abs(3.0 - true)
for k, (x, _) in enumerate(r.history[:6], 1):
    e = abs(x - true)
    print(f"{k:>5} {e:>12.4e} {prev * prev:>24.4e}")
    prev = e
