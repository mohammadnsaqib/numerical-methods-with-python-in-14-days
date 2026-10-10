"""Absolute error and relative error rank the same two results in opposite orders."""
from nmkit.err import abs_err, rel_err

cases = [("small", 0.000123, 0.000122), ("large", 1234567.0, 1234000.0)]
for name, true, approx in cases:
    print(f"{name:>6}  true = {true:<12g} approx = {approx:<12g}"
          f"  abs = {abs_err(approx, true):.4e}  rel = {rel_err(approx, true):.4e}")

print()
print("the large case has the bigger absolute error and the smaller relative error.")
