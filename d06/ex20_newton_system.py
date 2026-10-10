"""Newton for systems: the same method, with a solve where the division was."""
import numpy as np

from nmkit.nlsys import newton_system

def F(v):
    x, y = v
    return np.array([x * x + y * y - 4.0, np.exp(x) + y - 1.0])

for guess in ([1.0, 1.0], [-2.0, 0.0]):
    x, k, hist = newton_system(F, guess, tol=1e-13)
    print(f"from {guess}: {k} steps -> {np.array2string(x, precision=12)}")
    print(f"{'':16} residual {np.max(np.abs(F(x))):.3e}")
