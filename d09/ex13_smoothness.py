"""The slope jump at a knot is what separates a spline from straight pieces, so both are
measured."""
import numpy as np

from nmkit.spline import cubic_spline, piecewise_linear, spline_eval

xs = np.array([0.0, 1.0, 2.0, 3.0])
ys = np.array([0.0, 1.0, 0.0, 2.0])
m = cubic_spline(xs, ys)
eps = 1e-5

def slope_jump(f, x):
    """The slope just after a knot minus the slope just before it."""
    before = (f(x - eps) - f(x - 2 * eps)) / eps
    after = (f(x + 2 * eps) - f(x + eps)) / eps
    return abs(after - before)

spl = lambda t: spline_eval(xs, ys, m, t)
lin = lambda t: piecewise_linear(xs, ys, t)

print(f"{'knot':>6} {'spline slope jump':>20} {'straight pieces':>18}")
for i in (1, 2):
    print(f"{i:>6} {slope_jump(spl, xs[i]):>20.3e} {slope_jump(lin, xs[i]):>18.3e}")
print()
print("the spline's jumps are at the size of the difference step used to measure them;")
print("the straight pieces' are the real corners, of size 2 and 3.")
