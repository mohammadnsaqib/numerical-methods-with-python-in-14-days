"""The predicted loss of digits is checked against the digits a real solve actually
keeps."""
import numpy as np

from nmkit.linsolve import solve
from nmkit.norms import cond, hilbert, vnorm

print(f"{'n':>4} {'predicted loss':>16} {'measured loss':>15}")
for n in (2, 4, 6, 8, 10):
    A = hilbert(n)
    x_true = np.ones(n)
    x = solve(A, A @ x_true)
    re = vnorm(x - x_true, 2) / vnorm(x_true, 2)
    measured = -np.log10(re) if re > 0 else 16.0
    print(f"{n:>4} {np.log10(cond(A, 2)):>16.2f} {16 - measured:>15.2f}")
