import ecdsa
import socket
from hashlib import sha256
from Logic.BlockChain import *

IP = '132.64.143.125'
PORT = 8020

class Server:
    def __init__(self, user):
        self.__user = user
        self.__address = (IP, PORT)
        self.__socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        self.__socket.bind(self.__address)
        self.__block_chain = None

    def update_blockchain(self, BlockChain: bc):
        if bc.is_valid():
            self.__block_chain = bc

    def start_listening(self):
        while True:
            data, address = self.__socket.recvfrom(4096)
            json_got = data.decode('utf-8')
            print("GOT: ",json_got)
            print("FROM: ", address)
            # if i_got_blockchain:
            #     bc = None #something
            #     result = self.update_blockchain(bc) #bool
            # if i_got_transaction:
            #     bc = None #something
            #     self.update_blockchain(bc)
            send_data = "HI, I got your msg. I am "+IP+' xD'
            self.__socket.sendto(send_data.encode('utf-8'), address)
            print("\n\n Server sent : ", send_data, "\n\n")


if __name__ == '__main__':
    server = Server()
    server.start_listening()

