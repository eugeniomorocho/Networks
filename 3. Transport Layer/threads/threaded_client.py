# client.py
import socket, json
HOST = "localhost"; PORT = 9090
s = socket.socket(); s.connect((HOST, PORT))
for msg in [
    {"action":"join","name":"Tester"},
    {"action":"get_image"},
    {"action":"guess","value":"cat"}
]:
    s.send(json.dumps(msg).encode()); print(s.recv(4096).decode())
s.close()