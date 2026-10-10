"""The two routes agree to every digit, and then they separate."""
import numpy as np

from nmkit.lstsq import design_matrix, lstsq_qr, normal_equations, polyval

rng = np.random.default_rng(229)
xs = np.linspace(0.0, 1.0, 40)
ys = np.exp(xs) + rng.normal(scale=1e-10, size=40)

print(f"{'degree':>7} {'normal equations':>19} {'QR':>13}")
for d in (2, 4, 6, 8, 10, 12):
    A = design_matrix(xs, d)
    try:
        cn = normal_equations(A, ys)
        en = np.max(np.abs(polyval(cn, xs) - ys))
    except Exception:
        en = float("nan")
    cq = lstsq_qr(A, ys)
    eq = np.max(np.abs(polyval(cq, xs) - ys))
    print(f"{d:>7} {en:>19.4e} {eq:>13.4e}")
