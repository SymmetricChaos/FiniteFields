from itertools import cycle


def factorials():
    """Factorial Numbers: Product of the the first n positive integers"""
    
    ctr = 1
    out = 1
    
    yield out
    
    while True:
        out = out * ctr
        ctr += 1
        yield out


def alternating_factorials():
    """Alternating Factorial Numbers"""
    
    cyc = cycle([1,-1])
    out = 0
    
    for fac,p in zip(factorials(),cyc):
        out += fac*p
        yield abs(out)


def kempner_function():
    """Kempner Function: For each positive integer the index of the argument of the smallest factorial it is a factor of"""
    
    L = []
    
    for n,i in enumerate(factorials(),1):
        L.append(i)
        
        for ctr,f in enumerate(L,1):
            if f % n == 0:
                yield ctr
                break


def double_factorials():
    """Double Factorials: Double factorial of each non-negative integer"""
    
    odd = 1
    even = 2
    
    odd_ctr = 1
    even_ctr = 2
    
    yield 1
    
    while True:
        yield odd
        yield even
        
        odd_ctr += 2
        even_ctr += 2
        
        odd = odd*odd_ctr
        even = even*even_ctr


def odd_double_factorials():
    """Odd Double Factorials: Double factorial of each odd non-negative integer"""
    
    odd = 1
    odd_ctr = 1
    
    while True:
        yield odd
        
        odd_ctr += 2
        odd = odd*odd_ctr


def even_double_factorials():
    """Even Double Factorials: Double factorial of each even non-negative integer"""
    
    even = 2
    even_ctr = 2
    
    yield 1
    
    while True:
        yield even
        
        even_ctr += 2
        even = even*even_ctr
