"""At a repeated root Newton loses its second order and creeps in at first order
instead."""
from nmkit.roots import newton, order_estimate

f = lambda x: (x - 1.0) ** 2 * (x - 3.0)
df = lambda x: 2 * (x - 1.0) * (x - 3.0) + (x - 1.0) ** 2

r = newton(f, df, 1.6, tol=1e-14, max_iter=60)
errs = [abs(x - 1.0) for x, _ in r.history if abs(x - 1.0) > 1e-12]
print("steps to reach 1e-14:", r.iterations)
print("first six errors    :", [f"{e:.3e}" for e in errs[:6]])
print("ratio of successive :", [f"{b / a:.4f}" for a, b in zip(errs, errs[1:])][:5])
print("order estimates     :", [f"{p:.3f}" for p in order_estimate(errs)][:4])
