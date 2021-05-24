from time import time
from datetime import datetime
from hashlib import sha256


class Header:
    SEP = ","

    def __init__(self, prev_hash, root_hash, nonce, miner,
                 time_stamp=int(time()), n_bits=10):
        self.__prev_hash = prev_hash
        self.__root_hash = root_hash
        self.__nonce = nonce
        self.__miner = miner
        self.__time_stamp = time_stamp
        self.__n_bits = n_bits

    @classmethod
    def from_transactions(cls, prev_hash, transactions, nonce, miner,
                          time_stamp=int(time()), n_bits=10):
        return Header(prev_hash, cls.create_merkle_root(transactions), nonce,
                      miner, time_stamp=time_stamp, n_bits=n_bits)

    @classmethod
    def create_merkle_root(cls, transactions):
        if not transactions:
            return "0" * 32
        else:
            transactions = cls.hash_all(
                transactions)  # TODO: implement merkle tree
            # width_of_tree = len (transactions)
            # while width_of_tree > 1:
            #     hashes = []
            #     for i in range (0, width_of_tree, 2):
            #         if i == len (transactions) - 1:
            #             hashes.append (sha256(transactions[i] + transactions[i]).digest ())
            #         else:
            #             hashes.append (sha256(transactions[i] + transactions[i + 1]).digest ())
            #     width_of_tree = len (hashes)
            #     transactions = hashes
            return transactions[0]

    @classmethod
    def hash_all(cls, transactions):
        hashed = []
        for trans in transactions:
            hashed.append(sha256(str(trans).encode()).digest())
        return hashed

    def __str__(self):
        return str(self.__prev_hash) + Header.SEP + str(
            self.root_hash) + Header.SEP + str(
            self.__time_stamp) + Header.SEP + \
               str(self.__n_bits) + Header.SEP + str(
            self.__nonce) + Header.SEP + str(self.__miner)

    def __repr__(self):
        return "previous hash: " + str(
            self.__prev_hash) + "\nmerkle hash: " + str(
            self.root_hash) + "\ntime: " + \
               str(datetime.fromtimestamp(
                   self.__time_stamp)) + "\ntarget: " + str(
            self.__n_bits) + "\nnonce: " + str(
            self.__nonce) + "\nmined by: " + str(self.__miner)

    def get_miner(self):
        return self.__miner

    def get_prev_hash(self):
        return self.__prev_hash

    def get_root_hash(self):
        return self.__root_hash

    def get_nonce(self):
        return self.__nonce

    def get_n_bits(self):
        return self.__n_bits

    def get_time_stamp(self):
        return self.__time_stamp
