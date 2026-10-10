"""Q changes no length, so the part of the residual it cannot touch is the answer's own
error."""
import numpy as np

from nmkit.factor import householder_qr
from nmkit.lstsq import lstsq_qr, residual

rng = np.random.default_rng(233)
A = rng.normal(size=(12, 4))
b = rng.normal(size=12)
Q, R = householder_qr(A)
qtb = Q.T @ b

x = lstsq_qr(A, b)
r = residual(A, x, b)
print("length of b           :", f"{np.sqrt(b @ b):.10f}")
print("length of Q.T @ b     :", f"{np.sqrt(qtb @ qtb):.10f}")
print("last 8 entries of Q.T b, in length:", f"{np.sqrt(qtb[4:] @ qtb[4:]):.10f}")
print("length of the residual:", f"{np.sqrt(r @ r):.10f}")
