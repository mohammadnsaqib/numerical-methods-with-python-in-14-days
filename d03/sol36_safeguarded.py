"""Problem 3.36: Newton's speed with bisection's guarantee, by falling back when the
step escapes."""
import math

from nmkit.roots import bisect, newton

def safe_newton(f, df, a, b, tol=1e-13, max_iter=100):
    """Take the Newton step when it lands inside the bracket; otherwise bisect.

    The bracket is maintained exactly as in Day 2, so the guarantee survives every
    fallback. Returns the root and how many of each kind of step were used.
    """
    fa, fb = f(a), f(b)
    if fa * fb > 0:
        raise ValueError("not a bracket")
    x = a + (b - a) / 2
    newton_steps = bisect_steps = 0
    for _ in range(max_iter):
        d = df(x)
        step = f(x) / d if d != 0.0 else float("inf")
        cand = x - step
        if a < cand < b and abs(step) < 0.5 * (b - a):
            x, newton_steps = cand, newton_steps + 1
        else:
            x, bisect_steps = a + (b - a) / 2, bisect_steps + 1
            step = (b - a) / 2
        fx = f(x)
        if fa * fx < 0.0:
            b = x
        else:
            a, fa = x, fx
        if abs(step) < tol:
            break
    return x, newton_steps, bisect_steps

for name, f, df, a, b in (
        ("x**3-2x-5", lambda x: x ** 3 - 2 * x - 5, lambda x: 3 * x * x - 2, 2.0, 3.0),
        ("atan(x)  ", math.atan, lambda x: 1 / (1 + x * x), -5.0, 8.0)):
    root, n, bs = safe_newton(f, df, a, b)
    print(f"{name}: root {root:+.13f}  newton steps {n}, bisection steps {bs}")
