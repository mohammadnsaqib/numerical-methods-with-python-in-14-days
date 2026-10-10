"""A sign change proves a root only for a continuous function, and nothing checks
continuity."""
from nmkit.roots import bisect

def f(x):
    return 1.0 / (x - 1.0)

print("f(0) =", f(0.0), " f(3) =", f(3.0), " -> the signs differ")
r = bisect(f, 0.0, 3.0, tol=1e-14)
print("bisection returned:", f"{r.root:.15f}", "in", r.iterations, "steps")
print("f there           :", f"{f(r.root):.6e}")
print()
print("the method walked to the pole, not to a root. f is not continuous on [0, 3].")
