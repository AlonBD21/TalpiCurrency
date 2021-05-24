import socket
import json
from time import sleep
from Logic.User import *
from Logic.Transaction import *
from Support.CryptoJson import *
from Logic.BalanceAppliance import *

PORT = 8020


class Client:

    def __init__(self, user):
        self.__user = user

    def send_transaction(self, send_to, amount):
        transaction = Transaction (self.__user.get_vk_bytes (), send_to, amount).sign (self.__user)
        trans_json = json.dumps (transaction, cls=CryptoEncoder)
        interfaces = socket.getaddrinfo (host=socket.gethostname (), port=None, family=socket.AF_INET)
        all_ips = [ip[-1][0] for ip in interfaces]
        for ip in all_ips:
            print (f'sending on {ip}')
            sock = socket.socket (socket.AF_INET, socket.SOCK_DGRAM, socket.IPPROTO_UDP)  # UDP
            sock.setsockopt (socket.SOL_SOCKET, socket.SO_BROADCAST, 1)
            sock.bind ((ip, 0))
            sock.sendto (trans_json, ("255.255.255.255", PORT))
            sock.close ()

    def get_balance(self):
        ba = BalanceAppliance (self.__user.get_vk_bytes ())
        ba_json = json.dumps (ba, cls=CryptoEncoder)
        interfaces = socket.getaddrinfo (host=socket.gethostname (), port=None, family=socket.AF_INET)
        all_ips = [ip[-1][0] for ip in interfaces]
        for ip in all_ips:
            print (f'sending on {ip}')
            sock = socket.socket (socket.AF_INET, socket.SOCK_DGRAM, socket.IPPROTO_UDP)  # UDP
            sock.setsockopt (socket.SOL_SOCKET, socket.SO_BROADCAST, 1)
            sock.bind ((ip, 0))
            sock.sendto (ba_json, ("255.255.255.255", PORT))
            sock.close ()


        #TODO: FINISH LISTENING
        data, address = self.__socket.recvfrom (4096)
        json_got = data.decode ('utf-8')
        obj = json.loads (json_got, cls=CryptoDecoder)
        print ("GOT: ", json_got)
        print ("FROM: ", address)
        if isinstance (obj, BalanceAppliance):
            return obj.get_balance ()


if __name__ == "__main__":
    user = User ()
    client1 = Client (user)
