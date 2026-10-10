"""One reflection sends a whole column onto a single axis, zeroing everything below at
once."""
import numpy as np

x = np.array([3.0, 4.0, 12.0])
alpha = -np.sign(x[0]) * np.sqrt(x @ x)
v = x.copy()
v[0] -= alpha
v = v / np.sqrt(v @ v)
reflected = x - 2.0 * v * (v @ x)

print("x            :", x, " length", f"{np.sqrt(x @ x):.6f}")
print("after one reflection:", np.array2string(reflected, precision=12))
print("its length   :", f"{np.sqrt(reflected @ reflected):.6f}")
print("a reflection changes no length, which is why it cannot magnify an error.")
