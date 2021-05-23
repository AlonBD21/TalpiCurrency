from hashlib import sha256
from Logic.User import User
import time


class Transaction:
    SEP = ','

    def __init__(self, sender, receiver, amount, time_stamp=int(time.time()),
                 signature=None):
        """
        Creates new Transaction
        :param sender: who sends the money, verifying key, bytes
        :param receiver: who receives the money, verifying key, bytes
        :param amount: how much money to transfer
        :param signature: digital signature of the sender
        """
        self.__sender = sender
        self.__receiver = receiver
        self.__amount = amount
        self.__time = time_stamp
        self.__signature = signature

    @classmethod
    def from_string(cls, string):
        """
        Creates transaction from string
        :param string: string in the format of __str__
        :return: new Transaction
        """
        fields = string.split(cls.SEP)
        signature = None
        if len(fields) == 5:
            signature = bytes(fields[4])
        return Transaction(bytes(fields[0]), bytes(fields[1]),
                           float(fields[2]), int(fields[3]), signature)

    def __str__(self):
        """
        return string with the data of the transaction
        """
        fields = [str(self.__sender), str(self.__receiver), str(self.__amount),
                  str(int(self.__time)), str(self.__signature)]
        return self.SEP.join(fields)

    def sign(self, user):
        """
        puts signature on the transaction with the credentials on a given user
        :param user: credentials of the sender, User
        :return: signature, bytes
        """
        self.__signature = user.sign(self.__sign_on())

    def __sign_on(self):
        """
        :return: bytes that represents the data of the transaction to be signed
        """
        h1 = sha256(self.__sender).digest()
        h2 = sha256(self.__receiver).digest()
        h3 = sha256(bytes(str(self.__amount), encoding="ascii")).digest()
        h4 = sha256(bytes(self.__time)).digest()
        return sha256(h1 + h2 + h3 + h4).digest()

    def verify(self):
        """
        verifies the signature with the data of the transaction.
        :return: True if the signature is valid, False else.
        """
        if self.__signature is None:
            return False
        return User.verify(self.__sign_on(), self.__sender, self.__signature)

    def get_sender(self):
        return self.__sender

    def get_receiver(self):
        return self.__receiver

    def get_signature(self):
        return self.__signature

    def get_time(self):
        return self.__time

    def get_amount(self):
        return self.__amount


if __name__ == '__main__':
    alice = User.generate()
    bob = User.generate()
    trans = Transaction(alice.get_vk_bytes(), bob.get_vk_bytes(), 100.5,
                        int(time.time()))
    trans.sign(alice)
    print(trans)
    print(trans.verify())
