from Sequences.MathUtils import digits_to_int, int_to_digits, mod_inv
from Sequences.ModularArithmetic import weyl
from Sequences.NiceErrorChecking import require_integers, require_prime, require_true, require_geq
from Sequences.Manipulations import sequence_apply

from math import gcd, prod
from itertools import cycle

# Obviously these are all VERY inefficient

def _check_LFSR_args(vector,taps):
    
    if type(vector) != list:
        raise Exception("The vector must be a list")
    if type(taps) != list:
        raise Exception("The taps must be a list")
    
    for v in vector:
        if v not in (0,1):
            raise Exception("Vector must consist only of 1s and 0s")
    for t in taps:
        if t >= len(vector):
            raise Exception("Taps must be valid positions in the vector")


def lower_bits(x,b):
    """Return only the b lowest bits of x"""
    return x % (2**b)


def upper_bits(x,b):
    """Return only the b highest bits of x"""
    return (x >> b) % (2**b)


def LCG(x,a,c,m):
    """
    Linear Congruential Generator
    
    Args:
        x -- seed value
        a -- multiplicative constant
        c -- additive constant
        m -- modulus
    """
    
    require_integers(["x","a","c","m"],[x,a,c,m])
    
    while True:
        yield x
        x = ((a*x)+c)%m


def cLCG(X,A,C,M):
    """
    Combined Linear Congruential Generator
    
    Args:
        X -- list of seed values
        A -- list of multiplicative constants
        C -- list of additive constants
        M -- list of moduli
    """
    
    G = []
    
    for x,a,c,m in zip(X,A,C,M):
        G.append(LCG(x,a,c,m))
    
    m0 = M[0]-1
    
    while True:
        yield sum([(-1**j)*next(g) for j,g in enumerate(G)]) % m0


def lehmer(x,a,m):
    """
    Lehmer PRNG: Special case of LCG
    
    Args:
        x -- seed value, coprime to m
        a -- multiplicative constant
        m -- modulus
    """
    
    require_integers(["x","a","m"],[x,a,m])
    
    if gcd(x,m) != 1:
        raise Exception("The seed of a Lehmer PRNG must be coprime to the modulus")
    
    while True:
        yield x
        x = (a*x)%m


def MINSTD0(x):
    """
    Original MINSTD with constant 16807
    """
    
    yield from lehmer(x,16807,2**31-1)


def MINSTD(x):
    """
    Revised MINSTD with constant 48271
    """
    
    yield from lehmer(x,48271,2**31-1)


def RANDU(x):
    """
    RANDU: Famously flawed Linear Congruential Generator
    
    Args:
        x -- seed value, odd
    
    OEIS A096555 (yes, really)
    """
    
    require_integers(["x"],[x])
    
    if x % 2 != 1:
        raise Exception("RANDU only accepts odd seed numbers, sorry!")
    
    yield from LCG(x,65539,0,2**31)


def ICG(x,a,c,m):
    """
    Inversive Congruential Generator
    
    Args:
        x -- seed value
        a -- multiplicative constant
        c -- additive constant
        m -- modulus, a prime
    """
    
    require_integers(["x","a","c","m"],[x,a,c,m])
    require_prime( ["m"], [m])
    
    while True:
        yield x
        
        if x == 0:
            x = c
        
        else:
            x = (mod_inv(x,m)*a+c)%m


def CIG(P):
    """
    Compound Inversive Generator
    
    Args:
        P -- list of primes greater than 3
    """
    
    m = prod(P)
    T = [m//p for p in P]
    cycles = [cycle([i for i in range(p)]) for p in P]
    
    for vals in zip(*cycles):
        yield sum(t*v for t,v in zip(T,vals)) % m


def aLFG(a,b,m):
    """
    Additive Lagged Fibonacci Generator
    
    Args:
        a -- first term
        b -- second term
        m -- modulus
    """
    
    require_integers(["a","b","m"],[a,b,m])
    
    while True:
        yield a
        a,b = b,(a+b)%m


def mLFG(a,b,m):
    """
    Multiplicative Lagged Fibonacci Generator
    
    Args:
        a -- first term
        b -- second term
        m -- modulus
    """
    
    require_integers(["a","b","m"],[a,b,m])
    
    while True:
        yield a
        a,b = b,(a*b)%m


def gLFG(a,b,m,func):
    """
    Generalized Lagged Fibonacci Generator
    
    Args:
        a -- first term
        b -- second term
        m -- modulus
        func -- function with two arguments returning an integer
    """
    
    require_integers(["a","b","m"],[a,b,m])
    
    while True:
        yield a
        a,b = b,func(a,b)%m


def LFSR(vector,taps):
    """
    Linear Feedback Shift Register: Returns the state at each step
    
    Args:
        vector -- list of bits
        taps --positions used to control next term
    """
    
    _check_LFSR_args(vector,taps)
    
    while True:
        yield digits_to_int(vector,2,bigendian=True)
        vector = vector[1:] + [sum([vector[i] for i in taps])%2]


def middle_square(n):
    """
    Middle Square Method
    
    Args:
        n -- seed value
    """
    
    require_integers(["n"],[n])
    
    N = int_to_digits(n)
    width = len(N)+(len(N)%2)
    
    while True:
        a = n*n
        A = int_to_digits(a)
        
        if len(A) % 2 == 1:
            A = [0] + A
        
        n = digits_to_int(A[width//2:-width//2])
        
        yield n


def middle_square_weyl(n,k,m):
    """
    Middle Square Method Augmented with a Weyl Sequence
    
    Args:
        n -- seed value
        k -- initial value for Weyl Sequence
        m -- modulus of Weyl Sequence
    """
    
    # Only n has to be checked since the weyl() function will check k and m
    require_integers(["n"],[n])
    
    W = weyl(k,m)
    
    N = int_to_digits(n)
    width = len(N)+(len(N)%2)
    
    for w in W:
        a = n*n+w
        A = int_to_digits(a)
        
        if len(A) % 2 == 1:
            A = [0] + A
        
        n = digits_to_int(A[width//2:-width//2])
        
        yield n


def blum_blum_shub(x,p,q):
    """
    Blum Blum Shub
    
    Args:
        x -- seed value, coprime to pq
        p -- prime congruent to 3 mod 4
        q -- prime congruent to 3 mod 4
    """
    
    m = p*q
    
    require_prime( ["p","q"], [p,q])
    require_true(["p","q"], [p,q], lambda x: x % 4 == 3, "must be congruent to 3 mod 4")
    require_geq(["x"], [x], 2)
    
    if gcd(m,x) != 1:
        raise Exception("x must be coprime to M")
    
    while True:
        yield x
        
        x = (x*x)%m





if __name__ == '__main__':
    from Sequences.Manipulations import simple_test
    
    print("Linear Congruential Generator")
    simple_test(LCG(9,5,17,97),14,
                "9, 62, 36, 3, 32, 80, 29, 65, 51, 78, 19, 15, 92, 89")
    
    print("\nRANDU, lower 16 bits (note only odd values)")
    simple_test(sequence_apply(RANDU(2127401289),lambda x: lower_bits(x,16)),8,
                "37193, 46043, 7057, 21171, 63513, 59467, 47329, 10915")
    
    print("\nRANDU, upper 16 bits")
    simple_test(sequence_apply(RANDU(2127401289),lambda x: upper_bits(x,16)),8,
                "32461, 3505, 23792, 12897, 27094, 13725, 2340, 21583")
    
    # print("\nCompound LCG")
    # simple_test(cLCG([142,5],[40014,40692],[0,0],[2147483563,2147483399]),13,
    #             "")
    
    print("\nInversive Congruential Generator")
    simple_test(ICG(1,7,23,103),14,
                "1, 30, 61, 40, 0, 23, 86, 65, 96, 22, 28, 49, 82, 57")
    
    print("\nCompound Inversive Generator")
    simple_test(CIG([5,7]),15,
                "0, 12, 24, 1, 13, 25, 2, 14, 26, 3, 15, 27, 4, 16, 28")
    
    print("\nAdditive Lagged Fibonacci Generator")
    simple_test(aLFG(9,27,97),14,
                "9, 27, 36, 63, 2, 65, 67, 35, 5, 40, 45, 85, 33, 21")
    
    print("\nMultiplicative Lagged Fibonacci Generator")
    simple_test(mLFG(9,27,97),14,
                "9, 27, 49, 62, 31, 79, 24, 53, 11, 1, 11, 11, 24, 70")
    
    print("\nLinear Feedback Shift Register")
    simple_test(LFSR([1,0,0,1,0,1,1,0],[0,3,6,7]),11,
                "105, 180, 218, 237, 118, 187, 221, 110, 55, 155, 205")
    
    print("\nMiddle-Square Method")
    simple_test(middle_square(675248),6,
                "959861, 333139, 981593, 524817, 432883, 387691")
    
    print("\nMiddle-Square Weyl")
    simple_test(middle_square_weyl(675248,5743,7899),6,
                "959861, 333145, 985594, 395534, 447152, 944916")
    
    print("\nBlum Blum Shub")
    simple_test(blum_blum_shub(3,11,23),12,
                "3, 9, 81, 236, 36, 31, 202, 71, 234, 108, 26, 170")
    