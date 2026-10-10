"""A matrix norm is the most the matrix can stretch anything, and it can be found by
searching."""
import numpy as np

from nmkit.norms import mnorm, vnorm

A = np.array([[3.0, 1.0], [0.0, 2.0]])
rng = np.random.default_rng(61)
best = 0.0
for _ in range(200000):
    x = rng.normal(size=2)
    best = max(best, vnorm(A @ x, 2) / vnorm(x, 2))

print("largest stretch found by searching:", f"{best:.10f}")
print("mnorm(A, 2) computed directly     :", f"{mnorm(A, 2):.10f}")
print("the search approaches it from below, as it must.")
