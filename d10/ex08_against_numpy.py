"""The routine is checked against an independently written least squares solver."""
import numpy as np

from nmkit.lstsq import design_matrix, lstsq_qr

rng = np.random.default_rng(227)
print(f"{'rows':>6} {'columns':>9} {'largest gap':>14}")
for m, n in ((20, 3), (50, 5), (100, 8), (200, 4)):
    A = rng.normal(size=(m, n))
    b = rng.normal(size=m)
    mine = lstsq_qr(A, b)
    theirs = np.linalg.lstsq(A, b, rcond=None)[0]
    print(f"{m:>6} {n:>9} {np.max(np.abs(mine - theirs)):>14.3e}")
