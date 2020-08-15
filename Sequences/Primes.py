from Sequences.Simple import naturals
from Sequences.MathUtils import factorization
from collections import defaultdict
from itertools import takewhile
from Sequences.NiceErrorChecking import require_integers, require_positive

## Generator that returns primes (not my work)
def primes():
    """Prime Numbers: Positive integers with exactly two factors"""
    
    D = defaultdict(list)
    q = 2
    
    while True:
        
        if q not in D:
            yield q
            D[q * q] = [q]
        
        else:
            for p in D[q]:
                D[p+q].append(p)
            del D[q]
        
        q += 1


def composites():
    """Composite Numbers: Positive integers with more than two factors"""
    
    D = defaultdict(list)
    q = 2
    
    while True:
        
        if q not in D:
            D[q * q] = [q]
        
        else:
            yield q
            for p in D[q]:
                D[p+q].append(p)
            del D[q]
        
        q += 1


# Cumulative product of prime numbers.
def primorials():
    """Primoral Numbers: Cumulative product of primes"""
    
    out = 1
    for i in primes():
        
        yield out
        
        out *= i


def pythagorean_primes():
    """Pythagorean Primes: Primes that can be the hypotenuse of an integer right triangle"""
    
    for p in primes():
        if (p-1)%4 == 0:
            yield p


def smooth(B):
    """
    Smooth Numbers: Positive integers with no prime factors greater than B
    
    Args:
        B -- largest prime factor allowed
    """
    
    require_integers(["B"],[B])
    require_positive(["B"],[B])
    
    P = [p for p in takewhile(lambda x: x <= B,primes())]
    
    for n in naturals(1):
        out = n
        
        for f in P:
            while n % f == 0:
                n = n // f
            
            if n == 1:
                yield out
                break


def rough(B):
    """
    Rough Numbers: Positive integers with no prime factors less than B
    
    Args:
        B -- smallest prime factor allowed
    """
    
    require_integers(["B"],[B])
    require_positive(["B"],[B])
    
    P = [p for p in takewhile(lambda x: x < B,primes())]
    print(P)
    for n in naturals(1):
        r = True
        
        for f in P:
            if n % f == 0:
                r = False
                break
        
        if r:
            yield n


def highly_composite():
    """Highly Composite Numbers: Positive integers that have more factors than any smaller positive integer"""
    
    F = 0
    for i in naturals(1):
        L = len(factorization(i))
        
        if L > F:
            F = L
            yield i


def divisors():
    """Number of Divisors: Count of divisors for each positive integer"""
    
    for i in naturals(1):
        yield len(factorization(i))


def prime_divisors():
    """Number of Prime Divisors with Multiplicity: Length of prime factorization for each positive integer"""
    
    for n in naturals(1):
        ctr = 0
        
        for p in primes():
            while n % p == 0:
                ctr += 1
                n = n // p
            
            if n == 1:
                yield ctr
                break


def unique_prime_divisors():
    """Number of Unique Prime Divisors: Count of unique prime factors for each positive integer"""
    
    D = defaultdict(list)
    q = 2
    
    yield 1
    
    while True:
        if q not in D:
            yield 1
            D[q + q] = [q]
        
        else:
            yield len(D[q])
            
            for p in D[q]:
                D[p+q].append(p)
            
            del D[q]
        
        q += 1


def squarefree():
    """Squarefree Numbers: Positive integers not divisible by any prime more than once"""
    
    for n in naturals(1):
        for i in naturals(2):
            if n % i**2 == 0:
                break
            
            if (i**2) > n:
                yield n
                break


def squarefree_kernel():
    """Squarefree Kernels: Largest squarefree factor of each positive integer"""
    
    for n in naturals(1):
        K = 1
        
        for p in primes():
            if n % p == 0:
                K *= p
                
                while n % p == 0:
                    n //= p
            
            if n == 1:
                yield K
                break


def prime_counting():
    """Prime Counting Function: Count of primes less than each non-negative integer"""
    
    ctr = 0
    cur = 0
    
    for p in primes():
        for i in range(p-cur):
            yield ctr
        
        ctr += 1
        cur = p


def totients():
    """Totients: Count of positive integers coprime to each positive integer"""
    
    D = defaultdict(list)
    q = 2
    
    yield 1
    
    while True:
        if q not in D:
            yield q-1
            D[q + q] = [q]
        
        else:
            n,d = 1,1
            
            for p in D[q]:
                D[p+q].append(p)
                
                n *= (p-1)
                d *= p
            
            yield q*n//d
            
            del D[q]
        
        q += 1