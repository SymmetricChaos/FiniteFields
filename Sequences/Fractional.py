from Sequences.Simple import naturals
from Sequences.NiceErrorChecking import require_integers, require_nonnegative
from math import gcd


def numerators(sequence):
    """
    Numerators of a sequence of rational numbers
    Equivalently first value from each pair in a sequence
    """
    
    for a,b in sequence:
        yield a


def denominators(sequence):
    """
    Denominators of a sequence of rational numbers
    Equivalently second value from each pair in a sequence
    """
    
    for a,b in sequence:
        yield b


def _pretty_fracs(sequence):
    """
    Internal function to show fractions more compactly
    """
    
    for a,b in sequence:
        yield f"{a}/{b}"


def harmonic():
    """
    Harmonic series by pairs
    OEIS A001008, A002805
    """
    
    n0, d0 = 1,1
    
    for i in naturals(2):
        yield (n0,d0)
        
        n = n0*i+d0
        d = d0*i
        g = gcd(n,d)
        
        n0, d0 = n//g,d//g


def gen_harmonic(m):
    """
    Generalized harmonic series of order m by pairs
    
    Args:
        m -- exponent for the numerators of the terms
    
    OEIS
    """
    
    require_integers(["m"],[m])
    require_nonnegative(["m"],[m])
    
    if m == 0:
        for i in naturals(1):
            yield i
    
    n0, d0 = 1,1
    
    for i in naturals(2):
        yield (n0,d0)
        
        n = n0*i+d0
        d = d0*(i**m)
        g = gcd(n,d)
        
        n0, d0 = n//g,d//g


def farey():
    """
    Farey Sequences for each positive integer
    """
    
    for n in naturals(1):
        a,b,c,d = 0,1,1,n
        
        while a <= b:
            yield (a,b)
            
            k = (n+b)//d
            a,b,c,d = c,d,k*c-a,k*d-b


def stern_brocot():
    """
    Stern-Brocot Tree of Fully Reduced Fractions
    """
    
    def pair_add(A,B):
        return (A[0]+B[0],A[1]+B[1])
    
    row = [(0,1),(1,0)]
    new = []
    
    while True:
        for i in range(len(row)-1):
            t = pair_add(row[i],row[i+1])
            
            yield t
            
            new.append(row[i])
            new.append(t)
        
        new.append((1,0))
        row, new = new, []


#def bernoulli_numbers(n=-1):
#    
#    if n not in (1,-1):
#        raise Exception("The Bernoulli numbers should be specified by -1 for the negative version or 1 for the positive version")


def fibonacci_rationals():
    """
    Irregular triangle of generations of the Fibonacci ordering of the rationals by rows
    """
    
    def generation(n):
        if n == 1:
            return [(1,1)]
        else:
            L = []
            for i in range(1,n):
                prev = generation(n-1)
                for p in prev:
                    add = (p[0]+p[1],p[1])
                    inv = (p[1],p[0])
                    L.append(add)
                    L.append(inv)
                return L
    
    for n in naturals(1):
        yield from iter(generation(n))





if __name__ == '__main__':
    from Sequences.Manipulations import simple_test
    
    print("\nHarmonic Sequence")
    simple_test(_pretty_fracs(harmonic()),8,
                "1/1, 3/2, 11/6, 25/12, 137/60, 49/20, 363/140, 761/280")
    
    print("\nHarmonic Denominators")
    simple_test(denominators(harmonic()),11,
                "1, 2, 6, 12, 60, 20, 140, 280, 2520, 2520, 27720")
    
    print("\nGeneralized Harmonic Sequence of Order 2")
    simple_test(_pretty_fracs(gen_harmonic(2)),6,
                "1/1, 3/4, 13/36, 11/72, 127/1800, 427/10800")
    
    print("\nGeneralized Harmonic Denominators of Order 2")
    simple_test(denominators(gen_harmonic(2)),9,
                "1, 4, 36, 72, 1800, 10800, 529200, 4233600, 38102400")
    
    print("\nIrregular Triangle of Farey Sequences")
    simple_test(_pretty_fracs(farey()),11,
                "0/1, 1/1, 0/1, 1/2, 1/1, 0/1, 1/3, 1/2, 2/3, 1/1, 0/1")
    
    print("\nStern-Brocot Tree")
    simple_test(_pretty_fracs(stern_brocot()),11,
                "1/1, 1/2, 2/1, 1/3, 2/3, 3/2, 3/1, 1/4, 2/5, 3/5, 3/4")
    
    print("\nFibonacci Order of the Rationals")
    simple_test(_pretty_fracs(fibonacci_rationals()),11,
                "1/1, 2/1, 1/1, 3/1, 1/2, 2/1, 1/1, 4/1, 1/3, 3/2, 2/1")
    