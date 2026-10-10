"""A vector is a solution when substituting it back leaves nothing, and that is
checkable."""
import numpy as np

from nmkit.linsolve import residual

A = np.array([[2.0, 1.0, -1.0], [-3.0, -1.0, 2.0], [-2.0, 1.0, 2.0]])
b = np.array([8.0, -11.0, -3.0])

for name, x in (("the true answer", np.array([2.0, 3.0, -1.0])),
                ("a near miss   ", np.array([2.0, 3.0, -1.001])),
                ("a wrong guess ", np.array([1.0, 1.0, 1.0]))):
    r = residual(A, x, b)
    print(f"{name}: residual {np.array2string(r, precision=4)}  size "
          f"{np.linalg.norm(r):.4e}")
