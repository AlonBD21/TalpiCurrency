import socket
from Logic.User import User
from Logic.Transaction import Transaction
from Support import CryptoJson
from Logic.BalanceAppliance import BalanceAppliance
from Software.main import PORT, IP, ADDRESS, BROADCAST



class Client:

    def __init__(self, user):
        self.__user = user
        self.__bd_socket = socket.socket(socket.AF_INET,
                                         socket.SOCK_DGRAM, socket.IPPROTO_UDP)
        self.__bd_socket.setsockopt(socket.SOL_SOCKET, socket.SO_BROADCAST, 1)

        self.__bd_socket.bind(ADDRESS)

    def broadcast_transaction(self, send_to, amount):
        transaction = Transaction(self.__user.get_vk_bytes(), send_to,
                                  amount).sign(self.__user)
        trans_json = CryptoJson.dump(transaction)
        self.__bd_socket.sendto(bytes(trans_json, 'ascii'), BROADCAST)

    def get_user(self):
        return self.__user

    def ask_balance(self):
        ba = BalanceAppliance(self.__user.get_vk_bytes())
        ba_json = CryptoJson.dump(ba)
        self.__bd_socket.sendto(bytes(ba_json, 'ascii'), BROADCAST)

        data, address = self.__bd_socket.recvfrom(4096)
        json_string = data.decode('ascii')
        obj = CryptoJson.dump(json_string)
        if obj.__class__.__name__ is BalanceAppliance.__name__:
            return obj.ask_balance()
        return -1


# # TODO add broadcast bytes function
# def broadcast_json_string(json_string):
#     interfaces = socket.getaddrinfo(host=socket.gethostname(), port=None,
#                                     family=socket.AF_INET)
#     all_ips = [ip[-1][0] for ip in interfaces]
#     for ip in all_ips:
#         print(f'sending on {ip}')
#         bd_sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM,
#                                 socket.IPPROTO_UDP)  # UDP
#         bd_sock.setsockopt(socket.SOL_SOCKET, socket.SO_BROADCAST, 1)
#         bd_sock.bind((ip, 0))
#         bd_sock.sendto(bytes(json_string, "ascii"), ("255.255.255.255", PORT))
#         bd_sock.close()


if __name__ == "__main__":
    user = User.generate()
    client1 = Client(user)
    client1.ask_balance()
