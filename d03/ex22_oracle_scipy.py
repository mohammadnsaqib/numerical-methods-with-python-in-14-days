"""Two independent implementations of the same two methods, agreeing to the last digits.
"""
import math

from scipy.optimize import newton as sp_newton

from nmkit.roots import newton, secant

f = lambda x: math.cos(x) - x
df = lambda x: -math.sin(x) - 1

mine_n = newton(f, df, 1.0, tol=1e-15).root
mine_s = secant(f, 0.0, 1.0, tol=1e-15).root
theirs_n = sp_newton(f, 1.0, fprime=df, tol=1e-15)
theirs_s = sp_newton(f, 1.0, x1=0.0, tol=1e-15)

print("nmkit newton :", f"{mine_n:.16f}")
print("scipy newton :", f"{theirs_n:.16f}")
print("nmkit secant :", f"{mine_s:.16f}")
print("scipy secant :", f"{theirs_s:.16f}")
print("largest gap  :", f"{max(abs(mine_n - theirs_n), abs(mine_s - theirs_s)):.3e}")
