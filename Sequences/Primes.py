## Generator that returns primes (not my work)
def primes(n=0):
    D = {}
    q = 2
    
    ctr = 0
    while True:
        if q not in D:
            
            # If we have reached the nth prime return rather than yield
            # If the 0th prime is requested this never happens
            ctr += 1
            if ctr > n:
                return q
            
            yield q
                
            D[q * q] = [q]
        else:
            for p in D[q]:
                D.setdefault(p + q, []).append(p)
            del D[q]
        q += 1
