#Analyzes digital signals

import numpy as np

def analyze_signal(signal,name):
    high= np.sum(signal)
    low= len(signal)-high
    duty= (high/len(signal))*100
    rising =0
    falling=0

    #Rising edge (0 -> 1)
    for i in range(1,len(signal)):
        if signal[i-1]==0 and signal[i]==1:
            rising +=1

    #Falling edge (1 -> 0)
    for i in range(1,len(signal)):
        if signal[i-1]==0 and signal[i]==1:
            falling +=1

    #Return results as dictionary
    return{
        "Signal":name,
        "High":high,
        "Low":low,
        "Duty cycle":round(duty,2),
        "Rising edges":rising,
        "Falling edges":falling
    }