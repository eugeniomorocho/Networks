# auto_test.py
import socket
import json

def test_server(ip, port):
    try:
        s = socket.socket()
        s.settimeout(5)
        s.connect((ip, port))

        # Send valid request
        s.send(json.dumps({"a": 3, "b": 4}).encode())
        print("Response:", s.recv(1024).decode())

        # Send invalid request
        s.send(b"invalid json")
        print("Error Response:", s.recv(1024).decode())

        s.close()
    except Exception as e:
        print(f"Server {ip}:{port} unreachable. Error: {e}")

# Example test
servers = [
    ("127.0.0.1", 8080),
    ("192.168.1.10", 8080),
]

for ip, port in servers:
    test_server(ip, port)