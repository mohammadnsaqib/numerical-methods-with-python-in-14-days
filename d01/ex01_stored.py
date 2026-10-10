"""The number that is stored is not the number that was typed."""
from fractions import Fraction

typed = 0.1
print("typed        :", typed)
print("printed with 20 digits:", f"{typed:.20f}")
print("stored exactly:", Fraction(typed))
print("is it 1/10 ?  :", Fraction(typed) == Fraction(1, 10))
print("0.1 + 0.2     :", f"{0.1 + 0.2:.20f}")
print("equals 0.3 ?  :", 0.1 + 0.2 == 0.3)
