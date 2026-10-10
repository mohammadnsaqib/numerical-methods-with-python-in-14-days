"""Problem 6.38: Gauss-Seidel depends on the order the unknowns are updated in; Jacobi
does not."""
import numpy as np

from nmkit.iterative import gauss_seidel, jacobi

# A SYMMETRIC permutation -- the same reordering applied to the rows AND the columns --
# renames the unknowns without changing the system. Permuting the rows alone would be a
# different experiment: it moves a different entry onto each diagonal, so it changes
# what BOTH methods divide by, and it can destroy the diagonal dominance that made them
# converge at all.
A = np.array([[4.0, -1.0, -1.0], [-2.0, 6.0, 1.0], [-1.0, 1.0, 7.0]])
b = np.array([3.0, 9.0, -6.0])
answer = np.linalg.solve(A, b)

print(f"{'update order':>14} {'Jacobi':>8} {'Gauss-Seidel':>14} {'same answer':>13}")
for perm in ([0, 1, 2], [1, 0, 2], [2, 1, 0], [1, 2, 0]):
    p = np.array(perm)
    Ap, bp = A[np.ix_(p, p)], b[p]
    xj, kj, _ = jacobi(Ap, bp, tol=1e-10, max_iter=2000)
    xg, kg, _ = gauss_seidel(Ap, bp, tol=1e-10, max_iter=2000)
    agree = max(np.max(np.abs(xj[np.argsort(p)] - answer)),
                np.max(np.abs(xg[np.argsort(p)] - answer))) < 1e-8
    print(f"{str(perm):>14} {kj:>8} {kg:>14} {str(agree):>13}")
print("\nthe Jacobi column never moves: its sweep reads only old values, so the order")
print("the entries are written in cannot matter. The Gauss-Seidel column does move.")
