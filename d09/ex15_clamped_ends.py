"""Clamped ends use the true slopes instead, when they are known."""
import numpy as np

from nmkit.spline import cubic_spline, spline_eval

xs = np.linspace(0.0, 3.0, 7)
ys = np.sin(xs)
t = np.linspace(0.0, 3.0, 800)

nat = cubic_spline(xs, ys, bc="natural")
cla = cubic_spline(xs, ys, bc="clamped", slopes=(np.cos(0.0), np.cos(3.0)))
e_nat = np.max(np.abs(np.sin(t) - spline_eval(xs, ys, nat, t)))
e_cla = np.max(np.abs(np.sin(t) - spline_eval(xs, ys, cla, t)))
print("natural ends:", f"{e_nat:.4e}")
print("clamped ends:", f"{e_cla:.4e}")
print("ratio       :", f"{e_nat / e_cla:.2f}")
