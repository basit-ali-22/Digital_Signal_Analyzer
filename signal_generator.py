#generates digital signals for analysis

import numpy as np

def generate_signals(sample=10):
    
    time=np.arange(10)
    clock=time%2

    reset=np.zeros(10,dtype=int)
    reset[:4]=1

    data=np.random.randint(0,2,size=10)

    #return all generated signals
    return time, clock, reset, data