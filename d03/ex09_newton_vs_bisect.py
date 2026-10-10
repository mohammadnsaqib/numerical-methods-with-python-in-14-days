"""The same problem and tolerance, so the two step counts can be compared directly."""
import math

from nmkit.roots import bisect, newton, secant

cases = [
    ("x**3-2x-5", lambda x: x ** 3 - 2 * x - 5, lambda x: 3 * x * x - 2, 2.0, 3.0),
    ("cos(x)-x  ", lambda x: math.cos(x) - x, lambda x: -math.sin(x) - 1, 0.0, 1.0),
    ("exp(x)-3  ", lambda x: math.exp(x) - 3, math.exp, 0.0, 2.0),
]
print(f"{'function':<12}{'bisection':>11}{'secant':>9}{'newton':>9}")
for name, f, df, a, b in cases:
    bi = bisect(f, a, b, tol=1e-14).iterations
    se = secant(f, a, b, tol=1e-14).iterations
    ne = newton(f, df, b, tol=1e-14).iterations
    print(f"{name:<12}{bi:>11}{se:>9}{ne:>9}")
