import random                      # Used to simulate random transmission attempts
import matplotlib.pyplot as plt   # Used for plotting graphs
import numpy as np   

def simulate_fdma(num_nodes=4):
    """
    Simulates FDMA where each node has its own frequency channel.
    """

    plt.figure()

    # Each node gets a fixed frequency (y-axis position)
    for node in range(num_nodes):
        freq = node                   # Assign frequency channel
        plt.hlines(freq, 0, 10)       # Draw horizontal line (constant transmission)
        plt.text(5, freq, f"Node {node}", ha='center')  # Label node

    plt.title("FDMA (All nodes transmit simultaneously)")
    plt.xlabel("Time")
    plt.ylabel("Frequency Channel")
    plt.yticks(range(num_nodes))
    plt.grid()

    plt.show()

simulate_fdma()