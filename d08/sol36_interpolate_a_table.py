"""Problem 8.36: read values between the entries of a table nobody has a formula for."""
import numpy as np

from nmkit.interp import divided_differences, newton_eval

# Saturated vapour pressure of water, in kilopascals, at five temperatures in Celsius.
temps = np.array([0.0, 20.0, 40.0, 60.0, 80.0])
press = np.array([0.6113, 2.3390, 7.3849, 19.9460, 47.4140])

c = divided_differences(temps, press)[0]
print("Newton coefficients:", np.array2string(c, precision=8))
print(f"{'temperature':>12} {'interpolated':>14}")
for t in (10.0, 30.0, 50.0, 70.0):
    print(f"{t:>12.1f} {newton_eval(temps, c, t):>14.6f}")
print("\nat the tabulated points the interpolant reproduces the table:")
print("  largest miss:",
      f"{np.max(np.abs(newton_eval(temps, c, temps) - press)):.3e}")
