"""Problem 9.38: the order of each piecewise method, measured rather than quoted."""
import numpy as np

from nmkit.spline import (cubic_spline, hermite_eval, pchip_slopes, piecewise_linear,
                          spline_eval)

f = np.sin
t = np.linspace(0.0, 3.0, 4000)

def order_of(build):
    errs = []
    for n in (9, 17, 33, 65):
        xs = np.linspace(0.0, 3.0, n)
        errs.append(np.max(np.abs(f(t) - build(xs, f(xs), t))))
    # Halving the spacing divides the error by 2 to the power of the order.
    return [np.log2(a / b) for a, b in zip(errs, errs[1:])]

print("piecewise linear  :",
      [f"{p:.3f}" for p in order_of(lambda x, y, tt: piecewise_linear(x, y, tt))])
print("cubic spline      :",
      [f"{p:.3f}" for p in order_of(
          lambda x, y, tt: spline_eval(x, y, cubic_spline(x, y), tt))])
print("shape-preserving  :",
      [f"{p:.3f}" for p in order_of(
          lambda x, y, tt: hermite_eval(x, y, pchip_slopes(x, y), tt))])
print("\nthe spline's natural ends hold it below four; Example 9.17 clamps them.")
