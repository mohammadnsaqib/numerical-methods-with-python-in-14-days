"""Which method wins depends on the function, so the comparison is run rather than
asserted."""
import math

from nmkit.roots import bisect, false_position

cases = [
    ("exp(x) - 3      ", lambda x: math.exp(x) - 3.0, 0.0, 2.0),
    ("x**3 - 2x - 5   ", lambda x: x ** 3 - 2 * x - 5, 2.0, 3.0),
    ("x**10 - 1       ", lambda x: x ** 10 - 1.0, 0.0, 1.3),
]
print(f"{'function':<18}{'bisection':>12}{'false position':>18}")
for name, f, a, b in cases:
    bi = bisect(f, a, b, tol=1e-12)
    fp = false_position(f, a, b, tol=1e-12, max_iter=500)
    print(f"{name:<18}{bi.iterations:>12}{fp.iterations:>18}")
