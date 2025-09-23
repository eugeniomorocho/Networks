import socket
import json

servers = [
    ("SERVER_IP_1", PORT_1),
    ("SERVER_IP_2", PORT_2),
    ("SERVER_IP_3", PORT_3),
]

for ip, port in servers:
    s = socket.socket()
    try:
        s.connect((ip, port))
        s.send(json.dumps({"operation": "mul", "a": 2, "b": 3}).encode())
        response = json.loads(s.recv(1024).decode())
        print(ip, port, response)
    except Exception as e:
        print(ip, port, "ERROR", e)
    finally:
        s.close()
