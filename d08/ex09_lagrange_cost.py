"""Adding one point means starting over, because every basis function changes."""
import numpy as np

from nmkit.interp import lagrange_eval

xs = np.array([0.0, 1.0, 2.0])
ys = np.array([1.0, 3.0, 2.0])
print("with three points, value at 1.5:", f"{lagrange_eval(xs, ys, 1.5):.10f}")

xs4 = np.append(xs, 4.0)
ys4 = np.append(ys, 5.0)
print("with a fourth added,          :", f"{lagrange_eval(xs4, ys4, 1.5):.10f}")
print()
print("every basis function was rebuilt: none "
      "of the first three survives the addition.")
