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

        # TODO 1: Check if any required parameter is missing

        # TODO 2: Validate that a and b are valid numbers

        # TODO 3: Implement the supported operations (add, sub, mul, div)

        # TODO 4: Handle division by zero

        # TODO 5: Handle unsupported operations

        # Example of a successful response
        return {"code": 200, "result": a + b}      # Temporary example

    except json.JSONDecodeError:
        # TODO 6: Return an appropriate error for invalid JSON
        pass

# Create TCP socket
server_socket = socket.socket()                    # Create IPv4 TCP socket
server_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1) # setsockopt() allows you to configure options for the socket. In this case, it is used to set the SO_REUSEADDR option, which allows the socket to bind to an address that is already in use. This is useful when restarting a server, as it allows the new instance of the server to bind to the same address and port without waiting for the old instance to fully release them. 1 means that the option is enabled.
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