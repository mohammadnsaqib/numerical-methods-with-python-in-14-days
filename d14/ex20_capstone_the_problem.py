"""The capstone problem, and the term that makes it nonlinear."""
import numpy as np

from d14._fin import C1, C2, L, TA, U0, UL, loss

print(f"a fin of length {L} m, held at {U0:.0f} K at one end and {UL:.0f} K at the "
      f"other")
print(f"the air is at {TA:.0f} K")
print(f"u'' = {C1:.0f} (u - {TA:.0f}) + {C2:.0e} (u^4 - {TA:.0f}^4)")
print()
print(f"{'u':>7} {'carried by air':>16} {'radiated':>12} {'radiated share':>16}")
for u in (300.0, 350.0, 400.0, 450.0, 500.0):
    air = C1 * (u - TA)
    rad = C2 * (u ** 4 - TA ** 4)
    share = 0.0 if air + rad == 0 else rad / (air + rad) * 100
    print(f"{u:>7.0f} {air:>16.2f} {rad:>12.2f} {share:>15.1f}%")
print()
print(f"at {U0:.0f} K radiation carries "
      f"{C2 * (U0 ** 4 - TA ** 4) / loss(U0) * 100:.1f} percent of the loss.")
print("dropping it would be a different problem, not a simpler version of this one.")
