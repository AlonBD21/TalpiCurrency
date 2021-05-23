import socket
import sys
from time import sleep

from Transaction import *
# setup
interfaces = socket.getaddrinfo(host=socket.gethostname(), port=None, family=socket.AF_INET)
all_ips = [ip[-1][0] for ip in interfaces]
PORT = 5005

msg = b'hello world'
print(msg)
print(type(msg))

while True:

    for ip in all_ips:
        print(f'sending on {ip}')
        sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM, socket.IPPROTO_UDP)  # UDP
        sock.setsockopt(socket.SOL_SOCKET, socket.SO_BROADCAST, 1)
        sock.bind((ip,0))
        sock.sendto(msg, ("255.255.255.255", PORT))
        sock.close()
    msg = bytes (input (), "utf-8")

    sleep(2)

