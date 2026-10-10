"""A sign change on a continuous function is a guarantee, not a hint."""
from nmkit.roots import bisect

def f(x):
    return x ** 3 - 2 * x - 5

a, b = 2.0, 3.0
print("f(a) =", f(a), " f(b) =", f(b))
print("signs differ:", f(a) * f(b) < 0)

r = bisect(f, a, b, tol=1e-14)
print("bisection returned:", r)
print("root  :", f"{r.root:.15f}")
print("f(root):", f"{f(r.root):+.3e}")
