import ecdsa
import socket
from hashlib import sha256

from BlockChain import *
from Block import *
from Client import *

IP = '192.168.137.246'
PORT = 1110

s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
server_address = (IP, PORT)
s.bind(server_address)

while True:
    data, address = s.recvfrom(4096)
    data.decode('utf-8')
    ##Verify

    send_data = "Transaction Failed"
    ##Answer sender
    s.sendto(send_data.encode('utf-8'), address)
    print("\n\n 1. Server sent : ", send_data,"\n\n")
