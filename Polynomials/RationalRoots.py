# The rational root theorem makes it possible to determine all the rational
# roots of a polynomial.

from Polynomials import Polynomial
from Rationals import Rational
from Computation import factorization

def rational_roots(P):
    assert type(P) == Polynomial
    
    # Factor the leading and trailing coefficients
    # We will include positive and negative factors for the numerator
    n = factorization(abs(P[0]))
    n = n + [-i for i in n]
    d = factorization(abs(P[-1]))

    R = []

    # Test each of the possible roots
    for i in n:
        for j in d:
            q = Rational(i,j)
            r = P.evaluate(q)
            if r == Rational(0,1):
                R.append(q)
    
    return list(set(R))