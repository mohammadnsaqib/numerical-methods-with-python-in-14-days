"""Problem 1.40: the condition number by finite difference, against the analytic value.
"""
import math

def cond_fd(f, x):
    """Estimate the condition number using a central difference for the derivative."""
    h = 1e-6 * max(abs(x), 1.0)          # a step scaled to x, not a fixed absolute step
    d = (f(x + h) - f(x - h)) / (2 * h)
    return abs(x * d / f(x))

cases = [
    ("sqrt at 100", math.sqrt, lambda x: 0.5 / math.sqrt(x), 100.0),
    ("exp at 5",    math.exp,  math.exp,                     5.0),
    ("log at 1.5",  math.log,  lambda x: 1.0 / x,            1.5),
]
for name, f, df, x in cases:
    est = cond_fd(f, x)
    true = abs(x * df(x) / f(x))
    print(f"{name:<12} estimated {est:.9f}   analytic {true:.9f}   "
          f"rel diff {abs(est - true) / true:.2e}")
