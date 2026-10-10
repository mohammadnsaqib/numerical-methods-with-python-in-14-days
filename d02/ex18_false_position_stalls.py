"""On a strongly convex function one end never moves, so the bracket never shrinks."""
from nmkit.roots import false_position

def f(x):
    return x ** 10 - 1.0

r = false_position(f, 0.0, 1.3, tol=1e-12, max_iter=500)
print("iterations:", r.iterations, " converged:", r.converged)
print(f"{'step':>5} {'c':>18} {'f(c)':>16}")
for k, (c, fc) in enumerate(r.history[:8], 1):
    print(f"{k:>5} {c:>18.12f} {fc:>+16.6e}")
print("\nevery c is below the root, so the right end 1.3 is retained at every step.")
