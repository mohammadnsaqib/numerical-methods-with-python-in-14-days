"""The condition number predicts the digits lost, and the prediction can be checked
against a real perturbation."""
import math

x = 1.0001
k = abs(x * 1.0 / (x - 1))                     # condition number of x - 1 at this x
perturbed = math.nextafter(x, math.inf)        # move the input by one ulp

rel_in = abs(perturbed - x) / abs(x)
rel_out = abs((perturbed - 1) - (x - 1)) / abs(x - 1)

print("condition number      :", f"{k:.4e}")
print("relative change in x  :", f"{rel_in:.4e}")
print("relative change in x-1:", f"{rel_out:.4e}")
print("observed amplification:", f"{rel_out / rel_in:.4e}")
print("digits lost, predicted:", f"{math.log10(k):.2f}")
