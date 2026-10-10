"""Six independent checks on one answer, each from a different day of the book."""
import numpy as np
import scipy.integrate as si

from d14._fin import L, TA, U0, UL, loss, rhs_system
from nmkit.bvp import shoot
from nmkit.interp import lagrange_eval
from nmkit.lstsq import design_matrix, lstsq_qr, polyval, r_squared
from nmkit.quad import gauss_legendre, simpson_n
from nmkit.spline import cubic_spline, spline_eval

N = 2000
ts, ys, slope, miss, _ = shoot(rhs_system, 0.0, L, U0, UL, -2000.0, -500.0, n=N)
u, du = ys[:, 0], ys[:, 1]
h = L / N

# Day 11. The equation says u'' equals the loss. A centred second difference of the
# ANSWER should reproduce that, and it was never used to produce the answer.
d2 = (u[:-2] - 2 * u[1:-1] + u[2:]) / (h * h)
gap = float(np.max(np.abs(d2 - loss(u[1:-1]))))
print(f"1. the equation, checked by differencing the answer (Day 11)")
print(f"   largest gap between u'' and the loss : {gap:.3e}")
print(f"   as a share of u'' itself             : "
      f"{gap / float(np.max(np.abs(d2))):.3e}")

# Day 12. Integrating u'' across the fin must give the change in u', and the left side
# is a quadrature of a function of the answer while the right side is read off the
# endpoints.
def loss_at(x):
    return loss(np.interp(x, ts, u))


by_simpson = simpson_n(loss_at, 0.0, L, 2000)
by_gauss = gauss_legendre(loss_at, 0.0, L, 60)
print(f"2. the heat balance, by quadrature (Day 12)")
print(f"   integral of the loss, Simpson        : {by_simpson:.9f}")
print(f"   integral of the loss, Gauss          : {by_gauss:.9f}")
print(f"   change in the gradient, u'(L) - u'(0): {du[-1] - du[0]:.9f}")
print(f"   they differ by                       : "
      f"{abs(by_simpson - (du[-1] - du[0])):.3e}")

# Day 9. A spline through nine samples should reproduce the whole curve, and a single
# polynomial through the same nine should not do as well.
idx = np.linspace(0, N, 9).astype(int)
xs, us = ts[idx], u[idx]
sp = spline_eval(xs, us, cubic_spline(xs, us), ts)
poly = lagrange_eval(xs, us, ts)
print(f"3. the shape, resampled (Days 8 and 9)")
print(f"   a spline through 9 points is off by  : {np.max(np.abs(sp - u)):.3e}")
print(f"   one polynomial through the same 9    : {np.max(np.abs(poly - u)):.3e}")
print(f"   the POLYNOMIAL wins, by "
      f"{np.max(np.abs(sp - u)) / np.max(np.abs(poly - u)):.0f} times. Nine points on "
      f"a")
print("   smooth curve over a tenth of a metre is not where Day 8 broke down.")

# Day 10. The profile is close to, but not equal to, a decaying exponential. Least
# squares says how close, and r squared alone is not the answer -- Day 10 said so.
A = design_matrix(ts, 3)
c = lstsq_qr(A, u)
print(f"4. a model fitted to the profile (Day 10)")
print(f"   a cubic fit has r squared            : {r_squared(u, polyval(c, ts)):.9f}")
print(f"   and is still wrong by                : "
      f"{np.max(np.abs(polyval(c, ts) - u)):.4f} K")

# Day 5. The finite-difference matrix's conditioning says how many digits a solve can
# lose.
from nmkit.bvp import fd_matrix
from nmkit.norms import digits_lost
A_fd = fd_matrix(lambda x: 0.0, lambda x: -100.0, 0.0, L, 400)
print(f"5. the conditioning of the other route (Day 5)")
print(f"   digits a 400-panel solve may lose    : {digits_lost(A_fd, 2):.4f}")

# The oracle. An independent solver, given the same problem in its own form.
sol = si.solve_bvp(lambda x, y: np.vstack([y[1], loss(y[0])]),
                   lambda ya, yb: np.array([ya[0] - U0, yb[0] - UL]),
                   np.linspace(0.0, L, 40),
                   np.vstack([np.linspace(U0, UL, 40), np.full(40, -2000.0)]),
                   tol=1e-10)
print(f"6. against an independent solver")
print(f"   its status                           : {sol.status} ({sol.message})")
print(f"   its slope at x = 0                   : {sol.sol(0.0)[1]:.9f}")
print(f"   ours                                 : {slope:.9f}")
print(f"   largest gap in u across the fin      : "
      f"{np.max(np.abs(sol.sol(ts)[0] - u)):.3e} K")
