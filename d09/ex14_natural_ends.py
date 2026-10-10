"""Natural ends set the curvature to zero, which is a choice and not a property of the
data."""
import numpy as np

from nmkit.spline import cubic_spline

xs = np.linspace(0.0, 3.0, 7)
ys = np.sin(xs)
m = cubic_spline(xs, ys, bc="natural")

print("second derivatives at the knots:", np.array2string(m, precision=6))
print("the true second derivative of sin is -sin:",
      np.array2string(-np.sin(xs), precision=6))
print("\nat the ends the spline says 0 and the truth says",
      f"{-np.sin(xs[0]):.6f} and {-np.sin(xs[-1]):.6f}")
