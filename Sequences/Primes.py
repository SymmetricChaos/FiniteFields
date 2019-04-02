from Sequences.Naturals import naturals
from Other.Factors import factors

## Generator that returns primes (not my work)
def primes():
    """Prime Numbers"""
    D = {}
    q = 2
    
    while True:
        if q not in D:
            
            yield q
                
            D[q * q] = [q]
        else:
            for p in D[q]:
                D.setdefault(p + q, []).append(p)
            del D[q]
        q += 1


def primorials():
    """Primoral Numbers"""

    out = 1
    for i in primes():
        
        yield out
        
        out *= i


def smooth(B):
    """Smooth Numbers"""
    for n in naturals(1):
        out = n
        for f in range(2,B+1):
            while n % f == 0:
                n = n // f
            if n == 1:
                yield out
                break


def rough(B):
    """Rough Numbers"""
    for n in naturals(1):
        r = True
        for f in range(2,B):
            if n % f == 0:
                r = False
                break
        if r:
            yield n
            

def highly_composite():
    """High Composite Numbers"""
    F = 0
    for i in naturals(1):
        L = len(factors(i))
        if L > F:
            F = L
            yield i


def divisors():
    """Number of Divisors"""
    for i in naturals(1):
        yield len(factors(i))