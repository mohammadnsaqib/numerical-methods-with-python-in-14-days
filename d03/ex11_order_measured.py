"""The order is a number the run can be made to report, rather than a claim about the
method."""
from mpmath import mp, findroot, mpf

from nmkit.roots import newton, order_estimate

mp.dps = 40
true = float(findroot(lambda x: x ** 3 - 2 * x - 5, mpf(2)))
r = newton(lambda x: x ** 3 - 2 * x - 5, lambda x: 3 * x * x - 2, 3.0, tol=1e-16,
           max_iter=8)

errs = [abs(x - true) for x, _ in r.history if abs(x - true) > 2.3e-16]
print("errors used:", [f"{e:.2e}" for e in errs])
print("order estimates:", [f"{p:.4f}" for p in order_estimate(errs)])
print("Newton's stated order: 2")
