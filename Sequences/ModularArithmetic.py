from Sequences.Divisibility import primes
from Sequences.Simple import odds, naturals
from Sequences.MathUtils import egcd, prime_factorization, nth_sign, canonical_factorization
from Sequences.Figurate import squares
from Sequences.Manipulations import segment, partial_sums
from Sequences.NiceErrorChecking import require_integers

from itertools import cycle
from math import gcd
from sympy import legendre_symbol

def modular_inverses(flatten=False):
    """
    Triangle of Modular Multiplicative Inverses\n
    OEIS A102057
    """
    
    for a in naturals(2):
        T = []
        
        for b in range(1,a):
            g,x,y = egcd(b,a)
            
            if g != 1:
                T.append(0)
            
            else:
                T.append(x%a)
        
        if flatten == True:
            yield from T
        else:
            yield tuple(T)


def legendre_symbols(flatten=False):
    """
    Irreguar Array of Legendre Symbols: 1 at quadratic residues, -1 at nonresideus, 0 at zero
    One row for each prime, p, of length p\n
    OEIS A226520
    """
    
    for p in primes():
        T = [0]
        
        for a in range(1,p):
            out = pow(a,(p-1)//2,p)
            
            if out == 1:
                T.append(1)
            
            else:
                T.append(-1)
        
        if flatten == True:
            yield from T
        else:
            yield tuple(T)


def jacobi_symbols(flatten=False):
    """
    Irreguar Array of Jacobi Symbols: 1 at quadratic residues, -1 at nonresideus, 0 at zero
    One row for each odd natural, n, of length n\n
    OEIS
    """
    
    for p in odds():
        pfacs = canonical_factorization(p)
        
        T = []
        
        for a in range(p):
            out = 1
            
            for f,e in pfacs.items():
                out *= legendre_symbol(a,f)**e
            
            T.append(out)
        
        if flatten == True:
            yield from T
        else:
            yield tuple(T)


def kronecker_symbols():
    """
    Triangle of Kronecker Symbols: 1 at quadratic residues, -1 at nonresideus, 0 at zero
    One row for each natural, n, of length n\n
    OEIS A091337
    """
    
    yield from cycle([1,0,-1,0,-1,0,1,0])


def mobius_function():
    """
    Map of the Mobius Function\n
    OEIS A008683
    """
    
    yield 1
    
    for n in naturals(2):
        P = prime_factorization(n)
        
        if len(P) == len(set(P)):
            yield nth_sign(len(P))
        
        else:
            yield 0


def mertens_function():
    """
    Merten's Function: Partial sums of the Mobius Function\n
    OEIS A002321
    """
    
    yield from partial_sums(mobius_function())


def quadratic_residue(m):
    """
    Quadratic Residues Modulo m
    Finite generator
    """
    
    L = []
    
    for s in segment(squares(),0,m):
        L.append(s % m)
    
    yield from sorted(list(set(L)))


def quadratic_nonresidue(m):
    """
    Quadratic Nonresidues Modulo m
    Finite generator
    """
    
    S = set([i for i in range(2,m)])
    
    for s in segment(squares(),0,m):
        S.discard(s % m)
    
    yield from sorted(list(S))


def all_quadratic_residues():
    """
    Irregular array by rows listing all the quadratic residues for each positive natural\n
    OEIS A096008
    """
    
    for n in naturals(1):
        yield from quadratic_residue(n)


def all_quadratic_nonresidues():
    """
    Irregular array by rows listing all the quadratic nonresidues for each positive natural\n
    OEIS A096008
    """
    
    for n in naturals(1):
        yield from quadratic_nonresidue(n)


def squares_modulo_n(n):
    """
    Squares Modulo n\n
    OEIS A000004, A000035, A011655, A053879, A054580, A070430-A070470,
         A008959
    """
    
    L = []
    
    for i in segment(squares(),0,n):
        L.append(i % n)
    
    yield from cycle(L)


def weyl(k,m):
    """
    Weyl Sequence: Multiples of k modulo m
    Computational version using integers rather than Weyl's mathematical version with irrational k\n
    OEIS
    """
    
    if gcd(k,m) != 1:
        raise Exception("k and m must be coprime")
    
    require_integers(["k","m"],[k,m])
    
    n = 0
    
    while True:
        yield n
        
        n = (n+k)%m





if __name__ == '__main__':
    from Sequences.Manipulations import simple_test
    
    print("Triangle of Modular Inverses")
    simple_test(modular_inverses(),4,
                "(1,), (1, 2), (1, 0, 3), (1, 3, 2, 4)")
    
    print("\nIrregular Array of Legendre Symbols")
    simple_test(legendre_symbols(),3,
                "(0, 1), (0, 1, -1), (0, 1, -1, -1, 1)")
    
    print("\nIrregular Array of Jacobi Symbols")
    simple_test(jacobi_symbols(),3,
                "(1,), (0, 1, -1), (0, 1, -1, -1, 1)")
    
    print("\nTriangle of Kronecker Symbols")
    simple_test(kronecker_symbols(),17,
                "1, 0, -1, 0, -1, 0, 1, 0, 1, 0, -1, 0, -1, 0, 1, 0, 1")
    
    print("\nMobius Function")
    simple_test(mobius_function(),16,
                "1, -1, -1, 0, -1, 1, -1, 0, 0, 1, -1, 0, -1, 1, 1, 0")
    
    print("\nMerten's Function")
    simple_test(mertens_function(),14,
                "1, 0, -1, -1, -2, -1, -2, -2, -2, -1, -2, -2, -3, -2")
    
    print("\nQuadratic Residues of 22")
    simple_test(quadratic_residue(22),100,
                "0, 1, 3, 4, 5, 9, 11, 12, 14, 15, 16, 20")
    
    print("\nQuadratic Nonresidues of 22")
    simple_test(quadratic_nonresidue(22),100,
                "2, 6, 7, 8, 10, 13, 17, 18, 19, 21")
    
    print("\nTable of all Quadratic Residues")
    simple_test(all_quadratic_residues(),18,
                "0, 0, 1, 0, 1, 0, 1, 0, 1, 4, 0, 1, 3, 4, 0, 1, 2, 4")
    
    print("\nTable of all Quadratic Nonresidues")
    simple_test(all_quadratic_nonresidues(),18,
                "2, 2, 3, 2, 3, 2, 5, 3, 5, 6, 2, 3, 5, 6, 7, 2, 3, 5")
    
    print("\nSquares Modulo 7")
    simple_test(squares_modulo_n(7),18,
                "0, 1, 4, 2, 2, 4, 1, 0, 1, 4, 2, 2, 4, 1, 0, 1, 4, 2")
    
    print("\nWeyl Sequence for k = 36243 and m = 65536")
    simple_test(weyl(36243,2**16),8,
                "0, 36243, 6950, 43193, 13900, 50143, 20850, 57093")
    