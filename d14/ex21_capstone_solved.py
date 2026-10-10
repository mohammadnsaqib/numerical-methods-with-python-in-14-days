"""The same problem solved twice, by two methods that share no code."""
import numpy as np

from d14._fin import L, TA, U0, UL, loss, loss_slope, rhs_system
from nmkit.bvp import shoot
from nmkit.nlsys import newton_system

# Route one: shooting. Day 13's Runge-Kutta walks the trajectory and Day 2's secant
# hunts the missing slope at the left end.
ts, ys, slope, miss, iters = shoot(rhs_system, 0.0, L, U0, UL, -2000.0, -500.0, n=400)
print("SHOOTING")
print(f"  the slope found at x = 0 : {slope:.9f} K per metre")
print(f"  the miss at the far end  : {miss:.3e} K")
print(f"  secant steps             : {iters}")
print()


# Route two: finite differences. Day 11's centred formula turns the equation into one
# equation per interior point, and Day 6's Newton for systems solves the whole nonlinear
# set at once. Nothing marches, so no guess can send anything to infinity.
def residual(u_interior, n):
    """What the difference equations leave over at every interior point."""
    h = L / n
    u = np.concatenate(([U0], u_interior, [UL]))
    return (u[:-2] - 2.0 * u[1:-1] + u[2:]) / (h * h) - loss(u[1:-1])


def jacobian(u_interior, n):
    """The Jacobian of those equations, which is TRIDIAGONAL and known in closed form.
    """
    h = L / n
    m = u_interior.size
    J = np.zeros((m, m))
    np.fill_diagonal(J, -2.0 / (h * h) - loss_slope(u_interior))
    idx = np.arange(m - 1)
    J[idx, idx + 1] = 1.0 / (h * h)
    J[idx + 1, idx] = 1.0 / (h * h)
    return J


N = 400
x = np.linspace(0.0, L, N + 1)
start = U0 + (UL - U0) * x[1:-1] / L
root, steps, history = newton_system(lambda v: residual(v, N), start,
                                     J=lambda v: jacobian(v, N))
u_fd = np.concatenate(([U0], root, [UL]))
print("FINITE DIFFERENCES")
print(f"  interior unknowns        : {N - 1}")
print(f"  Newton steps             : {steps}")
print(f"  step sizes               : " + ", ".join(f"{v:.1e}" for v in history))
print(f"  largest residual left    : {np.max(np.abs(residual(root, N))):.3e}")
print()

print(f"{'x':>8} {'shooting':>14} {'differences':>14} {'gap':>12}")
for k in range(0, 401, 80):
    print(f"{x[k]:>8.4f} {ys[k, 0]:>14.8f} {u_fd[k]:>14.8f} "
          f"{abs(ys[k, 0] - u_fd[k]):>12.3e}")
print()
print(f"the two routes agree to {np.max(np.abs(ys[:, 0] - u_fd)):.3e} K everywhere,")
print("and they have no line of code in common past the definition of the equation.")
