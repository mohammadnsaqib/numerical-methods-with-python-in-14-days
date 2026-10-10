"""Problem 14.41: which day of the book each part of the capstone came from."""
import numpy as np

from d14._fin import L, U0, UL, loss, loss_slope, rhs_system
from nmkit.bvp import fd_matrix, shoot
from nmkit.err import rel_err
from nmkit.nlsys import newton_system
from nmkit.norms import cond, digits_lost
from nmkit.quad import gauss_legendre, simpson_n
from nmkit.spline import cubic_spline, spline_eval

ts, ys, slope, miss, iters = shoot(rhs_system, 0.0, L, U0, UL, -2000.0, -500.0, n=1600)
u, du = ys[:, 0], ys[:, 1]

rows = []
rows.append(("Day 1", "relative error of a 400-step answer",
             rel_err(float(shoot(rhs_system, 0.0, L, U0, UL, -2000.0, -500.0,
                                   n=400)[2]), slope)))
rows.append(("Day 2", "secant steps to find the missing slope", float(iters)))
N = 400


def residual(v):
    h = L / N
    w = np.concatenate(([U0], v, [UL]))
    return (w[:-2] - 2.0 * w[1:-1] + w[2:]) / (h * h) - loss(w[1:-1])


def jac(v):
    h = L / N
    J = np.zeros((v.size, v.size))
    np.fill_diagonal(J, -2.0 / (h * h) - loss_slope(v))
    idx = np.arange(v.size - 1)
    J[idx, idx + 1] = 1.0 / (h * h)
    J[idx + 1, idx] = 1.0 / (h * h)
    return J


grid = np.linspace(0.0, L, N + 1)
root, newton_steps, _ = newton_system(residual, U0 + (UL - U0) * grid[1:-1] / L, J=jac)
A = fd_matrix(lambda x: 0.0, lambda x: -100.0, 0.0, L, N)
rows.append(("Day 4", "unknowns in the difference system", float(root.size)))
rows.append(("Day 5", "digits that solve may lose", digits_lost(A, 2)))
rows.append(("Day 6", "Newton steps on the nonlinear grid", float(newton_steps)))
h = L / 1600
d2 = (u[:-2] - 2 * u[1:-1] + u[2:]) / (h * h)
rows.append(("Day 11", "relative gap between u'' and the loss",
             float(np.max(np.abs(d2 - loss(u[1:-1])))) / float(np.max(np.abs(d2)))))
q = simpson_n(lambda v: loss(np.interp(v, ts, u)), 0.0, L, 1600)
rows.append(("Day 12", "relative gap in the heat balance",
             abs(q - float(du[-1] - du[0])) / abs(q)))
idx = np.linspace(0, 1600, 17).astype(int)
sp = spline_eval(ts[idx], u[idx], cubic_spline(ts[idx], u[idx]), ts)
rows.append(("Day 9", "relative error of a 17-knot spline",
             float(np.max(np.abs(sp - u))) / U0))
rows.append(("Day 13", "steps the fourth-order stepper took", float(ts.size - 1)))
rows.append(("Day 14", "miss at the far boundary, in kelvin", miss))

print(f"{'day':>8} {'what it contributed':>40} {'value':>13}")
for day, what, v in rows:
    print(f"{day:>8} {what:>40} {v:>13.4e}")
print()
print("ten of the fourteen days appear in one answer, and every one of them is a")
print("number that can be read rather than a claim that has to be believed.")
