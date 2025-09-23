# threaded_server.py

import socket       # 'socket' module to create network connections (TCP/UDP).
import threading    # 'threading' module to handle multiple threads running in parallel.
import json         # 'json' module (not used here, but useful for sending/receiving structured data).

# IP address where the server will listen.
# "0.0.0.0" means "all available network interfaces" (accepts connections from any IP).
HOST = "0.0.0.0"

# Port where the server will listen for incoming connections.
# 9090 is a non-privileged port (>1024).
PORT = 9090

# Function that runs every time a client connects to the server.
# 'conn' → the socket object representing the client connection.
# 'addr' → a tuple (IP, port) identifying the client.
def client_handler(conn, addr):
    print(f"New connection: {addr}")                   # Print the client address.
    conn.send(b"Welcome to the threaded server!\n")    # Send a welcome message to the client (must be bytes).
    conn.close()                                       # Close the connection once the client is served.

# Create the server socket.
# By default, socket() creates an IPv4 (AF_INET) TCP (SOCK_STREAM) socket.
s = socket.socket()

# Bind the socket to the specified address and port.
# This tells the OS that the server will listen on (HOST, PORT).
s.bind((HOST, PORT))

# Put the socket into listening mode.
# The argument '5' is the backlog: maximum number of queued connections.
s.listen(5)

# Print a message so we know the server is running.
print(f"Threaded server running on {HOST}:{PORT}")

# Infinite loop to keep accepting clients.
while True:
    # Wait for a client to connect.
    # 'conn' → socket object to communicate with the client.
    # 'addr' → client's address as a tuple (IP, port).
    conn, addr = s.accept()

    # Create a new thread to handle the client.
    # target=client_handler → the function this thread will run.
    # args=(conn, addr) → arguments passed to that function.
    thread = threading.Thread(target=client_handler, args=(conn, addr))

    # Start the thread. This launches client_handler(conn, addr) in parallel,
    # so the server can keep accepting new clients without waiting for the current one to finish.
    thread.start()