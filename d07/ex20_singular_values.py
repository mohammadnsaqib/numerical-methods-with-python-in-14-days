"""Singular values exist for any matrix, square or not, and are never negative."""
import numpy as np

from nmkit.eigen import svd_from_eig

rng = np.random.default_rng(113)
for shape in ((4, 4), (6, 3), (3, 6)):
    A = rng.normal(size=shape)
    mine = svd_from_eig(A)[:min(shape)]
    theirs = np.linalg.svd(A, compute_uv=False)
    print(f"shape {shape}: {np.array2string(theirs, precision=6)}")
    print(f"{'':14} largest gap from mine {np.max(np.abs(mine - theirs)):.3e}")
