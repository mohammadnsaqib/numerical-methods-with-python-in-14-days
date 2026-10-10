"""Newton can enter a cycle and repeat two values for ever without approaching anything.
"""
from nmkit.roots import newton

f = lambda x: x ** 3 - 2 * x + 2
df = lambda x: 3 * x * x - 2

r = newton(f, df, 0.0, tol=1e-13, max_iter=12)
print("converged:", r.converged, "->", r.why)
print("the first eight iterates:")
for k, (x, _) in enumerate(r.history[:8], 1):
    print(f"  {k}: {x:+.15f}")
