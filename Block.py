import time
import Merkle
import Header

class Block:

    def _init__(self, prev_block):
        self.header = Header.header(prev_block.prev_hash, prev_block.n_bits)