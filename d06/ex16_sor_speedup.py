"""On a two-dimensional grid the best omega approaches 2 and the saving grows with the
size."""
import numpy as np

from nmkit.iterative import gauss_seidel, sor

def poisson(m):
    """The five-point Laplacian on an m by m grid: the standard test for these methods.
    """
    n = m * m
    A = np.zeros((n, n))
    for i in range(m):
        for j in range(m):
            k = i * m + j
            A[k, k] = 4.0
            for di, dj in ((-1, 0), (1, 0), (0, -1), (0, 1)):
                p, q = i + di, j + dj
                if 0 <= p < m and 0 <= q < m:
                    A[k, p * m + q] = -1.0
    return A

print(f"{'grid':>7} {'size':>6} {'Gauss-Seidel':>14} {'best SOR':>10} {'omega':>7} "
      f"{'speedup':>9}")
for m in (4, 6, 8, 10):
    A = poisson(m)
    b = np.ones(m * m)
    _, kg, _ = gauss_seidel(A, b, tol=1e-10, max_iter=8000)
    best = min(((sor(A, b, omega=float(w), tol=1e-10, max_iter=8000)[1], float(w))
                for w in np.arange(1.0, 1.99, 0.01)))
    print(f"{m:>3} by {m:<2} {m * m:>6} {kg:>14} {best[0]:>10} {best[1]:>7.2f} "
          f"{kg / best[0]:>9.2f}")
