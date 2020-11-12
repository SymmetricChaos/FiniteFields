from Manipulations import *
from Sequences.Divisibility import primes, safe_primes
from Simple import naturals, constant, powers, evens, odds
from Recurrence import companion_pell, fibonacci
from Divisibility import amicable_pairs
from Weird import even_odd


A142150 = interleave(naturals(0),constant(0))
A001333 = sequence_apply(companion_pell(),lambda x: x//2)
A259180 = chunk_by_n(amicable_pairs(),2)
A000217 = partial_sums(naturals())
binom_trans1 = binomial_transform(constant(1))
binom_trans2 = binomial_transform(powers(2),invert=True)
A001629 = convolution(fibonacci(),fibonacci())
sum_fib_nat = pairwise_sum(naturals(),fibonacci())
fib_diffs = differences(fibonacci())
superprimes = hypersequence(primes())
even_rep_odd = n_rep_a(offset(evens(),1),odds())
RLE = run_length_encoding(n_rep_a(offset(evens(),1),odds()))
iRLE = inv_run_length_encoding(naturals(1))
runs = run_lengths(n_rep_a(offset(evens(),1),odds()))
prime_perm = permute(primes(),prepend(0,even_odd()))
fib_primes = prime_subsequence(fibonacci())
three_mod_four_primes = filter(lambda x: x%4 == 3,safe_primes())


print("A142150")
simple_test(A142150,10,"0, 0, 1, 0, 2, 0, 3, 0, 4, 0")

print("\nA001333")
simple_test(A001333,10,"1, 1, 3, 7, 17, 41, 99, 239, 577, 1393")

print("\nA259180 by pairs")
simple_test(A259180,4,"(220, 284), (1184, 1210), (2620, 2924), (5020, 5564)")

print("\nA000217")
simple_test(A000217,10,"0, 1, 3, 6, 10, 15, 21, 28, 36, 45")

print("\nBinomial Transform of the 1s Sequence")
simple_test(binom_trans1,10,"1, 2, 4, 8, 16, 32, 64, 128, 256, 512")

print("\nInverse Binomial Transform of the Powers of Two")
simple_test(binom_trans2,10,"1, 1, 1, 1, 1, 1, 1, 1, 1, 1")

print("\nFirst Convolved Fibonacci Sequence")
simple_test(A001629,10,"0, 0, 1, 2, 5, 10, 20, 38, 71, 130")

print("\nPairwise Sum of the Fibonacci Sequence and the Natural Numbers")
simple_test(sum_fib_nat,10,"0, 2, 3, 5, 7, 10, 14, 20, 29, 43")

print("\nFirst Differences of the Fibonacci Sequence")
simple_test(fib_diffs,10,"1, 0, 1, 1, 2, 3, 5, 8, 13, 21")

print("\nSuperprimes")
simple_test(superprimes,10,"3, 5, 11, 17, 31, 41, 59, 67, 83, 109")

print("\nEach positive even number E, repeated E-1 times.")
simple_test(even_rep_odd,10,"2, 4, 4, 4, 6, 6, 6, 6, 6, 8")

print("\nRLE of 2,4,4,4,6,6,6,6,6,7...")
simple_test(RLE,10,"1, 2, 3, 4, 5, 6, 7, 8, 9, 10")

print("\nDecoding of 1,2,3,4,5,6,7,8 interpreted as a RLE")
simple_test(iRLE,10,"2, 4, 4, 4, 6, 6, 6, 6, 6, 8")

print("\nRun Lengths of 2,4,4,4,6,6,6,6,6,7...")
simple_test(runs,10,"1, 3, 5, 7, 9, 11, 13, 15, 17, 19")

print("\nA permutation of the primes")
simple_test(prime_perm,10,"2, 5, 3, 11, 7, 17, 13, 23, 19, 31")

print("\nFibonnaci Primes")
simple_test(fib_primes,6,"3, 5, 13, 89, 233, 1597")

print("\nSafe Primes Congruent to 3 mod 4")
simple_test(three_mod_four_primes,12,"7, 11, 23, 47, 59, 83, 107, 167, 179, 227, 263, 347")