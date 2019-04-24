from ModularArithmetic import gcd, lcm

class Rational:
    
    def __init__(self,n,d=1):
        self.n = n
        self.d = d
        self.simplify()
    
    def simplify(self):
        g = abs(gcd(self.n,self.d))
        self.n = self.n//g
        self.d = self.d//g
    
    def inv(self):
        return Rational(self.d,self.n)
    
    def __neg__(self):
        return Rational(-self.n,self.d)
    
    
    def __str__(self):
        return str(self.n) + "/" + str(self.d)
    
    
    def __mul__(self,multiplier):
        if type(multiplier) == int:
            multiplier = Rational(multiplier)
        
        n = self.n * multiplier.n
        d = self.d * multiplier.d
        
        return Rational(n,d)


    def __rmul__(self,multiplier):
        return self*multiplier


    def __add__(self,addend):
        if type(addend) == int:
            addend = Rational(addend)
        
        L = lcm(self.d,addend.d)
        
        n = (L//self.d)*self.n + (L//addend.d)*addend.n
        d = L
        
        return Rational(n,d)


    def __radd__(self,addend):
        return self + addend


    def __sub__(self,addend):
        return self + -addend


    def __rsub__(self,addend):
        return addend + -self
    
A = Rational(4,10)
B = Rational(7,16)
print(A)
print(B)
print(A+B)
print(A-A)
print(A*B)
print(-A)
print(A-B)