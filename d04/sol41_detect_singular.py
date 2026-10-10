"""Problem 4.41: the factorisation reports singularity, and a zero on U's diagonal is
the sign."""
import numpy as np

from nmkit.linsolve import lu_pivot

cases = [
    ("nonsingular  ", np.array([[2.0, 1.0], [1.0, 3.0]])),
    ("exactly singular", np.array([[1.0, 2.0], [2.0, 4.0]])),
    ("nearly singular ", np.array([[1.0, 2.0], [2.0, 4.0 + 1e-14]])),
]
for name, A in cases:
    LU, _, _ = lu_pivot(A)
    d = np.abs(np.diag(LU))
    print(f"{name}: diagonal of U {np.array2string(d, precision=3)}  "
          f"smallest {d.min():.3e}  ratio {d.min() / d.max():.3e}")
print("\nan exact zero is a certainty; a tiny ratio is a warning, and Day 5 measures "
      "it.")
