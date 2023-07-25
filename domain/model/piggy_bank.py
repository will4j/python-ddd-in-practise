class PiggyBank:
    def __init__(self, balance: float):
        self.__balance = balance

    def check_balance(self):
        return self.__balance

    def deposit(self, amount: float):
        self.__balance += amount
