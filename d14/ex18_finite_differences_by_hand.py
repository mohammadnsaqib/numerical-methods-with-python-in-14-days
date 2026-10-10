"""Replace every derivative with a difference, and the equation becomes a matrix."""
import numpy as np

from nmkit.bvp import fd_matrix

# y'' = -y on [0, pi/2] with y(0) = 0 and y(pi/2) = 1. Written as y'' = p y' + q y + r
# with p = 0, q = -1 and r = 0, which is the form fd_bvp takes.
A = fd_matrix(lambda x: 0.0, lambda x: -1.0, 0.0, np.pi / 2, 6)
print(f"6 panels give {A.shape[0]} interior points and a {A.shape[0]} by {A.shape[1]} "
      f"matrix")
print()
for row in A:
    print("  " + " ".join(f"{v:>8.5f}" for v in row))
print()
nonzero = int(np.sum(np.abs(A) > 1e-14))
band = max(abs(i - j) for i in range(A.shape[0]) for j in range(A.shape[1])
           if abs(A[i, j]) > 1e-14)
print(f"nonzero entries: {nonzero} out of {A.size}")
print(f"the widest band: {band}")
print()
print("three diagonals and nothing else. Day 9's Thomas algorithm arrives here from")
print("a completely different direction, and solves this in time proportional to n.")
