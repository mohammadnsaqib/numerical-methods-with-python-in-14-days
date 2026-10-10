"""Correct rearrangements are not interchangeable: two of these three run away from the
root."""
from nmkit.roots import fixed_point

g1 = lambda x: (2 * x + 5) ** (1 / 3)
g2 = lambda x: (x ** 3 - 5) / 2
g3 = lambda x: 5 / (x * x - 2)

for name, g in (("cube root form", g1), ("linear term", g2), ("constant term", g3)):
    r = fixed_point(g, 2.0, tol=1e-13, max_iter=60)
    state = (f"root {r.root:.12f} in {r.iterations} steps" if r.converged
             else f"FAILED: {r.why}")
    print(f"{name:<16} {state}")
