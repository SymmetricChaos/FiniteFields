from GeneralUtils import flatten

def collatz(n):
    while n > 1:
        yield n
        if n % 2 == 0:
            n = n//2
        else:
            n = 3*n+1
    yield n

def collatz_inv(n):
    if n % 6 == 4:
        return 2*n, (n-1)//3
    return 2*n

def collatz_inv_graph(n,levels):
    S = [n]
    for i in range(levels):
        S = [collatz_inv(m) for m in S]
        S = flatten(S)
        print(S)

def collatz_inv_print(levels):
    D = set([1])
    S = [1]
    for i in range(levels):
        for m in S:
            print(f"{collatz_inv(m)} → {m}")
        S = [collatz_inv(m) for m in S]
        S = set(flatten(S))
        S = S-D
        D = D|S
        S = list(S)

#
#for i in collatz(119):
#    print(i)


#collatz_inv_graph(1,9)