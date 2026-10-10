"""Problem 7.37: find every eigenvalue by sweeping a shift, accepting only what a
residual confirms."""
import numpy as np

from nmkit.eigen import inverse_iteration, residual

A = np.array([[4.0, 1.0, 0.0, 0.0], [1.0, 3.0, 1.0, 0.0],
              [0.0, 1.0, 2.0, 1.0], [0.0, 0.0, 1.0, 1.0]])
true = np.linalg.eigvalsh(A)
print("true:", np.array2string(true, precision=8))

# A converged flag is not enough. A run that stopped because two successive Rayleigh
# quotients happened to agree can return a value that is not an eigenvalue at all, and
# an earlier draft accepted one: it reported FIVE eigenvalues for a four by four matrix.
# The residual is what separates an answer from a stopping place.
found, rejected = [], 0
for shift in np.linspace(-1.0, 6.0, 29):
    lam, v, _, _ = inverse_iteration(A, float(shift), tol=1e-13, max_iter=300)
    if lam is None or residual(A, lam, v) > 1e-8:
        rejected += 1
        continue
    if not any(abs(lam - f) < 1e-7 for f in found):
        found.append(lam)

print("shifts tried    :", 29)
print("rejected by the residual:", rejected)
print("distinct found  :", len(found))
for f in sorted(found):
    print("   ", f"{f:.12f}")
print("largest gap from the true values:",
      f"{max(min(abs(f - t) for t in true) for f in found):.3e}")
