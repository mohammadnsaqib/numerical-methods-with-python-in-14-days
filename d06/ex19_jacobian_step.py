"""The step used for the estimate matters, and there is a best one."""
import numpy as np

from nmkit.nlsys import jacobian_fd

def F(v):
    x, y = v
    return np.array([x * x + y * y - 4.0, np.exp(x) + y - 1.0])

x = np.array([1.0, 1.7])
exact = np.array([[2 * x[0], 2 * x[1]], [np.exp(x[0]), 1.0]])
print(f"{'step':>10} {'largest gap':>14}")
for p in range(1, 13):
    h = 10.0 ** -p
    print(f"{h:>10.0e} {np.max(np.abs(jacobian_fd(F, x, h=h) - exact)):>14.3e}")
