
class BalanceAppliance:
    #VK in bytes
    def __init__(self, vk, balance = None):
        self.__vk = vk
        self.__balance = balance

    def get_vk(self):
        return self.__vk

    def set_balance(self, balance):
        self.__balance = balance

    def get_balance(self):
        return self.__balance
