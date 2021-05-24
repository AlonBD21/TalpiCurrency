import ecdsa
import socket
import json
from hashlib import sha256
from Logic.BlockChain import *
from Logic.BalanceAppliance import *
from Support.CryptoJson import *


IP = '132.64.143.125'
PORT = 8020


class Server:
    def __init__(self, user):
        self.__user = user
        self.__address = (IP, PORT)
        self.__socket = socket.socket (socket.AF_INET, socket.SOCK_DGRAM)
        self.__socket.bind (self.__address)
        self.__block_chain = None
        self.__transactions = []

    # def get_transactions(self):
    #     return self.__transactions

    def update_block_chain(self, BlockChain: bc):
        if bc.is_valid () and len (bc) > len (self.__block_chain):
            self.__block_chain = bc
            self.__transactions = []
            return True
        return False

    def add_transaction(self, transaction):
        self.__transactions.append (transaction)

    def get_balance(self, vk):
        return self.__block_chain.check_balance(vk)

    def start_listening(self):
        while True:
            data, address = self.__socket.recvfrom (4096)
            json_got = data.decode ('utf-8')
            obj = json.loads (json_got, cls=CryptoDecoder)
            print ("GOT: ", json_got)
            print ("FROM: ", address)
            if isinstance (obj, BlockChain):
                self.update_block_chain (obj)
            if isinstance (obj, Transaction):
                self.add_transaction (obj)
            if isinstance (obj, BalanceAppliance):
                vk = obj.get_vk()
                self.get_balance(vk)
            send_data = "HI, I got your msg. I am " + IP + ' xD'
            self.__socket.sendto (send_data.encode ('utf-8'), address)
            print ("\n\n Server sent : ", send_data, "\n\n")




if __name__ == '__main__':
    server = Server ()
    server.start_listening ()
