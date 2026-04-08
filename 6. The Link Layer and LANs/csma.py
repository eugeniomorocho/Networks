import random                      # Used to simulate random transmission attempts
import matplotlib.pyplot as plt   # Used for plotting graphs
import numpy as np   

def simulate_csma(num_nodes=4, time_steps=20, p_transmit=0.5):
    """
    Simulates CSMA with:
    - Random transmission attempts
    - Collision detection
    - Basic backoff behavior
    """

    timeline = []  # Store events per time step

    for t in range(time_steps):
        attempting_nodes = []

        # Each node decides randomly whether to transmit
        for node in range(num_nodes):
            if random.random() < p_transmit:   # Transmission probability
                attempting_nodes.append(node)

        # Determine outcome
        if len(attempting_nodes) == 0:
            timeline.append(("idle", []))      # No transmission
        
        elif len(attempting_nodes) == 1:
            timeline.append(("success", attempting_nodes))  # Successful transmission
        
        else:
            timeline.append(("collision", attempting_nodes))  # Collision occurs

    # Visualization
    plt.figure()

    for t, (status, nodes) in enumerate(timeline):
        for node in nodes:
            if status == "success":
                plt.scatter(t, node, marker='o')   # Successful transmission
            elif status == "collision":
                plt.scatter(t, node, marker='x')   # Collision mark

    plt.title("CSMA (Collisions and Successes)")
    plt.xlabel("Time")
    plt.ylabel("Node ID")
    plt.yticks(range(num_nodes))
    plt.grid()

    plt.show()

    return timeline

simulate_csma()