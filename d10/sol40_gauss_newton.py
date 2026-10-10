"""Problem 10.40: the same exponential fitted through logarithms and fitted as it
stands."""
import numpy as np

from nmkit.lstsq import design_matrix, lstsq_qr

rng = np.random.default_rng(20261)
xs = np.linspace(0.0, 4.0, 30)
ys = 3.0 * np.exp(-0.6 * xs) + rng.normal(scale=0.05, size=30)


def sse(p):
    """The quantity a direct fit is trying to make small."""
    return float(np.sum((ys - p[0] * np.exp(p[1] * xs)) ** 2))


# Route one: take logarithms and fit a straight line. It needs positive data.
keep = ys > 0
lin = lstsq_qr(design_matrix(xs[keep], 1), np.log(ys[keep]))
via_logs = np.array([np.exp(lin[0]), lin[1]])

# Route two: Gauss-Newton on the residual itself, started from route one's answer. Each
# step linearises the model about the current parameters and solves a least-squares
# problem for the correction -- so the whole of today's machinery is the inner loop of a
# nonlinear fit.
p = via_logs.copy()
print(f"{'step':>5} {'a':>11} {'b':>11} {'sum of squares':>17} {'step size':>12}")
print(f"{0:>5} {p[0]:>11.6f} {p[1]:>11.6f} {sse(p):>17.9f} {'':>12}")
for k in range(1, 7):
    e = np.exp(p[1] * xs)
    J = np.column_stack([e, p[0] * xs * e])
    delta = lstsq_qr(J, ys - p[0] * e)
    p = p + delta
    print(f"{k:>5} {p[0]:>11.6f} {p[1]:>11.6f} {sse(p):>17.9f} "
          f"{np.max(np.abs(delta)):>12.3e}")
print(f"\nthrough logarithms  a {via_logs[0]:.6f}  b {via_logs[1]:.6f}  "
      f"sum of squares {sse(via_logs):.6f}")
print(f"fitted directly     a {p[0]:.6f}  b {p[1]:.6f}  sum of squares {sse(p):.6f}")
print(f"the values used to make the data  a 3.000000  b -0.600000")
