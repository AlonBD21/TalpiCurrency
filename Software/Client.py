import socket
import json
from time import sleep
from Logic.User import *
from Logic.Transaction import *
from Support.CryptoJson import *
from Logic.BalanceAppliance import *

IP = "132.64.143.111"
PORT = 8204


class Client:

    def __init__(self, user):
        self.__user = user

    def broadcast_transaction(self, send_to, amount):
        transaction = Transaction(self.__user.get_vk_bytes(), send_to,
                                  amount)
        transaction.sign(self.__user)
        trans_json = json.dumps(transaction, cls=CryptoEncoder)
        broadcast_json_string(trans_json)

    def get_user(self):
        return self.__user

    def ask_balance(self):
        ba = BalanceAppliance(self.__user.get_vk_bytes())
        ba_json = json.dumps(ba, cls=CryptoEncoder)
        broadcast_json_string(ba_json)
        in_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        in_socket.bind((IP, PORT))
        data, address = in_socket.recvfrom(4096)
        json_string = data.decode('ascii')
        obj = json.loads(json_string, cls=CryptoDecoder)
        if obj.__class__.__name__ is BalanceAppliance.__name__:
            return obj.get_balance()
        return -1


# TODO add broadcast bytes function
def broadcast_json_string(json_string):
    interfaces = socket.getaddrinfo(host=socket.gethostname(), port=None,
                                    family=socket.AF_INET)
    all_ips = [ip[-1][0] for ip in interfaces]
    for ip in all_ips:
        print(f'sending on {ip}')
        bd_sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM,
                                socket.IPPROTO_UDP)  # UDP
        bd_sock.setsockopt(socket.SOL_SOCKET, socket.SO_BROADCAST, 1)
        bd_sock.bind((ip, 0))
        bd_sock.sendto(bytes(json_string,"ascii"), ("255.255.255.255", PORT))
        bd_sock.close()


if __name__ == "__main__":
    user = User.generate()
    client1 = Client(user)
    print(client1.ask_balance())
