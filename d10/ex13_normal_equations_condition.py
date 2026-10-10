"""Forming A transposed A squares the condition number, which is the whole objection to
it."""
import numpy as np

from nmkit.lstsq import design_matrix
from nmkit.norms import cond

print(f"{'degree':>7} {'cond of A':>14} {'cond of A.T A':>16} {'squared?':>11}")
xs = np.linspace(0.0, 1.0, 40)
for d in (2, 4, 6, 8, 10):
    A = design_matrix(xs, d)
    kA, kN = cond(A, 2), cond(A.T @ A, 2)
    print(f"{d:>7} {kA:>14.4e} {kN:>16.4e} {kN / kA ** 2:>11.4f}")
