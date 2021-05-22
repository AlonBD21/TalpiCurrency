import time
from hashlib import sha256

from Header import *
from Transaction import *


class Block:

    def __init__(self, nonce=0, prev_block=None, transactions="0" * 32):
        if prev_block:
            prev_hash = hash (prev_block)
        else:
            prev_hash = "0" * 32
        self.header = Header (prev_hash, transactions, nonce)
        self.transactions = transactions

    def __str__(self):
        s = str (self.header)
        for t in self.transactions:
            s += "," + str (t)
        return s

    def is_solved(self):
        hashed = ''.join (format (x, '08b') for x in self.hash ())
        for i in range (self.header.n_bits):
            if hashed[i]:
                return False
        return True

    def __hash__(self):
        h1 = sha256 (self.header).digest ()
        h2 = sha256 (self.transactions).digest ()
        hashed = sha256 (h1 + h2).digest ()
        return hashed
        # ''.join (format (x, '08b') for x in hashed)  if we want to make it binary
