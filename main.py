#DIGITAL SIGNAL ANALYZER
#Main Program

import pandas as pd

from signal_generator import generate_signals
from analyzer import analyze_signal
from plotter import plot_signals

#----------Generate signals----------
time, clock, reset, data= generate_signals()

#------------Plot signals------------
plot_signals(time, clock, reset, data)

#----------Save signal data----------
signals={
    "Time":time,
    "Clock":clock,
    "Reset":reset,
    "Data":data
}

df=pd.DataFrame(signals)
df.to_csv("data/signal.csv",index=False)

#----------Analyze signals-----------
statistics=[
    analyze_signal(clock,"clock"),
    analyze_signal(reset,"reset"),
    analyze_signal(data,"data")
    ]

#---------Store Statistics-----------
stats_df=pd.DataFrame(statistics)
stats_df.to_csv("data/statistics.csv",index=False)

print("Project Completed Successfully!")
print("Generated files:")
print("data/signals.csv")
print("data/statistics.csv")
print("images/waveform.png")