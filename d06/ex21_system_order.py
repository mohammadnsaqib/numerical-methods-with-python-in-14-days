"""The second order survives the generalisation, and the step sizes show it."""
import numpy as np

from nmkit.nlsys import newton_system
from nmkit.roots import order_estimate

def F(v):
    x, y = v
    return np.array([x * x + y * y - 4.0, np.exp(x) + y - 1.0])

_, _, hist = newton_system(F, [1.0, 1.0], tol=1e-15, max_iter=12)
print("step sizes:", [f"{h:.3e}" for h in hist])
print("order estimates:",
      [f"{p:.4f}" for p in order_estimate([h for h in hist if h > 1e-15])])
