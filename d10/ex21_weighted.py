"""A measurement known ten times as precisely should count for a hundred times as much.
"""
import numpy as np

from nmkit.lstsq import design_matrix, lstsq_qr, weighted

xs = np.array([0.0, 1.0, 2.0, 3.0, 4.0])
ys = np.array([1.0, 2.1, 2.9, 4.2, 12.0])            # the last is badly measured
sigma = np.array([0.1, 0.1, 0.1, 0.1, 5.0])          # and known to be

A = design_matrix(xs, 1)
plain = lstsq_qr(A, ys)
wtd = weighted(A, ys, 1.0 / sigma ** 2)
print("unweighted:", np.array2string(plain, precision=6))
print("weighted  :", np.array2string(wtd, precision=6))
print("the first four points alone:",
      np.array2string(lstsq_qr(design_matrix(xs[:4], 1), ys[:4]), precision=6))
