import ecdsa
import socket
from hashlib import sha256

HOST = socket.gethostbyname(socket.gethostname())
print(HOST)
PORT = 4567

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.bind((HOST, PORT))
    print("A")
    s.listen()
    print("B")
    conn, addr = s.accept()
    print("C")
    with conn:
        print('Connected by', addr)
        while True:
            data = conn.recv(1024)
            if not data:
                break
            conn.sendall(data)
