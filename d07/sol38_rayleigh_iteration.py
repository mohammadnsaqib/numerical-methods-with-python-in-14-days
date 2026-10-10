"""Problem 7.38: update the shift to the current Rayleigh quotient at every step."""
import numpy as np

from nmkit.eigen import rayleigh, residual
from nmkit.linsolve import solve

def rayleigh_iteration(A, x0, steps=8):
    """Inverse iteration whose shift is re-chosen every step from the current direction.

    A fixed shift converges at a fixed rate. Re-choosing it makes the shift better as
    the direction improves, and for a symmetric matrix the result is CUBIC: the digits
    triple.
    """
    x = np.asarray(x0, dtype=float)
    x = x / np.sqrt(x @ x)
    n = A.shape[0]
    hist = []
    for _ in range(steps):
        mu = rayleigh(A, x)
        try:
            y = solve(A - mu * np.eye(n), x)
        except (ZeroDivisionError, np.linalg.LinAlgError):
            break
        nrm = np.sqrt(y @ y)
        if not np.isfinite(nrm) or nrm == 0.0:
            break
        x = y / nrm
        hist.append(residual(A, rayleigh(A, x), x))
    return rayleigh(A, x), x, hist

A = np.array([[4.0, 1.0, 0.0], [1.0, 3.0, 1.0], [0.0, 1.0, 2.0]])
lam, v, hist = rayleigh_iteration(A, np.array([1.0, 0.4, 0.1]))
print("eigenvalue:", f"{lam:.14f}")
print("residual after each step:", [f"{h:.2e}" for h in hist])
print("the digits roughly triple each step, which is third order.")
