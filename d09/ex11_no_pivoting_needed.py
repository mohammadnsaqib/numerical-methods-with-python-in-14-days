"""The matrix is diagonally dominant by construction, so the pass needs no pivoting."""
import numpy as np

rng = np.random.default_rng(179)
worst = 1e9
for _ in range(500):
    xs = np.sort(rng.uniform(0, 10, 8))
    if np.min(np.diff(xs)) < 1e-6:
        continue
    h = np.diff(xs)
    for i in range(1, 7):
        diagonal = 2.0 * (h[i - 1] + h[i])
        neighbours = h[i - 1] + h[i]
        worst = min(worst, diagonal / neighbours)
print("500 random node sets, 8 knots each")
print("smallest ratio of the diagonal to the sum of its neighbours:", f"{worst:.6f}")
print("the diagonal is 2(h1+h2) and the neighbours add to h1+h2, whatever the spacing.")
