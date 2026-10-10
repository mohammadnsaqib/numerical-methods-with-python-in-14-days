"""Problem 14.38: one boundary problem two ways, on which the differences are EXACT."""
import numpy as np

from nmkit.bvp import fd_bvp, fd_matrix, shoot
from nmkit.norms import cond

# y'' = (2/x) y' - (2/x^2) y has solutions x and x^2. With y(1) = 1 and y(2) = 4 the
# answer is x^2 -- a quadratic, which the centred second difference reproduces with NO
# truncation error at all. That makes this problem a measurement of the conditioning by
# itself.
A, B = 1.0, 2.0
ALPHA, BETA = 1.0, 4.0


def exact(x):
    return x ** 2


ts, ys, slope, miss, iters = shoot(
    lambda x, y: np.array([y[1], (2.0 / x) * y[1] - (2.0 / x ** 2) * y[0]]),
    A, B, ALPHA, BETA, 1.0, 3.0, n=400)
print(f"SHOOTING: slope {slope:.12f} (the true one is 2), {iters} secant steps")
print(f"          largest error {np.max(np.abs(ys[:, 0] - exact(ts))):.3e}")
print()
print(f"{'panels':>8} {'largest error':>16} {'ratio':>8} {'condition number':>18} "
      f"{'ratio':>8}")
prev, prev_k = None, None
for n in (10, 20, 40, 80, 160, 320):
    x, y = fd_bvp(lambda v: 2.0 / v, lambda v: -2.0 / v ** 2, lambda v: 0.0,
                  A, B, ALPHA, BETA, n)
    e = float(np.max(np.abs(y - exact(x))))
    k = cond(fd_matrix(lambda v: 2.0 / v, lambda v: -2.0 / v ** 2, A, B, n), 2)
    print(f"{n:>8} {e:>16.3e} {'' if prev is None else f'{e / prev:.3f}':>8} "
          f"{k:>18.4e} {'' if prev_k is None else f'{k / prev_k:.3f}':>8}")
    prev, prev_k = e, k
print()
print("the error column RISES. There is no truncation error to fall: a quadratic is")
print("reproduced exactly by a centred second difference. What is left is round-off,")
print("amplified by a condition number that quadruples at every refinement, exactly as")
print("Example 14.19 measured. More panels is the wrong move on this problem.")
