"""Stiffness is a number, and it is read off the Jacobian."""
import numpy as np

from nmkit.nlsys import jacobian_fd

systems = [
    ("a mild system", lambda y: np.array([-2.0 * y[0] + y[1], y[0] - 3.0 * y[1]]),
     np.array([1.0, 1.0])),
    ("the stiff one", lambda y: np.array([-1000.0 * y[0] + 999.0 * y[1], -y[1]]),
     np.array([1.0, 1.0])),
    ("a chemical model", lambda y: np.array([-0.04 * y[0] + 1e4 * y[1] * y[2],
                                             0.04 * y[0] - 1e4 * y[1] * y[2]
                                             - 3e7 * y[1] ** 2,
                                             3e7 * y[1] ** 2]),
     np.array([1.0, 1e-5, 0.0])),
]
print(f"{'system':>18} {'slowest rate':>15} {'fastest rate':>15} {'ratio':>12}")
for name, F, at in systems:
    lam = np.linalg.eigvals(jacobian_fd(F, at))
    sizes = np.sort(np.abs(lam[np.abs(lam) > 1e-12]))
    print(f"{name:>18} {sizes[0]:>15.4e} {sizes[-1]:>15.4e} "
          f"{sizes[-1] / sizes[0]:>12.4e}")
print()
print("a ratio near one needs nothing special. A ratio in the thousands means the step")
print("is set by a component that stopped mattering long ago.")
