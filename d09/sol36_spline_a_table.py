"""Problem 9.36: a spline through measured data, checked at the points it was given."""
import numpy as np

from nmkit.spline import cubic_spline, spline_eval

# Density of water in kg per cubic metre, at five temperatures in Celsius.
temps = np.array([0.0, 20.0, 40.0, 60.0, 80.0])
dens = np.array([999.84, 998.21, 992.22, 983.20, 971.80])

m = cubic_spline(temps, dens)
print("reproduces the table:",
      bool(np.max(np.abs(spline_eval(temps, dens, m, temps) - dens)) < 1e-10))
print(f"{'temperature':>12} {'density':>12}")
for t in (10.0, 30.0, 50.0, 70.0):
    print(f"{t:>12.1f} {spline_eval(temps, dens, m, t):>12.4f}")
print("\nthe density falls throughout, and so does the spline:",
      bool(np.all(np.diff(spline_eval(temps, dens, m, np.linspace(0, 80, 400))) < 0)))
