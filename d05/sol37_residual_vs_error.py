"""Problem 5.37: the residual and the error on one family, so the gap between them is a
curve."""
import numpy as np

from nmkit.linsolve import residual, solve
from nmkit.norms import cond, hilbert, vnorm

print(f"{'n':>4} {'cond':>12} {'residual':>12} {'error':>12} {'error/residual':>16}")
for n in range(2, 13):
    A = hilbert(n)
    x_true = np.ones(n)
    b = A @ x_true
    x = solve(A, b)
    r = vnorm(residual(A, x, b), 2) / vnorm(b, 2)
    e = vnorm(x - x_true, 2) / vnorm(x_true, 2)
    ratio = e / r if r > 0 else float("inf")
    print(f"{n:>4} {cond(A, 2):>12.3e} {r:>12.3e} {e:>12.3e} {ratio:>16.3e}")
