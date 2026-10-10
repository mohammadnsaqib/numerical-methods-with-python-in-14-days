"""Problem 3.39: which root Newton reaches depends on where it starts, and the map is
not tidy."""
from nmkit.roots import newton

f = lambda x: x ** 3 - x            # roots at -1, 0 and +1
df = lambda x: 3 * x * x - 1

roots = [-1.0, 0.0, 1.0]
counts = {-1.0: 0, 0.0: 0, 1.0: 0, None: 0}
flips = 0
prev = None
for i in range(201):
    start = -2.0 + i * 0.02
    r = newton(f, df, start, tol=1e-12, max_iter=60)
    hit = None
    if r.converged:
        hit = min(roots, key=lambda t: abs(t - r.root))
        if abs(hit - r.root) > 1e-6:
            hit = None
    counts[hit] += 1
    if prev is not None and hit != prev:
        flips += 1
    prev = hit

print("starts tried            :", 201)
print("reached -1, 0, +1       :", counts[-1.0], counts[0.0], counts[1.0])
print("failed to converge      :", counts[None])
print("changes of destination  :", flips, "-- the map is not three tidy intervals")
