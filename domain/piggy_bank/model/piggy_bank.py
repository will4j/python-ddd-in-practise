from domain.domain_objects import AggregateRoot
from domain.piggy_bank.model.base import PiggyBankId


class PiggyBank(AggregateRoot):
    id: PiggyBankId
    balance: float

    def get_id(self) -> PiggyBankId:
        return self.id

    def check_balance(self):
        return self.balance

    def deposit(self, amount: float):
        self.balance += amount
