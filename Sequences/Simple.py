from Sequences.NiceErrorChecking import require_integers, require_nonnegative
from itertools import count, repeat
from math import gcd

def constant(n):
    """
    Constant Sequences: Returns n forever
    OEIS A000004, A000012, A007395, A010701
    """
    
    require_integers(["n"],[n])
    
    for i in repeat(n):
        yield i


def integers():
    """
    Integers: All integers starting with zero then with positive before negative\n
    OEIS A001057
    """
    
    yield 0
    
    for n in counting():
        yield n
        yield -n


def arithmetic(a,n):
    """
    Arithmetic Sequences: Integers with constant difference
    
    Args:
        a -- starting value
        n -- common difference
    """
    
    require_integers(["a","n"],[a,n])
    
    for i in count(a,n):
        yield i


def geometric(a,n):
    """
    Geometric Sequences: Integers with constant ratio
    
    Args:
        a -- starting values
        n -- common ratio
    """
    
    require_integers(["a","n"],[a,n])
        
    out = a
    
    while True:
        yield out
        
        out *= n


def arithmetrico_geometric(a,n,b,m):
    """
    Arithmetrico-Geometric Sequences: Product of an arithmetic sequence with a geometric sequence
    
    Args:
        a -- starting value for arithmetic sequence
        n -- common difference for arithmetic sequence
        b -- starting value for geometric sequence
        m -- common ratio for geometric sequence
    """
    
    require_integers(["a","n","b","m"],[a,n,b,m])
    
    for ari,geo in zip(arithmetic(a,n),geometric(b,m)):
        yield ari*geo


def polynomial(coef):
    """
    Polynomial Functions: Integer polynomial evaluated at each non-negative integer
    
    Args:
        coef -- coefficients of the polynomial is ascending order, all integers
    """
    
    for c in coef:
        if type(c) != int:
            raise TypeError("All coefficients must be integers")
    
    for n in naturals():
        out = 0
        
        for e,c in enumerate(coef):
            out += c*n**e
        
        yield out


def gen_polynomial(coef):
    """
    Polynomial Functions: Integer polynomial evaluated at each integer
    
    Args:
        coef -- coefficients of the polynomial is ascending order, all integers
    """
    
    for c in coef:
        if type(c) != int:
            raise TypeError("All coefficients must be integers")
    
    for i in integers():
        out = 0
        
        for e,c in enumerate(coef):
            out += c*i**e
        
        yield out


def fermat():
    """
    Fermat Numbers: 2^2^n+1 for n in naturals\n
    OEIS A000215
    """
    
    for n in naturals():
        yield 2**2**n+1


def harmonic_numerators():
    """
    Numerators of the harmonic series
    OEIS A001008
    """
    
    n0, d0 = 1,1
    
    for i in naturals(2):
        yield n0
        
        n = n0*i+ 1*d0
        d = d0*i
        g = gcd(n,d)
        
        n,d = n//g,d//g
        n0, d0 = n,d


def harmonic_denominators():
    """
    Denominators of the harmonic series
    OEIS A002805
    """
    
    n0, d0 = 1,1
    
    for i in naturals(2):
        yield d0
        
        n = n0*i+ 1*d0
        d = d0*i
        g = gcd(n,d)
        
        n,d = n//g,d//g
        n0, d0 = n,d


def gen_harmonic_numerators(m):
    """
    Numerators of the generalized harmonic series of order m
    
    Args:
        m -- exponent for the numerators of the terms
    """
    
    require_integers(["m"],[m])
    require_nonnegative(["m"],[m])
    
    if m == 0:
        for i in naturals(1):
            yield i
    
    n0, d0 = 1,1
    
    for i in naturals(2):
        yield n0
        
        n = n0*i+ 1*d0
        d = d0*(i**m)
        g = gcd(n,d)
        
        n,d = n//g,d//g
        n0, d0 = n,d


def gen_harmonic_denominators(m):
    """
    Denominators of the generalized harmonic series of order m
    
    Args:
        m -- exponent for the numerators of the terms
    """
    
    require_integers(["m"],[m])
    require_nonnegative(["m"],[m])
    
    if m == 0:
        for i in naturals(1):
            yield i
    
    n0, d0 = 1,1
    
    for i in naturals(2):
        yield d0
        
        n = n0*i+ 1*d0
        d = d0*(i**m)
        g = gcd(n,d)
        
        n,d = n//g,d//g
        n0, d0 = n,d





### Wrappers for common cases ###
def naturals(offset=0):
    """
    Natural Numbers: Nonnegative whole numbers, special case of arithmetic
    
     Args:
        offset -- nonnegative integer how many naturals to skip before starting
        
    OEIS A001477 (with default offset)
    """
    
    require_integers(["offset"],[offset])
    require_nonnegative(["offset"],[offset])
    
    for i in count(offset,1):
        yield i


def counting(offset=0):
    """
    Counting Numbers: Positive whole numbers, special case of arithmetic
    
    Args:
        offset -- nonnegative integer how many counting numbers to skip before starting
        
    OEIS A000027 (with default offset)
    """
    
    require_integers(["offset"],[offset])
    require_nonnegative(["offset"],[offset])
    
    for i in count(offset+1,1):
        yield i


def powers(n):
    """
    Powers of n: Special case of geometric
    
    Args:
        n -- constant multiple
        
    OEIS A000079, A000244, A000302, A000351, A000400, A000420, A001018-A001027, 
         A001029, A009964-A009992, A011557, A159991, A165800
    """
    
    require_integers(["n"],[n])
    require_nonnegative(["n"],[n])
    
    for g in geometric(1,n):
        yield g


def nth_powers(e):
    """
    Each non-negative integer raised to the power of n
    
    Args:
        e -- exponent
        
    OEIS 
    """
    
    require_integers(["e"],[e])
    require_nonnegative(["e"],[e])
    
    for n in naturals():
        yield n**e


def evens():
    """
    Even Numbers: Non-negative integers divisible by 2, special case of arithmetic\n
    OEIS A005843
    """
    
    for i in arithmetic(0,2):
        yield i


def gen_evens():
    """
    Even Numbers: Integers divisible by 2, special case of arithmetic\n
    OEIS A137501 (differs by including zero only once)
    """
    
    yield 0
    
    for i in arithmetic(2,2):
        yield i
        yield -i


def odds():
    """
    Odd Numbers: Non-negative integers not divisible by 2, special case of arithmetic\n
    OEIS A005408
    """
    
    for i in arithmetic(1,2):
        yield i


def gen_odds():
    """
    Odd Numbers: Integers not divisible by 2, special case of arithmetic\n
    OEIS A296063
    """
    
    for i in arithmetic(1,2):
        yield i
        yield -i





if __name__ == '__main__':
    from Sequences.SequenceManipulation import simple_test
    
    print("Counting Numbers")
    simple_test(counting(),15,
                "1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15")
    
    print("\nNatural Numbers")
    simple_test(naturals(),15,
                "0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14")
    
    print("\nIntegers")
    simple_test(integers(),15,
                "0, 1, -1, 2, -2, 3, -3, 4, -4, 5, -5, 6, -6, 7, -7")
    
    print("\nEven Naturals")
    simple_test(evens(),14,
                "0, 2, 4, 6, 8, 10, 12, 14, 16, 18, 20, 22, 24, 26")
    
    print("\nEven Integers")
    simple_test(gen_evens(),14,
                "0, 2, -2, 4, -4, 6, -6, 8, -8, 10, -10, 12, -12, 14")
    
    print("\nOdd Naturals")
    simple_test(odds(),14,
                "1, 3, 5, 7, 9, 11, 13, 15, 17, 19, 21, 23, 25, 27")
    
    print("\nOdd Integers")
    simple_test(gen_odds(),14,
                "1, -1, 3, -3, 5, -5, 7, -7, 9, -9, 11, -11, 13, -13")
    
    print("\nPolynomial 2x^2 - 10x + 1 Evaluated at Naturals")
    simple_test(polynomial([1,-10,2]),9,
                "1, -7, -11, -11, -7, 1, 13, 29, 49")
    
    print("\nPolynomial 2x^2 - 10x + 1 Evaluated at Integers")
    simple_test(gen_polynomial([1,-10,2]),9,
                "1, -7, 13, -11, 29, -11, 49, -7, 73")
    
    print("\nArithmetic Sequence 5+2n")
    simple_test(arithmetic(5,2),10,
                "5, 7, 9, 11, 13, 15, 17, 19, 21, 23")
    
    print("\nGeometric Sequence 5*2^n")
    simple_test(geometric(5,2),10,
                "5, 10, 20, 40, 80, 160, 320, 640, 1280, 2560")
    
    print("\nArithmetrico-Geometric Sequence (1+2n)(3*4^n)")
    simple_test(arithmetrico_geometric(1,2,3,4),9,
                "3, 36, 240, 1344, 6912, 33792, 159744, 737280, 3342336")
    
    print("\nPowers of 3")
    simple_test(powers(3),11,
                "1, 3, 9, 27, 81, 243, 729, 2187, 6561, 19683, 59049")
    
    print("\nFermat Numbers")
    simple_test(fermat(),7,
                "3, 5, 17, 257, 65537, 4294967297, 18446744073709551617")
    
    print("\nHarmonic Numerators")
    simple_test(harmonic_numerators(),11,
                "1, 3, 11, 25, 137, 49, 363, 761, 7129, 7381, 83711")
    
    print("\nHarmonic Denominators")
    simple_test(harmonic_denominators(),11,
                "1, 2, 6, 12, 60, 20, 140, 280, 2520, 2520, 27720")
    
    print("\nGeneralized Harmonic Numerators of Order 2")
    simple_test(gen_harmonic_numerators(2),8,
                "1, 3, 13, 11, 127, 427, 13789, 79939")
    
    print("\nGeneralized Harmonic Denominators of Order 2")
    simple_test(gen_harmonic_denominators(2),8,
                "1, 4, 36, 72, 1800, 10800, 529200, 4233600")
    
    print("\nThe Zero Sequence")
    simple_test(constant(0), 18,
                "0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0")