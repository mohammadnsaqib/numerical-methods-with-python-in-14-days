"""Problem 4.40: a matrix with three diagonals can be eliminated in a single pass."""
import numpy as np

from nmkit.linsolve import solve

def tri_solve(lower, diag, upper, b):
    """Eliminate a tridiagonal system in one forward pass and one backward pass.

    Only the entry directly below each pivot is nonzero, so a step touches two numbers
    rather than a whole submatrix. The cost falls from n cubed to n, which is Day 9's
    Thomas algorithm.
    """
    n = len(diag)
    c, d = np.array(upper, float), np.array(b, float)
    dg = np.array(diag, float)
    for i in range(1, n):
        m = lower[i - 1] / dg[i - 1]
        dg[i] -= m * c[i - 1]
        d[i] -= m * d[i - 1]
    x = np.zeros(n)
    x[-1] = d[-1] / dg[-1]
    for i in range(n - 2, -1, -1):
        x[i] = (d[i] - c[i] * x[i + 1]) / dg[i]
    return x

n = 8
lower, diag, upper = [1.0] * (n - 1), [4.0] * n, [1.0] * (n - 1)
A = np.diag(diag) + np.diag(lower, -1) + np.diag(upper, 1)
b = np.arange(1.0, n + 1.0)

print("tridiagonal "
      "pass:", np.array2string(tri_solve(lower, diag, upper, b), precision=10))
print("full elimination:", np.array2string(solve(A, b), precision=10))
print("largest gap     "
      ":", f"{np.max(np.abs(tri_solve(lower, diag, upper, b) - solve(A, b))):.3e}")
