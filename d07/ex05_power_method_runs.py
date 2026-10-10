"""The routine finds the largest eigenvalue of a matrix with no closed form for it."""
import numpy as np

from nmkit.eigen import power_method, residual

rng = np.random.default_rng(97)
B = rng.normal(size=(6, 6))
A = B + B.T  # symmetric, so the eigenvalues are real

lam, v, k, _ = power_method(A, tol=1e-13)
true = np.linalg.eigvalsh(A)
print("largest eigenvalue found:", f"{lam:.13f}")
print("largest from "
      "numpy      :", f"{max(abs(true)) * np.sign(true[np.argmax(abs(true))]):.13f}")
print("iterations              :", k)
print("residual                :", f"{residual(A, lam, v):.3e}")
