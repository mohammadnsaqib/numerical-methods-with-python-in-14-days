"""Problem 10.39: a decay curve whose weights come from the counts themselves."""
import numpy as np

from nmkit.lstsq import design_matrix, lstsq_qr, weighted

rng = np.random.default_rng(20259)
half_life = 12.0
minutes = np.arange(0.0, 60.0, 5.0)
mean_counts = 8000.0 * 0.5 ** (minutes / half_life)
counts = rng.poisson(mean_counts).astype(float)

# A count of N carries an uncertainty of about the square root of N, so the logarithm of
# a count carries an uncertainty of about 1 / sqrt(N). The weight is one over the square
# of that: N.
A = design_matrix(minutes, 1)
logs = np.log(counts)

plain = lstsq_qr(A, logs)
w = weighted(A, logs, counts)
print(f"{'minutes':>9} {'counts':>9} {'log':>10} {'weight':>10}")
for t, n in zip(minutes[:4], counts[:4]):
    print(f"{t:>9.0f} {n:>9.0f} {np.log(n):>10.5f} {n:>10.0f}")
print(f"\nhalf life, weights ignored   {-np.log(2.0) / plain[1]:>9.4f} minutes")
print(f"half life, weights used      {-np.log(2.0) / w[1]:>9.4f} minutes")
print(f"the value used to make the data {half_life:>6.4f} minutes")
