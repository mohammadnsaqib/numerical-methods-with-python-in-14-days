"""Problem 8.38: what each form costs to build and to evaluate."""
import time

import numpy as np

from nmkit.interp import divided_differences, lagrange_eval, newton_eval


def best_of(fn, repeats=5):
    """The shortest of several runs, which is the only reproducible one."""
    best = float("inf")
    for _ in range(repeats):
        t0 = time.perf_counter()
        fn()
        best = min(best, time.perf_counter() - t0)
    return best


rng = np.random.default_rng(173)
n = 40
xs = np.sort(rng.uniform(-1, 1, n))
ys = rng.uniform(-1, 1, n)
t = np.linspace(-1, 1, 4000)

build = best_of(lambda: divided_differences(xs, ys))
c = divided_differences(xs, ys)[0]
ev_newton = best_of(lambda: newton_eval(xs, c, t))
ev_lagrange = best_of(lambda: lagrange_eval(xs, ys, t))

print(f"{n} points, {t.size} evaluations")
print(f"  Newton: build {build:.4f}s, evaluate {ev_newton:.4f}s")
print(f"  Lagrange: build 0s, evaluate {ev_lagrange:.4f}s")
print(f"  ratio of the two evaluations: {ev_lagrange / ev_newton:.1f}")
print()
print("Newton pays once to build and little to "
      "evaluate. Lagrange pays nothing to build")
print("and the whole cost at every evaluation, "
      "which is the wrong way round for a curve")
print("that is drawn at four thousand points.")
