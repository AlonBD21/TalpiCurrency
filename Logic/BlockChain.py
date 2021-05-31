from Logic.Block import *


class BlockChain:
    SEP = "/"
    REWARD = 50

    def __init__(self, blocks):
        if len(blocks) > 0:
            self.__blocks = blocks
        else:
            genesis = Block.genesis()
            self.__blocks = [genesis]

    def add_block(self, block):
        if self.can_be_added(block):
            self.__blocks.append(block)
            return True
        return False

    @classmethod
    def genesis_chain(cls):
        return BlockChain([Block.genesis()])

    def is_valid(self):
        last = None
        if len(self.__blocks) == 1:
            return True
        for block in self.__blocks[1:]:
            if not block.is_solved():
                return False
            if last:
                if last.hash() != block.__header.__prev_hash:
                    return False
            last = block
        return self.check_all_balances()

    def can_be_added(self, block):
        """
        check 3 thing: valid prev hash, valid nonce in block, valid balance for all users
        :param block: the new block we want to add
        :return: True / False
        """
        last = self.__blocks[-1]
        if last.hash() != block.get_header().get_prev_hash():
            return False
        if not block.is_solved():
            return False
        return self.check_all_balances()  # returns True if valid, false if not

    def check_all_balances(self):
        """
        that is the function to check all balances for the validity of a block
        :return: TRUE / FALSE
        """
        users = dict()
        for block in self.__blocks:
            transactions = block.get_transactions()
            if not transactions:
                continue
            for trans in transactions:
                sender = trans.get_sender()
                receiver = trans.get_receiver()
                amount = trans.get_amount()
                if sender not in users.keys():
                    users[sender] = 0
                if receiver not in users.keys():
                    users[receiver] = 0
                users[sender] -= amount
                users[receiver] += amount
                users[block.get_header().get_mined_by()] += BlockChain.REWARD
        for balance in users.values():
            if balance < -100:  # TODO -100?
                return False
        return True

    def check_balance(self, vk):
        """
        that is the function for a single user to check his balance
        :param vk:
        :return: TRUE / FALSE
        """
        balance = 0
        for block in self.__blocks:
            transactions = block.get_transactions()
            if not transactions:
                continue
            for trans in transactions:
                sender = trans.get_sender()
                receiver = trans.get_receiver()
                amount = trans.get_amount()
                if vk == sender:
                    balance -= amount
                if vk == receiver:
                    balance += amount
                if block.get_header().get_mined_by() == vk:
                    balance += BlockChain.REWARD
        return balance

    def last_hash(self):
        return self.__blocks[-1].hash()

    def __len__(self):
        return len(self.__blocks)

    def __str__(self):
        s = ""
        for b in self.__blocks:
            s += str(b) + '\n'
        return s

    def __repr__(self):
        s = ""
        for b in self.__blocks:
            s += repr(b) + '\n'
        return s

    def get_blocks(self):
        return self.__blocks


if __name__ == '__main__':
    alice = User.generate()
    bob = User.generate()
    trans = Transaction(alice.get_vk_bytes(), bob.get_vk_bytes(), 30)
    trans.sign(alice)
    bc = BlockChain([])
    ph = bc.last_hash()
    b = Block.from_transactions(nonce, ph, [trans], alice.get_vk_bytes())
    bc.add_block(b)
    print(bc)
    print(repr(bc))
    print("Alice's balance", bc.check_balance(alice.get_vk_bytes()))
    print("Bob's balance", bc.check_balance(bob.get_vk_bytes()))
