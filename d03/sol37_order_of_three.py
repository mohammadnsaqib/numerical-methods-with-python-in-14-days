"""Problem 3.37: the measured order of three methods on one problem, side by side."""
from mpmath import mp, findroot, mpf

from nmkit.roots import fixed_point, newton, order_estimate, secant

mp.dps = 40
true = float(findroot(lambda x: x ** 3 - 2 * x - 5, mpf(2)))

runs = [
    ("fixed point",
    fixed_point(lambda x: (2 * x + 5) ** (1 / 3), 2.0, tol=1e-16, max_iter=90)),
    ("secant "
     "    ", secant(lambda x: x ** 3 - 2 * x - 5, 3.0, 2.5, tol=1e-16, max_iter=20)),
    ("newton     ", newton(lambda x: x ** 3 - 2 * x - 5, lambda x: 3 * x * x - 2, 3.0,
                           tol=1e-16, max_iter=20)),
]
for name, r in runs:
    errs = [abs(x - true) for x, _ in r.history if abs(x - true) > 2.3e-16]
    ps = order_estimate(errs)
    last = f"{ps[-1]:.4f}" if ps else "  --"
    print(f"{name}: {r.iterations:>3} steps, final order estimate {last}")
