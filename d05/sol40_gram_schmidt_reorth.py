"""Problem 5.40: running the classical method twice recovers what one pass lost."""
import numpy as np

from nmkit.factor import gram_schmidt, orthogonality_error

def twice(A):
    """Orthogonalise, then orthogonalise the result again.

    Two passes of the classical method cost twice the work and reach the accuracy of the
    modified one. The reason is that the second pass starts from vectors already nearly
    orthogonal, so the subtractions it makes are tiny and cannot lose much.
    """
    Q1, R1 = gram_schmidt(A, modified=False)
    Q2, R2 = gram_schmidt(Q1, modified=False)
    return Q2, R2 @ R1

print(f"{'nearly parallel':>16} {'once':>12} {'twice':>12} {'modified':>12}")
for eps in (1e-4, 1e-8, 1e-12):
    A = np.array([[1.0, 1.0, 1.0], [eps, 0.0, 0.0], [0.0, eps, 0.0], [0.0, 0.0, eps]])
    Q1, _ = gram_schmidt(A, modified=False)
    Q2, _ = twice(A)
    Qm, _ = gram_schmidt(A, modified=True)
    print(f"{eps:>16.0e} {orthogonality_error(Q1):>12.2e} "
          f"{orthogonality_error(Q2):>12.2e} {orthogonality_error(Qm):>12.2e}")
