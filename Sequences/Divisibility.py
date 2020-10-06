from Sequences.NiceErrorChecking import require_integers, require_geq
from Sequences.Primes import primes
from Sequences.Simple import naturals
from Sequences.MathUtils import factors, prime_factorization, unique_prime_factors, \
                                jordan_totient, multi_lcm, prime_power_factorization, \
                                nth_sign
from collections import defaultdict
from math import prod, gcd
from itertools import takewhile


def smooth(B):
    """
    Smooth Numbers: Positive integers with no prime factors greater than B
    
    OEIS A003586, A051037, A002473, A051038, A080197, A080681, A080682, A080683
    
    Args:
        B -- largest prime factor allowed
    """
    
    require_integers(["B"],[B])
    require_geq(["B"],[B],1)
    
    P = [p for p in takewhile(lambda x: x <= B,primes())]
    
    for n in naturals(1):
        out = n
        
        for f in P:
            while n % f == 0:
                n = n // f
            
            if n == 1:
                yield out
                break


def hamming():
    """
    Hamming Numbers: The 5-Smooth numbers also known as the Regular Numbers\n
    OEIS A051037
    """
    
    yield from smooth(5)


def rough(B):
    """
    Rough Numbers: Positive integers with no prime factors less than B
    
    Args:
        B -- smallest prime factor allowed
    
    OEIS A000027, A005408, A007310, A007775, A008364, A008365, A008366, A166061, A166063
    """
    
    require_integers(["B"],[B])
    require_geq(["B"],[B],1)
    
    P = [p for p in takewhile(lambda x: x < B,primes())]
    
    for n in naturals(1):
        confirm = True
        
        for f in P:
            if n % f == 0:
                confirm = False
                break
        
        if confirm:
            yield n


def highly_composite():
    """
    Highly Composite Numbers: Positive integers that have more factors than any smaller positive integer\n
    OEIS A002182
    """
    
    F = 0
    
    for i in naturals(1):
        L = len(factors(i))
        
        if L > F:
            F = L
            yield i


def highly_composite_factor():
    """
    Factors of each Highly Composite Number\n
    OEIS 
    """
    
    F = 0
    
    for i in naturals(1):
        L = len(factors(i))
        
        if L > F:
            F = L
            yield F


def highly_composite_prime_factor():
    """
    Prime Factors (with multiplicity) of each Highly Composite Number\n
    OEIS A112778
    """
    
    for h in highly_composite():
        yield len(prime_factorization(h))


def divisors():
    """
    Number of Divisors: Count of divisors for each positive integer\n
    OEIS A000005
    """
    
    for i in naturals(1):
        yield len(factors(i))


def prime_divisors():
    """
    Number of Prime Divisors with Multiplicity: Length of prime factorization for each positive integer\n
    OEIS A001222
    """
    
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
    """
    Number of Unique Prime Divisors: Count of unique prime factors for each positive integer\n
    OEIS A001221
    """
    
    D = defaultdict(list)
    
    yield 0
    
    for q in naturals(2):
        if q not in D:
            yield 1
            D[q + q] = [q]
        
        else:
            yield len(D[q])
            
            for p in D[q]:
                D[p+q].append(p)
            
            del D[q]


def squarefree():
    """
    Squarefree Numbers: Positive integers not divisible by any prime more than once\n
    OEIS A005117
    """
    
    for n in naturals(1):
        for i in naturals(2):
            if n % i**2 == 0:
                break
            
            if (i**2) > n:
                yield n
                break


def squarefree_kernel():
    """
    Squarefree Kernels: Largest squarefree factor of each positive integer\n
    OEIS A007947
    """
    
    D = defaultdict(list)
    
    yield 1
    
    for q in naturals(2):
        if q not in D:
            yield q
            
            D[q + q] = [q]
        
        else:
            yield prod(D[q])
            
            for p in D[q]:
                D[p+q].append(p)
            
            del D[q]


def squareful():
    """
    Complement of the Squarefree Numbers\n
    OEIS A013929
    """
    
    yield 0
    
    for n in naturals(1):
        for i in naturals(2):
            if n % i**2 == 0:
                yield n
                break
            
            if (i**2) > n:
                break


def powerful(n=2):
    """
    n-Powerful Numbers: Positive integers that are divisible by the nth power of each prime factor
    OEIS A001694
    """
    
    require_integers(["n"],[n])
    require_geq(["n"],[n],2)
    
    def is_n_powerful(a,n):
        U = unique_prime_factors(a)
        for u in U:
            if a % (u**n) != 0:
                return False
        return True
    
    yield 1
    
    for m in naturals(4):
        if is_n_powerful(m,n):
            yield m


def totients():
    """
    Totients: Count of positive integers coprime to each positive integer\n
    OEIS A000010
    """
    
    D = defaultdict(list)
    
    yield 1
    
    for q in naturals(2):
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


def cototients():
    """
    Cotients: Count of positive integers not coprime to each positive integer\n
    OEIS A051953
    """
    
    for n,t in enumerate(totients(),1):
        yield n-t


# def nontotients():


# def even_nontotients():


# def noncototient():


# def sparsely_totient():


def charmichael():
    """
    Charmichael Function: LCM of the orders of the elements of the finite multiplictive group on n
    OEIS A002322
    """
    
    yield 1
    
    def charm(n):
        if n > 4 and n%2 == 0:
            return jordan_totient(n)//2
        return jordan_totient(n)
    
    for n in naturals(2):
        T = [charm(p) for p in prime_power_factorization(n)]
        
        yield multi_lcm(T)


def jordan_totients(k):
    """
    Jordan's k-Totient Function
    OEIS A007434, A059376, A059377, A059378, A069091-A069095
    """
    
    for n in naturals(1):
        yield jordan_totient(n,k)


def coprimes(n):
    """
    All positive integers coprime to n
    """
    
    require_integers(["n"],[n])
    require_geq(["n"],[n],1)
    
    F = []
    for p in primes():
        if n%p == 0:
            F.append(p)
        if p >= n:
            break
    
    def divby(n,F):
        for f in F:
            if x%f == 0:
                return False
        return True
    
    for x in naturals(1):
        if divby(x,F):
            yield x


def coprime_characteristic():
    """
    Triangle of coprime pairs: 1 if the pair is coprimes and 0 if not\n
    OEIS A054521
    """
    
    for m in naturals(1):
        for n in range(1,m+1):
            if gcd(m,n) == 1:
                yield 1
            else:
                yield 0


def p_adic_order(p):
    """
    p-adic Orders: Exponent of the greatest power of p that divides each positive integer\n
    Technically only a p-adic order if p is prime but defined for all naturals\n
    OEIS A007814, A007949, A235127, A112765
    """
    
    require_integers(["p"],[p])
    require_geq(["p"],[p],1)
    
    for n in naturals(1):
        ctr = 0
        
        while n%p == 0:
            ctr += 1
            n //= p
        
        yield ctr


def liouville():
    """
    Liouville's Function: 1 if n is a product of an even number of primes, otherwise -1
    """
    
    yield 1
    
    for n in naturals(2):
        P = prime_factorization(n)
        yield nth_sign(len(P))





if __name__ == '__main__':
    from Sequences.Manipulations import simple_test
    
    print("\nTotient Numbers")
    simple_test(totients(),17,
                "1, 1, 2, 2, 4, 2, 6, 4, 6, 4, 10, 4, 12, 6, 8, 8, 16")
    
    print("\nCototient Numbers")
    simple_test(cototients(),18,
                "0, 1, 1, 2, 1, 4, 1, 4, 3, 6, 1, 8, 1, 8, 7, 8, 1, 12")
    
    print("\n5-Smooth (Hamming)")
    simple_test(smooth(5),16,
                "1, 2, 3, 4, 5, 6, 8, 9, 10, 12, 15, 16, 18, 20, 24, 25")
    
    print("\n5-Rough")
    simple_test(rough(5),14,
                "1, 5, 7, 11, 13, 17, 19, 23, 25, 29, 31, 35, 37, 41")
    
    print("\nHighly Composite")
    simple_test(highly_composite(),13,
                "1, 2, 4, 6, 12, 24, 36, 48, 60, 120, 180, 240, 360")
    
    print("\nNumber of Divisors")
    simple_test(divisors(),18,
                "1, 2, 2, 3, 2, 4, 2, 4, 3, 4, 2, 6, 2, 4, 4, 5, 2, 6")
    
    print("\nNumber of Prime Divisors (with multiplicity)")
    simple_test(prime_divisors(),18,
                "0, 1, 1, 2, 1, 2, 1, 3, 2, 2, 1, 3, 1, 2, 2, 4, 1, 3")
    
    print("\nNumber of Unique Prime Divisors")
    simple_test(unique_prime_divisors(),18,
                "0, 1, 1, 1, 1, 2, 1, 1, 1, 2, 1, 2, 1, 2, 2, 1, 1, 2")
    
    print("\nSquarefree Numbers")
    simple_test(squarefree(),15,
                "1, 2, 3, 5, 6, 7, 10, 11, 13, 14, 15, 17, 19, 21, 22")
    
    print("\nSquarefree Kernels")
    simple_test(squarefree_kernel(),16,
                "1, 2, 3, 2, 5, 6, 7, 2, 3, 10, 11, 6, 13, 14, 15, 2")
    
    print("\nSquareful Numbers")
    simple_test(squareful(),14,
                "0, 4, 8, 9, 12, 16, 18, 20, 24, 25, 27, 28, 32, 36")
    
    print("\nCharacteristic Triangle of Coprimes")
    simple_test(coprime_characteristic(),18,
                "1, 1, 0, 1, 1, 0, 1, 0, 1, 0, 1, 1, 1, 1, 0, 1, 0, 0")
    
    print("\nNaturals Coprime to 24")
    simple_test(coprimes(24),14,
                "1, 5, 7, 11, 13, 17, 19, 23, 25, 29, 31, 35, 37, 41")
    
    print("\nPowerful Numbers")
    simple_test(powerful(),14,
                "1, 4, 8, 9, 16, 25, 27, 32, 36, 49, 64, 72, 81, 100")
    
    print("\n3-Powerful Numbers")
    simple_test(powerful(3),13,
                "1, 8, 16, 27, 32, 64, 81, 125, 128, 216, 243, 256, 343")
    
    print("\nCount of Factors for each Highly Composite Number")
    simple_test(highly_composite_factor(),15,
                "1, 2, 3, 4, 6, 8, 9, 10, 12, 16, 18, 20, 24, 30, 32")
    
    print("\nCount of Prime Factors (with multiplicity) for each Highly Composite Number")
    simple_test(highly_composite_prime_factor(),18,
                "0, 1, 2, 2, 3, 4, 4, 5, 4, 5, 5, 6, 6, 7, 6, 6, 7, 7")
    
    print("\nJordan 2-Totients")
    simple_test(jordan_totients(2),13,
                "1, 3, 8, 12, 24, 24, 48, 48, 72, 72, 120, 96, 168")
    
    print("\nCharmichael Function")
    simple_test(charmichael(),17,
                "1, 1, 2, 2, 4, 2, 6, 2, 6, 4, 10, 2, 12, 6, 4, 4, 16")
    
    print("\n3-adic Orders")
    simple_test(p_adic_order(3),18,
                "0, 0, 1, 0, 0, 1, 0, 0, 2, 0, 0, 1, 0, 0, 1, 0, 0, 2")
    
    print("\nLiouville Function")
    simple_test(liouville(),15,
                "1, -1, -1, 1, -1, 1, -1, -1, 1, 1, -1, -1, -1, 1, 1")
    