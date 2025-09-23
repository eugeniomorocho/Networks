# server.py
import socket  # Imports the 'socket' module to create network connections (TCP/UDP).

HOST = '0.0.0.0'  # IP address where the server will listen. '0.0.0.0' means "all available network interfaces" (any IP of the machine).
PORT = 80         # Port where the server will listen for incoming connections. 80 is standard HTTP port.

s = socket.socket()        # Creates a TCP socket (IPv4 + TCP by default). The first `socket` is the module you imported. The second `socket()` is the class inside the module that creates a new socket.
s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)  # Allow reuse of the address
s.bind((HOST, PORT))       # Binds the socket to the specified address and port.
s.listen(1)                # Configures the socket to listen for incoming connections. The number (1) is the maximum number of queued connections. It does NOT create threads. For multiple clients, use threading/asyncio.
print("TCP server waiting for connection...")  # Prints a message indicating the server is ready.

conn, addr = s.accept()    # Waits for a client to connect. Returns a new socket object for this connection (conn) and the client's address (addr).
print(f"Connected to {addr}")    # formatted-string literal (the "f" before the string) allows embedding variables directly inside `{}`.
conn.send(b"Hello from Dockerized EC2 server!")    # Sends a message to the client. The 'b' before the string means "bytes literal". TCP sockets require bytes, not a regular string.

conn.close()  # Closes the connection with the client.
