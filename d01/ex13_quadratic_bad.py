"""The textbook quadratic formula loses every significant digit when b dominates."""
import math

a, b, c = 1.0, 1e8, 1.0
disc = math.sqrt(b * b - 4 * a * c)
r1 = (-b + disc) / (2 * a)
r2 = (-b - disc) / (2 * a)

print("a, b, c   :", a, b, c)
print("sqrt(disc):", f"{disc:.17g}")
print("-b        :", f"{-b:.17g}")
print("root 1    :", f"{r1:.17g}")
print("root 2    :", f"{r2:.17g}")
print("product of roots should be c/a =", c / a, "but is", f"{r1 * r2:.17g}")
