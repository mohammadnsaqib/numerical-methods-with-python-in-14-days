"""Problem 6.41: how the two methods' costs grow with the number of unknowns."""
import numpy as np

from nmkit.nlsys import broyden, count_calls, newton_system

def make(n):
    """A system whose answer is all ones, at any size."""
    def F(v):
        return np.array([v[i] ** 2 + v[(i + 1) % n] - 2.0 for i in range(n)])
    return F

print(f"{'n':>4} {'Newton steps':>13} {'Newton calls':>13} "
      f"{'Broyden steps':>14} {'Broyden calls':>14}")
for n in (2, 4, 8, 16):
    Fn = count_calls(make(n))
    _, kn, _ = newton_system(Fn, np.full(n, 1.5), tol=1e-11)
    Fb = count_calls(make(n))
    _, kb, _ = broyden(Fb, np.full(n, 1.5), tol=1e-11)
    print(f"{n:>4} {kn:>13} {Fn.count():>13} {kb:>14} {Fb.count():>14}")
print("\nNewton's calls grow with n; Broyden's barely move.")
