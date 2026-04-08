import random                      # Used to simulate random transmission attempts
import matplotlib.pyplot as plt   # Used for plotting graphs
import numpy as np   

def simulate_tdma(num_nodes=4, num_slots=12):
    """
    Simulates TDMA where each node transmits in a fixed time slot.
    """

    timeline = []  # This will store which node transmits at each time slot

    # Assign each time slot to a node in round-robin fashion
    for t in range(num_slots):
        node = t % num_nodes           # Cyclic assignment
        timeline.append(node)          # Store transmitting node

    # Plot the timeline
    plt.figure()
    
    for t, node in enumerate(timeline):
        plt.scatter(t, node)          # Plot (time, node)
    
    plt.title("TDMA Timeline (No Collisions)")
    plt.xlabel("Time Slot")
    plt.ylabel("Node ID")
    plt.yticks(range(num_nodes))
    plt.grid()

    plt.show()

    return timeline

simulate_tdma()