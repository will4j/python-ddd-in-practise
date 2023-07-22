from application.ports.output.piggy_bank_persistence import PiggyBankPersistence
from domain.model.piggy_bank import PiggyBank


class MemoryPiggyBankPersistence(PiggyBankPersistence):
    def __init__(self, balance):
        self.balance = balance

    def get(self) -> PiggyBank:
        return PiggyBank(self.balance)

    def save(self, piggy_bank: PiggyBank):
        self.balance = piggy_bank.check_balance()
