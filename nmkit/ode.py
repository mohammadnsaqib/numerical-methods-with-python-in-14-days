"""Stepping an initial value problem forward in time. Days 13 and 14.

Every routine here answers the same question: given where the solution is now and a rule
for its slope, where is it one step later? They differ in how many slopes they consult
before committing, and that count is what buys the order.

The vector form is the general one, so every routine works on a system without being
told it is one. Day 14 relies on that: a second-order equation becomes two first-order
ones, and nothing here has to change.
"""
import numpy as np


def _as_vec(y):
    return np.atleast_1d(np.asarray(y, dtype=float))


# --8<-- euler
def euler(f, t0, y0, h, n):
    """Take the slope at the start of the step and follow it for the whole step.

    This is the definition of the derivative used forward, and it is the crudest method
    that works. Its LOCAL error is proportional to h squared, and there are n steps, so
    the error at the end goes like h -- the same power lost that Day 12's composite
    rules lost.
    """
    y = _as_vec(y0)
    ts, ys = [float(t0)], [y.copy()]
    t = float(t0)
    for _ in range(n):
        y = y + h * _as_vec(f(t, y))
        t += h
        ts.append(t)
        ys.append(y.copy())
    return np.array(ts), np.squeeze(np.array(ys))
# --8<--


# --8<-- heun
def heun(f, t0, y0, h, n):
    """Take the slope at the start, look where it leads, and average the two slopes.

    The second evaluation is spent on a trial step that is then thrown away. What
    survives is the average, which is the trapezoidal rule applied to the derivative --
    so the method is second order for the same reason that rule is.
    """
    y = _as_vec(y0)
    ts, ys = [float(t0)], [y.copy()]
    t = float(t0)
    for _ in range(n):
        k1 = _as_vec(f(t, y))
        k2 = _as_vec(f(t + h, y + h * k1))
        y = y + h * (k1 + k2) / 2.0
        t += h
        ts.append(t)
        ys.append(y.copy())
    return np.array(ts), np.squeeze(np.array(ys))
# --8<--


# --8<-- midpoint_ode
def midpoint_ode(f, t0, y0, h, n):
    """Use the trial step to reach the MIDDLE of the interval, and take the slope there.

    It costs the same two evaluations as Heun's method and has the same order. The two
    differ in which second-order method they are, not in how good they are, and Example
    13.13 measures a case where each is the better of the pair.
    """
    y = _as_vec(y0)
    ts, ys = [float(t0)], [y.copy()]
    t = float(t0)
    for _ in range(n):
        k1 = _as_vec(f(t, y))
        k2 = _as_vec(f(t + h / 2.0, y + h / 2.0 * k1))
        y = y + h * k2
        t += h
        ts.append(t)
        ys.append(y.copy())
    return np.array(ts), np.squeeze(np.array(ys))
# --8<--


# --8<-- rk4
def rk4(f, t0, y0, h, n):
    """Four slopes per step, weighted 1, 2, 2, 1, giving fourth order.

    The weights are Simpson's rule's, and that is not a coincidence: for an equation
    whose right side does not depend on y at all, this method IS composite Simpson.
    Example 13.16 checks that by running both on such an equation and subtracting.
    """
    y = _as_vec(y0)
    ts, ys = [float(t0)], [y.copy()]
    t = float(t0)
    for _ in range(n):
        k1 = _as_vec(f(t, y))
        k2 = _as_vec(f(t + h / 2.0, y + h / 2.0 * k1))
        k3 = _as_vec(f(t + h / 2.0, y + h / 2.0 * k2))
        k4 = _as_vec(f(t + h, y + h * k3))
        y = y + h * (k1 + 2.0 * k2 + 2.0 * k3 + k4) / 6.0
        t += h
        ts.append(t)
        ys.append(y.copy())
    return np.array(ts), np.squeeze(np.array(ys))
# --8<--


# --8<-- rk45_step
def rk45_step(f, t, y, h):
    """One step by two methods at once, returning both answers and their difference.

    The Runge-Kutta-Fehlberg tableau is built so that six slopes serve a fourth-order
    method and a fifth-order one together. The difference between the two estimates is
    what the step size controller reads, and it costs nothing beyond the six evaluations
    already made.
    """
    y = _as_vec(y)
    k1 = h * _as_vec(f(t, y))
    k2 = h * _as_vec(f(t + h / 4, y + k1 / 4))
    k3 = h * _as_vec(f(t + 3 * h / 8, y + 3 * k1 / 32 + 9 * k2 / 32))
    k4 = h * _as_vec(f(t + 12 * h / 13,
                       y + 1932 * k1 / 2197 - 7200 * k2 / 2197 + 7296 * k3 / 2197))
    k5 = h * _as_vec(f(t + h,
                     y + 439 * k1 / 216 - 8 * k2 + 3680 * k3 / 513 - 845 * k4 / 4104))
    k6 = h * _as_vec(f(t + h / 2, y - 8 * k1 / 27 + 2 * k2 - 3544 * k3 / 2565
                       + 1859 * k4 / 4104 - 11 * k5 / 40))
    y4 = y + 25 * k1 / 216 + 1408 * k3 / 2565 + 2197 * k4 / 4104 - k5 / 5
    y5 = (y + 16 * k1 / 135 + 6656 * k3 / 12825 + 28561 * k4 / 56430
          - 9 * k5 / 50 + 2 * k6 / 55)
    return y4, y5, float(np.max(np.abs(y5 - y4)))
# --8<--


# --8<-- adaptive_rk
def adaptive_rk(f, t0, y0, t_end, tol=1e-8, h0=None, hmin=1e-12, max_steps=100000):
    """Choose every step from the error the last one made.

    A rejected step is not wasted work to be hidden: it is the mechanism. The controller
    shrinks h and tries again, and the count of rejections is returned so a reader can
    see what the tolerance cost. The exponent 0.2 is one over the order of the lower
    method plus one.
    """
    y = _as_vec(y0)
    t = float(t0)
    h = (t_end - t0) / 100.0 if h0 is None else float(h0)
    ts, ys = [t], [y.copy()]
    accepted, rejected = 0, 0
    for _ in range(max_steps):
        if t >= t_end - 1e-14:
            break
        h = min(h, t_end - t)
        y4, y5, err = rk45_step(f, t, y, h)
        if err <= tol or h <= hmin:
            t += h
            y = y5
            ts.append(t)
            ys.append(y.copy())
            accepted += 1
        else:
            rejected += 1
        factor = 0.9 * (tol / err) ** 0.2 if err > 0 else 5.0
        h = h * min(5.0, max(0.1, factor))
    return np.array(ts), np.squeeze(np.array(ys)), accepted, rejected
# --8<--


# --8<-- stability_region
def stability_region(method, z):
    """The factor by which one step multiplies the solution of y' = lambda y, with z = h
    lambda.

    A method is absolutely stable at this z when the factor's size is at most one. That
    is a statement about the METHOD and the STEP, not about accuracy: an unstable step
    does not give a poor answer, it gives one that grows without bound while the true
    solution decays.
    """
    z = np.asarray(z, dtype=complex)
    if method == "euler":
        return np.abs(1.0 + z)
    if method in ("heun", "midpoint"):
        return np.abs(1.0 + z + z ** 2 / 2.0)
    if method == "rk4":
        return np.abs(1.0 + z + z ** 2 / 2.0 + z ** 3 / 6.0 + z ** 4 / 24.0)
    if method == "implicit_euler":
        return np.abs(1.0 / (1.0 - z))
    if method == "trapezoid":
        return np.abs((1.0 + z / 2.0) / (1.0 - z / 2.0))
    raise ValueError(f"unknown method: {method}")
# --8<--


# --8<-- euler_implicit
def euler_implicit(f, t0, y0, h, n, jac=None, tol=1e-12, maxit=50):
    """Take the slope at the END of the step, which means solving for where the end is.

    The unknown appears on both sides, so every step is a root-finding problem -- Day
    6's Newton for systems, called n times. That is the price. What it buys is a growth
    factor of 1/(1 - z), whose size is below one for EVERY negative z, so no step is
    ever too long for stability. Day 14 needs exactly that.
    """
    from .nlsys import jacobian_fd

    y = _as_vec(y0)
    ts, ys = [float(t0)], [y.copy()]
    t = float(t0)
    for _ in range(n):
        t_next = t + h
        guess = y + h * _as_vec(f(t, y))
        for _ in range(maxit):
            g = guess - y - h * _as_vec(f(t_next, guess))
            if np.max(np.abs(g)) < tol:
                break
            J = np.eye(guess.size) - h * (jac(t_next, guess) if jac is not None
                                          else jacobian_fd(lambda v: _as_vec(f(t_next,
                                          v)),
                                                           guess))
            guess = guess + np.linalg.solve(J, -g)
        y = guess
        t = t_next
        ts.append(t)
        ys.append(y.copy())
    return np.array(ts), np.squeeze(np.array(ys))
# --8<--


# --8<-- trapezoid_ode
def trapezoid_ode(f, t0, y0, h, n, tol=1e-12, maxit=50):
    """Average the slope at both ends, which is implicit and second order at once.

    Its growth factor is (1 + z/2)/(1 - z/2), whose size is below one for every negative
    z, so it is stable at any step like the implicit Euler method. Unlike that method it
    does not damp: at a very long step the factor approaches one in size rather than
    zero, so a stiff component is neither grown nor removed but left oscillating.
    Example 14.14 measures it.
    """
    from .nlsys import jacobian_fd

    y = _as_vec(y0)
    ts, ys = [float(t0)], [y.copy()]
    t = float(t0)
    for _ in range(n):
        t_next = t + h
        f_now = _as_vec(f(t, y))
        guess = y + h * f_now
        for _ in range(maxit):
            g = guess - y - h * (f_now + _as_vec(f(t_next, guess))) / 2.0
            if np.max(np.abs(g)) < tol:
                break
            J = np.eye(guess.size) - h / 2.0 * jacobian_fd(
                lambda v: _as_vec(f(t_next, v)), guess)
            guess = guess + np.linalg.solve(J, -g)
        y = guess
        t = t_next
        ts.append(t)
        ys.append(y.copy())
    return np.array(ts), np.squeeze(np.array(ys))
# --8<--


# --8<-- to_system
def to_system(coeffs_rhs, order):
    """Turn one equation of order n into n equations of order one.

    The trick is to name the derivatives: y[0] is the function, y[1] its first
    derivative, and so on. Then each of the first n-1 equations just says that the next
    entry IS the derivative of this one, and only the last row carries the original
    equation. Nothing else in this module has to know it happened.
    """
    def rhs(t, y):
        out = np.zeros(order)
        out[:-1] = y[1:]
        out[-1] = coeffs_rhs(t, y)
        return out
    return rhs
# --8<--
