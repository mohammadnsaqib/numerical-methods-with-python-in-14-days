"""The iteration that works creeps in by a constant factor, which is what first order
means."""
from nmkit.roots import fixed_point

g = lambda x: (2 * x + 5) ** (1 / 3)
r = fixed_point(g, 2.0, tol=1e-13, max_iter=60)

print("converged:", r.converged, " steps:", r.iterations)
print(f"{'step':>5} {'x':>20} {'change':>14}")
for k, (x, d) in enumerate(r.history[:9], 1):
    print(f"{k:>5} {x:>20.15f} {d:>14.3e}")
