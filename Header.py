import time
import Merkle

class header:
    def __init__(self, prev_hash, n_bits, nonce):
        self.prev_hash = prev_hash
        self.root_hash = Merkle.calc_root()
        self.time = time.time()
        self.n_bits = n_bits
        self.nonce = nonce