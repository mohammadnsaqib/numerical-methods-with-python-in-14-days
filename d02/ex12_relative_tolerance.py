"""An absolute tolerance means different things at different magnitudes."""
from nmkit.roots import bisect

def small_root(x):
    return x - 1e-8

def large_root(x):
    return x - 1e8

r1 = bisect(small_root, -1.0, 1.0, tol=1e-6)
r2 = bisect(large_root, 0.0, 1e9, tol=1e-6)
print("root near 1e-8:", f"{r1.root:.12e}", "in", r1.iterations, "steps")
print("root near 1e8 :", f"{r2.root:.12e}", "in", r2.iterations, "steps")
print()
print("relative error, small root:", f"{abs(r1.root - 1e-8) / 1e-8:.3e}")
print("relative error, large root:", f"{abs(r2.root - 1e8) / 1e8:.3e}")
