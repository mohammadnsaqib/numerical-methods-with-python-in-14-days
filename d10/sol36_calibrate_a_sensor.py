"""Problem 10.36: a calibration line through measured data, with the fit checked three
ways."""
import numpy as np

from nmkit.lstsq import design_matrix, lstsq_qr, r_squared, residual

# A platinum thermometer, read at seven temperatures in Celsius. Resistance in ohms.
temps = np.array([0.0, 20.0, 40.0, 60.0, 80.0, 100.0, 120.0])
ohms = np.array([100.02, 107.82, 115.51, 123.28, 130.85, 138.55, 146.29])

A = design_matrix(temps, 1)
c = lstsq_qr(A, ohms)
r = residual(A, c, ohms)

print(f"resistance at zero    {c[0]:.4f} ohms")
print(f"change per degree     {c[1]:.6f} ohms")
print(f"r squared             {r_squared(ohms, A @ c):.8f}")
print(f"largest residual      {np.max(np.abs(r)):.5f} ohms")
print(f"residual against 1    {float(A[:, 0] @ r):+.3e}")
print(f"residual against T    {float(A[:, 1] @ r):+.3e}")
print(f"\nreading at 50 C       {c[0] + c[1] * 50.0:.4f} ohms")
