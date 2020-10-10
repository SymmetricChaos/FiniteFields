from Sequences.Manipulations import speed_compare, memoize_multiplicative, memoize_total_additive
from itertools import count
from Sequences.MathUtils import jordan_totient, prime_factorization
from Sequences.Primes import primes
from collections import defaultdict
from Sequences.Simple import naturals


def memoization_example():
    
    print("Memoization has an overhead cost in storing and looking up values."
          "Thus it only provides an improvement in speed if the underlying "
          "function is slow. Here we demonstrate this my comparing the "
          "memoization of a quick to evaluation function with a slow to "
          "evaluate function\n")
    
    def F_fast(n):
        return jordan_totient(n,1)
    
    def F_slow(n):
        for i in range(10):
            jordan_totient(n,1)
        return jordan_totient(n,1)
    
    def F_fast_mem():
        yield from memoize_multiplicative(F_fast)
    
    def F_fast_dir():
        for n in count(1,1):
            yield F_fast(n)
    
    def F_slow_mem():
        yield from memoize_multiplicative(F_slow)
    
    def F_slow_dir():
        for n in count(1,1):
            yield F_slow(n)
    
    print("Quick Function, first 3000 terms")
    speed_compare([F_fast_mem(),F_fast_dir()],["Memoized","Direct"],n=3000,reps=1)
    
    print("\nSlow Function, first 3000 terms")
    speed_compare([F_slow_mem(),F_slow_dir()],["Memoized","Direct"],n=3000,reps=1)





def prime_omega_example():
    
    print("The prime Ω function counting prime divisors with multiplicity is "
          "expensive to compute because a factorization of n is needed. For "
          "the purpose of producing the sequence it is preferable to not do "
          "this. Two alternative are apparent. Using a sieve method the unique "
          "prime factors can be found iteratively and no others need be "
          "checked. Alternatively because it is a total additive function that "
          "property can be exploited.\n")
    
    def omega():
        
        for n in naturals(1):
            ctr = 0
            
            for p in primes():
                while n % p == 0:
                    ctr += 1
                    n = n // p
                
                if n == 1:
                    yield ctr
                    break
    
    
    def omega_mem1():
        
        D = defaultdict(list)
        
        yield 0
        
        for q in naturals(2):
            if q not in D:
                yield 1
                D[q + q] = [q]
            
            else:
                q_copy = q
                ctr = 0
                for fac in D[q]:
                    while q_copy % fac == 0:
                        ctr += 1
                        q_copy //= fac
                yield ctr
                
                for p in D[q]:
                    D[p+q].append(p)
                
                del D[q]
    
    
    def omega_mem2():
        
        def f(n):
            return len(prime_factorization(n))
        
        yield from memoize_total_additive(f)
    
    
    print("Counting Prime Factors, first 7000 terms")
    speed_compare([omega(),omega_mem1(),omega_mem2()],["Direct","Sieved","Additive"],n=8000,reps=1)





if __name__ == '__main__':
    
    memoization_example()
    
    print("\n\n")
    
    prime_omega_example()




