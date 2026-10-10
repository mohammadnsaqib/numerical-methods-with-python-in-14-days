"""Truncation error is what is left when an infinite process is stopped, and it is not
round-off."""
import math

x = 1.0
term, total = 1.0, 1.0
print(f"{'terms':>6} {'partial sum':>20} {'truncation error':>20}")
for n in range(1, 9):
    term *= x / n
    total += term
    print(f"{n + 1:>6} {total:>20.15f} {abs(total - math.e):>20.3e}")

print("\nthe error falls by a growing factor and never reaches zero after finitely "
      "many terms.")
