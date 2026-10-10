"""The 2-norm and the condition number of Day 5 were singular values all along."""
import numpy as np

from nmkit.norms import cond, hilbert, mnorm

for name, A in (("random 5 by 5", np.random.default_rng(127).normal(size=(5, 5))),
                ("Hilbert 6    ", hilbert(6))):
    s = np.linalg.svd(A, compute_uv=False)
    print(f"{name}: largest singular value {s[0]:.10e}   2-norm {mnorm(A, 2):.10e}")
    print(f"{'':15} largest over smallest {s[0] / s[-1]:.6e}   cond {cond(A, 2):.6e}")
