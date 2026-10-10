"""Second order in the spacing, and a conditioning that grows like its square."""
import numpy as np

from nmkit.bvp import fd_bvp, fd_matrix
from nmkit.norms import cond

B = np.pi / 2
prev = None
print(f"{'panels':>8} {'h':>10} {'largest error':>16} {'ratio':>8} "
      f"{'condition number':>18} {'ratio':>8}")
prev_k = None
for n in (10, 20, 40, 80, 160, 320, 640):
    x, y = fd_bvp(lambda v: 0.0, lambda v: -1.0, lambda v: 0.0, 0.0, B, 0.0, 1.0, n)
    e = float(np.max(np.abs(y - np.sin(x))))
    k = cond(fd_matrix(lambda v: 0.0, lambda v: -1.0, 0.0, B, n), 2)
    r1 = "" if prev is None else f"{prev / e:.4f}"
    r2 = "" if prev_k is None else f"{k / prev_k:.4f}"
    print(f"{n:>8} {B / n:>10.6f} {e:>16.3e} {r1:>8} {k:>18.4e} {r2:>8}")
    prev, prev_k = e, k
print()
print("the error quarters and the conditioning quadruples. One buys what the other")
print("spends, so the digits actually gained per refinement are fewer than they look.")
