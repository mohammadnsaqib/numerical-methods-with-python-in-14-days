"""The secant method's order is 1.618, and the measurement should land on it rather than
on 2."""
import math

from mpmath import mp, findroot, mpf

from nmkit.roots import order_estimate, secant

mp.dps = 40
true = float(findroot(lambda x: x ** 3 - 2 * x - 5, mpf(2)))
r = secant(lambda x: x ** 3 - 2 * x - 5, 3.0, 2.5, tol=1e-16, max_iter=12)

errs = [abs(x - true) for x, _ in r.history if abs(x - true) > 2.3e-16]
print("order estimates:", [f"{p:.4f}" for p in order_estimate(errs)])
print("the golden ratio:", f"{(1 + math.sqrt(5)) / 2:.4f}")
