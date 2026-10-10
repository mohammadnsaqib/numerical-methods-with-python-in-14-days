"""The closer the shift, the fewer the steps, because the separation it creates is
larger."""
import numpy as np

from nmkit.eigen import inverse_iteration

A = np.array([[4.0, 1.0, 0.0], [1.0, 3.0, 1.0], [0.0, 1.0, 2.0]])
target = float(np.linalg.eigvalsh(A)[1])
print("the eigenvalue being sought:", f"{target:.12f}")
print(f"{'shift':>10} {'distance':>12} {'steps':>7}")
for off in (1.0, 0.5, 0.1, 0.01):
    lam, _, k, _ = inverse_iteration(A, target + off, tol=1e-13, max_iter=500)
    print(f"{target + off:>10.4f} {off:>12.2f} {k:>7}")
