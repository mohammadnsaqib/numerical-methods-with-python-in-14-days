"""On a curve that flattens away from its root, each tangent lands further out than the
last."""
import math

from nmkit.roots import newton

f = math.atan
df = lambda x: 1.0 / (1.0 + x * x)

for start in (1.0, 1.39, 1.40, 2.0):
    r = newton(f, df, start, tol=1e-13, max_iter=25)
    if r.converged:
        print(f"start {start:>5}: converged in {r.iterations:>2} steps to "
              f"{r.root:+.12f}")
    else:
        last = r.history[-1][0] if r.history else float("nan")
        print(f"start {start:>5}: {r.why}; reached {last:+.6e}")
