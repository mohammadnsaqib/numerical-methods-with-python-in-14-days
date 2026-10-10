"""A tolerance the format cannot reach never fires, and the iteration cap becomes the
real rule."""
import math

from nmkit.fp import ulp
from nmkit.roots import bisect

r = bisect(math.cos, 0.0, 3.0, tol=1e-18, max_iter=80)
print("requested tolerance :", 1e-18)
print("ulp at the root     :", f"{ulp(math.pi / 2):.3e}")
print("iterations run      :", r.iterations, "of a cap of 80")
print("converged           :", r.converged, "->", r.why)
print()
print("the last six midpoints:")
for m, _ in r.history[-6:]:
    print("   ", f"{m:.17f}")
print("they are identical, so the bracket stopped shrinking long before the cap.")
