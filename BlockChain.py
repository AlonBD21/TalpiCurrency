from Block import *

class BlockChain:
    SEP = "/"
    def __init__(self, blocks=None):
        if blocks:
            self.blocks=blocks # maybe we want blocks to be string so that part might need to change
        else:
            genesis = Block()
            self.blocks = [genesis]

    def add_block(self, block):
        if self.can_be_added(block):
            self.blocks.append(block)

    def can_be_added(self, block):
        """
        check 3 thing: valid prev hash, valid nonce in block, valid balance for all users
        :param block: the new block we want to add
        :return: True / False
        """
        last = self.blocks[-1]
        if hash(last) != block.header.prev_hash:
            return False
        if not block.is_solved():
            return False
        # we need to add here a check for the balance of all users
        return True

    def check_balance(self, vk):
        pass

    def last_hash(self):
        return hash(self.blocks[-1])

    def __len__(self):
        return len(self.blocks)

    def __str__(self):
        s = ""
        for b in self.blocks:
            s += str(b)
        return s

    def __repr__(self):
        s = ""
        for b in self.blocks:
            s += repr (b)
        return s

bc = BlockChain()
# ph = bc.last_hash()
# t = Transaction()
# for i in range(10**10):
#     b = Block(i,ph,t)
#     if b.is_solved():
#         bc.add_block(b)
# print(bc)
print(repr(bc))

