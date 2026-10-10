"""The capstone problem, stated once so all three programs solve the SAME thing.

A cooling fin of length L, joined to a hot body at one end and a cooler one at the
other. Its steady temperature obeys

    u'' = C1 (u - Ta) + C2 (u^4 - Ta^4)

where the first term is the heat carried away by the air and the second is the heat
radiated. The radiating term is what makes the problem nonlinear, and it is not
negligible: Example 14.20 measures its share.
"""
import numpy as np

L = 0.1
TA = 300.0
C1 = 100.0
C2 = 1e-7
U0 = 500.0
UL = 400.0


def loss(u):
    """The right-hand side: how fast the temperature gradient must change at temperature
    u."""
    return C1 * (u - TA) + C2 * (u ** 4 - TA ** 4)


def rhs_system(x, y):
    """The same equation as two first-order ones, for Day 13's steppers."""
    return np.array([y[1], loss(y[0])])


def loss_slope(u):
    """The derivative of `loss` with respect to u, which the Jacobian needs."""
    return C1 + 4.0 * C2 * u ** 3
