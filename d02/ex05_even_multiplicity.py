"""The guarantee runs one way only: no sign change does not mean no root."""
from nmkit.roots import bracket_scan

def touch(x):
    return (x - 1.0) ** 2

def cross(x):
    return (x - 1.0) ** 3

# 25 steps, so the scan lands on 0.96 and 1.04 and never on the root itself. A scan that
# steps exactly onto a root reports it as a degenerate bracket, which is correct and
# would hide the difference this example exists to show.
print("(x-1)**2 on [0, 2]:", bracket_scan(touch, 0.0, 2.0, n=25))
print("(x-1)**3 on [0, 2]:", bracket_scan(cross, 0.0, 2.0, n=25))
print()
print("both have a root at x = 1. Only the odd power changes sign there.")
