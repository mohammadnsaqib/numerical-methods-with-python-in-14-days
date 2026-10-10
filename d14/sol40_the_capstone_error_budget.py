"""Problem 14.40: where the capstone's error actually comes from."""
import numpy as np

from d14._fin import L, U0, UL, loss, loss_slope, rhs_system
from nmkit.bvp import shoot
from nmkit.nlsys import newton_system

REF, _, _, _, _ = shoot(rhs_system, 0.0, L, U0, UL, -2000.0, -500.0, n=12800)
_, ref_ys, ref_slope, _, _ = shoot(rhs_system, 0.0, L, U0, UL, -2000.0, -500.0, n=12800)
print(f"the reference slope at x = 0 is {ref_slope:.12f} K per metre")
print()

print("SHOOTING, whose stepper is fourth order")
prev = None
print(f"{'steps':>8} {'slope found':>18} {'error':>12} {'ratio':>8}")
for n in (50, 100, 200, 400, 800):
    _, _, s, _, _ = shoot(rhs_system, 0.0, L, U0, UL, -2000.0, -500.0, n=n)
    e = abs(s - ref_slope)
    ratio = "" if prev is None else f"{prev / e:.2f}"
    print(f"{n:>8} {s:>18.9f} {e:>12.3e} {ratio:>8}")
    prev = e
print()


def residual(v, n):
    h = L / n
    w = np.concatenate(([U0], v, [UL]))
    return (w[:-2] - 2.0 * w[1:-1] + w[2:]) / (h * h) - loss(w[1:-1])


def jac(v, n):
    h = L / n
    m = v.size
    J = np.zeros((m, m))
    np.fill_diagonal(J, -2.0 / (h * h) - loss_slope(v))
    idx = np.arange(m - 1)
    J[idx, idx + 1] = 1.0 / (h * h)
    J[idx + 1, idx] = 1.0 / (h * h)
    return J


print("FINITE DIFFERENCES, which are second order")
prev = None
print(f"{'panels':>8} {'largest error in u':>20} {'ratio':>8} {'Newton steps':>14}")
ref_u = ref_ys[:, 0]
for n in (25, 50, 100, 200, 400):
    x = np.linspace(0.0, L, n + 1)
    root, steps, _ = newton_system(lambda v: residual(v, n),
                                   U0 + (UL - U0) * x[1:-1] / L, J=lambda v: jac(v, n))
    u = np.concatenate(([U0], root, [UL]))
    e = float(np.max(np.abs(u - np.interp(x, REF, ref_u))))
    print(f"{n:>8} {e:>20.3e} {'' if prev is None else f'{prev / e:.2f}':>8} "
          f"{steps:>14}")
    prev = e
print()
print("the two columns fall at different rates, which is the whole difference between")
print("the routes: one inherits its stepper's order and one is fixed at two. The last")
print("shooting ratio overshoots 16 because the secant's own tolerance of 1e-12 is")
print("being approached, so that row measures the root finder, not the stepper.")
