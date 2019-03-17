from PolynomialRepresentation import poly_norm, poly_degree, poly_pad, \
                                     poly_print, poly_add, poly_mult, \
                                     poly_divmod, eq_print

# Four polynomials
P = [-42,1,-12,-1]
Q = [-3,1,0,0]
R = [9,6,7,1,3,4,5]
S = [1,1,0,1,1,0,0,0,1]

print("Four Polynomials in Ascending Vector Form")
for i in [P,Q,R,S]:
    eq_print(i,3)

print("\n\nThe Same Polynomials in Descending Written Form")
for i in [P,Q,R,S]:
    poly_print(i)
    
print("\n\nPolynomials With Degree")
for i in [P,Q,R,S]:
    print("Degree {}".format(poly_degree(i)),i)
    
print("\n\nFinite Field Addition GF(3^2)")
eq_print(P,3)
eq_print(R,3)
eq_print(poly_add(P,R,9),3)

print("\n\nFinite Field Multiplication GF(3^2)")
eq_print(P,3)
eq_print(R,3)
eq_print(poly_mult(P,R,9),3)

print("\n\nFinite Field Division GF(3^2)")
eq_print(S,1)
eq_print(R,1)
print()
div,mod = poly_divmod(S,R,9)
print("Quotient ",end=" ")
eq_print(div,1)
print("Remainder",end=" ")
eq_print(mod,1)