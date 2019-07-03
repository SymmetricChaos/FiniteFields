from TropicalSemiring import Tropical
from TropicalPolynomial import TropicalPoly
import numpy as np
import matplotlib.pyplot as plt

a = Tropical(5)
b = Tropical(8)

print("Tropical addition is the minimum operation")
print(f"{a} + {b} = {a+b}")

print("\nTropical multiplication is the same as ordinary addition")
print(f"{a} * {b} = {a*b}")

print("\nRaising a tropical number to a non-negative integer power is the same as ordinary multiplication.")
print(f"{a}^{b} = {a**b}")

print("\nThis is sufficient to define tropical polynomials.")

a = Tropical(4)
b = Tropical(1)
c = Tropical(2)
P = TropicalPoly([a,b,c])
print("\nTropical Polynomial")
print(P)

x = list(np.linspace(-2,6,51))
y = P.evaluate(x)

plt.plot(x,y)
plt.title("Graph of the Polynomial")