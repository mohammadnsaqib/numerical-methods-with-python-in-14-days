"""The 1 and infinity norms have closed forms: the largest column sum and the largest
row sum."""
import numpy as np

from nmkit.norms import mnorm

A = np.array([[3.0, -1.0, 2.0], [0.0, 4.0, -1.0], [1.0, 1.0, 1.0]])
print("A =\n", A)
print("column sums of |A|:", np.sum(np.abs(A), axis=0), " largest:", mnorm(A, 1))
print("row sums of |A|   :", np.sum(np.abs(A), axis=1), " largest:", mnorm(A, np.inf))
print("numpy agrees      :", np.linalg.norm(A, 1), np.linalg.norm(A, np.inf))
