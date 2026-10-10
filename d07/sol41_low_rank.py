"""Problem 7.41: keeping the largest singular values is the best approximation of its
size."""
import numpy as np

rng = np.random.default_rng(151)
A = rng.normal(size=(12, 10))
U, s, Vt = np.linalg.svd(A, full_matrices=False)

print(f"{'kept':>6} {'error in the 2-norm':>21} {'the next singular value':>25}")
for k in (1, 2, 4, 6, 8, 10):
    Ak = U[:, :k] @ np.diag(s[:k]) @ Vt[:k, :]
    err = np.linalg.norm(A - Ak, 2)
    nxt = s[k] if k < len(s) else 0.0
    print(f"{k:>6} {err:>21.10f} {nxt:>25.10f}")
print("\nthe error equals the first singular value that was dropped, every time.")
