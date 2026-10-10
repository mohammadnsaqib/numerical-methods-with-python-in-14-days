"""Problem 5.39: Cholesky against LU, counted rather than timed."""
import numpy as np

from nmkit.factor import cholesky
from nmkit.linsolve import lu_pivot

def count_chol(n):
    """Roughly n**3 / 6: the inner sum runs over j entries for each of the n(n+1)/2
    cells."""
    return sum(j + 1 for i in range(n) for j in range(i + 1))

def count_lu(n):
    return sum((n - k) * (n - k) for k in range(n - 1))

rng = np.random.default_rng(83)
print(f"{'n':>5} {'Cholesky':>10} {'LU':>10} {'ratio':>8} {'largest rebuild gap':>21}")
for n in (4, 8, 16, 32, 64):
    B = rng.normal(size=(n, n))
    A = B @ B.T + n * np.eye(n)
    L = cholesky(A)
    gap = np.max(np.abs(L @ L.T - A))
    c, l = count_chol(n), count_lu(n)
    print(f"{n:>5} {c:>10} {l:>10} {l / c:>8.2f} {gap:>21.3e}")
