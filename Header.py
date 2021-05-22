import time
from hashlib import sha256

class header:
    def __init__(self, prev_hash, n_bits, nonce):
        self.prev_hash = prev_hash
        # self.root_hash = Merkle.calc_root()
        self.root_hash = 
        self.time = time.time()
        self.n_bits = n_bits
        self.nonce = nonce

    
    def create_merkle_root(self, transactions):
        width_of_tree = len (transactions)
        while width_of_tree > 1:
            hashes = []
            for i in range(0,width_of_tree,2):
                if i == len (transactions) - 1:
                    hashes.append (hash (transactions[i], transactions[i]))
                else:
                    hashes.append (hash (transactions[i], transactions[i + 1]))
            width_of_tree = len (hashes)
            transactions = hashes
        self.root_hash = transactions[0]