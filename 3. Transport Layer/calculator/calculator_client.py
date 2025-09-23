# simple_calculator_client.py

import socket
import json

# -----------------------------
# Configuration
# -----------------------------
HOST = "localhost"  # Server IP
PORT = 80         # Must match server's port

# -----------------------------
# Ask user for numbers first
# -----------------------------
a_input = input("Enter first number: ")
b_input = input("Enter second number: ")

# Convert input to float (so server receives a number)
try:
    a = float(a_input)
    b = float(b_input)
except ValueError:
    print("Invalid input! Please enter numeric values.")
    exit(1)

# Prepare payload
payload = {"a": a, "b": b}
payload_json = json.dumps(payload)  # Convert dictionary to JSON string

# -----------------------------
# Connect to server and send data
# -----------------------------
client_socket = socket.socket()            # Create TCP socket
try:
    client_socket.connect((HOST, PORT))   # Connect to server
    client_socket.send(payload_json.encode())  # Send JSON as bytes

    # Receive response
    response_data = client_socket.recv(1024)
    response = json.loads(response_data.decode())

    # Print result
    if response.get("code") == 200:
        print(f"Result from server: {response['result']}")
    else:
        print(f"Error from server: {response.get('error')} (code {response.get('code')})")

except ConnectionRefusedError:
    print("Could not connect to server. Make sure the server is running.")
finally:
    client_socket.close()  # Always close the socket
