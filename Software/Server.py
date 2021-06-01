import socket

from Logic.BalanceAppliance import BalanceAppliance
from Support.CryptoJson import bytes_to_string
from Support.CryptoJson import string_to_bytes
from Logic.Block import Block
from Logic.BlockChain import BlockChain
from Logic.Transaction import Transaction
from Logic.User import User
from Software.Client import Client
from Support import CryptoJson
import threading
from Software.main import PORT, IP, ADDRESS, BROADCAST


class Server(Client):
    def __init__(self, user):
        Client.__init__(self, user)
        self.__address = (IP, PORT)
        self.__socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        self.__bd_socket = socket.socket(socket.AF_INET,
                                         socket.SOCK_DGRAM, socket.IPPROTO_UDP)
        self.__bd_socket.setsockopt(socket.SOL_SOCKET, socket.SO_BROADCAST, 1)
        self.__socket.bind(self.__address)
        self.__block_chain = BlockChain.genesis_chain()
        self.__transactions_queue = []
        self.__mine_thread = self.make_daemon(self.mine)
        self.__listen_thread = self.make_daemon(self.listen)
        self.__notify_mine = False

    def listen(self):
        while True:
            data, address = self.__socket.recvfrom(4096)
            print(data.decode("ascii"))
            obj = CryptoJson.load(data.decode('ascii'))
            if isinstance(obj, BlockChain):
                self.update_block_chain(obj)
                self.__notify_mine = True

            elif isinstance(obj, Transaction):
                self.__transactions_queue.append(obj)
                if len(self.__transactions_queue) == 1:
                    self.__notify_mine = True

            elif isinstance(obj, BalanceAppliance):
                vk = obj.get_vk()
                obj.set_balance(self.find_balance(vk))
                self.send_bytes(bytes(CryptoJson.dump(obj),"ascii"),(address[0],PORT))

            else:
                print("GOT UNCLASSIFIED DATA FROM", IP, "  -  ", obj)

    def mine(self):
        while True:
            nonce = 0
            if len(self.__transactions_queue) == 0:
                transactions = []
            else:
                transactions = [self.__transactions_queue[0]]
            b = Block.from_transactions(nonce,
                                        self.__block_chain.last_hash(),
                                        transactions,
                                        self.get_user().get_vk_bytes())
            while True:
                if self.__notify_mine:
                    self.__notify_mine = False
                    break
                b.set_nonce(nonce)
                if b.is_solved():
                    added = self.__block_chain.add_block(b)
                    print("solved")
                    if added:
                        print("Found new block! publishing...")
                        if len(transactions) > 0:
                            self.__transactions_queue.pop(0)

                        self.send_bytes(
                            bytes(CryptoJson.dump(self.__block_chain),"ascii"),
                            BROADCAST)

                        break
                nonce += 1

    def start_server(self):
        self.__mine_thread.start()
        self.__listen_thread.start()

    def update_block_chain(self, bc):
        if bc.is_valid() and len(bc) > len(self.__block_chain):
            self.__block_chain = bc
            self.__transactions_queue = []
            return True
        return False

    def find_balance(self, vk):
        return self.__block_chain.check_balance(vk)

    def send_bytes(self, data, address):
        self.__socket.sendto(data, address)
        print("SENT BYTES TO", address)

    @classmethod
    def make_daemon(cls, func, *args):
        return threading.Thread(target=func, args=args, daemon=False)


if __name__ == '__main__':
    miner = User.generate()
    print(bytes_to_string(miner.get_vk_bytes()))
    server = Server(miner)
    server.start_server()

