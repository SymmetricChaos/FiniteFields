from Choose import choose

def lobb_number(m,n):
    assert type(m) == int
    assert type(n) == int
    assert n >= m >= 0
    a = choose(2*n,m+n)
    b = 2*m+1
    c = m+n+1
    return (a*b)//c
#
#for i in range(6):
#    for j in range(i+1):
#        print(lobb_number(j,i),end = " ")
#    print()