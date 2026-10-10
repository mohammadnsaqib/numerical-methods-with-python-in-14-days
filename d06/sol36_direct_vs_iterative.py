"""Problem 6.36: the size at which an iteration overtakes elimination, measured rather
than assumed."""
import time

import numpy as np

from nmkit.iterative import gauss_seidel
from nmkit.linsolve import solve

def best_of(fn, repeats=5):
    """The shortest of several runs, which is the only reproducible one.

    A crossover found from one reading of each side is a crossover that moves between
    runs.
    """
    best = float("inf")
    for _ in range(repeats):
        t0 = time.perf_counter()
        fn()
        best = min(best, time.perf_counter() - t0)
    return best


print(f"{'size':>6} {'elimination':>13} {'sweeps':>8} {'iteration':>11} {'winner':>12}")
for n in (20, 40, 80, 160):
    A = (np.diag(4.0 * np.ones(n)) + np.diag(-1.0 * np.ones(n - 1), 1)
         + np.diag(-1.0 * np.ones(n - 1), -1))
    b = np.ones(n)
    direct = best_of(lambda: solve(A, b))
    iterative = best_of(lambda: gauss_seidel(A, b, tol=1e-10, max_iter=4000))
    _, k, _ = gauss_seidel(A, b, tol=1e-10, max_iter=4000)
    print(f"{n:>6} {direct:>13.4f} {k:>8} {iterative:>11.4f} "
          f"{'elimination' if direct < iterative else 'iteration':>12}")
