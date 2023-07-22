class PiggyBank:
    def __init__(self, balance):
        self.__balance = balance

    def check_balance(self):
        return self.__balance

    def deposit(self, amount):
        self.__balance += amount
