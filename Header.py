from time import time
from datetime import datetime
from hashlib import sha256


class Header:
    SEP = ","

    def __init__(self, prev_hash, transactions, nonce, mined_by, n_bits=10):
        self.prev_hash = prev_hash
        self.create_merkle_root (transactions)
        self.time = int (time ())
        self.n_bits = n_bits
        self.nonce = nonce
        self.mined_by = mined_by

    def create_merkle_root(self, transactions):
        if not transactions:
            self.root_hash = "0" * 32
        else:
            transactions = self.hash_all (transactions)  #TODO: implement merkle tree
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
            self.root_hash = transactions[0]

    def hash_all(self, transactions):
        hashed = []
        for trans in transactions:
            hashed.append (sha256(str(trans).encode()).digest())
        return hashed

    def __str__(self):
        return str (self.prev_hash) + Header.SEP + str (self.root_hash) + Header.SEP + str (self.time) + Header.SEP + \
               str (self.n_bits) + Header.SEP + str (self.nonce) + Header.SEP + str (self.mined_by)

    def __repr__(self):
        return "previous hash: " + str (self.prev_hash) + "\nmerkle hash: " + str (self.root_hash) + "\ntime: " + \
               str (datetime.fromtimestamp (self.time)) + "\ntarget: " + str (self.n_bits) + "\nnonce: " + str (
            self.nonce)+ "\nmined by: " + str (self.mined_by)

    def get_mined_by(self):
        return self.mined_by


# header1 = Header ("23567fac2332cd2312be2", ["Shachar,Alon,100"], nonce=874561)
# print (repr (header1))
# print (header1)
