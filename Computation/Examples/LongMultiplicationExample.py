from Computation.LongMultiplication import long_multiplication
from random import randint    

for i in range(3):
    A = randint(0,20000)
    B = randint(0,A)
    print(f"{A:>7}")
    print(f"x{B:>6}\n")
    C = long_multiplication(A,B)
    if C != A*B:
        print("ERROR")
    print("\n\n")