"""The backward difference, and the situation that forces it."""
import numpy as np

from nmkit.diff import backward_diff, forward_diff

# A table of measurements. There is no value after the last row, so no forward
# difference exists there, and no centred one either.
ts = np.linspace(0.0, 1.0, 11)
vs = np.exp(ts)

h = ts[1] - ts[0]
print(f"{'t':>6} {'forward':>12} {'backward':>12} {'exact':>12}")
for i, t in enumerate(ts):
    fwd = f"{(vs[i + 1] - vs[i]) / h:.6f}" if i + 1 < ts.size else "none"
    bwd = f"{(vs[i] - vs[i - 1]) / h:.6f}" if i > 0 else "none"
    print(f"{t:>6.1f} {fwd:>12} {bwd:>12} {np.exp(t):>12.6f}")
print()
print(f"at the last row only the backward difference exists: "
      f"{backward_diff(np.exp, 1.0, h):.6f}")
