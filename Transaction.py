import ecdsa
from hashlib import sha256


class Transaction:
    def __init__(self, sender, reciever, amount):
        self.sender = sender
        self.reciever = reciever
        self.amount = amount

    def sign_material(self):
        return sha256(sha256(self.sender).digest() + sha256(
            self.reciever).digest() + sha256(self.amount).digest()).digest()


    def sign(self, sk):
        self.sign = ecdsa.sbytes(self)
        sk.sign()

    def verify(self, sig, pk):
        return pk.verify(sig, sign_material())
