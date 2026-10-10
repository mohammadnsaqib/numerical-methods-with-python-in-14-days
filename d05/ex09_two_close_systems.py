"""Two right-hand sides that differ by a whisker can have answers that differ
completely."""
import numpy as np

from nmkit.linsolve import solve
from nmkit.norms import cond, vnorm

A = np.array([[1.0, 1.0], [1.0, 1.0 + 1e-10]])
b1 = np.array([2.0, 2.0])
b2 = np.array([2.0, 2.0 + 1e-10])

x1, x2 = solve(A, b1), solve(A, b2)
print("b1 =", b1, "->", x1)
print("b2 =", b2, "->", x2)
print("relative change in b:", f"{vnorm(b2 - b1, 2) / vnorm(b1, 2):.3e}")
print("relative change in x:", f"{vnorm(x2 - x1, 2) / vnorm(x1, 2):.3e}")
print("condition number    :", f"{cond(A, 2):.3e}")
