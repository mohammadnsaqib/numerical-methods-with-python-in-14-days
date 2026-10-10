"""The composite Simpson rule, and the factor of sixteen that names its order."""
import numpy as np

from nmkit.quad import simpson_n

exact = np.e - 1.0
prev = None
print(f"{'panels':>8} {'estimate':>20} {'error':>12} {'error ratio':>13}")
for n in (2, 4, 8, 16, 32, 64, 128):
    est = simpson_n(np.exp, 0.0, 1.0, n)
    e = abs(est - exact)
    ratio = "" if prev is None else f"{prev / e:.4f}"
    print(f"{n:>8} {est:>20.14f} {e:>12.3e} {ratio:>13}")
    prev = e
print()
try:
    simpson_n(np.exp, 0.0, 1.0, 7)
except ValueError as exc:
    print(f"an odd count is refused: {exc}")
