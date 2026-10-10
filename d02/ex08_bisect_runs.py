"""The routine in nmkit does what the hand steps did, and reports what happened."""
import math

from nmkit.roots import bisect

r = bisect(math.cos, 0.0, 3.0, tol=1e-14)
print("root       :", f"{r.root:.15f}")
print("pi/2       :", f"{math.pi / 2:.15f}")
print("iterations :", r.iterations)
print("converged  :", r.converged)
print("absolute error against pi/2:", f"{abs(r.root - math.pi / 2):.3e}")
