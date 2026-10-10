"""A relative error of ten to the minus k is k correct digits, and the count can be
printed."""
from nmkit.err import rel_err, sig_digits

true = 3.141592653589793
for approx in (3.0, 3.1, 3.14, 3.1416, 3.14159265):
    print(f"approx = {approx:<12} rel err = {rel_err(approx, true):.3e}"
          f"   correct digits = {sig_digits(approx, true):.2f}")
