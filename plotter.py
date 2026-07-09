#Plots digital signals

import matplotlib.pyplot as plt

def plot_signals(time,clock,reset,data):
    plt.figure(figsize=(10,7))

    #----------Clock signal----------
    plt.subplot(3,1,1)
    plt.step(time, clock, where ="post", linewidth=2)
    plt.title("Clock Signal")
    plt.ylabel("Logic")
    plt.yticks([0,1],["LOW","HIGH"])
    plt.grid(True)

    #----------Reset signal----------
    plt.subplot(3,1,2)
    plt.step(time, reset, where="post", linewidth=2)
    plt.ylabel("Logic")
    plt.yticks([0,1],["LOW","HIGH"])
    plt.grid(True)

    #----------Data signal----------
    plt.subplot(3,1,3)
    plt.step(time, data, where="post", linewidth=2)
    plt.xlabel("Time")
    plt.ylabel("Logic")
    plt.grid(True)

    plt.ylim(-0.5,1.5)
    plt.yticks([0,1],["LOW","HIGH"])
    plt.tight_layout()
    plt.savefig("images/waveform.png", dpi=300, bbox_inches="tight")

    #Display graph
    plt.show()