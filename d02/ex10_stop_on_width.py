"""Stopping on the bracket width bounds the error, because the root is inside the
bracket."""
import math

from nmkit.roots import bisect

for tol in (1e-2, 1e-4, 1e-8, 1e-12):
    r = bisect(math.cos, 0.0, 3.0, tol=tol)
    err = abs(r.root - math.pi / 2)
    print(f"tol {tol:<8.0e} -> {r.iterations:>3} steps, root {r.root:.12f}, "
          f"true error {err:.2e}, within tol: {err <= tol}")
