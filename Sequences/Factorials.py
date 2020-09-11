from Sequences.Manipulations import offset
from Sequences.Simple import naturals
from itertools import cycle


def factorials():
    """
    Factorial Numbers: Product of the the first n positive integers\n
    OEIS A000142
    """
    
    out = 1
    
    yield out
    
    for n in naturals(1):
        out = out * n
        yield out


def alternating_factorials_1():
    """
    Alternating Factorial Numbers: Absolute value of each term\n
    OEIS A005165
    """
    
    cyc = cycle([1,-1])
    F = offset(factorials(),1)
    out = 0
    
    yield 0
    
    for f,s in zip(F,cyc):
        out += f*s
        yield abs(out)


def alternating_factorials_2():
    """
    Alternating Factorial Numbers: Integer value of each term\n
    OEIS A058006
    """
    
    cyc = cycle([1,-1])
    F = factorials()
    out = 0
    
    for f,s in zip(F,cyc):
        out += f*s
        yield out


def kempner():
    """
    Kempner Numbers: Smallest positive integer m such that n divides m!\n
    OEIS A002034
    """
    
    yield 1
    
    for n in naturals(2):
        for i,f in enumerate(factorials()):
            if f%n == 0:
                yield i
                break


def double_factorials():
    """
    Double Factorials: Double factorial of each non-negative integer\n
    OEIS A006882
    """
    
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
    """
    Odd Double Factorials: Double factorial of each odd non-negative integer\n
    OEIS A001147
    """
    
    odd = 1
    odd_ctr = 1
    
    while True:
        yield odd
        
        odd_ctr += 2
        odd = odd*odd_ctr


def even_double_factorials():
    """
    Even Double Factorials: Double factorial of each even non-negative integer\n
    OEIS A000165
    """
    
    even = 2
    even_ctr = 2
    
    yield 1
    
    while True:
        yield even
        
        even_ctr += 2
        even = even*even_ctr





if __name__ == '__main__':
    from Sequences.Manipulations import simple_test
    
    print("Factorials")
    simple_test(factorials(),11,
                "1, 1, 2, 6, 24, 120, 720, 5040, 40320, 362880, 3628800")
    
    print("\nAlternating Factorials (A005165)")
    simple_test(alternating_factorials_1(),11,
                "0, 1, 1, 5, 19, 101, 619, 4421, 35899, 326981, 3301819")
    
    print("\nAlternating Factorials (A058006)")
    simple_test(alternating_factorials_2(),10,
                "1, 0, 2, -4, 20, -100, 620, -4420, 35900, -326980")
    
    print("\nKempner Function")
    simple_test(kempner(),17,
                "1, 2, 3, 4, 5, 3, 7, 4, 6, 5, 11, 4, 13, 7, 5, 6, 17")
    
    print("\nDouble Factorials")
    simple_test(double_factorials(),12,
                "1, 1, 2, 3, 8, 15, 48, 105, 384, 945, 3840, 10395")
    
    print("\nOdd Double Factorials")
    simple_test(odd_double_factorials(),9,
                "1, 3, 15, 105, 945, 10395, 135135, 2027025, 34459425")
    
    print("\nEven Double Factorials")
    simple_test(even_double_factorials(),9,
                "1, 2, 8, 48, 384, 3840, 46080, 645120, 10321920")
    