from Logic.Header import *
from Logic.Transaction import *


class Block:
    SEP = "|"

    def __init__(self, nonce=0, prev_block=None, transactions=None):
        if prev_block:
            prev_hash = prev_block.hash()
        else:
            prev_hash = "0" * 32
        self.header = Header (prev_hash, transactions, nonce)
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

    def is_solved(self):
        hashed = ''.join (format (x, '08b') for x in self.hash ())
        for i in range (self.header.n_bits):
            if hashed[i]:
                return False
        return True

    def hash(self):
        h1 = sha256 (str(self.header).encode()).digest ()
        h2 = sha256 (str(self.transactions).encode()).digest ()
        hashed = sha256 (str(h1 + h2).encode()).digest ()
        return hashed
        # ''.join (format (x, '08b') for x in hashed)  if we want to make it binary
