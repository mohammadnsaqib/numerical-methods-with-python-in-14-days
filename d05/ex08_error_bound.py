"""The residual does bound the error, once it is multiplied by the condition number."""
import numpy as np

from nmkit.linsolve import residual, solve
from nmkit.norms import cond, hilbert, vnorm

print(f"{'n':>4} {'rel residual':>14} {'rel error':>12} {'cond':>12} {'bound':>12}")
for n in (4, 6, 8, 10, 12):
    A = hilbert(n)
    x_true = np.ones(n)
    b = A @ x_true
    x = solve(A, b)
    rr = vnorm(residual(A, x, b), 2) / vnorm(b, 2)
    re = vnorm(x - x_true, 2) / vnorm(x_true, 2)
    k = cond(A, 2)
    print(f"{n:>4} {rr:>14.3e} {re:>12.3e} {k:>12.3e} {k * rr:>12.3e}")
