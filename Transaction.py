from hashlib import sha256

class Transaction:

    def __init__(self, sender, receiver, amount):
        self.__sender = sender
        self.__receiver = receiver
        self.__amount = amount
        self.__signature = None

    def __init__(self, string):
        data = string.split(',')
        self.__sender, self.__reciever, self.__amount, self.__signature = data

    def __str__(self):
        fields = [str(self.__sender),str(self.__reciever), str(self.__amount), str(self.__signature)]
        return ','.join(fields)


    def sign(self, user):
        ecdsa


    def __hash__(self):
        sha256().digest()


