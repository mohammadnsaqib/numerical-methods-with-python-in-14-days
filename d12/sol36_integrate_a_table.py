"""Problem 12.36: an integral from measurements, where the integrand cannot be called
again."""
import numpy as np

from nmkit.quad import simpson_n, trapezoid_n

# Power drawn by a machine, in kilowatts, read every quarter hour for four hours. The
# integral is the energy used, in kilowatt hours.
hours = np.arange(0.0, 4.01, 0.25)
kw = np.array([2.10, 2.35, 2.80, 3.60, 4.15, 4.30, 4.05, 3.55, 3.10, 2.95,
               3.40, 4.20, 4.85, 5.10, 4.60, 3.70, 2.90])
h = 0.25

trap = h * (kw[0] / 2 + kw[1:-1].sum() + kw[-1] / 2)
simp = h / 3 * (kw[0] + 4 * kw[1:-1:2].sum() + 2 * kw[2:-1:2].sum() + kw[-1])

print(f"readings              : {kw.size}")
print(f"panels                : {kw.size - 1}")
print(f"trapezoidal rule      : {trap:.6f} kilowatt hours")
print(f"composite Simpson     : {simp:.6f} kilowatt hours")
print(f"they differ by        : {abs(trap - simp):.6f}")
print()
print(f"the mean power was {trap / 4.0:.6f} kilowatts over the four hours")
print("no rule of higher order can be used: there are no values between the readings")
