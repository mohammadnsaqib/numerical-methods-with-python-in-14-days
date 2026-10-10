"""The order of the composite trapezoidal rule, on three integrands."""
import numpy as np

from nmkit.quad import trapezoid_n

cases = [("exp(t) on [0, 1]", np.exp, 0.0, 1.0, np.e - 1.0),
         ("sin(t) on [0, pi]", np.sin, 0.0, np.pi, 2.0),
         ("1/(1+t^2) on [0, 1]", lambda v: 1.0 / (1.0 + v * v), 0.0, 1.0, np.pi / 4)]

print(f"{'integrand':>22} {'n = 16':>11} {'n = 32':>11} {'n = 64':>11} {'order':>8}")
for name, f, a, b, exact in cases:
    e = [abs(trapezoid_n(f, a, b, n) - exact) for n in (16, 32, 64)]
    print(f"{name:>22} {e[0]:>11.3e} {e[1]:>11.3e} {e[2]:>11.3e} "
          f"{np.log2(e[1] / e[2]):>8.4f}")
