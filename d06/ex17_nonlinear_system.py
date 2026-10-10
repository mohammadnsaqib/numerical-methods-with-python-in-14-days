"""Two equations, two unknowns, and neither is a straight line."""
import numpy as np

def F(v):
    x, y = v
    return np.array([x * x + y * y - 4.0,       # a circle of radius 2
                     np.exp(x) + y - 1.0])      # a curve crossing it twice

for guess in ([1.0, 1.0], [-1.0, -1.0], [0.0, 2.0]):
    print(f"F({guess}) = {np.array2string(F(np.array(guess)), precision=6)}")
print("\nnone of these is a root; the crossings have to be found.")
