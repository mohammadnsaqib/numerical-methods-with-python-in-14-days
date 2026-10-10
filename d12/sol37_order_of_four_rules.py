"""Problem 12.37: four rules, one measured order each, on one integrand."""
import numpy as np

from nmkit.quad import composite, midpoint, simpson_n, trapezoid, trapezoid_n

exact = np.e - 1.0


def midpoint_n(f, a, b, n):
    """The composite midpoint rule, for comparison on the same panels."""
    return composite(midpoint, f, a, b, n)


def gauss2_n(f, a, b, n):
    """Two-point Gauss on every panel, which is fourth order like Simpson."""
    from nmkit.quad import gauss_legendre
    edges = np.linspace(a, b, n + 1)
    return float(sum(gauss_legendre(f, edges[i], edges[i + 1], 2) for i in range(n)))


rules = [("midpoint", midpoint_n), ("trapezoidal", trapezoid_n),
         ("Simpson", simpson_n), ("two-point Gauss", gauss2_n)]
print(f"{'rule':>17} {'n = 8':>12} {'n = 16':>12} {'n = 32':>12} "
      f"{'measured order':>16}")
for name, fn in rules:
    e = [abs(fn(np.exp, 0.0, 1.0, n) - exact) for n in (8, 16, 32)]
    print(f"{name:>17} {e[0]:>12.3e} {e[1]:>12.3e} {e[2]:>12.3e} "
          f"{np.log2(e[1] / e[2]):>16.4f}")
