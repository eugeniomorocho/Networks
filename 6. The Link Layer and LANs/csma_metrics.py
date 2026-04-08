import random                      # Used to simulate random transmission attempts
import matplotlib.pyplot as plt   # Used for plotting graphs
import numpy as np   

def csma_metrics(num_nodes=4, time_steps=50, p_transmit=0.5):
    """
    Computes performance metrics for CSMA:
    - Throughput
    - Collisions
    """

    success = 0
    collisions = 0

    for t in range(time_steps):
        attempts = sum([1 for _ in range(num_nodes) if random.random() < p_transmit])

        if attempts == 1:
            success += 1
        elif attempts > 1:
            collisions += 1

    efficiency = success / time_steps

    print("CSMA Performance Metrics")
    print("------------------------")
    print(f"Success: {success}")
    print(f"Collisions: {collisions}")
    print(f"Efficiency: {efficiency:.2f}")

csma_metrics()