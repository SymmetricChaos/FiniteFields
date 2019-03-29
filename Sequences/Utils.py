def sequence_params(num_vals,offset):
    
    if type(num_vals) != int:
        raise Exception("n_vals must be an integer")
    if type(offset) != int:
        raise Exception("offset must be an integer")
        
    if num_vals < 0:
        raise Exception("n_vals must be nonnegative")
    if offset < 0:
        raise Exception("offset must ber nonnegative")


    if offset > num_vals:
        raise Exception("offset cannot be greater than num_vals")
        
        
def sequence_maker(generator):
    
    def S(num_vals=0,offset=0,**kwargs):
        
        sequence_params(num_vals, offset)
                
        if num_vals == 0:
            num_vals = float('inf')
            
        for ctr,val in enumerate(generator(**kwargs)):
            if ctr >= num_vals+offset:
                break
            
            if ctr >= offset:
                yield val
                
    return S