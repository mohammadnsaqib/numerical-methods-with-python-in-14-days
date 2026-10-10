"""Round-off does not cancel out over many operations; it accumulates."""
from nmkit.fp import ulp

n = 1_000_000
total = 0.0
for _ in range(n):
    total += 0.1

exact = n * 0.1
err = abs(total - exact)
print("added 0.1 one million times")
print("  computed      :", f"{total:.10f}")
print("  n * 0.1       :", f"{exact:.10f}")
print("  absolute error:", f"{err:.6e}")
print("  the gap between neighbouring numbers here:", f"{ulp(exact):.3e}")
print("  so the total is wrong by", round(err / ulp(exact)), "representable steps")
