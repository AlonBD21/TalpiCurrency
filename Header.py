from time import time
from datetime import datetime

class Header:
    def __init__(self, prev_hash, transactions, nonce, n_bits=10):
        self.prev_hash = prev_hash
        self.create_merkle_root(transactions)
        self.time = int(time())
        self.n_bits = n_bits
        self.nonce = nonce

    def create_merkle_root(self, transactions):
        transactions = self.hash_all(transactions)
        width_of_tree = len (transactions)
        while width_of_tree > 1:
            hashes = []
            for i in range(0,width_of_tree,2):
                if i == len (transactions) - 1:
                    hashes.append (hash(transactions[i]), transactions[i])
                else:
                    hashes.append (hash (transactions[i], transactions[i + 1]))
            width_of_tree = len (hashes)
            transactions = hashes
        self.root_hash = transactions[0]

    def hash_all(self, transactions):
        hashed = []
        for trans in transactions:
            hashed.append(hash(trans))
        return hashed

    def __str__(self):
        return str(self.prev_hash)+","+str(self.root_hash)+","+str(self.time)+","+str(self.n_bits)+","+str(self.nonce)

    def __repr__(self):
        return "previous hash: "+str(self.prev_hash)+"\nmerkle hash: "+str(self.root_hash)+"\ntime: "+\
               str(datetime.fromtimestamp(self.time))+"\ntarget: "+str(self.n_bits)+"\nnonce: "+str(self.nonce)

# header1 = Header("23567fac2332cd2312be2",["Shachar,Alon,100"],nonce=874561)
# print(repr(header1))
# print(header1)

# t=time()
# p = datetime.fromtimestamp(int(t))
# print(p)