import ecdsa
import socket
from hashlib import sha256

IP = '132.64.143.125'
PORT = 8020

class Server:
    def __init__(self):
        self.__address = (IP, PORT)
        self.__socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        self.__socket.bind(self.__address)

    def start_listening(self):
        while True:
            data, address = self.__socket.recvfrom(4096)
            print("GOT: ",data.decode('utf-8'))
            print("FROM: ", address)

            send_data = "HI, I got your msg. I am "+IP+' xD'
            self.__socket.sendto(send_data.encode('utf-8'), address)
            print("\n\n 1. Server sent : ", send_data, "\n\n")


if __name__ == '__main__':
    server = Server()
    server.start_listening()

