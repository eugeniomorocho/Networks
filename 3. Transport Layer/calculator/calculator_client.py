# calculator_client.py

import socket                                      # TCP socket communication
import json                                        # JSON serialization

HOST = "3.91.252.148"                              # Server IP address
PORT = 80                                          # Server port

a = input("Enter first number: ")                  # Read first value as text
b = input("Enter second number: ")                 # Read second value as text
operation = input("Enter operation (+, -, *, /): ") # Read operation as text

payload = {                                        # Create request dictionary
    "a": a,                                        # Store first value
    "b": b,                                        # Store second value
    "operation": operation                         # Store requested operation
}

client_socket = socket.socket()                    # Create TCP socket

client_socket.connect((HOST, PORT))                # Connect to server

client_socket.send(json.dumps(payload).encode())   # Serialize and send request

response = client_socket.recv(1024).decode()       # Receive server response

print("Server response:", response)                # Display response

client_socket.close()                              # Close connection