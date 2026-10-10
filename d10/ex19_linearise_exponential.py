"""Taking logarithms turns a curve that is not linear in its parameters into one that
is."""
import numpy as np

from nmkit.lstsq import design_matrix, lstsq_qr

rng = np.random.default_rng(239)
xs = np.linspace(0.0, 3.0, 30)
ys = 2.5 * np.exp(0.8 * xs) * np.exp(rng.normal(scale=0.05, size=30))

c = lstsq_qr(design_matrix(xs, 1), np.log(ys))
print("fitting log(y) = log(a) + b x")
print("  a recovered:", f"{np.exp(c[0]):.6f}", " true 2.5")
print("  b recovered:", f"{c[1]:.6f}", " true 0.8")
