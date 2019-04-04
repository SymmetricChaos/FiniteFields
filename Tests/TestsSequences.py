from Sequences import naturals, fibonacci, lucas, pell, pell_lucas, tribonacci, \
                      padovan, integers, \
                      triangular, gen_triangular, cen_triangular, \
                      square, gen_square, cen_square, \
                      pentagonal, cen_pentagonal, gen_pentagonal, \
                      primes, primorials, \
                      pascal, bell, catalan, factorials, alternating_factorials, \
                      divisors, squarefree


from Sequences.Utils import show_vals


for seq in [naturals, integers, 
            triangular, gen_triangular, cen_triangular,
            square, gen_square, cen_square,
            pentagonal, cen_pentagonal, gen_pentagonal,
            fibonacci, lucas, pell, pell_lucas, tribonacci, padovan, 
            primes, primorials, pascal, bell, catalan,
            factorials, alternating_factorials, divisors,
            squarefree]:
    show_vals(seq)
