import random                      # Used to simulate random transmission attempts
import matplotlib.pyplot as plt   # Used for plotting graphs
import numpy as np   

def simulate_5g_scheduler(num_nodes=4, time_slots=10, subcarriers=4):
    """
    Simulates a simplified 5G scheduler:
    - Time division (TDMA)
    - Frequency division (FDMA / OFDMA style)
    """

    grid = np.full((num_nodes, time_slots), -1)  
    # Matrix to store resource allocation (-1 = no allocation)

    for t in range(time_slots):
        assigned_nodes = random.sample(range(num_nodes), k=min(num_nodes, subcarriers))
        # Randomly select nodes to assign resources at this time slot

        for sc, node in enumerate(assigned_nodes):
            grid[node][t] = sc   # Assign subcarrier to node

    # Visualization
    plt.figure()

    for node in range(num_nodes):
        for t in range(time_slots):
            if grid[node][t] != -1:
                plt.scatter(t, node)  # Node is transmitting

    plt.title("5G-like Scheduling (Time + Frequency)")
    plt.xlabel("Time Slot")
    plt.ylabel("Node ID")
    plt.yticks(range(num_nodes))
    plt.grid()

    plt.show()

    return grid

simulate_5g_scheduler()