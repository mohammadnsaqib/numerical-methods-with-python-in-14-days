"""Below one the error dies away; above one it grows from any start, however good."""
import numpy as np

from nmkit.iterative import jacobi

# b is chosen so the answer is NOT the starting guess: an iteration handed its own
# answer reports one sweep and a step of zero, which measures nothing at all.
for name, A in (("radius 0.25", np.array([[4.0, -1.0], [-1.0, 4.0]])),
                ("radius 2.00", np.array([[1.0, 2.0], [2.0, 1.0]]))):
    b = np.array([1.0, -2.0])
    _, k, hist = jacobi(A, b, x0=np.array([0.5, 0.5]), tol=1e-12, max_iter=40)
    print(f"{name}: stopped after {k} sweeps, last step {hist[-1]:.3e}")
    print(f"{'':13}  steps 1 to 6: {[f'{h:.2e}' for h in hist[:6]]}")
