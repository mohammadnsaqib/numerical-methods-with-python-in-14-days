"""The factorisation is built one entry at a time, and each row uses only the rows above
it."""
import numpy as np

A = np.array([[4.0, 2.0, -2.0], [2.0, 10.0, 2.0], [-2.0, 2.0, 5.0]])
L = np.zeros((3, 3))

L[0, 0] = np.sqrt(A[0, 0])
print(f"L[0,0] = sqrt({A[0,0]}) = {L[0,0]}")
L[1, 0] = A[1, 0] / L[0, 0]
L[2, 0] = A[2, 0] / L[0, 0]
print(f"L[1,0] = {A[1,0]} / {L[0,0]} = {L[1,0]}    L[2,0] = {L[2,0]}")
L[1, 1] = np.sqrt(A[1, 1] - L[1, 0] ** 2)
print(f"L[1,1] = sqrt({A[1,1]} - {L[1,0]}**2) = {L[1,1]}")
L[2, 1] = (A[2, 1] - L[2, 0] * L[1, 0]) / L[1, 1]
L[2, 2] = np.sqrt(A[2, 2] - L[2, 0] ** 2 - L[2, 1] ** 2)
print(f"L[2,1] = {L[2,1]}    L[2,2] = {L[2,2]}")
print("\nL @ L.T:\n", np.array2string(L @ L.T, precision=10))
