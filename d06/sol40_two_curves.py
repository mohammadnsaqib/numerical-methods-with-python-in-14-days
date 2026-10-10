"""Problem 6.40: find every crossing of two curves by starting Newton from a grid of
points."""
import numpy as np

from nmkit.nlsys import newton_system

def F(v):
    x, y = v
    return np.array([x * x + y * y - 4.0, np.exp(x) + y - 1.0])

found = []
for gx in np.linspace(-3, 3, 13):
    for gy in np.linspace(-3, 3, 13):
        x, k, _ = newton_system(F, [gx, gy], tol=1e-12, max_iter=40)
        if np.max(np.abs(F(x))) < 1e-9:
            if not any(np.max(np.abs(x - f)) < 1e-6 for f in found):
                found.append(x)

print("starting points tried:", 13 * 13)
print("distinct crossings found:", len(found))
for f in sorted(found, key=lambda v: v[0]):
    print("   ", np.array2string(f, precision=12), " residual",
          f"{np.max(np.abs(F(f))):.2e}")
