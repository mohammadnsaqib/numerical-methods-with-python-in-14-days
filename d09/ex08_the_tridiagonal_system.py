"""Each interior knot's equation touches only its two neighbours, so the matrix is
tridiagonal."""
import numpy as np

xs = np.array([0.0, 1.0, 2.0, 3.0, 4.0])
n = xs.size
h = np.diff(xs)
A = np.zeros((n, n))
A[0, 0] = A[-1, -1] = 1.0
for i in range(1, n - 1):
    A[i, i - 1] = h[i - 1]
    A[i, i] = 2.0 * (h[i - 1] + h[i])
    A[i, i + 1] = h[i]

print(A)
print("\nnonzero entries:", int(np.count_nonzero(A)), "out of", n * n)
print("every row's diagonal exceeds the sum of the rest:",
      bool(np.all(np.abs(np.diag(A)) > np.sum(np.abs(A), axis=1) - np.abs(np.diag(A)))))
