"""Past a condition number of 1e16 no digit of the answer is guaranteed, and none
survives."""
import numpy as np

from nmkit.linsolve import solve
from nmkit.norms import cond, hilbert

n = 14
A = hilbert(n)
x_true = np.ones(n)
x = solve(A, A @ x_true)

print("condition number:", f"{cond(A, 2):.4e}")
print("first four entries of the answer, all of which should be 1:")
for v in x[:4]:
    print("   ", f"{v:+.6f}")
print("largest entry in size:", f"{np.max(np.abs(x)):.4f}")
