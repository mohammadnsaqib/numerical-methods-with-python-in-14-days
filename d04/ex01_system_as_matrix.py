"""Three equations become one matrix and one vector, and nothing about the problem
changes."""
import numpy as np

# 2x + y -  z =   8
# -3x - y + 2z = -11
# -2x + y + 2z =  -3
A = np.array([[2.0, 1.0, -1.0],
              [-3.0, -1.0, 2.0],
              [-2.0, 1.0, 2.0]])
b = np.array([8.0, -11.0, -3.0])

print("A =\n", A)
print("b =", b)
print("shape of A:", A.shape, " length of b:", b.size)
print("the unknown x has length", A.shape[1])
