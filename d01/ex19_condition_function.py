"""A problem's conditioning is a property of the problem, and it can be computed before
any method is chosen."""
import math

def cond_f(f, df, x):
    """The relative condition number of evaluating f at x."""
    return abs(x * df(x) / f(x))

cases = [
    ("sqrt(x) at 4",      math.sqrt,          lambda x: 0.5 / math.sqrt(x), 4.0),
    ("1/(1-x) at 0.999",  lambda x: 1 / (1 - x), lambda x: 1 / (1 - x) ** 2, 0.999),
    ("x - 1 at 1.0001",   lambda x: x - 1,    lambda x: 1.0,                1.0001),
]
for name, f, df, x in cases:
    print(f"{name:<20} condition number = {cond_f(f, df, x):.4e}")
