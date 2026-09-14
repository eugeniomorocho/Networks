# calculator_server.py

import socket                                      # TCP socket communication
import json                                        # JSON parsing and serialization

HOST = "0.0.0.0"                                    # Listen on all network interfaces
PORT = 80                                          # Server port

def handle_request(data):                          # Process one client request
    try:
        payload = json.loads(data)                 # Convert JSON string into dictionary

        a = payload.get("a")                       # Get first value
        b = payload.get("b")                       # Get second value
        operation = payload.get("operation")       # Get requested operation

        if a is None or b is None or operation is None:  # Check missing parameters
            return {"code": 400, "error": "MISSING_PARAMETER"}

        try:
            a = float(a)                            # Convert first value to number
            b = float(b)                            # Convert second value to number
        except ValueError:
            return {"code": 400, "error": "INVALID_NUMBER"}

        if operation == "+":                       # Addition
            result = a + b

        elif operation == "-":                     # Subtraction
            result = a - b

        elif operation == "*":                     # Multiplication
            result = a * b

        elif operation == "/":                     # Division
            if b == 0:                              # Check division by zero
                return {"code": 400, "error": "DIVISION_BY_ZERO"}

            result = a / b

        else:                                      # Unsupported operation
            return {"code": 400, "error": "UNSUPPORTED_OPERATION"}

        return {"code": 200, "result": result}      # Successful response

    except json.JSONDecodeError:                   # Invalid JSON received
        return {"code": 400, "error": "INVALID_JSON"}

# Create TCP socket
server_socket = socket.socket()                    # Create IPv4 TCP socket

server_socket.setsockopt(
    socket.SOL_SOCKET,                             # Socket level
    socket.SO_REUSEADDR,                           # Allow address reuse
    1
)

server_socket.bind((HOST, PORT))                   # Bind socket to IP and port
server_socket.listen(5)                            # Start listening for connections

print(f"Calculator server running on {HOST}:{PORT}") # Display server status

while True:                                        # Keep server running
    conn, addr = server_socket.accept()            # Accept incoming connection

    print(f"Connection from {addr}")               # Display client address

    data = conn.recv(1024).decode()                # Receive client data

    response = handle_request(data)                # Process request on server

    response_json = json.dumps(response)           # Convert response to JSON

    conn.send(response_json.encode())              # Send response to client

    conn.close()                                   # Close client connection