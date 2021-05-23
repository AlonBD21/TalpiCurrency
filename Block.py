import time
from hashlib import sha256

from Header import *
from Transaction import *

#TODO: make vavibles private in all classes
class Block:
    SEP = "ץ"

    def __init__(self, nonce=0, prev_hash="0" * 32, transactions=None, mined_by=None):
        self.header = Header (prev_hash, transactions, nonce, mined_by)
        self.transactions = transactions

    def __str__(self):
        s = str (self.header)
        if self.transactions:
            for t in self.transactions:
                s += Block.SEP + str (t)
        return s

    def __repr__(self):
        s = repr (self.header)
        if self.transactions:
            for t in self.transactions:
                s += Block.SEP + str (t)
        return s

    def set_nonce(self, nonce):
        self.header.nonce = nonce

    def get_transactions(self):
        return self.transactions

    def get_header(self):
        return self.header

    def is_solved(self):
        h = self.hash ()
        hashed = ''.join (format (x, '08b') for x in h)
        for i in range (self.header.n_bits):
            if hashed[i] == '1':
                return False
        return True

    def hash(self):
        h1 = sha256 (str (self.header).encode ()).digest ()
        h2 = sha256 (str (self.transactions).encode ()).digest ()
        hashed = sha256 (str (h1 + h2).encode ()).digest ()
        return hashed
        # ''.join (format (x, '08b') for x in hashed)  if we want to make it binary
