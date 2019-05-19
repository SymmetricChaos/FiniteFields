def naturals(n=0):
    """Natural Numbers"""
    
    assert type(n) == int
    assert n >= 0
    
    ctr = n
    
    while True:
        yield ctr
        
        ctr += 1
        

def integers(n=0):
    """Integers"""
    
    assert type(n) == int
    assert n >= 0
    
    ctr = n*2-1
    n = n
    
    while True:
        
        yield n
        
        ctr += 1
        if ctr % 2 == 0:
            n -= ctr
        else:
            n += ctr
        

def arithmetic(b=0,n=1):
    """Arithmetic Sequence"""
    
    assert type(b) == int
    assert type(n) == int
        
    out = b
    
    while True:
        
        yield out
        
        out += n
        
def geometric(b=1,n=2):
    """Geometric Sequence"""
    
    assert type(b) == int
    assert type(n) == int
        
    out = b
    
    while True:
        
        yield out
        
        out *= n
        
def powers(n):
    """Powers of N"""
    assert type(n) == int
    assert n >= 0
    
    pw = 1
    
    while True:
        yield pw
        
        pw *= n
        
