"""A real problem: the position of a body on an elliptical orbit is defined by a root.
"""
import math

from nmkit.roots import bisect, steps_needed

e = 0.6                          # eccentricity of the orbit
M = 0.7                          # mean anomaly, in radians

def kepler(E):
    """Kepler's equation, written so its root E is the eccentric anomaly."""
    return E - e * math.sin(E) - M

print("predicted steps:", steps_needed(0.0, math.pi, 1e-13))
r = bisect(kepler, 0.0, math.pi, tol=1e-13)
print("eccentric anomaly E:", f"{r.root:.13f}", "in", r.iterations, "steps")
print("residual E - e sin E - M:", f"{kepler(r.root):+.3e}")
true_anomaly = 2 * math.atan2(math.sqrt(1 + e) * math.sin(r.root / 2),
                              math.sqrt(1 - e) * math.cos(r.root / 2))
print("true anomaly, radians:", f"{true_anomaly:.13f}")
