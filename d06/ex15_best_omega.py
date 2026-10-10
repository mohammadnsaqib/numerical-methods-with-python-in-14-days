"""The best value of omega is found by search, and outside 0 to 2 nothing converges at
all."""
import numpy as np

from nmkit.iterative import sor

n = 20
A = (np.diag(4.0 * np.ones(n)) + np.diag(-1.0 * np.ones(n - 1), 1)
     + np.diag(-1.0 * np.ones(n - 1), -1))
b = np.ones(n)

best_w, best_k = None, 10 ** 9
for w in np.arange(0.5, 1.96, 0.05):
    _, k, _ = sor(A, b, omega=float(w), tol=1e-10, max_iter=3000)
    if k < best_k:
        best_w, best_k = float(w), k
print(f"best omega found: {best_w:.2f} at {best_k} sweeps")

for w in (2.0, 2.1):
    _, k, hist = sor(A, b, omega=w, tol=1e-10, max_iter=60)
    print(f"omega {w}: stopped after {k} sweeps with a step of {hist[-1]:.3e}")
