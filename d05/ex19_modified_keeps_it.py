"""One reordering of the same subtractions is the whole difference, measured across four
cases."""
import numpy as np

from nmkit.factor import gram_schmidt, orthogonality_error

print(f"{'nearly parallel to':>20} {'classical':>14} {'modified':>14}")
for eps in (1e-2, 1e-4, 1e-6, 1e-8):
    A = np.array([[1.0, 1.0, 1.0], [eps, 0.0, 0.0], [0.0, eps, 0.0], [0.0, 0.0, eps]])
    Qc, _ = gram_schmidt(A, modified=False)
    Qm, _ = gram_schmidt(A, modified=True)
    print(f"{eps:>20.0e} {orthogonality_error(Qc):>14.3e} "
          f"{orthogonality_error(Qm):>14.3e}")
