"""Problem 5.41: the condition number estimated by perturbing, against the computed one.
"""
import numpy as np

from nmkit.linsolve import solve
from nmkit.norms import cond, hilbert, vnorm

rng = np.random.default_rng(89)

def estimate(A, trials=400):
    """The largest amplification found by moving b a little, in many random directions.
    """
    n = A.shape[0]
    b = np.ones(n)
    x = solve(A, b)
    worst = 0.0
    for _ in range(trials):
        d = rng.normal(size=n)
        d = d / vnorm(d, 2) * 1e-8 * vnorm(b, 2)
        worst = max(worst, (vnorm(solve(A, b + d) - x, 2) / vnorm(x, 2))
                    / (vnorm(d, 2) / vnorm(b, 2)))
    return worst

print(f"{'n':>4} {'estimated':>14} {'computed':>14} {'ratio':>8}")
for n in (3, 5, 7, 9):
    A = hilbert(n)
    est, true = estimate(A), cond(A, 2)
    print(f"{n:>4} {est:>14.4e} {true:>14.4e} {est / true:>8.4f}")
print("\nthe estimate is a lower bound: it finds the worst direction it happened to "
      "try.")
