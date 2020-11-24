from Sequences.MathUtils import nontrivial_factors, all_subsets
from Sequences.Combinatorics.PermutationUtils import int_to_comb
from Sequences.Simple import naturals, powers
from Sequences.Manipulations import make_triangle

from math import comb


def catalan():
    """
    Catalan Numbers: Number of non-crossing partitions of a set with n elements\n
    OEIS A000108
    """
    C = 1
    
    for n in naturals():
        yield C
        C = C*(4*n+2)//(n+2)


# Building the triangle using only addition and index look ups is about 100 
# times faster than calculating the binomial coefficients directly on my
# machine
# There is probably a way to do this is place
def pascal():
    """
    Pascal's Triangle: Number triangle with binomial coefficients\n
    OEIS A007318
    """
    
    L = [1,0]
    
    while True:
        T = [0]
        
        for i in range(len(L)-1):
            x = L[i]+L[i+1]
            T.append(x)
            yield x
        
        T.append(0)
        L = T


def pascal_triangle():
    """
    Pascal's Triangle by Rows\n
    OEIS A007318
    """
    
    yield from make_triangle(pascal())


# Find a more efficient way to do this
def central_binomial():
    """
    Central Binomial Coefficients: Middle term of the odd rows of Pascal's Triangle
    OEIS A000984
    """
    
    for n in naturals():
        yield comb(2*n,n)


def gould():
    """
    Gould's Sequence: Number of odd values on the nth row of Pascal's Triangle\n
    OEIS A001316
    """
    
    P = pascal()
    
    for n in naturals(1):
        val = 0
        
        for i in range(n):
            if next(P) % 2 == 1:
                val += 1
        
        yield val


# As with Pascal's triangle I found this memoized version to be vastly faster
# than directly calculating the values, which involved both binomial
# coefficients and exponentiation
def eulerian():
    """
    Eulerian Triangle: Triangle with number of permutations of a set with n elements where there are m increases\n
    OEIS A008292
    """
    
    L = [1,0]
    
    for a in naturals(1):
        T = []
        
        for b in range(a):
            x = (a-b)*L[b-1] + (b+1)*L[b]
            T.append(x)
            yield x
        
        T.append(0)
        L = T


def eulerian_triangle():
    """
    Eulerian Triangle by Rows\n
    OEIS A007318
    """
    
    yield from make_triangle(eulerian())


def bell():
    """
    Bell Numbers: Number of equivalence classes on a set with n elements\n
    OEIS A000110
    """
    
    R0 = [1]
    R1 = [1,2]
    
    while True:
        yield R0[0]
        R2 = [R1[-1]]
        
        for i in R1:
            R2.append(i+R2[-1])
        
        R0, R1 = R1, R2


def lazy_caterer():
    """
    Lazy Caterer Numbers: Maximum number of pieces produced when cutting a circle with exactly n lines\n
    OEIS A000124
    """
    
    for n in naturals():
        yield (n*(n+1))//2+1


# Generalized cake numbers?
def cake():
    """
    Cake Numbers: Maximum number of pieces produced when cutting a sphere with exactly n planes\n
    OEIS A000125
    """
    
    for n in naturals():
        yield (n*n*n+5*n+6)//6


# Potentially memoizeable
def multiplicative_partition():
    """
    Multiplicative Partition Numbers: Sets of integers, not including one, that have a product of n\n
    OEIS A001055
    """
    
    def all_factorizations_inner(n,m=1):
        F = [f for f in nontrivial_factors(n) if f >= m]
        
        if len(F) == 0:
            yield [n]
        
        else:
            for f in F:
                for a in all_factorizations_inner(n//f,f):
                    yield [f] + a
    
    def num_factorizations(n):
        S = set([(n,)])
        
        for i in all_factorizations_inner(n):
            S.add(tuple(sorted(i)))
        
        return len(S)
    
    for n in naturals(1):
        yield num_factorizations(n)


def natural_subsets(index=0):
    """
    All subsets of the natural numbers in colexicographic order (aka prefix order)
    
    Args:
        index -- 0 or 1, least element
    
    OEIS
    """
    
    if index not in (0,1):
        raise Exception("index must be 0 or 1")
    
    yield ()
    yield from all_subsets(naturals(index))


def combinadic(k):
    """
    k-Combinadic Numbers: Natural numbers represented as descending combinations of k elements\n
    OEIS
    """
    
    for n in naturals():
        yield int_to_comb(n,k)


def dyck_words(n):
    """
    The Dyck words of order n with 'up' as +1 and 'down' as -1
    """
    
    def dyck_recur(S):
        a = S.count(1)
        b = S.count(-1)
        if len(S) > 2*n or b > a:
            return None
        elif a == b == n:
            yield S
        else:
            yield from dyck_recur(S+(1,))
            yield from dyck_recur(S+(-1,))
    
    yield from dyck_recur(())


def dyck_language():
    """
    All the Dyck words with 'up' as +1 and 'down' as -1
    """
    
    for n in naturals(1):
        yield from dyck_words(n)


def dyck_words_str(n):
    """
    All words consisting of n pairs of correctly matched parentheses
    """
    
    def dyck_recur(S):
        a = S.count("(")
        b = S.count(")")
        if len(S) > 2*n or b > a:
            return None
        elif a == b == n:
            yield S
        else:
            yield from dyck_recur(S+"(")
            yield from dyck_recur(S+")")
    
    yield from dyck_recur("")


def dyck_language_str():
    """
    All words consisting of correctly matched pairs of parentheses
    """
    
    for n in naturals(1):
        yield from dyck_words_str(n)


def naranya():
    """
    Triangle of Naranya Numbers: Number of Dyck words of order n with k peaks\n
    OEIS A001263
    """
    
    for n in naturals(1):
        for k in range(1,n+1):
            yield (comb(n,k)*comb(n,k-1))//n


def naranya_triangle():
    """
    Naranya's Triangle by Rows\n
    OEIS A001263
    """
    
    yield from make_triangle(naranya())


def schroder():
    """
    Schröder Numbers: The big Schröder numbers\n
    OEIS A006318
    """
    
    yield 1
    
    S = [1,2]
    
    for n in naturals(1):
        yield S[n]
        
        t = 3*S[-1]
        for k in range(1,n):
            t += S[k]*S[n-k]
        
        S.append(t)


def schroder_hipparchus():
    """
    Schröder-Hipparchus Numbers: The little Schröder numbers\n
    OEIS A001003
    """
    
    yield 1
    
    a,b = 1,1
    
    for n in naturals(2):
        t = ((6*n-9)*b-(n-3)*a)//n
        a,b = b,t
        
        yield b//2






if __name__ == '__main__':
    from Sequences.Manipulations import simple_test
    
    print("\nCatalan Numbers")
    simple_test(catalan(),11,
                "1, 1, 2, 5, 14, 42, 132, 429, 1430, 4862, 16796")
    
    print("\nPascal's Triangle")
    simple_test(pascal(),18,
                "1, 1, 1, 1, 2, 1, 1, 3, 3, 1, 1, 4, 6, 4, 1, 1, 5, 10")
    
    print("\nPascal's Triangle by Rows")
    simple_test(pascal_triangle(),4,
                "(1,), (1, 1), (1, 2, 1), (1, 3, 3, 1)")
    
    print("\nCentral Binomial Coefficients")
    simple_test(central_binomial(),11,
                "1, 2, 6, 20, 70, 252, 924, 3432, 12870, 48620, 184756")
    
    print("\nGould's Sequence")
    simple_test(gould(),18,
                "1, 2, 2, 4, 2, 4, 4, 8, 2, 4, 4, 8, 4, 8, 8, 16, 2, 4")
    
    print("\nEulerian Triangle")
    simple_test(eulerian(),16,
                "1, 1, 1, 1, 4, 1, 1, 11, 11, 1, 1, 26, 66, 26, 1, 1")
    
    print("\nEulerian Triangle by Rows")
    simple_test(eulerian_triangle(),4,
                "(1,), (1, 1), (1, 4, 1), (1, 11, 11, 1)")
    
    print("\nBell Numbers")
    simple_test(bell(),11,
                "1, 1, 2, 5, 15, 52, 203, 877, 4140, 21147, 115975")
    
    print("\nLazy Caterer's Numbers")
    simple_test(lazy_caterer(),14,
                "1, 2, 4, 7, 11, 16, 22, 29, 37, 46, 56, 67, 79, 92")
    
    print("\nCake Numbers")
    simple_test(cake(),13,
                "1, 2, 4, 8, 15, 26, 42, 64, 93, 130, 176, 232, 299")
    
    print("\nMultiplicative Partitions")
    simple_test(multiplicative_partition(),18,
                "1, 1, 1, 2, 1, 2, 1, 3, 2, 2, 1, 4, 1, 2, 2, 5, 1, 4")
    
    print("\nAll Subsets of Natural Numbers")
    simple_test(natural_subsets(),7,
                "(), (0,), (1,), (0, 1), (2,), (0, 2), (1, 2)")
    
    print("\n2-Combinadic Numbers")
    simple_test(combinadic(2),7,
                "(1, 0), (2, 0), (2, 1), (3, 0), (3, 1), (3, 2), (4, 0)")
    
    print("\nPascal's Triangle by Rows")
    simple_test(pascal_triangle(),5,
                "(1,), (1, 1), (1, 2, 1), (1, 3, 3, 1), (1, 4, 6, 4, 1)")
    
    print("\nDyck Words of Order 4")
    simple_test(dyck_words_str(4),5,
                "(((()))), ((()())), ((())()), ((()))(), (()(()))")
    
    print("\nDyck Language")
    simple_test(dyck_language_str(),7,
                "(), (()), ()(), ((())), (()()), (())(), ()(())")
    
    print("\nDyck Words of Order 3 (numeric)")
    simple_test(dyck_words(3),2,
                "(1, 1, 1, -1, -1, -1), (1, 1, -1, 1, -1, -1)")
    
    print("\nDyck Language (numeric)")
    simple_test(dyck_language(),3,
                "(1, -1), (1, 1, -1, -1), (1, -1, 1, -1)")
    
    print("\nNaranya's Triangle")
    simple_test(naranya(),16,
                "1, 1, 1, 1, 3, 1, 1, 6, 6, 1, 1, 10, 20, 10, 1, 1")
    
    print("\nNaranya's Triangle By Rows")
    simple_test(naranya_triangle(),4,
                "(1,), (1, 1), (1, 3, 1), (1, 6, 6, 1)")
    
    print("\nSchröder Numbers")
    simple_test(schroder(),10,
                "1, 2, 6, 22, 90, 394, 1806, 8558, 41586, 206098")
    
    print("\nSchröder-Hipparchus Numbers")
    simple_test(schroder_hipparchus(),10,
                "1, 1, 3, 11, 45, 197, 903, 4279, 20793, 103049")
    
    