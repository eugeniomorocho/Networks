# client.py
import socket

HOST = 'localhost'
PORT = 80

s = socket.socket()
s.connect((HOST, PORT))
data = s.recv(1024) # Maximum number of bytes to receive per reading block
print("Received:", data.decode())
s.close()