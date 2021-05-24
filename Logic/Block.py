from Logic.Header import *
from Logic.Transaction import *


# TODO: make vavibles private in all classes
class Block:
    SEP = "ץ"
    ZEOROS_HASH = "0" * 32

    def __init__(self, header, transactions):
        self.__header = header
        self.__transactions = transactions

    @classmethod
    def from_transactions(cls, nonce, prev_hash, transactions, mined_by):
        header = Header.from_transactions(prev_hash, transactions, nonce,
                                          mined_by)
        return cls(header, transactions)

    @classmethod
    def genesis(cls):
        header = Header.from_transactions(cls.ZEOROS_HASH, None, 0, None)
        return cls(header, None)

    def __str__(self):
        s = str(self.__header)
        if self.__transactions:
            for t in self.__transactions:
                s += Block.SEP + str(t)
        return s

    def __repr__(self):
        s = repr(self.__header)
        if self.__transactions:
            for t in self.__transactions:
                s += Block.SEP + str(t)
        return s

    def set_nonce(self, nonce):
        self.__header.__nonce = nonce

    def get_transactions(self):
        return self.__transactions

    def get_header(self):
        return self.__header

    def is_solved(self):
        h = self.hash()
        hashed = ''.join(format(x, '08b') for x in h)
        for i in range(self.__header.get_n_bits()):
            if hashed[i] == '1':
                return False
        return True

    def hash(self):
        h1 = sha256(str(self.__header).encode()).digest()
        h2 = sha256(str(self.__transactions).encode()).digest()
        hashed = sha256(str(h1 + h2).encode()).digest()
        return hashed
        # ''.join (format (x, '08b') for x in hashed)  if we want to make it binary

    def get_header(self):
        return self.__header

    def get_transactions(self):
        return self.__transactions
