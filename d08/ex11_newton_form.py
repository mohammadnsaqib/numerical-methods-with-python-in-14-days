"""The nested form costs one multiply and one add per point, and never forms a large
power."""
import numpy as np

from nmkit.interp import divided_differences, lagrange_eval, newton_eval

xs = np.array([0.0, 1.0, 2.0, 4.0])
ys = np.array([1.0, 3.0, 2.0, 5.0])
c = divided_differences(xs, ys)[0]

t = np.linspace(-1, 5, 7)
print("Newton form :", np.array2string(newton_eval(xs, c, t), precision=8))
print("Lagrange    :", np.array2string(lagrange_eval(xs, ys, t), precision=8))
print("largest gap "
      ":", f"{np.max(np.abs(newton_eval(xs, c, t) - lagrange_eval(xs, ys, t))):.3e}")
