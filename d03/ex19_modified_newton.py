"""Multiplying the step by the multiplicity restores the second order that the repeat
destroyed."""
from nmkit.roots import newton, newton_modified, order_estimate

f = lambda x: (x - 1.0) ** 2 * (x - 3.0)
df = lambda x: 2 * (x - 1.0) * (x - 3.0) + (x - 1.0) ** 2

plain = newton(f, df, 1.6, tol=1e-14, max_iter=60)
fixed = newton_modified(f, df, 1.6, m=2, tol=1e-14, max_iter=60)
print("plain Newton   :", plain.iterations, "steps -> ", f"{plain.root:.14f}")
print("multiplied by 2:", fixed.iterations, "steps -> ", f"{fixed.root:.14f}")

errs = [abs(x - 1.0) for x, _ in fixed.history if abs(x - 1.0) > 1e-15]
print("order estimates:", [f"{p:.3f}" for p in order_estimate(errs)][:3])
